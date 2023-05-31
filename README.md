# Losing-Weight
#### - BMI Calculator
#### - Calories
#### - Recommendations
### Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/OmonovSardorbek/losing_weight.git
$ cd /losing_weight
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install pipenv
$ pipenv shell
```
Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd losing_weight
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
