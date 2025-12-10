from flask import Flask,render_template,request,redirect
from mydatabase import Database
import nlpcloud

app=Flask(__name__)
db_obj=Database()

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/perform_registration' ,methods=['post'])
def perform_registration():
    f_name=request.form.get('user_first_name')
    l_name=request.form.get('user_last_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    response=db_obj.add_data(f_name,l_name,email,password)

    if response==1:
        return render_template("login.html",message="Registration Successful! Please proceed to login",category="success")
    else:
        return render_template("register.html",message="Email already exists!",category="error")

@app.route("/check_user", methods=["post"])
def check_user():
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    response = db_obj.search_user(email,password)

    if response==0:
        return redirect('/home_page')
    elif response==1:
        return render_template("login.html",message="Please Register First",category="warning")
    else:
        return render_template("login.html",message="Incorrect Email/Password",category="alert")

@app.route('/home_page')
def home_page():
    return render_template("home_page.html")

@app.route('/ner')
def ner():
    return render_template("ner.html")

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text=request.form.get('text_input')
    entity=request.form.get('entity_text')

    client = nlpcloud.Client("gpt-oss-120b", "YOUR_API_KEY", gpu=True)
    response = client.entities(
        text,
        searched_entity=entity
    )
    return response

@app.route('/ld')
def language_detection():
    return render_template('ld.html')

@app.route('/perform_detection', methods=['post'])
def perform_detection():
    text=request.form.get('user_text')
    client = nlpcloud.Client("python-langdetect", "YOUR_API_KEY", gpu=False)
    response=client.langdetection(text)
    return response

@app.route('/analysis')
def sentiment_analysis():
    return render_template('analysis.html')

@app.route('/perform_analysis', methods=['post'])
def perform_analysis():
    text=request.form.get('user_text')
    client = nlpcloud.Client("gpt-oss-120b", "YOUR_API_KEY", gpu=True)
    response=client.sentiment(text,
        target="NLP Cloud"
    )
    return response

app.run(debug=True)