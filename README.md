# tudelft_X_automated_course_grabber
## New usage of the script
```bash
usage: script.py [-h] -u USERNAME -p PASSWORD {gym,course} ...

Automate booking process with Selenium.

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Your username for login.
  -p PASSWORD, --password PASSWORD
                        Your password for login.

subcommands:
  {gym,course}          Available subcommands
    gym                 Book a gym session for a specific date and time
    course              Book a course session for today
```

### Gym
The `gym` subcommand allows you to book a gym session for a specific date and time.

> If the specified date is before the current date, the script will automatically try to find a spot for **today**.

```bash
usage: script.py -u USERNAME -p PASSWORD gym [-h] date time

positional arguments:
  date        Specify the date in the format DD-MM-YYYY
  time        Specify the time in 24-hour format HH

optional arguments:
  -h, --help  show this help message and exit
```

Example:
```bash
script.py -u "your_username" -p "your_password" gym 01-01-2024 12
```

### Courses
The `course` subcommand allows you to book a course session for today.

> It is the same as the old script.
```bash
usage: script.py course [-h] course_name instructor_name

positional arguments:
  course_name      Specify the course name
  instructor_name  Specify the instructor name

optional arguments:
  -h, --help       show this help message and exit
```

Example:
```bash
script.py -u "your_username" -p "your_password" course "Spartan Workout" "Mascha"
```