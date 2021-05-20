from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/numberresults")
def render_page1():
    x=request.args['number1']
    x
    return render_template('layout.html', number1 number2 number3)
    
if __name__=="__main__":
    app.run(debug=False)
