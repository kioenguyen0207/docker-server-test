from resources import *

#init
app = Flask(__name__)
api = Api(app)

#endpoint(s)
api.add_resource(Test, "/")

if __name__=='__main__':
    app.run(ssl_context='adhoc', host="0.0.0.0", port=443)
    # app.run()