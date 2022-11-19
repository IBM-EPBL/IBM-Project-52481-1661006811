
#                   Car resale value predication


#                   Team ID - PNT2022TMID47297



# import flask module

from flask import Flask

app = Flask(__name__)

@app.route("/") # for the url

# Example code

def home():             
    return "Anandhakrishnan,  nalan,  jayaram,  ragul<h1>CAR RESALE VALUE PREDICTION<h1>"

if __name__ == "__main__":

    app.run()

# the output terminal show the link.

# and we follow the link to acheive the python flask website.
