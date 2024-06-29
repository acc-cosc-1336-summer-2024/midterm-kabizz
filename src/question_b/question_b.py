#write functions here, don't add input('') statements here!
#Criteria for Category
Adult = 20
Teenager = 13
Child = 2
Infant = 1
#Converts Age to Category
def get_person_category(a):    
      if a >= Adult:
        return ('Adult')
      elif a >= Teenager:
        return ('Teenager')    
      elif a >= Child:
        return ('Child')
      else: a >= Infant 
      return ('Infant')