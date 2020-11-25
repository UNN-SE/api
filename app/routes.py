from flask import send_file

from app import app

@app.route('/')
def hello_world():
    return 'TODO render main page'
    
@app.route('/api/photo/<int:photo_id>')
def photo_get_by_id(photo_id):
    return send_file('static/mock/lena.png', mimetype='image/png')