from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

@app.route('/')
def index():	
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

#Retrieves the user input desired search and then creates a giphy object that contains all the images from that search
@app.route('/results')
def results():
	searchterm = request.values.get('name')
	giphyobject = giphypop.Giphy()
	results = giphyobject.search(searchterm) 
	return render_template('results.html', results=results)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
