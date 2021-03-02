import psycopg2
import pymongo
from psycopg2 import Error




client = pymongo.MongoClient()

database = client["huwebshop"]
products = database["products"]


def data_laden_product():
    try:
        con = psycopg2.connect(
            host="localhost",
            database="huwebshop1",
            user="postgres",
            password="Xplod_555")
        cur = con.cursor()
        print("PostgreSQL server information")
        print(con.get_dsn_parameters(), "\n")

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

            cur.execute("insert into  product (id , naam , category , sub_category , sub_sub_category ,brand , gender ) values (%s ,%s , %s , %s , %s, %s , %s)",[id1, naam, category, sub_category, sub_sub_category, brand, gender])
            cur.execute("insert into  properties (id , variant) values (%s ,%s )",[id1, variant])
            cur.execute("insert into  prijs (id ,discount,selling_price) values (%s ,%s,%s )", [id1, discount,selling_price])


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


    finally:
        print("data is successfully transferred")
        if (con):
            cur.close()
            con.close()
            print("PostgreSQL connection is closed")


data_laden_product()

