    def p(self):
       try: 
          id=int(self.entrada_id.get())
          registro=self.pooo(id)
          self.entrada_id
          self.entrada_nombre
          self.entrada_email
          self.entrada_curp
          self.entrada_matricula
       except ValueError:
           messagebox.showerror("dame la id ","nesesito la id para poder empezar")
        
    
    def pooo(self,id):
        idd=int(id)
        cursor = self.db.cursor()
        sentencia = '''SELECT id,nombre,edad,email,curp,matricula FROM alumnos WHERE id=%s'''.format(idd)
        cursor.execute(sentencia)
        registro = cursor.fetchall()
        return registro