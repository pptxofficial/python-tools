# python-tools
Tools to make your python better... maybe.

## [frame_text.py](frame_text.py)
Example use:
```python
from frame_text import frame_text as frame
print(frame("This will be framed with a shadow", "heavy", shadow="medium", margin_x=4))
```
Output:
```
 
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                                         ┃
    ┃    This will be framed with a shadow    ┃ ▒▒
    ┃                                         ┃ ▒▒
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ▒▒
      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

```
This is what it looks like in a console:
![image](https://github.com/pptxofficial/python-tools/assets/76122659/24e9b84f-fb30-4e96-8bb7-e6b83cd9a157)
