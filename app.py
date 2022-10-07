from flask import Flask
app = Flask(  
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
# Set secret key
app.secret_key = "secret key"