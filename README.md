### Prereqsites
 1. python3.7

###Setting Up

To set up the environment, update below environment variable  
1. Environment = QA/


## Dependencies
### Create virtual environment  
    virtualenv venv
    source venv/bin/activate


###Install the required python dependencies by running the command  
    pip install -r requirments.txt

## Running Test Cases 
```py.test  tests/api_tests/ --alluredir=result```
where result is the allure directory


## How to serve Allure Report
```allure serve result```