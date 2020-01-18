# Diskmap

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE.md)

# Table of Contents

- [Overview](#overview)
  - [Features](#features)
  - [Supported Platforms](#supported-platforms)
- [Development](#development)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Running](#running)
  - [Contributing](#contributing)
- [Codebase](#codebase)
  - [Structure](#structure)

# Overview:

Diskmap is a hard drive space visualization utility. This program displays all the files and folders within a selected location as a rectangular map where each rectangle is proportional to the size of the file it represents. Each rectangular tile on the map is selectable; to select it simply hover over the tile with your mouse. Right click on a selected tile to bring up a popup menu containing options to rename, move and delete the selected file. For optimal viewing, it is recommended to use the application in full screen mode.

<p align="center">
	<img src="https://user-images.githubusercontent.com/12175684/72670077-382ee180-3a07-11ea-9301-c2988f09ab13.gif" alt="screen capture"/>
</p>

## Features:

- Graphical visualization of files and folders
- Rename, move and delete files in the visualizer
- Save screenshots of the visualization

## Supported Platforms:

- Windows 10, Mac OS X and Linux based distributions

# Development

> Information describing how to install and configure all the required tools to begin development.

## Prerequisites:

Ensure that you have the following installed and configured any environment variables.

- **Python**
  - Version 3.7.5+

## Setup:

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

## Running:

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

Diskmap welcomes contributions from anyone and everyone. Please see our [contributing guide](/CONTRIBUTING.md) for more info.

# Codebase

> Information describing the software architecture and how to maintain it while adding additional functionality.

## Structure

    .
    ├── ...
    ├── assets                      # Assets
    │    ├── icon.svg               # Diskmap window icon
    │    └── ...
    ├── structnodes                 # Python package for Node data structures
    │   ├── __init__.py             # Package init file
    │   ├── dirnode.py              # Directory node data structure
    │   ├── filenode.py             # File node data structure
    │   ├── node.py                 # Node data structure
    │   └── ...
    ├── diskmap.py                  # Main application
    ├── guiwindow.py                # PyQt5 GUI window setup and config
    ├── tileframe.py                # PyQt4 frame for rending the treemap
    ├── treemap.py                  # Logic to generate a recursive treemap of the file structure
    ├── requirements.txt            # Dependencies to install with pip
    └── ...
