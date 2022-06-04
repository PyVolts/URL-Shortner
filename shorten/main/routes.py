from flask import render_template, request, Blueprint, flash, url_for, redirect
from shorten.main import utils
from shorten.main.forms import shortURL
from shorten.models import urls
from shorten import db
from validators import url
main = Blueprint('main', __name__)


# TODO create real database; using dict for time being

@main.route('/', methods=['GET', 'POST'])
def home():
    # TODO if request made; check against db to see if custom url exist if provided; else create random url (also check for duplicate)
    # TODO then enter new url into db
    # TODO then display short url as hyper link on page
    form = shortURL()
    link = ""
    if form.validate_on_submit():
        valid = url(form.original_url.data)
        if not valid:
            flash('Invalid URL')
            redirect(url_for('main.home'))
        if len(form.custom_url.data) > 0:
            check_url = urls.query.filter_by(short_url=form.custom_url.data).first()
            if check_url is not None:
                flash('URL taken')
                redirect(url_for('main.home'))
            else:
                new_url = urls(original_url=form.original_url.data,short_url=form.custom_url.data)
                db.session.add(new_url)
                db.session.commit()
                flash('Success')
                link = "http://localhost:5000/" + form.custom_url.data
         
        else:
            custom = utils.generate_short_id(5)
            while urls.query.filter_by(short_url=custom).first():
                custom = utils.generate_short_id(5)
            
            new_url = urls(original_url=form.original_url.data,short_url=custom)
            link = "http://localhost:5000/" + custom
            db.session.add(new_url)
            db.session.commit()
            flash('Success')
            redirect(url_for('main.home'))
            
    
    
    return render_template('index.html', form=form, link=link)

@main.route('/<short_id>')
def redirct_url(short_id):
    # TODO check if short_id is present in database
    url = urls.query.filter_by(short_url=short_id).first()
    if url:
        return redirect(url.original_url)
    else:
        return redirect(url_for('main.home'))
