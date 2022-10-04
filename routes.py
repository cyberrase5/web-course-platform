from app import app
from flask import render_template, request, redirect
import users, courses

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    if users.login(username, password):
        return redirect("/")
    else:
        return render_template("error.html", message="Väärä käyttäjätunnus tai salasana (todennäköisesti)")
    

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        firstname=request.form["firstname"]
        lastname=request.form["lastname"]
        username=request.form["username"]
        password = request.form["password"]
        proof = request.form["teacherness"]
        role=int(request.form["type"])
        pos = "opiskelija"
        bool = False
        if role == 1:
            pos = "opettaja"
            bool = True
            if users.authenticate_teacherness(proof) == False:
                return render_template("error.html", message="Et ole oikeasti opettaja, et tiedä salasanaa")

        if users.register(firstname, lastname, password, username, bool):
            return render_template("reg.html", fname=firstname, lname=lastname, uname=username, role=pos)
        else:
            return render_template("error.html", message="Rekisteröityminen epäonnistui, käyttäjänimi todennäköisesti jo käytössä")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/course/<int:id>")
def course(id):
    data = courses.course(id)
    return render_template("course.html", id=id, data=data)

@app.route("/allCourses")
def allCourses():
    list = courses.list_courses(1)
    return render_template("allCourses.html", list=list)

@app.route("/myCourses")
def myCourses():
    print()


@app.route("/createCourse", methods=["GET", "POST"])
def createCourse():
    if request.method == "GET":
        return render_template("createCourse.html")
    if request.method == "POST":
        name=request.form["name"]
        desc=request.form["description"]
        if courses.create_course(name, desc):
            return redirect("/")
        else:
            return render_template("error.html", message="Virhe, samanniminen kurssi on jo olemassa, lisää esim. syksy 2022")
        

@app.route("/error")
def error():
    return render_template("error.html")

