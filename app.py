import requests
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

# create Flask app
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

# GET request to ip.jsontest.com
def home():
# My microservice!!!
    return render_template('home.html')

def rest_request_example():
	links = ["http://129.157.179.180:3000/fighters/45/0/red/mariaApp", "http://129.157.179.180:3000/fighters/45/1/red/mariaApp", "http://129.157.179.180:3000/fighters/45/2/red/mariaApp", "http://129.157.179.180:3000/fighters/45/3/red/mariaApp", "http://129.157.179.180:3000/fighters/45/4/red/mariaApp", "http://129.157.179.180:3000/fighters/45/5/red/mariaApp", "http://129.157.179.180:3000/fighters/45/6/red/mariaApp", "http://129.157.179.180:3000/fighters/45/7/red/mariaApp", "http://129.157.179.180:3000/fighters/45/8/red/mariaApp", "http://129.157.179.180:3000/fighters/45/9/red/mariaApp"]
	for url in links:
		page = requests.get(url)
		print(page.text)

def read_db_SQL_example():
    conn = db.get_engine().connect()
    sql = "SELECT * FROM SampleTable"
    results = conn.execute(sql)
    rows = ""
    for row in results:
        rows = rows + ','.join(row) + "<br/>"
    print(rows)
	
rest_request_example()
try:
	read_db_SQL_example()
except:
	print ('Could not connect to database')
	
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
