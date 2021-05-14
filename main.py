from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/82975389c85afb34e389").json()
post_objects = [
    Post(id_post=post["id"],
         title=post["title"],
         subtitle=post["subtitle"],
         body=post["body"]) for post in posts]


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:blog_id>')
def blog(blog_id):
    request_post = None
    for post in post_objects:
        if post.id == blog_id:
            request_post = post
    return render_template('post.html', blog_id=blog_id, post=request_post)


if __name__ == "__main__":
    app.run(debug=True)
