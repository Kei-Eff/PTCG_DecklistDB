from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("homepage.html")


    @app.route("/profile")
    def profile():
        return render_template("profile.html")


    @app.route("/user_decks")
    def user_decks():
        return render_template("user_decks.html")


    @app.route("/decks/<id>/")
    def deck(id):
        return render_template("deck.html")


    @app.route("/decks")
    def decks():
        return render_template("decks.html")

    @app.route("/decks/new/")
    def create_deck():
        return render_template("create_deck.html")


    @app.route("/user_index")
    def users():
        return "List of users registered on this website."


    @app.route("/cards")
    def cards():
        return "Card search page."

    @app.route("/decks/<id>/add_card/")
    def add_card(id):
        return render_template("add_card.html")


    @app.route("/login")
    def login():
        return render_template("login.html")


    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)

    return app