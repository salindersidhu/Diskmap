#Diskmap

##Description:
A disk space visualization utility. This program displays all the files and folders within a selected location as a rectangle map where each rectangle is proportional to the size of the file it represents.

##Features:
- Graphical visualization of files and folders
- Rename files in the visualizer
- Move files in the visualizer
- Delete files in the visualizer
- Save screenshots of the visualization

##Supports:
- Microsoft Windows 7, 8, 8.1, 10
- Linux and Unix based distributions

##Dependencies:
- `Python 3` [(Build 3.4)](https://www.python.org/downloads/)
- `PyQt 4` [(Build 4.11)](https://riverbankcomputing.com/software/pyqt/download)

##Running the Visualizer:
###Windows:
1. Clone the repo to obtain the source code
2. Download and install `Python3`
3. Download and install `PyQt 4`
4. Open a `command prompt` and navigate to the cloned repo's directory using the `cd` command
5. Run the following command, `python diskmap.py` to launch the Visualizer

###Linux:
1. Clone the repo to obtain the source code
2. If needed, install python3 by running the command `sudo apt-get install python3` from the terminal
3. To install PyQt 4 run the following command from the terminal `sudo apt-get install python3-pyqt4`
4. Navigate to the cloned repo's directory from the terminal using the `cd` command
5. Run the following command from the terminal, `python3 diskmap.py` to launch the Visualizer

##Troubleshooting:
This application is cross platform compatible with most operating systems (Windows, Linux and Mac). If the application crashes, a log is generated in the application's directory. This log contains error and exception details on why the application crashed. Please refer to the known issues below when reading the crash log.
####PermissionError: [WinError 5] Access is denied:
This occurs when you do not have permission on your user account to read files and folders on a Windows operating system. Windows, by default, is known to restrict access to specific protected files. This issue can be resolved by running `Diskmap` as an Administrator.

##License:
Copyright (c) 2016 Salinder Sidhu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
