def City_Pais(City, Pais, Po=""):
   if Po: 
       flag = City+ ", " +Pais+ " e População = " + Po 
   else:
       flag = City+ ", " +Pais
   return flag.title()