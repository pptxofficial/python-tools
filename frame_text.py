def frame_text(text: str, char="#", padding_x=4, padding_y=1, margin_x=20, margin_y=1, double_sides=False, shadow:str=None):
  """
  Add a frame around text.

  :param text: A single line of text to frame.
  :param char: A single character to use as a border of one of the following: "light", "heavy", "light dashed", "heavy dashed", "double".
  :param padding_x: Number of characters used for the horizontal padding.
  :param padding_y: Number of lines used for the vertical padding.
  :param margin_x: Number of characters used for the horizontal margin.
  :param margin_y: Number of lines used for the vertical margin.
  :param double_sides: Doubles the leftmost and rightmost broder characters
  :param shading: Adds a shadow to the frame. String is one of the following: "light", "medium", "dark".
  :return: The framed text.

  Example:
    print(frame_text("frame me", "heavy", shadow="medium"))
  """
  width = len(text)
  again = 2 if double_sides else 1

  # Broder data
  if len(char) == 1: char = char * 6
  elif char == "light": char = "┌─┐│└┘"
  elif char == "heavy": char = "┏━┓┃┗┛"
  elif char == "light dashed": char = "┌╌┐┊└┘"
  elif char == "heavy dashed": char = "┏╍┓┋┗┛"
  elif char == "double": char = "╔═╗║╚╝"
  else: char = char[0] * 6
  
  # Initialize array of lines of strings.
  lines = []

  # Top margin
  for _ in range(margin_y): 
    lines.append(" ")

  # Top border
  lines.append("".join([
    " " * margin_x,                     # Left margin
    char[0] * again,                    # Top-left border
    char[1] * (2 * padding_x + width),  # Top border
    char[2] * again                     # Top-right border
  ]))

  # Top padding
  for _ in range(padding_y): 
    lines.append("".join([
      " " * margin_x,                 # Left margin
      char[3] * again,                # Left border
      " " * (2 * padding_x + width),  # Top padding
      char[3] * again                 # Right border
    ]))
  
  # Text content
  lines.append("".join([
    " " * margin_x,    # Left margin
    char[3] * again,   # Left border
    " " * padding_x,   # Left padding
    text,              # Text content
    " " * padding_x,   # Right padding
    char[3] * again    # Right border
  ]))

  # Bottom padding
  for _ in range(padding_y): 
    lines.append("".join([
      " " * margin_x,                 # Left margin
      char[3] * again,                # Left border
      " " * (2 * padding_x + width),  # Bottom padding
      char[3] * again                 # Right border
    ]))
  
  # Bottom border
  lines.append("".join([
    " " * margin_x,                     # Left margin
    char[4] * again,                    # Bottom-left border
    char[1] * (2 * padding_x + width),  # Bottom border
    char[5] * again                     # Bottom-right border
  ]))

  # Shadow
  if shadow is not None:
    if shadow == "light": shadow = "░"
    elif shadow == "medium": shadow = "▒"
    elif shadow == "dark": shadow = "▓"
    else: shadow = "░"
    for i in range(len(lines)):
      if i <= (margin_y + 1): 
        continue
      elif i == (len(lines) - 1):
        lines[i] = lines[i] + " " + shadow * 2
        lines.append(" " * (margin_x + 2) + shadow * (len(lines[margin_y]) - margin_x + 1))
      else: 
        lines[i] = lines[i] + " " + shadow * 2

  # Bottom margin
  for _ in range(margin_y): 
    lines.append(" ")

  # Return final string
  return "\n".join(list(filter(None, lines)))
