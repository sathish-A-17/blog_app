from blog_app import app,db
from blog_app.models import User

if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()






