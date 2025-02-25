from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST","GET"]) #decorater/ 
def hello():
 if request.method=="POST":
    name = request.form.get("fname")
    name1 = request.form.get("lname")
    print(f"hello this is first : {name}")
    print(f"hello this is last name : {name1}")

 return render_template("index.html")


@app.route("/about")
def test():
   return "hello about"

if __name__== "__main__":
    app.run(debug=True)