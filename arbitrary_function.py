# INteger ko matrai sum nikaleko
def sum_number(*num):
    sum = 0
    for i in num:
      if isinstance(i,int):
         sum = sum +i
    return f'Sum of the integer part only is {sum}'
      

print(sum_number(1,2,3,4,"hello","test",5))      
  # diffference between arbitrary and keywowrd arbitrary-->read that

## if using ** keyword arbitrary then it store in dictionary

def per(**data):
   
    if 'eng' not in data or 'nep' not in data or 'math' not in data:
      print("ERROR")
    else:
       print("eng",data['eng']) 
       print("nep",data['nep']) 
       print("math",data['math'])  
per (eng=100, nep=12,math=50)    
per (eng=100, nep=12) 

## positional argument pahila auxa ani then arbitraray  argumentday