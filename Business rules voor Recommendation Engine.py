import psycopg2
import pymongo
from psycopg2 import Error

client = pymongo.MongoClient()
database = client["huwebshop"]
products = database["products"]
profiles = database["profiles"]



def connect():
    """This function is the connection with the postgres db"""

    connection = psycopg2.connect(host='localhost', database='huwebshop', user='postgres', password='Xplod_555')
    return connection

def disconnect():
    """This function disconnects the program with the postgres db"""
    con = connect()
    return con.close()

def sql_execute(sql,value):
    """This function executes a query on the Postgres db"""
    cur = connect().cursor()
    cur.execute(sql,value)

def sql_query(sql):
    cur = connect().cursor()
    cur.execute(sql)




def Meest_gekochte_producten():
    """ """
    c = connect()
    cur = c.cursor()
    try:
        cur.execute("""SELECT orders.prodid, products.name,
        COUNT(*)
FROM orders
INNER JOIN products ON Orders.prodid = products.id
GROUP BY prodid ,products.name 
ORDER BY COUNT(*) DESC ; """)
        i = cur.fetchall()
        print(i)



    except (Exception, psycopg2.DatabaseError) as error:
            print(error)


def meeste_aanbelvende_producten():
    c = connect()
    cur = c.cursor()
    try:
        cur.execute("""SELECT profiles_previously_viewed.prodid, products.name,products.category ,
            COUNT(*)
    FROM profiles_previously_viewed
    INNER JOIN products ON profiles_previously_viewed.prodid = products.id
    GROUP BY prodid ,products.name ,products.category
    ORDER BY COUNT(*) DESC ; """)
        records = cur.fetchall()
        for i in records:

            print(i)


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def profiel_meest_aanblevende():
    c = connect()
    cur = c.cursor()
    try:
        cur.execute("""SELECT profiles.id, profiles.segment,profiles_previously_viewed.prodid, products.name , 
                    
            FROM profiles
            INNER JOIN profiles_previously_viewed ON profiles.id = profiles_previously_viewed.profid
            INNER JOIN products on profiles_previously_viewed.prodid = products.id
            GROUP BY  profiles.id, profiles.segment ,profiles_previously_viewed.prodid ,products.name ;
             """)
        records = cur.fetchall()
        for i in records:
            print(i)



    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

profiel_meest_aanblevende()