# # 1. import Flask
# from flask import Flask

# # 2. Create an app, being sure to pass __name__
# app = Flask(__name__)


# # 3. Define what to do when a user hits the index route
# @app.route("/")
# def home():
#     print("Server received request for 'Home' page...")
#     return "Welcome to my 'Home' page!"


# # 4. Define what to do when a user hits the /about route
# @app.route("/about")
# def about():
#     print("Server received request for 'About' page...")
#     return "Welcome to my 'About' page!"


from flask import Flask, jsonify

app = Flask(__name__)

hello_list = ["Hello", "World!"]
hello_dict = {"Hello": "World!"}

@app.route("/")
def home():
    return "Hi"

@app.route("/normal")
def normal():
    return str(hello_list)

@app.route("/jsonified")
def jsonified_list():
    return jsonify(hello_list)

@app.route("/dict")
def dictionary():
    return hello_dict

if __name__ == "__main__":
    app.run(debug=True)


# To run this code open command prompt 
# then type python -m flask run


