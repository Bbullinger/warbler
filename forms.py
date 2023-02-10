from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, URL, InputRequired


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField("text", validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])
    image_url = StringField("(Optional) Image URL")


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class UserProfileForm(FlaskForm):
    """Form for adding details to User profile"""

    username = StringField("Username")
    email = StringField("E-mail")
    image_url = StringField("(Optional) Image URL")
    location = StringField("Location", validators=[Length(max=30)])
    bio = StringField("Biography", validators=[Length(max=250)])
    header_image_url = StringField("Header")
    password = PasswordField("Password", validators=[InputRequired()])
