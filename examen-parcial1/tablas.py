# Miguel Heranadez
# tablas.py
# 4.- programa tablas.py, que permita capturar un numero positivo
# e imprima su tabla de multiplicar.
# Ejemplo:

# n = 5
# 5
# 10
# 15
# ..
# 50

# n = -1

# ERROR

# NOTA: Validar que solo permite valores positivos

 mientras que es  cierto :

    number  =  input ( "Ingrese un numero:" )
    prueba :
        val  =  int ( número )
        si  val  <  0 :  
            print ( "Debe ser un valor positivo, intenta de nuevo." )
            Seguir
        rotura
    excepto  ValueError :
        print ( "Tiene que se un entero" )     

para  i  en el  rango ( 1 , 11 ):
   imprimir ( val , 'x' , i , '=' , val * i )
