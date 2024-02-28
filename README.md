# Diskmap

[![Contributors](https://img.shields.io/github/contributors/salindersidhu/Diskmap?style=for-the-badge)](https://github.com/salindersidhu/Diskmap/graphs/contributors) [![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fsalindersidhu%2FDiskmap&countColor=%23263759)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fsalindersidhu%2FDiskmap) [![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=for-the-badge)](/LICENSE.md)

## Overview

Diskmap is a hard drive space visualization utility. This program displays all the files and folders within a selected location as a rectangular map where each rectangle is proportional to the size of the file it represents. Each rectangular tile on the map is selectable; to select it simply hover over the tile with your mouse. Right click on a selected tile to bring up a popup menu containing options to rename, move and delete the selected file. For optimal viewing, it is recommended to use the application in full screen mode. Built using Python and other open source technologies.

<p float="left">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" height="150" width="150">
    <img src="https://pic4.zhimg.com/v2-f7c3d79d423db49691daaf3b78e3fb07_ipico.jpg" height="150" width="150">
</p>

## Features

<p align="left">
	<img src="https://user-images.githubusercontent.com/12175684/72670077-382ee180-3a07-11ea-9301-c2988f09ab13.gif" alt="screen capture"/>
</p>

- Graphical visualization of files and folders
- Rename, move and delete files in the visualizer
- Save screenshots of the visualization

## Prerequisite Software

| Software       | Version   |
| :------------- | :-------- |
| Python         | 3.11+     |

## Getting Started

You will need to setup a python virtual environment and install the project's dependencies.

1. Skip this step if you're using Windows. If you're using Mac or Linux, you may need to install `pip` and `virtualenv` first:

```bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```

2. Navigate to your Diskmap repo and create a new virtual environment with the following command:

```bash
# Windows
python -m venv venv

# Mac or Linux
virtualenv venv
```

3. Enable your virtual environment with the following command:

```bash
# Windows
source venv/Scripts/activate

# Mac or Linux
source venv/bin/activate
```

Your command line will be prefixed with `(venv)` which indicates that the virtual environment is enabled.

4. Install the project's dependencies with the following command:

```bash
pip install -r requirements.txt
```

If you have recently pulled changes from a remote branch, you should re-run the above command to obtain any new dependencies that may have been added to the project.

## Running

1. Enable your virtual environment with the following command:

```bash
# Windows
source venv/Scripts/activate

# Mac or Linux
source venv/bin/activate
```

2. Launch the visualizer with the following command:

```bash
python diskmap.py
```

## Contributing

Please see our [Contributing Guide](/CONTRIBUTING.md) for more info.

## Project Structure

    .
    ├── ...
    ├── assets                      # Assets
    │    ├── icon.svg               # Diskmap window icon
    │    └── ...
    ├── treemap                     # Python Treemap package and it's node data structures
    │   ├── __init__.py             # Package main file generates a recursive treemap of the file structure
    │   ├── dirnode.py              # Directory node data structure
    │   ├── filenode.py             # File node data structure
    │   ├── node.py                 # Node data structure
    │   └── ...
    ├── diskmap.py                  # Main application
    ├── guiwindow.py                # PyQt5 GUI window setup and config
    ├── tileframe.py                # PyQt5 frame for rending the treemap
    ├── requirements.txt            # Dependencies to install with pip
    └── ...
