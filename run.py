from flask import Flask, render_template, url_for, request
app = Flask(__name__)  

@app.route('/')
@app.route('/home')                  
def index():
    return render_template('index.html')

@app.route('/fruits')         
def fruits():
    return render_template('fruits.html', title='Fruits')

@app.route('/checkout', methods=['GET','POST'])         
def checkout():
    print(request.form)
    return render_template('checkout.html', title='Checkout')

if __name__=="__main__":   
    app.run(debug=True)    