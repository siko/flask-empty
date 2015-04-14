from app.core.models.resource import Resource

class Repository():

    def getResources(self):

        resources = []
        resources.append(Resource('Large app how to', 'https://github.com/mitsuhiko/flask/wiki/Large-app-how-to'))

        return resources