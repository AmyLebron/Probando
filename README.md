def notas(examenA,examenB,dias_asistidos,practica):
                                                          

  calificacion_final= int(examenA) + 
int(examenB)+ int(dias_asistidos)+ 
int(practica)

  if calificacion_final<70:

   print("No aprobado.")

  elif calificacion_final>=70
and calificacion_final <80:

    print("Su nota es:",calificacion_final,". Pasaste a chepita.")

  elif calificacion_final >=80
and calificacion_final <90:

      print("Su nota es:",calificacion_final,". Está aprobado.")

  elif calificacion_final >=90
and calificacion_final <=100:

    print("Su nota es:",calificacion_final,". Felicidades, tiene una calificación sobresaliente.")

      

  else:

      print("¿Tú estás seguro de que eres de esta clase?")



#Para completar un total de cien puntos, el estudiante debe haber sacado la

#siguiente nota: 20 primer parcial, 30 segundo parcial, 30 días de asistencia para obtener 30, y 20 de práctica.



examenA=input("inserta el valor obtenido en tu primer parcial: ")

examenB=input("inserta el valor obtenido en tu segundo parcial: ")

dias_asistidos=input("inserta los días asistidos: ")

practica=input("inserta el valor obtenido en tu práctica: ")



notas(examenA,examenB,dias_asistidos,practica)
