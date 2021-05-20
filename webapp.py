from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/numberresults")
def render_page1():
    x=request.args['numberrequest'] #setting x to the first number
    x
    return render_template('layout.html', number1=x*x, number2=x*x*x, number3=x*x*x*x, number4=x*x*x*x*x, number5=x*x*x*x*x*x, number6=x*x*x*x*x*x*x, number7=x*x*x*x*x*x*x*x, number8=x*x*x*x*x*x*x*x*x, number9=x*x*x*x*x*x*x*x*x*x, number10=x*x*x*x*x*x*x*x*x*x*x) #rendering results
    
if __name__=="__main__":
    app.run(debug=False)
