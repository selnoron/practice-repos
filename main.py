from flask import Flask
from flask.app import Flask as FlaskApp


app: FlaskApp = Flask(__name__)

@app.route("/home")
def home_page() -> str:
    result: str = "Я <b>знал</b> что ты придешь"
    
        
    return result

@app.route("/")
def main_page() -> str:
    return '''
    <h1 style="color: red">MAIN PAGE</h1>
    <a href="/home">HOME</a> <br> <br>
    '''

if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    )

