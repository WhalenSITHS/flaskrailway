from flask import Flask, render_template
import os

me = {
    "first_name":"Michael",
    "last_name" : "Whalen",
    "occupation" :"Teaching",
    "interests": [{'name':"Video Games", "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvryjc1XPfXADvT7nPvNSnHYx7turyVMmwvA&usqp=CAU","desc":"Video Games are cool"}, {"name" : "Football", "image":"https://images.unsplash.com/photo-1566577739112-5180d4bf9390?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1926&q=80", "desc":"I love fantasy football and all the stats surrounding it"}, {"name":"Programming", "image":"https://images.unsplash.com/photo-1587620962725-abab7fe55159?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZ3JhbW1pbmd8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60", "desc":"I love programming and building web apps. There's always something new to learn"}],
    "meme":"https://i.imgflip.com/6zu3w0.jpg"
}

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
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

app = create_app()
app.run(debug=True, port=os.getenv("PORT", default=5000))