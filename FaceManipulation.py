import face_recognition #Responsável por fazer o reconhecimento facial
import numpy as np #Responsável por manipular números de formas diferentes
import sqlite3

faceFolder = 'Face_Encodings'

def Recognition(image):
    aluno = face_recognition.load_image_file(image)
    face = face_recognition.face_encodings(aluno)[0]
    return face

def FacesToArchive(face, matricula):
    stringArray = str(face)
    file = open('%s/%s.txt'%(faceFolder, matricula), "w+")
    file.write(stringArray)
    file.close()
    np.save('%s/%s.npy'%(faceFolder, matricula), face)

def Register(name, image, matricula, cursor):        
    cursor.execute("CREATE TABLE IF NOT EXISTS ALUNO (nome varchar(50) NOT NULL, matricula varchar(20) NOT NULL, primary key(matricula))")
    face = Recognition(image)
    FacesToArchive(face, matricula)
    cursor.execute("INSERT INTO ALUNO VALUES('%s', '%s')"%(name, matricula))
    print('O registro do aluno %s foi concluído com sucesso!'%name)

def FacesFromArchive(matricula):
    with open('%s/%s.txt' %(faceFolder, matricula), 'r', encoding='utf8') as archive:
        file = archive.read()
        chars = '[]'
        file = file.translate(str.maketrans('', '', chars))
        brokenArray = np.array(file.split()) 
        floatArray = brokenArray.astype(float)
    return floatArray
