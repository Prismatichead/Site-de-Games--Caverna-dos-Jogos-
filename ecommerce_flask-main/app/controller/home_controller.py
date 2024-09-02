from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Eletrônicos"), Category(2, "Livros"), Category(3, "Outros")]
products = [
    Product(1, "Câmera", 1200.00, 1, "Câmera digital de alta resolução.", [
        "https://blog.bbbaterias.com.br/wp-content/uploads/2018/06/205868-tipos-de-camera-fotografica-qual-devo-escolher-1023x640.jpg",
        "https://blog.bbbaterias.com.br/wp-content/uploads/2018/06/205868-tipos-de-camera-fotografica-qual-devo-escolher-1023x640.jpg",
        "https://blog.bbbaterias.com.br/wp-content/uploads/2018/06/205868-tipos-de-camera-fotografica-qual-devo-escolher-1023x640.jpg",
        "https://blog.bbbaterias.com.br/wp-content/uploads/2018/06/205868-tipos-de-camera-fotografica-qual-devo-escolher-1023x640.jpg",
        "https://blog.bbbaterias.com.br/wp-content/uploads/2018/06/205868-tipos-de-camera-fotografica-qual-devo-escolher-1023x640.jpg"
    ]),
    Product(2, "Livro de Python", 45.00, 2, "Aprenda Python facilmente.", [
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
    ]),
    Product(3, "Action Figure Spider-Man", 29.95, 3, "Boneco articulado do Spider-Man, perfeito para colecionadores.", [
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
    ]),
    Product(4, "Carro Hot Wheels", 9.99, 3, "Carro Hot Wheels edição limitada, modelo esportivo.", [
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
    ]),
    Product(5, "Mouse Gamer RGB", 35.00, 3, "Mouse gamer com iluminação RGB e alta precisão.", [
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
    ]),
    Product(6, "Cadeira de Escritório Ergonômica", 189.99, 3, "Cadeira de escritório ergonômica com suporte lombar ajustável.", [
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=Product.all_products)
