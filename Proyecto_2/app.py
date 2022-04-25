#IMPORTS
import json
from urllib import response
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_socketio import SocketIO
import pymongo
from bson import json_util
import datetime

#ENDPOINTS CALLS
from usuarios import usuarios_service


app=Flask(__name__)
CORS(app)
socket = SocketIO(app, cors_allowed_origins="")

##ENDPOINTS

{
    "id_user": "a13asd16655asd3166",
    "user_display_name": "Usuario Usac",
    "user_nickname":"usuario_usac",
    "user_password":"USAC12345",
    "user_age":17,
    "user_career":"Ingeniería en Ciencias y Sistemas",
    "user_carnet": 202213546
}

app.register_blueprint(usuarios_service ,url_prefix="/api/v1/usuarios")

#ENDPOINTS
@app.route('/ping')
def ping():
    try:
        resp = jsonify({"message": "pong!"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"message": "error :("})
        resp.status_code = 503
        return resp

@app.route("/", methods = ["GET","POST","PUT"] )
def init():
    return jsonify({
        "Curso" : "Introducción a la programación y computación 1"
    })

@app.route("/create_user", methods=["POST"])
def create_user():
    if request.method == "POST":
        data = request.json
        if "id_user" in data and "user_display_name" in data and "user_nickname" in data and "user_password" in data and "user_age" in data and "user_career" in data and "user_carnet" in data:
            usuario_insertar = {
                "id_user": data["id_user"],
                "user_display_name": data["user_display_name"],
                "user_nickname": data["user_nickname"],
                "user_password":data["user_password"],
                "user_age":data["user_age"],
                "user_career":data["user_career"],
                "user_carnet":data["user_carnet"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["usuario"]
                respuesta_mongo = mongo_collections.insert_one(usuario_insertar)
                print(respuesta_mongo.inserted_id)
                resp = jsonify({
                    "status":"200",
                    "msg":"response"
                })
                resp.status_code = 200
                return resp
            except Exception as e:
                return Response(jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))    
        else:
            resp = (jsonify({
                "msg":"Petición incorrecta"
            }))
            resp.status_code=401
            return resp
    else:
        return jsonify({
            "mensaje": "Service Unavailable"
        })

@app.route("/user", methods=["POST"])
def user():
    if request.method == "POST":
        data = request.json
        if "user_nickname" in data and "user_password" in data:
            usuario_insertar = {
                "user_nickname": data["user_nickname"],
                "user_password": data["user_password"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["usuario"]
                usuarios_search = mongo_collections.find(usuario_insertar)
                Response= json_util.dumps(usuarios_search)
                return Response
            except Exception as e:
                return (jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))
        else:
            resp = (jsonify({
            "msg":"Petición incorrecta"
            }))
            resp.status_code=401
            return resp
    else:
        return jsonify({
            "mensaje": "Service Unavailable"
        })

@app.route("/book", methods=["POST"])
def book():
    if request.method == "POST":
        data = request.json
        if "id_book" in data and "book_title" in data and "book_type" in data and "author" in data and "book_count" in data and "book_available" in data and "book_not_available" in data and "book_year" in data and "book_editorial" in data:
            usuario_insertar = {
                "id_book": data["id_book"],
                "book_title": data["book_title"],
                "book_type": data["book_type"],
                "author":data["author"],
                "book_count":data["book_count"],
                "book_available":data["book_available"],
                "book_not_available":data["book_not_available"],
                "book_year":data["book_year"],
                "book_editorial":data["book_editorial"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["libros"]
                respuesta_mongo = mongo_collections.insert_one(usuario_insertar)
                print(respuesta_mongo.inserted_id)
                resp = jsonify({
                    "status":"200",
                    "msg":"response"
                })
                resp.status_code = 200
                return resp
            except Exception as e:
                return Response(jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))    
        else:
            resp = (jsonify({
                "msg":"Petición incorrecta"
            }))
            resp.status_code=401
            return resp
    else:
        return jsonify({
            "mensaje": "Service Unavailable"
        })

@app.route("/put_book", methods=["PUT"])
def put_book():
    if request.method == "PUT":
        data = request.json
        if "id_book" in data and "book_title" in data and "book_type" in data and "author" in data and "book_count" in data and "book_available" in data and "book_not_available" in data and "book_year" in data and "book_editorial" in data:
            usuario_insertar = {
                "id_book": data["id_book"],
                "book_title": data["book_title"],
                "book_type": data["book_type"],
                "author":data["author"],
                "book_count":data["book_count"],
                "book_available":data["book_available"],
                "book_not_available":data["book_not_available"],
                "book_year":data["book_year"],
                "book_editorial":data["book_editorial"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["libros"]
                mongo_collections.update_one({"id_book": data["id_book"]},{ "$set": usuario_insertar })
                print("Funciona")
                resp = jsonify({
                    "status":"200",
                    "msg":"response"
                })
                resp.status_code = 200
                return resp
            except Exception as e:
                return Response(jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))    
        else:
            resp = (jsonify({
                "msg":"Petición incorrecta"
            }))
            resp.status_code=401
            return resp
    else:
        return jsonify({
            "mensaje": "Service Unavailable"
        })

@app.route("/read_book", methods=["GET"])
def get_book():
    if request.method == "GET":
        data = request.json
        if "id_book" in data:
            usuario_insertar = {
                "id_book": data["id_book"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["libros"]
                book_search = mongo_collections.find(usuario_insertar)
                print("Funciona")
                Response= json_util.dumps(book_search)
                return Response
            except Exception as e:
                return (jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))
        elif "book_type" in data:
            usuario_insertar = {
                "book_type": data["book_type"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["libros"]
                book_search = mongo_collections.find(usuario_insertar)
                print("Funciona")
                Response= json_util.dumps(book_search)
                return Response
            except Exception as e:
                return (jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))
        elif "book_title" in data:
            usuario_insertar = {
                "book_title": data["book_title"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["libros"]
                book_search = mongo_collections.find(usuario_insertar)
                print("Funciona")
                Response = json_util.dumps(book_search)
                return Response
            except Exception as e:
                return (jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))  
        elif "author" in data:
            usuario_insertar = {
                "author": data["author"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["libros"]
                book_search = mongo_collections.find(usuario_insertar)
                print("Funciona")
                Response = json_util.dumps(book_search)
                return Response
            except Exception as e:
                return (jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))  
        else:
            resp = (jsonify({
                "msg":"Petición incorrecta"
            }))
            resp.status_code=401
            return resp
    else:
        return jsonify({
            "mensaje": "Service Unavailable"
        })

@app.route("/loan", methods=["POST"])
def loan():
    if request.method == "POST":
        data = request.json
        if "id_book" in data and "id_user" in data:
            usuario_insertar = {
                "id_book": data["id_book"],
                "id_user": data["id_user"]
            }
            try:
                cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
                mongo_db = cliente_mongo["proyecto2"]
                mongo_collections = mongo_db["usuario"]
                mongo_collections2 = mongo_db["libros"]
                mongo_collections3 = mongo_db["prestamos"]
                id_user = {"id_user" : usuario_insertar["id_user"]}
                id_book = {"id_book" : usuario_insertar["id_book"]}
                usuarios_search = mongo_collections.find(id_user)
                book_search = mongo_collections2.find(id_book)
                fecha = datetime.date.today()
                print(str(fecha))
                fecha_regreso = datetime.timedelta(7)
                print(str(fecha+fecha_regreso))
                final_search = [{"id_loan" : 1},{book_search},{"loan_date": str(fecha), "return_date" : str(fecha+fecha_regreso)},{usuarios_search}]
                respuesta_mongo = mongo_collections3.insert_one({"id_loan" : 1})
                Response= json_util.dumps(final_search)
                return Response
            except Exception as e:
                return (jsonify({
                    "estado":"-3",
                    "mensaje":"e"
                }))
        else:
            resp = (jsonify({
            "msg":"Petición incorrecta"
            }))
            resp.status_code=401
            return resp
    else:
        return jsonify({
            "mensaje": "Service Unavailable"
        })

#INIT
if __name__=="__main__" :
    app.run(host="0.0.0.0", port="3000", debug=True)