import psycopg2
import pymongo
from psycopg2 import Error

#These are the determined variables to connect with the MongoDB
client = pymongo.MongoClient()
database = client["huwebshop"]
products = database["products"]

def connect():
    """This function is the connection with the postgres db"""
    connection = psycopg2.connect(host='localhost', database='huwebshop', user='postgres', password='Xplod_555')

    return connection

def disconnect():
    con = connect()
    return con.close()




def data_laden_product():
    """This function loads the data from the MongoDB
     and sends it to the Postgres DB"""
    connection = connect()

    try:
        cur = connection.cursor()

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


                    cur.execute(
                        "insert into  product (id_product , naam , category , sub_category , sub_sub_category ,gender , brand ) values (%s ,%s , %s , %s , %s, %s , %s)",
                        [id1, naam, category, sub_category, sub_sub_category, gender, brand])

                    cur.execute("insert into  prijs (id_prijs ,discount ,selling_price) values (%s ,%s,%s )",
                            [id1, discount, selling_price])

                    cur.execute("insert into  properties (id_properties ,variant) values (%s ,%s )", [id1, variant])

                else:
                    #omdat niet alle producten hebben sub_category & sub_sub_category dus ze worden als None opeslaan.
                    sub_category = None
                    sub_sub_category = None
            else:
                continue

        connection.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)






    disconnect()


data_laden_product()
