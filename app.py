from flask import Flask, render_template

app = Flask (__name__)

menu_items = [
    {"id": 1,'title': "Шашлык из баранины", "price": 400},
    {"id": 1,'title': "Шашлык из свинины", "price": 300},
    {"id": 1,'title': "Шашлык из курицы", "price": 500}
]

@app.route("/")

def index():
    return render_template("index.html", menu_items=menu_items)

if __name__ == '__main__':
    app.run()
           