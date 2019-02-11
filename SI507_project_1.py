
from flask import Flask, render_template
from lab3_code import *
# * is wildcard for everything
# how can I use codes in lab3 and clsses here?


app = Flask(__name__)
# create instances for Flask application
# set up application

# Routes
@app.route('/')
def bank_hi():
    return '<h1> Welcome to my bank <h1>'

@app.route('/bank/<name>')
def welcome_bank(name):
    bank_inst = Bank(name, Currency)
    return '<h1> Welcome to {} <h1>'.format(bank_inst.name)


@app.route('/dollar/<amt>')
def dollar_amt(amt):
    dollar = Dollar(int(amt))
    if dollar > 1:
        return "{} {}".format(amt,'Dollar')

@app.route('/pound/<amt>')
def pound_amt(amt):
    pound = Pound(int(amt))
    if pound > 1:
        return "{} {}".format(amt, 'Pounds')
    else:
        return "{} {}".format(amt, 'Pound')

@app.route('/yuan/<amt>')
def yuan_amt(amt):
    yuan = Yuan(int(amt))
    return "{} {}".format(amt,'Yuan')

@app.route('/bank/<name>/<currency>/<value>')
def welcome_bank_currency_value(name, currency, value):
    if currency == "dollar":
        currency = Dollar
    elif currency == "pound":
        currency = Pound
    elif currency == "yuan":
        currency = Yuan
    else:
        return 'invalid input for bank'

    return '<h1> Welcome to the {} bank! {} Bank holds the {} currency and currently hold {} of {}. <h1>'.format(name, name, currency.unit_name, value, currency.unit_name)


# Call this file as a main. Run this
# If it's not main, python doesn't run it
if __name__ == '__main__':
    app.run()
# only the class definitions will be imported
