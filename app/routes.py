# 1. Importa render_template
from flask import Flask, render_template 
from app.scraper.application.scraper_routes import scraper_bp

@scraper_bp.before_request
def must_be_logged():
    return 

def set_routes(app:Flask) -> None:

    # 2. AÑADE ESTA RUTA PARA LA PÁGINA PRINCIPAL
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health_check():
        return "CAT OK"

    #Auth routes
    #Cat routes
    app.register_blueprint(scraper_bp)
