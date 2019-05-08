# Python as a Server Side language using Flask. 
# This is a exercise for implementation of a cloud development enverioment.
# I have been testing with larger datasets to test running time and my 2014 Macbook isn't keeping up with it.

#To use Render Template your .html file needs to be inside a Template Folder.
#Flask works as the server side interpreter.
from flask import Flask, render_template             

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    #I have used port 42927 because it is one of the only opened ports in my company proxy(had to bruteforce it).
    app.run(host="127.0.0.1",port=42927,debug=False)