import psycopg2
import pymongo
from psycopg2 import Error

#These are the determined variables to connect with the MongoDB
client = pymongo.MongoClient()
database = client["huwebshop"]
products = database["products"]

def connect():
    """This function is the connection with the postgres db"""
    con = psycopg2.connect(host='localhost',database='huwebshop',user='postgres',password='Xplod_555')
    return con

def execute(SQL,values):
    """This function excecutes a commmand with the postgres db"""
    connection = None
    try:
        connection = connect()
        cur = connection.cursor()
        cur.execute(SQL,values)
        connection.commit()
        cur.close()
        print("Done")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Connection is closed")


def data_laden_product():
    """This function loads the data from the MongoDB
     and sends it to the Postgres DB"""

    for product in products.find({ },{"name", "_id","category","sub_category","sub_sub_category", "brand", "gender","price","properties"}):
        if len(product.keys()) > 1 :
            if len(product.keys()) > 7 :

                id1 = product["_id"]
                naam = product["name"]
                category = product["category"]
                sub_category = product["sub_category"]
                sub_sub_category = product["sub_sub_category"]
                brand = product["brand"]
                gender = product["gender"]
                price = product["price"]
                properties = product["properties"]
                selling_price = price["selling_price"]
                discount =  price["discount"]
                variant = properties["variant"]

            else:
                sub_category = None
                sub_sub_category = None
        else:
            continue


        execute("insert into  product (id_product , naam , category , sub_category , sub_sub_category ,gender , brand ) values (%s ,%s , %s , %s , %s, %s , %s)",
                [id1, naam, category, sub_category, sub_sub_category, gender, brand])


        execute("insert into  prijs (id_prijs ,discount ,selling_price) values (%s ,%s,%s )",
                [id1, discount,selling_price])

        execute("insert into  properties (id_properties ,variant) values (%s ,%s )",[id1, variant])


data_laden_product()
