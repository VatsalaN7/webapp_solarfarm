# INIT
# LOAD MODULES

from flask import Flask, render_template, request, make_response
from openpyxl import load_workbook

# FLASK settings and INIT
host_name = "localhost"
host_port = 5000
app       = Flask(__name__)

# Read Excel and Generate HTML Table
@app.route("/")
def homepage():
	""" Display the hyperlinks for viewing the data """
	return render_template("display.html")



@app.route("/testing/<string:test>", methods=["POST", "GET"])
def testing(test):
	""" View function for displaying one aspect of the data """
	if test == 'Quadrats':
		return render_template("test.html", message=test)


@app.route("/displaySubset/<string:test>", methods=["POST", "GET"])
def displaySubset(test):
	""" View function for displaying one aspect of the data """
	if test == 'Quadrats':
		return render_template("display.html", message=test)

	return render_template("display.html")
	#if type == 'Quadrats':
	#	book  = load_workbook("static/PollinatorData/Field_data_2021_Quadrats_Anonym.csv")
	#	sheet = book.active
	#	return render_template("display.html", sheet=sheet, type=type)
	#return render_template("display.html")



@app.route("/test/<string:type1>", methods=["POST", "GET"])
def test():
	if type1 == "Transects":
		return render_template("test.html")

# START
if __name__ == "__main__":
	app.run(host_name, host_port)