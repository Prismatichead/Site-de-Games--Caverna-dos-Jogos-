from flask import Blueprint, render_template

from app.model.category import Category

category_bp = Blueprint('category', __name__)

categories = [Category(1, "Eletrônicos"), Category(2, "Livros"), Category(3, "Casa e Cozinha")]

@category_bp.route('/categories')
def list_categories():
    return render_template('categories.html', categories=categories)
