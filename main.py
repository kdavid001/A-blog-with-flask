import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def blog():
    response = requests.get(f'https://api.npoint.io/950904c4ef53f07bab33')
    data = response.json()
    titles = []
    subtitle = []
    for n in data:
        titles.append(n['title'])
        subtitle.append(n['subtitle'])
    return render_template("index.html", titles=titles, subtitle=subtitle)

@app.route("/post/<int:num>")
def post(num):
    response = requests.get(f'https://api.npoint.io/950904c4ef53f07bab33')
    data = response.json()

    return render_template("post.html",data=data, num=num)



if __name__ == "__main__":
    app.run(debug=True)
