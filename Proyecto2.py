faceId_list = [{'faceId': 'f04acf0e-92cc-46f7-a9e9-6bccd6227792', 
'name': 'Rose Park Chaeyoung',
'profession':'Vocalist',
'nationality': 'korean',
'group': 'BlackPink',
'faceRectangle': {'top': 290, 'left': 267, 'width': 187, 'height': 187}, 
'faceAttributes': {'smile': 0.998, 'headPose': {'pitch': 2.3, 'roll': -10.7, 'yaw': -7.9}, 'gender': 'female', 'age': 21.0, 
                    'facialHair': {'moustache': 0.0, 'beard': 0.0, 'sideburns': 0.0}, 'glasses': 'NoGlasses', 
                    'emotion': {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 0.998, 'neutral': 0.002, 'sadness': 0.0, 'surprise': 0.0}, 
                    'blur': {'blurLevel': 'low', 'value': 0.0}, 'exposure': {'exposureLevel': 'goodExposure', 'value': 0.67}, 'noise': {'noiseLevel': 'medium', 'value': 0.54}, 
                    'makeup': {'eyeMakeup': True, 'lipMakeup': True}, 
                    'accessories': [], 'occlusion': {'foreheadOccluded': False, 'eyeOccluded': False, 'mouthOccluded': False}, 'hair': 
                    {'bald': 0.02, 'invisible': False, 
                    'hair': 'blond', 'hairColor': [{'color': 'blond', 'confidence': 0.99}, {'color': 'red', 'confidence': 0.79}, {'color': 'other', 'confidence': 0.66}, {'color': 'gray', 'confidence': 0.2}, {'color': 'brown', 'confidence': 0.18}, {'color': 'black', 'confidence': 0.03}, {'color': 'white', 'confidence': 0.0}]}}}]

#dic0= faceId_list[0]

#dic0_faceRectangle= dic0['faceRectangle']
#dic0_faceAttributes= dic0['faceAttributes']
#dic0_name= dic0['name']
#haircolor = dic0_faceAttributes['hair']
#dic0_emotions= dic0_faceAttributes['emotion']
#dic0_profession= dic0['profession']
#dic0_nationality= dic0['nationality']
#makeup= dic0_faceAttributes['makeup']
#gender= dic0_faceAttributes['gender']
#age= dic0_faceAttributes['age']
#accessories= dic0_faceAttributes['accessories']
#group= dic0['group']


#print("El nombre de la persona es", dic0_name)
#print("La edad de", dic0_name, "es", age)
#print("El genero de", dic0_name,"es", gender)
#print("La profesion de", dic0_name, "es", dic0_profession)
#print(dic0_name, "pertenece al grupo", group)
#print("La nacionalidad de", dic0_name, "es", dic0_nationality)
#print("El color del pelo de", dic0_name, "es", haircolor)
#print("Los accesorios de", dic0_name,"son", accessories)
#print("El maquillaje de", dic0_name, "es", makeup)
#print("Las emociones escaneadas de", dic0_name, "son", dic0_emotions)


#sizes_top = dic0_faceRectangle['top']
#sizes_left = dic0_faceRectangle['left']
#sizes_width = dic0_faceRectangle['width']
#sizes_height = dic0_faceRectangle['height']

#print(sizes_top, "Es el top del rectangulo en la foto de la cara" )
#print(sizes_left, "Es el left del rectangulo en la foto de la cara" )
#print(sizes_width, "Es el width del rectangulo en la foto de la cara")
#print(sizes_height, "Es el height del rectangulo en la foto de la cara")


import sys
sys.path.append(".")

class persona:
    Id = "f04acf0e-92cc-46f7-a9e9-6bccd6227792"
    nombre = "Rose Park Chaeyoung"
    edad = 23
    genero = "Female"
    nacionalidad = "neozelandesa"
    Rute = "https://i.pinimg.com/originals/9f/03/b8/9f03b815508309bd6d3951364c0baff9.jpg"

class persona2:
    Id = "6e93e837-70de-44ba-985b-1dc4118a8395"
    nombre = "Lalisa Manoban"
    edad = 23
    genero = "Female"
    nacionalidad = "tailandesa"
    rute = "https://vz.cnwimg.com/thumb-1200x/wp-content/uploads/2019/07/lm.jpg"

class persona3:
    Id = "4f85bfc8-98b9-4c30-b909-1a5fe346cc1f"
    nombre = "Kim Jisoo"
    edad = 25
    genero = "Female"
    nacionalidad = "coreana"
    rute = "https://vignette.wikia.nocookie.net/kpop/images/d/d8/Kim_Ji_Soo_para_How_You_Like_That.jpg/revision/latest/top-crop/width/360/height/450?cb=20200618005301&path-prefix=es"

class Rapper(persona2):
    
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self):
        return "Nombre {}, edad {} , nacionalidad{}".format( self.nombre, 
                                                             self.edad, 
                                                             self.nacionalidad )

class Visual(persona3):
    
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self):
        return "Nombre {}, edad {} , nacionalidad{}".format( self.nombre, 
                                                             self.edad, 
                                                             self.nacionalidad )


class Vocalist(persona):
    
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self):
        return "Nombre {}, edad {} , nacionalidad{}".format( self.nombre, 
                                                             self.edad, 
                                                             self.nacionalidad, )



persona = Vocalist("Rose Park Chaeyoung", "23", "Female")
print(persona)

#Nombre Rose Park Chaeyoung, Edad 23 , Genero Female

persona2 = Rapper("Lalisa Manoban", "23", "Female")
print(persona)

#Nombre Lalisa Manoban, Edad 23 , Genero Female

persona3 = Visual("Kim Jisoo", "25", "Female")
print(persona)

#Nombre Kim Jisoo, Edad 23 , Genero Female

    
