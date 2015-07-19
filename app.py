from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('show_404'))

@app.route('/not-found')
def show_404():
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run()
