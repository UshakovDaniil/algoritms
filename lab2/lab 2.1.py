import math
ffffffff=0
func_glob =  lambda x: x**3
func_glob2= lambda x: math.fabs(x-0.2)
func_glob3= lambda x: x*math.sin(1/x)

a1, b1 = 0.0, 1.0
a2=0.01
e = 0.001

def brute_force_method(a, b, f):
    n = (b-a) / e
    f1=1
    y = f(a)
    for i in range(int(n)):
        x=a+i*(b-a)/(n+1)
        f1+=1
        if f(x)<y:
            y=f(x)
            f1+=1
    print("calculations ",f1, "\t iterations ",int(n)+1)
    return x

def half_divide_method(a, b, f):
    x = (a + b) / 2
    f1,itera=0,0
    while math.fabs(b-a) >= e:
        x = (a + b) / 2
        itera+=1
        f1+=2
        if f(a) * f(x) < 0:
            a = x
        else:
            b = x
    print("calculations ", f1, "\t iterations ", itera)
    return (a + b) / 2

def golden_section_method(a, b, f):
    f1,itera=0,0
    while (True):
        x1 = b - (b - a) / 1.618033
        x2 = a + (b - a) / 1.618033
        y1 = f(x1)
        y2 = f(x2)
        f1+=2
        itera+=1
        if (y1 >= y2):
            a = x1
        else:
            b = x2
        if (math.fabs(b - a) < e):
            print("calculations ", f1, "\t iterations ", itera)
            return (a+b)/2


print("x^3")
print ('root of the equation brute_force_method %s' % brute_force_method(a1, b1, func_glob))
print ('root of the equation half_divide_method %s' % half_divide_method(a1, b1, func_glob))
print ('root of the equation golden_section_method %s' % golden_section_method(a1, b1, func_glob))
print("|x-0.2|")
print ('root of the equation brute_force_method %s' % brute_force_method(a1, b1, func_glob2))
print ('root of the equation half_divide_method %s' % half_divide_method(a1, b1, func_glob2))
print ('root of the equation golden_section_method %s' % golden_section_method(a1, b1, func_glob2))
print("x sin(1/x)")
print ('root of the equation brute_force_method %s' % brute_force_method(a2, b1, func_glob3))
print ('root of the equation half_divide_method %s' % half_divide_method(a2, b1, func_glob3))
print ('root of the equation golden_section_method %s' % golden_section_method(a2, b1, func_glob3))