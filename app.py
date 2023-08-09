# Import Libraries
import os 
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__ )
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    #Write the code for the function here

    return render_template("index.html", **locals())
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True )

