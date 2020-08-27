from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length

class LoginForm(FlaskForm):
    username=StringField(label='Username',validators=[DataRequired()])
    password=StringField(label='Password',validators=[DataRequired()])
    remember_me=BooleanField(label='Remember me')
    submit=SubmitField(label='Sign in')


class RegistrationForm(FlaskForm):
    username=StringField(label='Username',validators=[DataRequired()])
    email=StringField(label='Enter email',validators=[DataRequired(),Email()])
    password=StringField(label='password',validators=[DataRequired()])
    password2=StringField(label='Repeat password',
    validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='Register')

    def validate_username(self,username):
        user=User.query.filter(User.username == username).first()
        if user is not None:
            raise ValidationError('please use a different username')

    def validate_email(self,email):
        em=User.query.filter(User.username == email).first()
        if em is not None:
            raise ValidationError('please use a different Email Address')

class EditProfileForm(FlaskForm):
    username=StringField(label='Username',validators=[DataRequired()])
    about_me= TextAreaField(label='About me',validators=[Length(min=0,max=140)])
    submit= SubmitField(label='submit')

    # def __init__(self,original_username,*args,**kwargs):
    #     super(FlaskForm,self).__init__(*args,**kwargs)
    #     self.original_username=original_username

    # def validate_username(self,username):
    #     if username.data!=self.original_username:
    #         user=User.query.filter(User.username == username).first()
    #         if user is not None:
    #             raise ValidationError('please use a different username')
