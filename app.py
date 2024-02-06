from flask import Flask,render_template,redirect,request,url_for
App=Flask(__name__)
student_list=[{"Name":"Sivapackia","Age":22 ,"RollNO": 101, "Marks":[90,75,80,98,65]},
                    {"Name":"Siva","Age":21 ,"RollNO": 102, "Marks":[90,75,80,78,99]},
                    {"Name":"Vilobin","Age":21 ,"RollNO": 103, "Marks":[94,75,80,88,35]},
                    {"Name":"Mahadevi","Age":27 ,"RollNO": 104, "Marks":[70,85,80,98,35]},          
                    {"Name":"Nisha","Age":23 ,"RollNO": 105, "Marks":[90,75,85,98,35]},
                    {"Name":"Vaishali","Age":27 ,"RollNO": 106, "Marks":[80,98,35,90,75]},
                    {"Name":"Vijay","Age":22 ,"RollNO": 107, "Marks":[90,80,98,35,75]},
                    {"Name":"Mohamed Ismail","Age":22 ,"RollNO": 108, "Marks":[75,80,90,98,35]},
                    ]
@App.route("/")
def index():
    return render_template("index.html")

@App.route("/login",methods=["GET","POST"])
def login():
    
    Username="Vaishali"
    password="Vaishu123"
    if request.method == "POST":
        Name=request.form.get("username")
        Password=request.form.get("password")
        if Username == Username and password==Password:
            return redirect(url_for("Home"))
        else:
            return "incorrect!!!!!Please check the username and password"
        
    return render_template("login.html")

@App.route("/home")
def Home():
    return render_template("home.html",data=student_list)

@App.route("/addstudent",methods=["GET","POST"])
def Add():
    if request.method == "POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("RollNo")
        Marktamil=request.form.get("Tamil")
        Markenglish=request.form.get("English")
        Markmaths=request.form.get("Maths")
        Markscience=request.form.get("Science")
        Marksocial=request.form.get("Socialscience")
        mark_list=list()
        mark_list.append(int(Marktamil))
        mark_list.append(int(Markenglish))
        mark_list.append(int(Markmaths))
        mark_list.append(int(Markscience))
        mark_list.append(int(Marksocial))
        student_dict={}
        student_dict.update({"Name":Name})
        student_dict.update({"Age":Age})
        student_dict.update({"RollNO":RollNo})
        student_dict.update({"Marks":mark_list})
        student_list.append(student_dict)
        return redirect(url_for("Home"))
    return render_template("add.html")

@App.route("/delete/<int:index>",methods=["GET","POST"])
def delete(index):
    student_list.pop(int(index-1))
    return render_template("home.html",data=student_list)

@App.route("/edit/<int:index>",methods=["GET","POST"])
def edit(index):
    if request.method == "POST":
        edit_name=request.form.get("Name")
        edit_age=request.form.get("Age")
        edit_rollno=request.form.get("RollNo")
        edittamil=request.form.get("Marktamil")
        editenglish=request.form.get("Markenglish")
        editmaths=request.form.get("Markmaths")
        editscience=request.form.get("Markscience")
        editsocial=request.form.get("Marksocialscience")
        edit_mark=[edittamil,editenglish,editmaths,editscience,editsocial]
        student=student_list[int(index-1)]
        student.update({"Name":edit_name})
        student.update({"Age":edit_age})
        student.update({"RollNO":edit_rollno})
        student.update({"Marks":edit_mark})
        return redirect(url_for('Home'))
    student_edit=student_list[int(index-1)]
    return render_template("edit.html",data=student_edit)

if __name__ == ("__main__"):
    App.run(debug=True)