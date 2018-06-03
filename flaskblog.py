from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = '88602628d7c83008fa8b1ecd01691ba8'

posts = [
    {
        'author': 'Weilin Zou',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '6/3/18'
    },
    {
        'author': 'Not Me',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '6/3/18'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
