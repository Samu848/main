from datetime import date, datetime
from os import mkdir
import os
import os.path

class Cuentas():
    def __init__(self,usuario,password,correo,lesion,grado,dia_i,dia_u,dia_a):
        self.usuario = usuario
        self.password = password
        self.correo = correo
        self.lesion = lesion
        self.grado = grado
        self.dia_i = dia_i
        self.dia_u =dia_u
        self.dia_a =dia_a
    
    def guardar_archivo(self):
        _file = 'usuarios.csv'
        archivo = open(_file,'a')
        archivo.write(self.usuario+";"+self.password+";"+self.correo+";"+self.lesion+";"+self.grado+";"+self.dia_i+";"+self.dia_u+";"+self.dia_a+"\n")
        archivo.close()

    def crear_carpetat(self):
        pa = os.path.join("Archivos\Tobillo",self.usuario)
        mkdir(pa) 

    def crear_carpetam(self):
        pa = os.path.join("Archivos\Muñeca",self.usuario)
        mkdir(pa) 

    def crear_carpetar(self):
        pa = os.path.join("Archivos\Rodilla",self.usuario)
        mkdir(pa) 

def validar_usuario():
    _file = 'usuarios.csv'
    archivo = open(_file, 'r')
    lineas = archivo.readlines()
    del[lineas[0]]
    return lineas

def menu_registro(usuario,password,correo,lesion,grado):
    today = date.today()
    existe = usuario.lower()
    datos = validar_usuario()
    for d in datos:
        d = d.replace("\n","").split(";")
        d[0] = d[0].lower()
        if existe == d[0]:
            return "0"
    
    m = Cuentas(usuario,password,correo,lesion,grado,str(today),"1",str(today))
    m.guardar_archivo()

    if lesion == "Rodilla":
        m1 = Cuentas(usuario,password,correo,lesion,grado,str(today),"1",str(today))
        m1.crear_carpetar()
    if lesion == "Muneca":
        m1 = Cuentas(usuario,password,correo,lesion,grado,str(today),"1",str(today))
        m1.crear_carpetam()
    if lesion == "Tobillo":
        m1 = Cuentas(usuario,password,correo,lesion,grado,str(today),"1",str(today))
        m1.crear_carpetat()
    return "1"

def menu_validacion(usuario,password):
    datos = validar_usuario()
    ban=0
    _file = "usuarios.csv"
    archivo = open(_file,'w')
    archivo.write("USUARIO;PASSWORD;CORREO;LESION;GRADO;DIA_INICIO;DIA_RECUPERACION;ULTIMO_DIA_ACCESO"+"\n")
    archivo.close()
    for d in datos:
        c = 0
        d = d.replace("\n","").split(";")
        if d[0] == usuario:
            c = c+1
        if d[1] == password:
            c = c+1
        if c == 2:
            today = date.today()
            fecha = today-datetime.strptime(d[5], '%Y-%m-%d').date()
            fecha_r = str(fecha)
            L = fecha_r.split(",")
            S = L[0].split(" ")
            if S[0] == "0:00:00":
                S[0]= "1"
            
            if d[3] == "Rodilla":
                initial_count = 0
                dir = './Archivos/Rodilla'+"/"+usuario
                for path in os.listdir(dir):
                    if os.path.isfile(os.path.join(dir, path)):
                        initial_count += 1
                print(initial_count)
            if d[3] == "Tobillo":
                initial_count = 0
                dir = './Archivos/Tobillo'+"/"+usuario
                for path in os.listdir(dir):
                    if os.path.isfile(os.path.join(dir, path)):
                        initial_count += 1
                print(initial_count)
            if d[3] == "Muneca":
                initial_count = 0
                dir = './Archivos/Muñeca'+"/"+usuario
                for path in os.listdir(dir):
                    if os.path.isfile(os.path.join(dir, path)):
                        initial_count += 1
                print(initial_count)

            if S[0] > str(initial_count):
                dia_r = str(initial_count)
            elif str(initial_count) > S[0]:
                dia_r = S[0]
            elif str(initial_count) == S[0]:
                dia_r = S[0]

            if dia_r == "0":
                dia_r="1"
            ##sustituir dias
            ban=1
            l= Cuentas(d[0],d[1],d[2],d[3],d[4],d[5],dia_r,str(today))
            l.guardar_archivo()
        else:
            l = Cuentas(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])
            l.guardar_archivo()
    if ban == 1:
        return "1"
    else:
        return "0"

def tipo_menu(usuario,password):
    datos = validar_usuario()
    for d in datos:
        c = 0
        d = d.replace("\n","").split(";")
        if d[0] == usuario:
            c = c+1
        if d[1] == password:
            c = c+1
        if c == 2:
            tipo = d[3]
            print(tipo)
            return tipo
    return

def tipo_dia(usuario,password):
    datos = validar_usuario()
    for d in datos:
        c = 0
        d = d.replace("\n","").split(";")
        if d[0] == usuario:
            c = c+1
        if d[1] == password:
            c = c+1
        if c == 2:
            L = d[6].split(",")
            S = L[0].split(" ")
            dia = S[0]
            return dia
    return

def tipo_grado(usuario,password):
    datos = validar_usuario()
    for d in datos:
        c = 0
        d = d.replace("\n","").split(";")
        if d[0] == usuario:
            c = c+1
        if d[1] == password:
            c = c+1
        if c == 2:
            grado = d[4]
            print(grado)
            return grado
    return