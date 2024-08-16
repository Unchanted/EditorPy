# EditorPy

**EditorPy** is a simple text editor built using Python's `tkinter` library. It allows users to create, open, edit, and save text files.

## Features

- **New File:** Clears the current text area to start a new file.
- **Open File:** Opens an existing text file and displays its content in the text area.
- **Save File:** Saves the current content to the existing file.
- **Save As:** Saves the current content to a new file with a specified name and extension.

## Code Overview

The main features are implemented as follows:

- **new_file():** Clears the text area and sets the filename to "Untitled".
- **save_file():** Saves the content of the text area to the currently open file. If no file is open, it calls `save_as()` to prompt the user to save the file with a new name.
- **save_as():** Prompts the user to save the file with a new name and extension, and writes the content of the text area to the file.
- **open_file():** Opens a dialog to select a file, reads its content, and displays it in the text area.

The graphical user interface (GUI) is built using `tkinter`, with a text area for editing and a menu bar for file operations.

## How to Run the Project

To run **EditorPy**, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Unchanted/EditorPy.git
cd EditorPy
pip install -r requirements.txt
python textEditor.py


---

Arcade6
