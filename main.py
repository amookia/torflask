from flask import Flask,request,url_for,redirect,render_template
from lib.on import get_price
from functools import wraps
import os
app = Flask(__name__)

def link_verify(func):
    @wraps(func)
    def verfication():
        get = os.popen('cat /var/lib/tor/hidden_service/hostname')
        out = get.read().replace('\n','')
        if request.host == out:
            return func()
        else:
            return 'It works'
    return verfication

@app.route('/link')
def get_link():
    get = os.popen('cat /var/lib/tor/hidden_service/hostname')
    out = get.read()
    return out


@app.route('/')
@link_verify
def home():
    return render_template('price.html',price=get_price())


@app.route('/<path:st>')
def not_found(st):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000)
