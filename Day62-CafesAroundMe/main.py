from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, URLField, SelectField
from wtforms.validators import DataRequired, URL 
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField('location', validators=[DataRequired(), URL(), ])
    open_time = TimeField('open', validators=[DataRequired()])
    closing_time = TimeField('closing', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee', validators=[DataRequired()], choices=[('☕️', "☕️"), ('☕️☕️', "☕️☕️"), ('☕️☕️☕️', "☕️☕️☕️")], )
    wifi_rating = SelectField('wifi', validators=[DataRequired()], choices=[('💪', "💪"), ('💪💪', "💪💪"), ('💪💪💪', "💪💪💪")])
    power_rating = SelectField('power', validators=[DataRequired()], choices=[('🔌', "🔌"), ('🔌🔌', "🔌🔌"), ('🔌🔌🔌', "🔌🔌🔌")])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = [
            form.cafe.data,
            form.location_url.data,
            form.open_time.data.strftime("%H:%M"),
            form.closing_time.data.strftime("%H:%M"),
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data
        ]

        with open("cafe-data.csv", mode="a", newline='', encoding="utf-8-sig") as my_csv:
            writer = csv.writer(my_csv)
            writer.writerow(new_cafe)

        return redirect(url_for("cafes"))
    
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8-sig') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
