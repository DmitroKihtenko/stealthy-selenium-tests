# Stealthy Selenium Tests for Stealthy UI
Tests for base service requirements for Stealthy UI based on Selenium
Web driver library.

### Technologies
Build with:
 - Python 3.11.0
 - Selenium 4.20.0

### Requirements
 * installed Python 3.11.0 for development purposes
 * installed `pipenv` for python
 * installed Chrome web browser (chromedriver file path
required)
 * 

### How to up and run
1. Launch Stealthy application components: `stealthy-backend`, `stealthy-ui`.
2. Configure tests using global constants in file `main.py`.
3. Create virtual environment and sync dependencies.
```bash
python -m pipenv sync
```
4. Run tests.
```bash
python main.py
````
