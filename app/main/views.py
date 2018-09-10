from flask import render_template
from . import main
from .forms import PitchForm
from ..models import User,Pitch
from ..import db

@main.route('/')

def index():

    '''
    View root function that returns the index page
    '''

    return render_template('index.html')

@main.route('/pitch/new',methods=["GET","POST"])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title = form.title.data, body = form.body.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Nice pitching!')
        return redirect (url_for('main.new_pitch'))
    title = "Show us what you've got"
    pitches = Pitch.query.all()

    return render_template('pitch.html', title=title, form=form, pitch_list=pitches)