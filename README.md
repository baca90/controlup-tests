# ControlUp Tests

## Requirements

1. Python >=__3.10__
2. PIP

## Setup

1. Verify default_config.ini, especially username, password. All variables can be set as environment variable. If not exists, then configuration
   from default_config.ini will be taken.



## Installation

1. Run following command from project root:

   pip install -r requirements.txt

## Run examples
1. run all tests in module using command:
   - using shell, go to repository root (controlup-tests)
   - run command ``pytest .\controlup-tests\tests\``
2. run tests from module using PyCharm run configuration (recommended)
   - open Pycharm, click File -> Open and choose cloned repository
   - in terminal tab at IDE bottom run command ``pip install -r requirements.txt``
   - venv environment should be created automatically
   - go to Run -> Edit Configurations
   - add new configuration -> pytest
   - set ``control_up.tests`` as module to run
   - set working directory to path which ends in project root, e.g. ``/Users/myuser/repositories/controlup-tests``
   - click Run
   - Report will show after a test run in output folder