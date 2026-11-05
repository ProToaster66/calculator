#Calculator

A Python 3 calculator used from the Terminal, built step by step in SCCM4910.

## What it will do
Add, subtract, multiply and divide two numbers; display the result.

## How to run it
To run file: python3 calculator.py
Operations: + - * /
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer.

repeatable startup script available as run.sh
end program with ^C Keyboard interrupt
sample test 6 * 7 = 42.0

#test stuff
enter virtual environment for testung using:

source /opt/python-venv/sccm-4910/bin/activate
python3 -m pytest --version

ensure pytest is there

command for test script is:
./check.sh

expected output is 5 passed tests
nano $?
to view exit status, 0 is all test passed, 1 is a failed test

