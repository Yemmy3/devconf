from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length


class ProductForm(FlaskForm):
    item_name = StringField('Product Name',validators=[DataRequired()])
    item_price = StringField('Product Price',validators=[Length(min=4)])
    submit = SubmitField('Add Product')

class MakeForm(FlaskForm):
    post_title = StringField('Post Title',validators=[DataRequired(message="Your post must come with title")])
    post_content = TextAreaField('Post Content',validators=[DataRequired(message="You need to supply the content"),Length(min=10, message="The content can not be less than 10 characters bros")])
    submit = SubmitField('Post')