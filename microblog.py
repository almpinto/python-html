from flask import Flask

app = Flask("microblog")


@app.route("/") 
def index():
    return "Olá mundo!"

app.run()