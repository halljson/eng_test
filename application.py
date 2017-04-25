from application import application
from config import FLASK_DEBUG
if __name__ == '__main__':
    application.run(debug=FLASK_DEBUG)
