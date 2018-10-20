from app import create_app

app = create_app("development")
app = Flask(__name__)



if __name__ == '__main__':
	#port = int(os.environ.get('PORT', 5000))
   	app.run(debug=True)