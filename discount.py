amt=float(input('enter the amount: '))
if(amt>0):
    if amt>=1000:
       disc = amt*0.1
    elif amt>=2000:
        disc=amt*0.2
    elif amt>=3000:
        disc= amt*0.3
    elif amt>=5000:
        dic= amt*0.4
    else:
         print("no discount")

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
    
    
    '''output
    enter amount = 1200
    disount = 120
    net pay = 1080'''
    
