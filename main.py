from flask import Flask, render_template, request
import webbrowser
webbrowser.open('http://localhost:5000')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('expression')
        try:
            result = eval(expression)
        except Exception as e:
            result = str(e)
    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run()
