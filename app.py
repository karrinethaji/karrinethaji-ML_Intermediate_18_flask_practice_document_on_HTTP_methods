from flask import Flask, render_template,request

app = Flask(__name__)

users={"nethaji":"1234","mahendra":"1234"}

# Default routing
@app.route("/")
def default():
    return render_template("nethaji.html")

# 
@app.route("/post_method",methods=["POST"])
def post_method():
    if request.method=="POST":
        user_name=request.form["user"]
        password=request.form["password"]
        print(user_name, password)
        if user_name in users and users[user_name]==password:
            return f"<h1> Welcome {user_name}, Thanks for using our application :) </h1>"
        else:
            
            return render_template("create.html", user_name=user_name)

    # else:
    #     return render_template("nethaji.html")

# 
@app.route("/create_method",methods=["POST"])
def create_method():
    if request.method=="POST":
        if request.form["user"] in users:
            return "<h1> The user name already exists</h1>"
        else:
            users[request.form["user"]]=request.form["password"]
        print(users)
        return render_template("crete_login.html")
    

    # return render_template("create.html")
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)