def divide(a,b):
    try:
      div= a/b
      return div
    except:
        print("Cannot division by zeroooo")  

print(divide(1,0))

#exception handling
def divide(a,b):
    try:
      div = a/b
      
    except ZeroDivisionError:
       print("cannot divide by 0")
    except TypeError:
       print("Invalid DataType")

    except Exception as e: ## e means the temporary variable to denote the error
       print(e)  
    else:
       print("I will run if there is no exception")  
       return div   
    
    finally : ## error aaye pani run hunxa error na aaye pani run hunxa
       print("I will run no matter what happens in the code.")
print(divide(1,2))          

