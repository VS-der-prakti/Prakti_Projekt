from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json


app = FastAPI()

middleware = {
    'allow_origins': ['http://localhost:5173'],
    'allow_credentials': True,
    'allow_methods': ['*'],
    'allow_headers': ['*'],
}

app.add_middleware(CORSMiddleware, **middleware)


@app.get("/year/{year}")
async def schaltjahr(year: int):
    is_schaltjahr = False
    mod = year % 4
    print(mod)  
    
    if mod == 0:
        is_schaltjahr = True
        if year % 100 == 0:
            is_schaltjahr = False
        if year % 400 == 0:
            is_schaltjahr = True
    return {"Schaltjahr": is_schaltjahr}


@app.get("/listen")
async def listen():

    list1 = [1,2,3,4,5,6,7,8,9,345435]
    list2 = [3,45,324,6,7,875]
    list_result = []
    print(list1)
    for i in list1:
        if i %2 == 0:
            list_result.append(i)
            print(i)
#    for i in list1:   
#        for j in  list2:
#            if i == j:
#                list_result.append(j)
#                print(i)        
    
    return {"liste": list_result}


@app.get("/words")
async def words():

    word1 = 'hallo'
    word2 = 'hoWelt test ha' #ha test howelt
    length1 = len(word1)
    length2 = len(word2)
    word3 = ""

    list_result = []
    word_result = ''
    hallo_liste = ["hallo"]
    liste2 = ["hoWelt", "test", "ha"]
    
#    for i in word1:
#        list_result.append(i)
#    for o in reversed(list_result):
#        word_result = word_result + o     
#    print(word_result)

   
#    for k in reversed(liste2):
#        print(k)

    temp = word2.split(" ")
    anzahl = len(temp)

    
    for element in reversed(temp):
            print(element)
#    print(anzahl)


    
    


#    for i in range(length2):
#        print(word2[12])
#        print(word2[13])
#    for i in range(length2):
#        print(word2[7])
#        print(word2[8])
#        print(word2[9])
#        print(word2[10])




#    for i in range(length1): # range(length) = range(len(word1)) = range(5) = [0,1,2,3,4]
#        print(word1[i]) # i = 0 -> word1[0] = h; i = 1 -> word1[1] = a
#    for i in range(length1):
#        print(word1[4])



    
#    for i in word1:
#        for j in word2:
#            if i == j:
#                word_result = word_result + i
#                print(j)




    return {"liste": liste2}




#    for i in word1:
#        if i == "l":
#            i = "p"
#        word_result = word_result + i

@app.get("/words/{words}")
async def words(words: str):



    list_result = []
    word_result = ''
    liste2 = ["hoWelt", "test", "ha"]

    temp = word.split(" ")
    anzahl = len(temp)

    
    for element in reversed(temp):
        list_result.append(element)
        print(element)

    return {"liste": list_result}


@app.get("/points/{x}/{y}")
async def points(x: int, y: int):
#    wall1 = [[3,3],[9,9]]
    brick = [[[3,3],[4,2]],[[9,9],[10,8]]]

    breite1 = brick[0]
    breite2 = brick[1]

    punkt1b1 = breite1[0]
    punkt2b1 = breite1[1]

    punkt1b2 = breite2[0]
    punkt2b2 = breite2[1]

    xcoordp1b1 = punkt1b1[0]
    xcoordp2b1 = punkt2b1[0]

    ycoordp1b1 = punkt1b1[1]
    ycoordp2b1 = punkt2b1[1]

    xcoordp1b2 = punkt1b2[0]
    xcoordp2b2 = punkt2b2[0]

    ycoordp1b2 = punkt1b2[1]
    ycoordp2b2 = punkt2b2[1]


    wand = False
    if xcoordp1b1 <= x <= xcoordp2b1 and xcoordp1b2 <= x <= xcoordp2b2 and ycoordp1b1 <= y <= ycoordp2b1 and ycoordp1b2 <= y <= ycoordp2b2:
        wand = True
    print(wand)


#    wandanfang = wall[0]
#    wandende = wall[1]
#    w2 = wandende[1]
#    w1 = wandanfang[1]

#    ycoord1 = wall[0][1]
#    ycoord2 = wall[1][1]

#    xcoord1 = wall[0][0]
#    xcoord2 = wall[1][0]

#    wand = False
#    if ycoord1 <= y <= ycoord2 and xcoord1 <= x <= xcoord2:
#        wand = True
#    print(wand)    
    
    
    point = [x,y]

#    if point == [xcoord1,w1>4] and point == [xcoord2,w2<9]:
#        wand = True
#    print(wand)
        
    return {"point": [x, y]}


def division(a: int, b: int):
    c = a / b
    print(c)
    return c

def datenbank_erstellen(name1: str, name2: str, age: int):
    
    daba = {
        "Vorname" : name1,
        "Nachname" : name2,
        "Alter" : age
    }
    return daba

@app.get("/database")
async def database():

    db1 = {
        'name1': 'Tim',
        'name2': 'Müller',
        'age': 30
    }

    db2 = {
        'name1': 'Lisa',
        'name2': 'Schmidt',
        'age': 20
    }

    db3 = {
        'name1': 'Heiko',
        'name2': 'Schmidt',
        'age': 45
    }

    db = [db1, db2, db3]

    emailname1 = db1["name1"] + "." + db1["name2"]
    emailname2 = db2["name1"] + "." + db2["name2"]
    email1 = emailname1+"@test.com"
    email2 = emailname2+"@test.com"
    länge_vorname = len("name1")
    anzahl_vornamen = len(db)

#    print(db2['age'])

#    db1['mail'] = 'tim.müller@test.com' #for schleife/ email für jeden benutzer mit name1.name2@test.com

#    for i in db1:
#        db1.append(email)

#    db1["email"] = email1
#    db2['email'] = email2

    count_age = 0
    gesamtlänge_vornamen = 0
    gesamtanzahl_vornamen = 0

    # count_age = count_age + db1['age']

    for i in db:
        emailname = i["name1"] + "." + i["name2"]
        email = emailname+"@test.com"
        i["email"] = email
        count_age = i["age"] + count_age # count_age = 30; 
        gesamtlänge_vornamen = len(i["name1"]) + gesamtlänge_vornamen
    print(gesamtlänge_vornamen)
    print(anzahl_vornamen)
    durchschnitt = division(gesamtlänge_vornamen, anzahl_vornamen)


    output = {
        'database': db,
        'gesamtalter': count_age,
        "Durchschnittliche Anzahl der Buchstaben im Vornamen": durchschnitt
    }

    json.dump( output, open( "database.json", 'w'))
    
    return output

@app.get("/readdatabase")
async def readdatabase():

    output = json.load( open( "database.json"))

    

    return output["database"]
    
@app.get("/deleteuser/{name1}/{name2}")
async def deleteuser(name1: str, name2: str):

    output = json.load( open( "database.json"))

    newdata = []

    for i in output["database"]:
        
        if not i["name1"] == name1 or not i["name2"] == name2:
            newdata.append(i)
       

#    if user_exists == True and name1 in output["database"] and name2 in output["database"]:
#        del output["database"["name1"]] and output["database"["name2"]]

    output['database'] = newdata

    json.dump( output, open( "database.json", 'w'))

    return {"Namensliste" : output["database"]          
    }

@app.get("/adduser/{name1}/{name2}")
async def adduser(name1: str, name2: str):

    output = json.load( open( "database.json"))
    
    db4 = {
        "name1" : name1,
        "name2" : name2
    }
    
    

    user_exists = False

    for i in output["database"]:
        
        if i["name1"] == name1 and i["name2"] == name2:
            user_exists = True
    if not user_exists:
        olddata = output["database"]
        olddata.append(db4)
        output["database"] = olddata 


    json.dump( output, open( "database.json", 'w'))

    return {"Namensliste" : output["database"]}
    

#@app.options("/score")
#async def options_score():
#    return {"msg": "OK"}

@app.get("/score")
async def get_score():
    try:
        score = json.load(open("score.json"))
        return {"highscore" : score["highscore"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class HighScore(BaseModel):
    highscore: int

@app.post("/newscore")
async def post_score(highscore: HighScore):
    try:
        get_score = json.load(open("score.json"))
        get_score["highscore"] = highscore.highscore
        json.dump(get_score, open("score.json", "w"))
        return {"highscore": highscore}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
