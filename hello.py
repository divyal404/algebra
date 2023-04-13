def solve_equation(eq):
    # Remove all spaces from the equation
    eq = eq.replace(" ", "")
    
    # Check if the equation is linear or quadratic
    if "^2" in eq:
        # Quadratic equation
        a = int(eq.split("x^2")[0])
        b = int(eq.split("x^2")[1].split("x")[0])
        c = int(eq.split("x^2")[1].split("x")[1].split("=")[0])
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "No real solutions"
        elif discriminant == 0:
            return -b/(2*a)
        else:
            return (-b + discriminant**0.5)/(2*a), (-b - discriminant**0.5)/(2*a)
    else:
        # Linear equation
        x = eq.split("x")[0]
        y = eq.split("x")[1].split("=")[0]
        return int(y)/int(x)
e = " 5x - 3 = 0"
s = solve_equation(e)
print(s)