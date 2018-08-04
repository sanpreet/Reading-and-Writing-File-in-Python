# Reading-and-Writing-File-in-Python
## Different Modes of operations with Files in Python :smiley:
| Mode  | Explanation|
| ------------- | ------------- |
|'r'  | Open a file for reading. (default) |
| 'w'  | Open a file for writing.  |
|  'a'   |     Open for appending at the end of the file without truncating it.     |   
|'b'|  Open in binary mode.  |

### Read the file in python
```
def main():
    # provide the path where the file is located
    #Please take care that if you are using the windows please use the double backslash so that you will not get error while reading
    open_mode = open("xx\\MY_Description.txt","r")
    if open_mode.mode == "r":
        content = open_mode.read()
        print("Content to be read:")
        print(content)
```  
### Writing read file in Python

```
def main():
    #write the file in the current directory
    write_mode = open("nltk.txt","w+")
    if write_mode.mode == "w+":
        content = write_mode.write(content)
        print("Content is written. Please check the required file:")
  ```
  ### How to run the code
  Please download the file write_read.py in an folder and points to that folder in the command prompt or if you are using the ubuntu you can perform the same action in the terminal.  
  Please run the following command
  ```
  python write_read.py
  ```
  
  
  
