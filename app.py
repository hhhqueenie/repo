#Flask information could be found here: https://pythonbasics.org/what-is-flask-python/
from flask import Flask
from flask import render_template
import forms
import processor

#initialize a flask object
app = Flask(__name__)

#from webpage https://stackoverflow.com/questions/47687307/how-do-you-solve-the-error-keyerror-a-secret-key-is-required-to-use-csrf-whe
app.config.update(dict(
    SECRET_KEY="nyawuwunyanya",
    WTF_CSRF_SECRET_KEY="csrf fffffwwwww"
))

#@app.route creating different address to get to the same Flask object
#decor allow index() to be run whenever the route is accessed
#@app.route("/")
@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])
def index():
    #render template can do more than opening the file, it allow us to modify file
    f = forms.AddTaskForm()
    if f.validate_on_submit():
        result = processor.do(f.str.data)
        return render_template("success.html", form = f, head2 = result[0], head3 = result[1], head4 = result[2], bod = result[3])
    return render_template("index.html", form = f)

@app.route("/about")
def about():
    return render_template("about.html", about_head1="关于这个测试", about_p1="其实是随便写着玩的啦，但这里是一个很有趣的灯光开关",about_head2="Surprise the buttons are just for show")

@app.route("/trick")
def trick():
    return render_template("trick.html")

@app.route("/fancierIndex", methods = ["GET", "POST"])
def fancy():
    f = forms.AddTaskForm()
    if f.validate_on_submit():
        result = processor.do(f.str.data)
        return render_template("fancierSucc.html", form = f, head2 = result[0], head3 = result[1], head4 = result[2], bod = result[3])
    return render_template("fancierIndex.html", form=f)


#something that is like a main() in java
if __name__ == "__main__":
    app.run(debug = True)

#we need to switch to wsgi or something because （开发版本性能太差）
"uwsgi is in charge of connecting socket and it is fast with dynamic code"
"nginx is quick for static code"