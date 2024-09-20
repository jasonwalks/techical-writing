# What is 12msCheck.py
A python program that checks for reg pattern `\d+[a-zA-Z]` in all .docx files in the folder `12mscheck` inside the Downloads folder.

# Why is this helpful
- "12ms" with no space between is correct in coding but wrong in English writing. <br>
- These mistakes are often created through sheer force of habit. <br>
- `12msCheck.py` identifies such error in .docx files. <br>

# Preparations
## Install Python (version 3.x)
- Windows & macOS <br>
  - Download the installer from python.org.
  - Run the installer and follow the prompts.
- Linux
  - Most Linux distributions come with python pre-installed. Check by running: `python3 --version`
## Install the `python-docx` library using 'pip'
### Install pip (package manager for Python)
- Windows & macOS
  - Open a terminal or command prompt: <br>
    1. `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` <br>
    2. `python3 get-pip.py` <br>
### Install `python-docx` library: <br>
```
pip install python-docx
```
## Create a directory for storing .docx files to be checked.
1. Create a folder named `12mscheck` under Downloads.
2. Put all the .docx files that need to be checked for "12ms" type of erros. 
## Run 12mscheck.py from the command line. 
1. Put `12msCheck.py` in the `12mscheck` folder.
2. Open terminal navigate to `12mscheck`.
3. Run `12msCheck.py`: <br>
`python3 12msCheck.py`

## Troubleshooting
docx module not found, try and following and run again:
```
pip3 install python-docx
```


