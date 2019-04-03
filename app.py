from flask import Flask, render_template


app = Flask(__name__)
app.static_url_path='/static'

@app.route('/')
def index():
    return render_template('temp.html')


if __name__ == "__main__":
    app.run()