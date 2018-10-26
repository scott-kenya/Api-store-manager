import os
from app import create_app
#from app import create_tables

app = create_app("development")


if __name__ == '__main__':
	app.run(debug=True)