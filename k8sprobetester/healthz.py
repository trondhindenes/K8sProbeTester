from flask_restful import Resource
from k8sprobetester import app, api

class HealthEndpoint(Resource):
    def get(self):
        #app.logger.info('the healthz!!')
        return {'status': 'ok'}

api.add_resource(HealthEndpoint, '/healthz')