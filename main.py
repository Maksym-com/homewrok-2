from flask import Flask, render_template

app = Flask(__name__)

workers_list = [
    {"name": "John", "work": 'сhief'},
    {"name": "George", "work": 'cook'},
    {"name": "Mark", "work": 'cook'},
    {"name": "Leo", "work": 'waiter'},
]

menu_list = [
    {'name': 'Margherita', 'ingredients': 'tomato sauce, mozzarella, basil.', 'price': '3.5$'},
    {'name': '4 cheeses', 'ingredients': 'parmesan, emmental, ricotta, gorgonzola.', 'price': '4$'},
    {'name': '4 seasons', 'ingredients': 'tomato sauce, salami, ham, arugula, tomato, feta, cherry, mozzarella, oregano.', 'price': '6$'},
    {'name': '4 meats', 'ingredients': 'tomato sauce, bacon, marinated chicken, ham, fresh tomatoes, mozzarella ', 'price': '4$'},
    {'name': 'Vegetarian with tofu', 'ingredients': 'tomato sauce, tofu cheese, mushrooms, tomatoes, corn, onions, olives, herbs', 'price': '5$'},
]


@app.route('/')
@app.route('/home')
def first_page():
    return render_template("index.html", title='Home page')

@app.route('/menu')
def menu():
    menu_info = {
        "title": "Меню",
        "block_title": "Menu",
        "menu": menu_list
    }
    return render_template("menu.html", **menu_info)

@app.route('/images')
def photos():
    images_info = {
        'block_title': "Images"
    }
    return render_template("images.html", **images_info)

@app.route('/about')
def info():
    worker_info = {
        "title": "Інформація",
        "block_title": "Workers",
        "workers": workers_list
    }
    return render_template("info.html", **worker_info)




if __name__ == "__main__":
    app.run(debug=True)