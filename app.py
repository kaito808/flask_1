from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = "mmmm"

debug = DebugToolbarExtension(app)

c = CurrencyRates(force_decimal=False)


@app.route('/')
def home_page():
    """shows home page"""

    return render_template("hello.html")

@app.route('/result') 
def return_result():
    """return the results"""

    original = request.args["convert_from"]
    neww = request.args["convert_to"]
    numm = request.args["amount"]

    ori = original.upper()
    new = neww.upper()
    num = int(numm)

    code = CurrencyCodes().get_symbol(new)
    # rr = c.convert(original, new, Decimal(num))
    rr = c.convert(original, new, num)
    r = format(rr,'.2f')
    # r = c.convert(original, new, float(num))
    return render_template("result.html",oo=code, 
                           nn=new, aa=num, rrr=r)



@app.route('/test')    
def get_rate():
    rr = c.convert('USD', 'INR', 100)
    """try find rates"""

    return render_template("try.html",r = rr)

