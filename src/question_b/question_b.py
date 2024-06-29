#write functions here, don't add input('') statements here!
Adult = 20
Teenager = 13
Child = 2
Infant = 1
def get_person_category(a):    
      if a >= Adult:
        return ('Adult')
      elif a >= Teenager:
        return ('Teenager')    
      elif a >= Child:
        return ('Child')
      else: a >= Infant 
      return ('Infant')