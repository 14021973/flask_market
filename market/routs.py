from flask import render_template, url_for, flash, request
from werkzeug.utils import redirect

from market import app, db
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market.models import Kzitem, Kzuser
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()


    if request.method =='POST':

        # Purchasing logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Kzitem.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_buy(p_item_object):
                p_item_object.add_owner(current_user)
                flash(f"You've purchased item {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"You don't have enough money to buy {p_item_object.name}!", category='danger')

        # Selling logic
        sold_item = request.form.get('sold_item')
        s_item_object = Kzitem.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.remove_owner(current_user)
                flash(f"You've sold item {s_item_object.name} for {s_item_object.price}$", category='success')
            else:
                flash(f"Something went wrong with selling item  {s_item_object.name}!", category='danger')

        return redirect(url_for('market'))

    if request.method =='GET':
        items = Kzitem.query.filter_by(owner=None)
        owned_items = Kzitem.query.filter_by(owner=current_user.Id)
        return render_template('market.html', items=items, purchase_form=purchase_form,owned_items=owned_items,selling_form  = selling_form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():

        user_to_create = Kzuser(username=form.username.data,
                                email_address=form.email_address.data,
                                password=form.password1.data
                                )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfuly! You are now logged in as : {user_to_create.username}', category='success')
        return redirect(url_for('market'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'Errors...:{err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Kzuser.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password1.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as : {attempted_user.username}', category='success')
            return redirect(url_for('market'))
        else:
            flash('Username and password are not correct !', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out !",category='info')
    return redirect(url_for('home_page'))

