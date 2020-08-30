# cd Flask_blog
# set FLASK_APP=flaskblog.py
# python -m flask run
"""set FLASK_DEBUG=1

"""

from flaskblog import app

if __name__ == '__main__':
	app.run(debug=True)