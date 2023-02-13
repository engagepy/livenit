import os
import iss
from flask import render_template, flash
import forms
from replit import db
from weathers import weather
from airport import airport_message
from crypto import coin
from primes import prime
from analysis import reverse, NonAlphanumeric
from superhero import superhero
from gpt import generate
from __main__ import app


@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/gpt', methods=['GET', 'POST'])
def gpt():
    name = None
    form = forms.gpt_form()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        x = str(generate(name))
        flash(x)
    return render_template('gpt.html', name=name, form=form)


@app.route('/community', methods=['GET', 'POST'])
def user():
    name = None
    form = forms.first_user_form()

    if form.validate_on_submit():
        name = form.name.data

        db["user"] += name
        form.name.data = ''
        email_id = form.email.data
        db["email"] += email_id
        form.email.data = ''
        flash("Cool, you're signed up ")
    return render_template('user.html', name=name, form=form)


@app.route('/iss', methods=['GET', 'POST'])
def iss_page():
    name = None
    form = forms.iss_form()
    if form.validate_on_submit():
        os.system('python iss.py')
        name = form.name.data.strip()
        form.name.data = ''
        flash(iss.message())
    return render_template('iss.html', name=name, form=form)


@app.route('/tax', methods=['GET', 'POST'])
def tax_page():
    total = 0
    tax = 0
    pre_tax = 0
    tax_amount = 0
    form = forms.tax_form()

    if form.validate_on_submit():
        total = form.total.data
        form.total.data = ''
        tax = form.tax.data
        tax_1 = (tax + 100) / 100
        form.tax.data = ''

        pre_tax = total / tax_1
        tax_amount = total - pre_tax

        flash('Total, Tax, Pre-Tax Total & Tax Amount - That Easy! Refer Us. ')

    return render_template('tax.html',
                           total=total,
                           tax=tax,
                           pre_tax=round(pre_tax, 2),
                           tax_amount=round(tax_amount, 2),
                           form=form)


@app.route('/flight', methods=['GET', 'POST'])
def airport_page():
    airport = None

    form = forms.airport_form()

    if form.validate_on_submit():
        airport = form.airport.data.strip()
        form.airport.data = ''
        x = airport_message(airport)
        flash(x['name'])
        flash(x['city'])
        flash(x['country'])
        flash(x['phone'])
        flash(x['website'])
        flash(x['icao'])

    return render_template('airport.html', airport=airport, form=form)


@app.route('/weathers', methods=['GET', 'POST'])
def weathery():

    city = None
    form = forms.weather_form()
    if form.validate_on_submit():
        city = form.city.data.strip()
        form.city.data = None
        x = weather(city)
        print(x)
        for i in x[0:]:
            flash(i)

    return render_template('weather.html', city=city, form=form)


@app.route('/crypto', methods=['GET', 'POST'])
def btc():
    symbol = None
    form = forms.crypto_form()
    if form.validate_on_submit():
        symbol = form.symbol.data.strip()
        form.symbol.data = ''
        result = coin(symbol)
        flash(result[0])
        flash(result[1])
        flash(result[2])
        flash(result[3])
        flash(result[4])
        flash(result[5])
        print("btc_run")
    return render_template('crypto.html', symbol=symbol, form=form)


@app.route('/analysis', methods=['GET', 'POST'])
def reverse_page():
    name = None
    form = forms.reverse_form()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
        result = reverse(name)
        alpha_num = NonAlphanumeric(name, result[5])

        alpha = f"Alphabets: {result[0]}"
        digit = f"Digits: {result[1]}"
        upper = f"Uppercase: {result[2]}"
        lower = f"lowercase: {result[3]}"
        num = f"Special: {alpha_num[0][0]}"
        space = f"Spaces Used: {result[4]}"
        total = f"Character Count: {alpha_num[3]}"
        char = f"Unique Special Types {alpha_num[2]}"
        flash(alpha)
        flash(upper)
        flash(lower)
        flash(space)
        flash(digit)
        flash(num)
        flash(total)
        flash(char)
    return render_template(
        'reverse.html',
        name=name,
        form=form,
    )


@app.route('/prime', methods=['GET', 'POST'])
def prime_page():
    name = None
    form = forms.prime_form()
    count = None
    mathops = None

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
        result = prime()

        flash(result[0])
        mathops = result[2]
        count = result[3]
    return render_template('prime.html',
                           name=name,
                           form=form,
                           count=count,
                           mathops=mathops)


@app.route('/nft', methods=['GET', 'POST'])
def nft():
    return render_template('nft.html')


@app.route('/superhero', methods=['GET', 'POST'])
def superhero_page():
    name = None
    form = forms.superhero_form()

    if form.validate_on_submit():
        name = form.superhero.data
        form.superhero.data = " "
        data = superhero(name)
        n = data['name']
        a = data['powerstats']
        intelligence = f"Intelligence: {a['intelligence']}"
        strength = f"Strength: {a['strength']}"
        speed = f"Speed: {a['speed']}"
        durability = f"Durablity: {a['durability']}"
        power = f"Power: {a['power']}"
        combat = f"Combat: {a['combat']}"
        flash(n)
        flash(intelligence)
        flash(strength)
        flash(speed, durability)
        flash(power)
        flash(combat)

    return render_template('superhero.html', name=name, form=form)
