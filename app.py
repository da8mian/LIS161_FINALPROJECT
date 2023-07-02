from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/establishments/<cafe_area>')
def establishments(cafe_area):
    cafes_list = read_cafes_by_cafe_area(cafe_area)
    return render_template("establishments.html", cafe_area=cafe_area, cafes=cafes_list)

@app.route('/establishments/<int:cafe_id>')
def cafe(cafe_id):
    cafe = read_cafe_by_cafe_id(cafe_id)
    return render_template("cafe.html", cafe=cafe)

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['post'])
def processing():
    cafe_data = {
        "cafe_area": request.form['cafe_area'],
        "name": request.form['cafe_name'],
        "desc": request.form['cafe_desc'],
        "url": request.form['cafe_url'],
        "address": request.form['cafe_address'],
        "time": request.form['cafe_time'],
        "outlet": request.form['cafe_outlet'],
        "parking": request.form['cafe_parking'],
        "number": request.form['cafe_number'],
        "email": request.form['cafe_email'],
        "website": request.form['cafe_website'],
        "fb": request.form['cafe_fb'],
        "ig": request.form['cafe_ig'],
    }
    insert_cafe(cafe_data)
    return redirect(url_for('establishments', cafe_area=request.form['cafe_area']))


@app.route('/modify', methods=['post'])
def modify():
    # 1. identify whether user clicked edit or delete
       # if edit, then do this:
    if request.form["modify"] == "edit":
        # retrieve record using id
        cafe_id = request.form["cafe_id"] 
        cafe = read_cafe_by_cafe_id(cafe_id)
        # update record with new data
        return render_template('update.html', cafe=cafe)
    # if delete, then do this
    elif request.form["modify"] == "delete":
        cafe_id = request.form["cafe_id"] 
        cafe = read_cafe_by_cafe_id(cafe_id)
        delete_cafe(cafe_id)
        return redirect(url_for('establishments', cafe_area=cafe['area']))

@app.route('/update', methods=['post'])
def update():
    cafe_data = {
        "cafe_id" : request.form["cafe_id"],
        "cafe_area": request.form['cafe_area'],
        "name": request.form['cafe_name'],
        "desc": request.form['cafe_desc'],
        "url": request.form['cafe_url'],
        "address": request.form['cafe_address'],
        "time": request.form['cafe_time'],
        "outlet": request.form['cafe_outlet'],
        "parking": request.form['cafe_parking'],
        "number": request.form['cafe_number'],
        "email": request.form['cafe_email'],
        "website": request.form['cafe_website'],
        "fb": request.form['cafe_fb'],
        "ig": request.form['cafe_ig'],
    }
    update_cafe(cafe_data)
    return redirect(url_for('cafe',cafe_id = request.form['cafe_id']))



if __name__ == "__main__":
    app.run(debug=True)