from flask import Flask, jsonify
from flask_restful import Api, Resource

class Test(Resource):
    def get(self):
        try:
            return {'status': 'OK'}, 200
        except:
            return {'msg': "Something's happened, server is on but your request is incompleted"}, 500