from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('chatbot.html')

if __name__=='__main__':
    app.run(debug=False,host='8000')