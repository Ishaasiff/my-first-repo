from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def pageFirst():
    return render_template('index.html')

@app.route('/Support.html')
def contact():
    return render_template('Support.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/registration.html')
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)

