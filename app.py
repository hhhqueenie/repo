#Flask information could be found here: https://pythonbasics.org/what-is-flask-python/
from flask import Flask
from flask import render_template
import forms
import processor
from redisUse import getAllFrenquency, getAllUserInputs

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
    return render_template("about.html", about_head1="关于这个测试", about_p1="其实是随便写着玩的啦，但这里是一个很有趣的灯光开关",about_head2="这个灯泡好像被我修好了")


@app.route("/secret", methods = ["GET", "POST"])
def secretdata():
    f = forms.SecretForm()
    if f.validate_on_submit():
        return render_template("query.html", form=forms.QueryForm())
    return render_template("secret.html", form=f)


@app.route("/query", methods = ["GET", "POST"])
def querydata():
    f = forms.QueryForm()
    if f.validate_on_submit():
        return render_template("userInput.html", resType="统计", myList=getAllFrenquency())
        # if f.fields.data == "user" :
        #     result = getAllUserInputs()
        #     return render_template("userInput.html", resType="用户" ,myList=result)
        # else: 
        #     result = getAllFrenquency()
        #     return render_template("userInput.html", resType="统计", myList=result)
    return render_template("query.html", form=f)    
# @app.route("/trick")
# def trick():
#     return render_template("trick.html")

# @app.route("/fancierIndex", methods = ["GET", "POST"])
# def fancy():
#     f = forms.AddTaskForm()
#     if f.validate_on_submit():
#         result = processor.do(f.str.data)
#         return render_template("fancierSucc.html", form = f, head2 = result[0], head3 = result[1], head4 = result[2], bod = result[3])
#     return render_template("fancierIndex.html", form=f)

# user = ""
# input = ""

# @app.route("/join", methods = ["GET", "POST"])
# def join():
#     f = forms.OtherForm()
#     if f.validate_on_submit():
#         global user, input
#         user = f.user_name.data
#         input = f.input.data
#         return render_template("userIndex.html", form=forms.AddTaskForm())
#     return render_template("join.html", form = f)

# @app.route("/userIndex", methods = ["GET", "POST"])
# def userIndex():
#     f = forms.AddTaskForm()
#     if f.validate_on_submit():
#         result = processor.input_test(input, f.str.data, user)
#         return render_template("userSuccess.html", form = f, head2 = result[0], head3 = result[1], head4 = result[2], head5 = result[3], bod=result[4])
#     return render_template("userIndex.html", form = f)

# @app.route("/https://sbaladjsbavdf.wordpress.com/")
# def testget():
#     data = request.json  # Retrieve JSON data from WordPress
#     # Process the received data
#     print(data)
#     return 'Data received successfully'

#something that is like a main() in java
if __name__ == "__main__":
    app.run(debug = True)

#we need to switch to wsgi or something because （开发版本性能太差）
"uwsgi is in charge of connecting socket and it is fast with dynamic code"
"nginx is quick for static code"