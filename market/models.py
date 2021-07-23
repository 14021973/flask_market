from market import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Kzuser.query.get(user_id)


class Kzuser(db.Model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=55), nullable=False, unique=True)
    email_address = db.Column(db.String(length=55), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=100), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Kzitem', backref='owned_user', lazy=True)


    @property
    def kwota_z_przecinkiem(self):
        if len(str(self.budget))>=4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f'{self.budget}$'
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)

    def get_id(self):
           return (self.Id)

    def can_buy(self, item_obj):
        return self.budget>=item_obj.price

    def can_sell(self, item_obj):
        return item_obj in self.items

class Kzitem(db.Model):
    Id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=55), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=255), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('kzuser.Id'))

    def __repr__(self):
        return f'Item {self.name}'

    def add_owner(self, user):
        self.owner = user.Id
        user.budget -= self.price
        db.session.commit()


    def remove_owner(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()
