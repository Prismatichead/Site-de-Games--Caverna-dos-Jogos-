class Product:
    all_products = []  # Define all_products as a class attribute

    def __init__(self, id, name, price, category_id, description, images):
        self.id = id
        self.name = name
        self.price = price
        self.category_id = category_id
        self.description = description
        self.images = images  # List of image URLs

        # Add this product instance to the class-wide list of all products
        Product.all_products.append(self)
