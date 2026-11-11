from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def register():
    return render_template('register.html')

@app.route()