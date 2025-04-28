-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# GitHub Login Test

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notes](#notes)

## Introduction
The GitHub Login Test project automates the process of logging into GitHub.  
It is useful for QA engineers, developers, and testers who want to validate authentication functionality automatically using Selenium and Pytest.

## Installation

### Setting up the Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv/Scripts./activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Install the necessary packages:
   ```bash
   pip install selenium pytest pytest-html
   ```

## Usage
1. **Run the test**:
   - To run the test and generate an HTML report, use:
     ```bash
     pytest tests/log/test_log.py --html=report.html
     ```

2. **View the report**:
   - After running the test, open the `report.html` 

## Project Structure
```bash
GithubLoginTest/
├── venv                  # Virtual environment
├── tests/log              # Test files
│     └─ test_log.py       # Login test script
├── report.html            # HTML report
```

## Notes
- Ensure you have Python installed on your system before running the script.
- Always activate the virtual environment before running any command to ensure dependencies are properly managed.

markx98!
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
