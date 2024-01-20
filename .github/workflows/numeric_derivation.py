
def derive(f, x, h=0.0001):
   # return None  # TODO: implement this function 
    pd = (f(x+h)-f(x))/h
    return pd
