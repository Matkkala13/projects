#This is sort of a library for formulas. It is very clumsy, with time I will do it better,
# but it has been a while since I wrote python code so I am rusty. I want it to be an equation solver for useful formulas, like the 
# quadratic equation, some physics equations and others that will be very useful to do quickly. Perhaps this project can evolve in
# a serious equation solver, which performs actual algebra and is not just this messy agroupation of solved formulas for each variable.
#it would be cool to make a math engine, in which you write any equation and it solves it. But for now, I will just do it like this.


# Equation of voltage divider: Vout=(Z2/Z1+Z2)*Vin

def voltage_divider_conversion(Vin, Vout, Z1, Z2, r):
    if r == "Vin":
        return (Vout*(Z1+Z2))/Z1
    elif r == "Vout":
        return (Z2/Z1+Z2)*Vin
    elif r == "Z1":
        return (-Vout*Z2)/(Vout-Vin)
    elif r == "Z2":
        return (Z1*(Vout-Vin))/(-Vout)
    else:
        return "Variable to solve is not valid."

