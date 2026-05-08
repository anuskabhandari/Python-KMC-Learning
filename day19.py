# Dictionary comprehension
# get all prices below 5 in Us dollars

us_price = {'milk':2.05 , 'bread': 2.6,'butter':3.6 , 'mobile':50, 'television':1000 , 'refrigerator':700}

nep_price={}

# non-pythonic way
for k,v in us_price.items():
    if v<5:
        nep_price.update({k:v})

print(nep_price)        


#  Using comprehension
us_price = {'milk':2.05 , 'bread': 2.6,'butter':3.6 , 'mobile':50, 'television':1000 , 'refrigerator':700}

nep_price ={
    k:v
    for k,v in us_price.items()
    if v<5
}
print(nep_price)

#price <5 => 13% tax
#else 20% tax
us_price = {'milk':2.05 , 'bread': 2.6,'butter':3.6 , 'mobile':50, 'television':1000 , 'refrigerator':700}
# non-pythonic using
for k, v in us_price.items():
    if v<5:
        nep_price.update({k: v *145 *1.13})
    else:
        nep_price.update({k: v *145 *1.20})

print(nep_price)        

# Using pythonic
us_price = {'milk':2.05 , 'bread': 2.6,'butter':3.6 , 'mobile':50, 'television':1000 , 'refrigerator':700}

output = {
    k:round(v*145*1.13 ,2)if v<5 else round(v* 145 * 1.20)
    for k,v in us_price.items()
}
print(output)