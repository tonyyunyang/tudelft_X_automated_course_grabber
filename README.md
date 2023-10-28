# TU Delft Automated Course Grabber

Automate your course booking at TU Delft with ease. This script helps users to quickly grab their desired courses without manual intervention.

## Pre-requisites

### 1. GeckoDriver Setup

#### Windows & Linux Users:

1. **Installation**:
   - Download GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases).
   - Choose the appropriate `.zip` file based on your system architecture (typically 64-bit).
     
     ![GeckoDriver Download](https://hackmd.io/_uploads/rkd5do9fa.png)

   - Extract the downloaded `.zip` file to get the `.exe` file.

2. **Setting Path**:
   - Create a folder named `geckodriver` in your `C:` drive and move the `.exe` file to this folder.
     
     ![Folder Structure](https://hackmd.io/_uploads/Sks15ocG6.png)
     
   - Add `C:\geckodriver` to your system's PATH:
     - Open `Advanced System Settings` -> `Environment Variables`.
     - Under `PATH`, click `Edit`.
     - Add a new entry: `C:\geckodriver`.

     ![PATH Setup](https://hackmd.io/_uploads/Symb2oqMa.png)

   - Reboot your computer.

**Note**: For Linux users, please figure out things yourself. I believe you :)

#### MacOS Users:

1. Install `brew` from [here](https://brew.sh/).
2. Close the current terminal, open a new one, and run: 
```bash
brew install geckodriver
```


## Requirement 2: Python (For all OS)
Any version of Python would work. I assume you also have python, if not, please follow some tutorials online, there are plenty.

Simply do `pip install selenium` in your terminal, wait for everything to be done. You are good to go.

## Usage:

### Command Line Arguments

The script accepts the following command line arguments:

1. **username**: Your username for login.
2. **password**: Your password for login.
3. **course_name**: Name of the course you want to search for.
4. **instructor_name**: First name of the instructor you want to search for.

### Example

To run the script:

```bash
python script.py "your_username" "your_password" "Spartan Workout" "Mascha"
```
![](https://hackmd.io/_uploads/SkFGz3qG6.png)


## Improtant Note:
1. Please keep in mind that this script is not faster than human speed. It is recommended that you book the courses a day in advance at 13.00.
2. The script is designed for the day the course is scheduled. For instance, if "Hiit" is on Tuesday, run the script on Tuesday.
3. This automation works for instructor-led courses. It's not designed for Gym or Space slots.
