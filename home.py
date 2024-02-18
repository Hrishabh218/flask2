from flask import Flask,render_template

FOI=Flask(__name__)

@FOI.route('/send_html')
def send_html():
    
    return render_template('send_html.html') 

@FOI.route('/connect_static')
def connect_static():



    return render_template('connect_static.html')
    

FOI.run(debug=True)