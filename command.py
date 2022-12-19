import sqlite3

database = "usuarios.db"

class command_a:

  @staticmethod
  def command_iniciarsesion(var_a,var_p):

      conexion = sqlite3.connect("usuariostest.db")
      cursor = conexion.cursor()
      cursor.execute("SELECT * FROM USUARIOS USERNAME")
      datos = cursor.fetchall()
      conexion.commit()
      conexion.close()
      open = None
      for iter in datos:
        nombre = iter[4]
        password = iter[6]
        rol = iter[7]
        if nombre == var_a and password == var_p and rol == "cliente":
          open = "cliente"
        elif nombre == var_a and password == var_p and rol == "Cinemark Team":
          open = "Cinemark Team"
      return open  

  """@staticmethod
  def command_salas():
      lista = []
      conexion = sqlite3.connect("CinemarkSalas.db")
      cursor = conexion.cursor()
      cursor.execute("SELECT * FROM SALAS NOMBRE")
      datos = cursor.fetchall()
      conexion.commit()
      conexion.close()
      for iter in datos:
        lista.append(iter[1])
      print(lista)
      return lista"""

  @staticmethod
  def update_nombre(var):
      conexion = sqlite3.connect("CinemarkSalas.db")
      cursor = conexion.cursor()
      cursor.execute("UPDATE SALAS SET NOMBRE(?) WHERE")
      conexion.commit()
      conexion.close()  