import psycopg2
import pymongo
from psycopg2 import Error

#These are the determined variables to connect with the MongoDB
client = pymongo.MongoClient()
database = client["huwebshop"]
products = database["products"]
profiles = database["profiles"]
sessions = database["sessions"]

def connect():
    """This function is the connection with the postgres db"""
    connection = psycopg2.connect(host='localhost', database='huwebshop', user='postgres', password='Xplod_555')
    return connection

def disconnect():
    """This function disconnects the program with the postgres db"""
    con = connect()
    return con.close()

def data_laden_product():
    """This function loads data from the table "Products" out of the MongoDB
     and sends it to the Postgres DB"""
    connection = connect()
    cur = connection.cursor()

    try:
        #Data is being loaded from de Mongo db
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

                    # The data is being sent to the Postgres db.
                    cur.execute(
                        "insert into  product (id_product , naam , category , sub_category , sub_sub_category ,gender , brand ) values (%s ,%s , %s , %s , %s, %s , %s)",
                        [id1, naam, category, sub_category, sub_sub_category, gender, brand])
                    cur.execute("insert into  prijs (id_prijs ,discount ,selling_price) values (%s ,%s,%s )",
                            [id1, discount, selling_price])
                    cur.execute("insert into  properties (id_properties ,variant) values (%s ,%s )",
                                [id1, variant])

                else:
                    #The products without a sub_category & sub_sub_category will be forwarded as None.
                    sub_category = None
                    sub_sub_category = None
            else:
                continue
        connection.commit()

    #In case an error occures, an error-message will be shown.
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    disconnect()
    print("Products is done")

def data_laden_profiles():
    """This function loads data from the table "Profiles" out of the MongoDB
     and sends it to the Postgres DB"""
    connection = connect()
    cur = connection.cursor()

    try:
        #Data is being loaded from de Mongo db
        for profile in profiles.find({ },{"_id","buids", "recommendations","previously_recommended","latest_activity"}):

            if (len(profile.keys())) == 5:
                id1 = str(profile["_id"])
                buids = profile["buids"]
                recommendations = profiles["recommendations"]
                previously_recommended = profile["previously_recommended"]
                segment = str(recommendations["segment"])
                last_visit = profile["latest_activity"]
                for i in previously_recommended:
                    product_id = i
                    continue
                for j in buids:
                    browserid = j
                    continue

                # The data is being sent to the Postgres db.
                cur.execute("insert into  profiels(id_profiel ,  segment , last_date ) values (%s ,%s , %s )",
                            [id1, segment, last_visit])
                cur.execute("insert into  previously_recommended (id_profiel , id_product  ) values (%s ,%s  )",
                            [id1, product_id])
                cur.execute("insert into  buids(id_profiel , browsersid  ) values (%s ,%s  )",
                            [id1, browserid])
                connection.commit()

            else:
                buids = None

    #In case an error occures, an error-message will be shown.
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    disconnect()
    print("Profiles is done")

def data_laden_sessions():
    """This function loads data from the table "Sessions" out of the MongoDB
     and sends it to the Postgres DB"""
    connection = connect()
    cur = connection.cursor()

    try:
        # Data is being loaded from de Mongo db
        for session in sessions.find({ },{ "_id","session_start","has_sale","session_end","segment","user_agent","buid"}):

            if len(session.keys()) > 6:
                id1 = session["_id"]
                buid =session["buid"][0]
                user_agent = session["user_agent"]
                session_start = session["session_start"]
                session_end = session["session_end"]
                has_sale =session["has_sale"]
                segment = session["segment"]
                user_agent_browser = user_agent["browser"]["familiy"]
                user_agent_device = user_agent["device"]["family"]

                # The data is being sent to the Postgres db.
                cur.execute("insert into  sessions(session_id , profile_id , session_start, session_end, has_sale, user_agent_browser, user_agent_device, segment_sessions) values (%s ,%s , %s ,%s ,%s , %s ,%s , %s )",
                            [id1, buid,session_start,session_end,has_sale,user_agent_browser,user_agent_device,segment])
                connection.commit()

            else:
               segment =None

    #In case an error occures, an error-message will be shown.
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    disconnect()
    print("Sessions is done")



#Here are the three functions that will load all of the data into the Postgres db. They need to be called one at a time because of the large data sets that have to load.
#data_laden_sessions()
#data_laden_profiles()
data_laden_product()


