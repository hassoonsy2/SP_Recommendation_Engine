import pymongo


""" """






#Er wordt hier de naam en de collection namen van MongoDB doorgegeven
client = pymongo.MongoClient()

database = client["huwebshop"]


products = database["products"]
profiles = database["profiles"]
sessions = database["sessions"]






def Naam_en_prijs_van_product():
    """ Een fuctie die return de naam en prijs van het eerste product in de database """
    return print(products.find_one({ },{"name":1,"price":1 , "_id": 0 }),"\nde naam en prijs van het eerste product in de database" )




def Eerste_product_met_R():
    """ Een functie die return de naam van het eerste product waarvan de naam begint met een 'R"""
    ides_en_namen= []
    for i in range(len(products.find_one({},{"name"}))):
        for x in products.find({},{"name"}):
            ides_en_namen.extend(x.values())

    ides_en_namen = set(ides_en_namen)
    name_met_R = []
    for i in ides_en_namen:
        if i[0] == "R":
            name_met_R.append(i)
        else:
            continue


    return print(name_met_R[0] ,"\nDe naam van het eerste product waarvan de naam begint met een 'R' "  )




def pijzen_gemiddeld():
    """ Een functie die return de gemiddelde prijs van de producten in de database"""
    price_lijst = []
    for i in range(len(products.find_one({},{"price"}))):
        for data in products.find({},{"price"}):
            price_lijst.extend(data.values())

    lst2 = []
    for price in price_lijst :
        if type(price) == dict:
            lst2.append(price)
        else:
            continue

    selling_price = []
    for elment in lst2:
        for u in elment.keys():
            a, b, c = elment.values()
            if c is not None:
                selling_price.append(c)
            else:
                continue

    gem = sum(selling_price) // len(selling_price)
    return print(sum(selling_price),"\nDe gemiddelde prijs van de producten in de database")



Naam_en_prijs_van_product()
Eerste_product_met_R()
pijzen_gemiddeld()





