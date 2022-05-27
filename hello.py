from flask import Flask, request, jsonify
import flask_excel as excel

app = Flask(__name__)

@app.route("/")
def hello():
 return "hello"

@app.route("/download", methods=['GET'])
def download_file():
	#return("hello world")
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv")

if __name__ == "__main__":
    excel.init_excel(app)
    app.run()




