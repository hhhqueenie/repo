from app import app
from flask import render_template
import forms
import processor

#@app.route creating different address to get to the same Flask object
#decor allow index() to be run whenever the route is accessed
#@app.route("/")
@app.route("/")
@app.route("/home", methods = ["GET", "POST"])
def index():
    #render template can do more than opening the file, it allow us to modify file
    f = forms.AddTaskForm()
    if f.validate_on_submit():
        return render_template("success.html", form = f, head2 = processor.do(f.str.data))
    return render_template("index.html", form = f)

@app.route("/about")
def about():
    return render_template("about.html", about_head1="关于这个测试", about_p1="其实是随便写着玩的啦，但这里是一个很有趣的灯光开关",about_head2="Surprise it's just for show")



