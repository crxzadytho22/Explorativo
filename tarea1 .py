import urllib.request
import json



clave = "CAACEdEose0cBAA0WHX70XN2B75yaUIOD33Yj0SusgaDF1Hx0T6JGnBRHEyrKepeScmM0jlFmjIVMRkYGRbgiahGf7fh5NxN0B7p3j0ZBZBxNqCuMwsJgGqh6x3qTZCyjfOzI7HrgRPHNPDLOaCdTKN3vZCXPZCR8eXPeL1Cc3bHTWdN2z7uS7xIKPVoa26DiZCZC9rLFSQF7AZDZD"
user = "1352821093"
n = urllib.request.urlopen("https://graph.facebook.com/"+user+"?fields=name,picture.width(400).height(400),friends.fields(birthday,gender,languages,relationship_status,location)&method=GET&format=json&suppress_http_code=1&access_token=" + clave).read()
n=str(n)[2:-1]
n = n.replace("\\'", "")


d = json.loads(n)

f1=open("archivo.json","w")
f1.write(json.dumps(d,indent=2,separators=(":",",")))
f1.close()
         

jason_mio=d["name"]
jason = d["friends"]["data"]
lenguages = []
genero = []
cumpleaños = []
relacion1 = []
ciudad =[]
contador_mujeres=0
contador_hombres=0
relacion=[]

contador_amigos=0

for i in jason:
    contador_amigos+=1
    if "languages" in i:
        if i["languages"] !=None:
            for j in i["languages"]:
                lenguages.append(j["name"])
                
    if "gender" in i:
        if i["gender"] !=None:
            genero.append(i["gender"])
                           

    if "birthday" in i:
        if len(i["birthday"]) >= 8 :
            cumpleaños.append(i["birthday"][8:13])
    if "relationship_status" in i:
        if i["relationship_status"] !=None:
                relacion1.append(i["relationship_status"])
    if "location" in i:
        if i["location"] != None:
            for m in i["location"]:
                ciudad.append(i["location"]["name"])
for x in relacion1:
    relacion.append(x.lower())

for x in range(len(relacion)):
    if relacion[x]=="in a relationship":
        relacion[x]="in_a_relationship"
   
    if relacion[x]=="in an open relationship":
        relacion[x]="open_relationship"

jason_foto=d["picture"]["data"]["url"]
jason_foto1=d["picture"]["data"]["width"]
jason_foto2=d["picture"]["data"]["height"]
    
lista_edad=[]
for x in cumpleaños:
    edad=0
    edad = 2014 - int(x)
    lista_edad.append(edad)


mas_viejo=max(lista_edad)
mas_joven=min(lista_edad)
promedio=sum(lista_edad) //len(lista_edad)


    
generos=""

def contar_genero(w):
    q={}
    for i in w:
        if not i in q:
            q[i] = 1
        else:
            q[i]=q[i] +1
    return q

sexo = contar_genero(genero)
for i in sexo:
    generos+= "{gender:" +str(i)+",\n"+ "count: "+str(sexo[i])+"\n}"

idioma=""
def contar_idiomas(s):
    d={}
    for i in s:
        if not i in d:
            d[i] = 1
        else:
            d[i]=d[i] +1
    return d

h = contar_idiomas(lenguages)
for i in h:
    idioma+= "{language:" +str(i)+",\n"+ "count: "+str(h[i])+"\n}"
    

def contar_location(j):
    c={}
    for k in j:
        if not k in c:
            c[k]=1
        else:
            c[k]=c[k] +1
    return c

p=contar_location(ciudad)

hometown=""
for i in p:
    hometown+= "{hometown:"+str(i)+",\n"+ "count: "+ str(p[i])+"\n}"
    
def contar_relacion(l):
    b={}
    for k in l:
        if not k in b:
            b[k]=1
        else:
            b[k]=b[k] +1
    return b

relaciones=contar_relacion(relacion)

situacion=""
for i in relaciones:
    situacion+= "{relationship_status:" +str(i)+",\n"+ "count: "+ str(relaciones[i])+"\n}"



r = ({
    'name':jason_mio,
    "picture":{
        "url":jason_foto,
        "width":jason_foto1,
        "height":jason_foto2
        },
    "friends":{
        "count":contador_amigos,
        "gender":generos,
        "age":{
            "average":promedio,
            "youngest":mas_joven,
            "oldest":mas_viejo
            },
        "languages":[
            idioma
            ],
        "relationship_status":situacion,
        "hometown":[
            hometown
            ]
        }
    })
        
    
    
        
        
        
            
       

f1=open("archivo.json","w")
f1.write(json.dumps(r,indent=2,separators=(":",",")))
f1.close()
