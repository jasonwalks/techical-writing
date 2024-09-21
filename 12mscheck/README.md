# What is 12msChecker.py
A python program that checks for reg pattern `\d+[a-zA-Z]` (12ms, 5kg, 34mnm, etc.) in all .docx files in the folder `12mscheck` inside the Downloads folder.

# Why is this helpful
- "12ms" with no space between is correct in coding but wrong in English writing. <br>
- Engineers often creat these mistakes through sheer force of habit. <br>
- `12msChecker.py` identifies such errors in .docx files. <br>

# Preparations
## Install Python (version 3.x)
- Windows & macOS <br>
  - Download the installer from python.org.
  - Run the installer and follow the prompts.
- Linux
  - Most Linux distributions come with python pre-installed. Check by running: `python3 --version`
## Install the `python-docx` library using 'pip'
### Install pip (package manager for Python)
- Windows & macOS <br>
Open a terminal or command prompt and run the following commands: <br>
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
### Install `python-docx` library: <br>
```
pip install python-docx
```
## Create a directory for storing .docx files to be checked.
1. Create a folder named `12mscheck` under Downloads.
2. Put all the .docx files that need to be checked for "12ms" type of erros. 
## Run `12msChecker.py` from the command line. 
1. Put `12msChecker.py` in the `12mscheck` folder.
2. Open a terminal or command prompt and navigate to `12mscheck`:
```
cd ~/Downloads/12mscheck/
```
4. Run `12msChecker.py`: <br>
```
python3 12msChecker.py
```
6. If successful, `12msChecker.py` should produce results similar to the folloing: <br>
```
File: demo.docx
  Found matches: ['12ms', '6ms']

File: demo copy.docx
  Found matches: ['4mn']

File: 5kg.docx
  Found matches: ['5kg']
```

## Troubleshooting
For `docx module not found` error, try and following and run again:
```
pip3 install python-docx
```


