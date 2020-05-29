from flask import Flask,request,url_for,redirect,render_template
from lib.on import get_price
from functools import wraps
app = Flask(__name__)

def link_verify(func):
    @wraps(func)
    def verfication():
        if request.host == 'kgwz6rkpnknsuw7o.onion':
            return verfication
        else:
            return 'It Works'
    return verfication



@app.route('/')
@link_verify
def home():
    return render_template('price.html',price=get_price())


@app.route('/<path:st>')
def not_found(st):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000)
