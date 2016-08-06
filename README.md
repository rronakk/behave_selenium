Sample Automated test using behave and selenium
=============
### Table of Contents
- [Introduction: Installation and Dependencies](#introduction)
- [Running Tests](#running-tests)
- [Future Improvements](#future-improvement)


## <a name="introduction"></a>Introduction: Installation and Dependencies

This repo is compatible with **[python v 3.4+](https://www.python.org/downloads/)+**.

On your machine, make a directory for your python projects if you've not already and clone the project:
```
mkdir python_projects; cd python_projects

git clone https://github.com/{your_user_name}/UI-Automation.git

cd {your_clone_directory_name}
```

install the desired python package required for this repo by running.
```
pip install -r requirements.txt
```
Logs of the packages being downloaded will display in your shell, and you'll be good to go.

Key packages used in this repo :
- [python-selenium-binding](http://selenium-python.readthedocs.io/)
- [behave](http://pythonhosted.org/behave/)

## <a name="#running-tests"></a>Running Tests
Running test is pretty straight forward using behave.
cd into the directory where feature files are located.
for e.g. in this case, assuming you are inside project directory.
```
cd coding_challenges/features
```
Run the below command with intended feature file to run your test:
e.g :
```
behave amazon.feature
```
## <a name="#future-improvement"></a>Future Improvements

- Make use of page object model.
- seperate out locator startegies of web element into a seperate file, to make tests easy to maintain.
- Adding more logging, making it easier to debug.




