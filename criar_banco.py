from fakepinterest import database, app
from fakepinterest import Usuario, Foto

with app.app_context():
    database.create_all()