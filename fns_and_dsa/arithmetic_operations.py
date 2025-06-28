def perform_operation(num1t,num2,operation):
   
    if operation=='add':
        return(num1+num2)
    elif operation=='subtract':
        return(num1-num2)
    elif operation=='divide':
        if num2==0:
            raise ValueError('cannot divide by zero')
        return(num1/num2)
    elif operation=='multiply':
        return(num1*num2)
    else:
         raise ValueError("Unsupported operation. Use add,subtract,divide or multiply")
print(perform_operation(5,0,'divide'))

