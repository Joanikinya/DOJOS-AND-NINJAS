from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.ninja import Ninja

DATABASE = "Dojos_Ninjas"

class Dojo:
    def __init__(self, data:dict) -> None:
        self.ninjas = []
        self.name = data['names']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
        
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (names) VALUES (%(names)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def join_with_ninjas(cls, id):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,{'id': id})
        dojo = Dojo(results[0])
        for item in results:
            temp_ninja = {
                'id': item['ninjas.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'age': item['age'],
                'created_at': item['ninjas.created_at'],
                'updated_at': item['ninjas.updated_at'],
                'dojo_id': item['dojo_id']
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        return dojo