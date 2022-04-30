from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data',methods=['post'])
def data():
    firstname=request.form.get('first_name')
    lastname=request.form.get('last_name')
    phonenumber=request.form.get('phone_number')
    email=request.form.get('email')
    print(firstname,lastname,phonenumber,email)
    return 'data received'

'''HTTP: Hyper text transfer protocol
127.0.0.1: ip address
:5000--port number
/--route'''

app.run(debug=True)