from flask import Blueprint, render_template, redirect, url_for
from app.forms.shipping_form import Shipping
from app.models import Package, db

index_bp = Blueprint("index", __name__, url_prefix="/")

@index_bp.route("/")
def index():
    title = 'Package Tracker'
    body = 'Welcome! Package status home page'
    packages = Package.query.all()
    return render_template("package_status.html", title=title, body=body, packages=packages)
    # return '<h1> welcome </h1>'


@index_bp.route("/new_package", methods = ['GET', 'POST'])
def new_package():
    form = Shipping()
    if form.cancel.data:  #form.cancel is the cancel SubmitField
        # which causes form.cancel.data to be True when clicked
        return (f"""<h1>Cancelled</h1>
                <a href="{url_for('.index')}">Return to home</a>""")

    if form.validate_on_submit():
        data = form.data
        Package.advance_all_locations() # movement simulation. moves all packages one city closer to destination
        new_package = Package(sender=data["sender"],
                              recipient=data["recipient"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"],
                              express=data["express"])
        db.session.add(new_package)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('shipping_request.html', form = form)
