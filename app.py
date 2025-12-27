from flask import Flask
from config import Config
from extensions import db, migrate, jwt
from flask import render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app) # enabling JWT

    from routes.auth import auth_bp
    from routes.content import content_bp
    from routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(content_bp)
    app.register_blueprint(admin_bp)

    return app



app = create_app()
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/admin")
def admin_page():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)