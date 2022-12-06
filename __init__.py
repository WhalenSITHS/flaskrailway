from flask import Flask, render_template
import os

import me.me

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if __name__ == '__main__':
        app.run(debug=True, port=os.getenv("PORT", default=5000))
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

  
    @app.route("/")
    def index():
        return render_template('index.html', me=me)

   
    @app.route('/interest/<path:interest>')
    def getInterest(interest):
        def getInterest(interest, user):
            try:
                for element in user["interests"]:
                    if interest in element['name']:
                        return element
            except:
                return 'Not Found'
            
        
        data = getInterest(interest, me)
        return render_template('interest.html', data=data)
    
    return app
    