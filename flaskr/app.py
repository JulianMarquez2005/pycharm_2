from flaskr import create_app
from .modelos import db, Usuario, Album, Medio, Cancion
app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


with app.app_context():
    c = Cancion(titulo='pruebas', minutos=2, segundos=25, interprete='Artista')
    u = Usuario(nombre='julian', contrasena='Julian12345')
    a = Album(titulo='Chocoaventuras', anio='2023', description='Album de pruebitas varias', medio=Medio.CD)
    a.canciones.append(c)
    u.albunes.append(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albunes)
    db.session.delete(u)
    print(Album.query.all())
    print(Cancion.query.all())


