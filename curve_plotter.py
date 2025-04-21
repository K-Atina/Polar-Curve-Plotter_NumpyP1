import numpy as np
import time
import sys
import os
import matplotlib.pyplot as plt

def plot_polars(r_func , theta_range=(0,2 *np.pi),label=''):
    #We define function plot_polars that will take in a function,a range and a label or "name" for the curve
    theta = np.linspace(*theta_range, 1000)
    #the linspace function will give us evenly spaced values defined in the tuple (theta_range)
    #theta_range will give 1000 values from 0 to 2pi (360 degrees)
    r=r_func(theta)
    
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111,polar=True)
    #Will create a polar plot with one row,one column and one plot hence: 111
    ax.plot(theta,r,label=label)
    ax.legend()
    plt.show()
    

#Cardioid Function --> A polar function that produces a heart-shaped graph
#Function: r(Θ)= 1 + cos(Θ)
def cardioid(theta):
    return 1 + np.cos(theta)

#Lemniscate of Bernoulli --> A polar function that produced the plane curve
#Function: r(θ) = ((2)^(1/2)*cos(θ))/(1+(sin(θ)^2)) OR r^2 = (a^2)*cos(2θ)
def lemniscate(theta,a=1):
    return np.sqrt(a**2 * np.cos(2 * theta))


#Archimedean Spiral
#Function: r(θ)= a +bθ
# a controls the size and b controls the spacing
def archimedean_spiral(theta,a=0.5,b=2):
    return a + b * theta


#Rose Curve
#Function: r(θ)= a * sin(kθ)
# k determines the number of petals and a determines the size
def rose_curve(theta,a=1,k=5):
    return a * np.sin(k * theta)

#Spiral of fermat
#Function r(θ)= a * sqrt(θ)
def fermat_spiral(theta, a=1):
    return a * np.sqrt(theta)

#Logarithmic spiral
def logarithmic_spiral(theta, a=0.1, b=0.2):
    return a * np.exp(b * theta)

#Butterfly curve
#Function: r(θ)=e ^(sin(θ))−2cos(4θ)+sin^5((2θ−π)/24)
def butterfly_curve(theta):
    return np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) + np.sin((2 * theta - np.pi) / 24) ** 5

#Epispiral Equation
#Function:r(θ)=a/(1+bsin(θ))
def epispiral(theta, a=1, b=0.5):
    return a / (1 + b * np.sin(theta))



#Function to have type-out effect
def type_out(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 
    
#Function to clear terminal 
def clear_screen():
    os.system('cls' if os.name== 'nt' else 'clear')
    
def exit_program():
    type_out("Exiting program...",delay=0.08)
    time.sleep(0.4)
    type_out("Program exited successfully!")
    sys.exit()

    
#Main function
def main():
    
    while True:
        type_out("Welcome to the curve plotter.")
        time.sleep(0.3)
        type_out("\n===== MENU =====")
        time.sleep(0.3)
        type_out("1. Cardioid Curve")
        time.sleep(0.3)
        type_out("2. Lemniscate of Bernoulli")
        time.sleep(0.3)
        type_out("3. Archimediean Spiral")
        time.sleep(0.3)
        type_out("4. Rose curve")
        time.sleep(0.3)
        type_out("5. Spiral of Fermat")
        time.sleep(0.3)
        type_out("6. Logarithmic Spiral")
        time.sleep(0.3)
        type_out("7. Butterfly Curve")
        time.sleep(0.3)
        type_out("8. Epispiral")
        time.sleep(0.3)
        type_out("9. Exit")
        time.sleep(0.3)
        
        type_out("Awaiting choice: ")
        choice = input()
        
        if choice == "1":
            try:
                plot_polars(cardioid,label="Cardioid Curve")   
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                print("The lemniscate of Bernoulli function has 'a' which is meant to define the size of the graph")
                a = float(input("Enter the value for a: "))
                plot_polars(lambda theta: lemniscate(theta, a), label=f"Lemniscate (a={a})")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            try:
                print("Define a the size of the graph and b the spacing.")
                a = float(input("Enter value for a: "))
                b = float(input("Enter value for b: "))
                plot_polars(lambda theta: archimedean_spiral(theta, a, b), label=f"Archimedean Spiral (a={a}, b={b})")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "4":
            try:
                print("In the rose function a defines the size and k defines the no. of petals")
                a = float(input("Enter value for a: "))
                k = float(input("Enter value for k: "))
                plot_polars(lambda theta: rose_curve(theta, a, k), label=f"Rose Curve (a={a}, k={k})")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            try:
                print("a controls the size of the spiral")
                a = float(input("Enter value for a: "))
                plot_polars(lambda theta: fermat_spiral(theta, a), label=f"Fermat Spiral (a={a})")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "6":
            try:
                print("a controls the size while b controls how tightly the spirals winds")
                a = float(input("Enter value for a: "))
                b = float(input("Enter value for b: "))
                plot_polars(lambda theta: logarithmic_spiral(theta, a, b), label=f"Log Spiral (a={a}, b={b})")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "7":
            try:
                plot_polars(butterfly_curve, theta_range=(0, 12 * np.pi), label="Butterfly Curve")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "8":
            try:
                print("a controls the size and b controls the bulge")
                a = float(input("Enter value for a: "))
                b = float(input("Enter value for b: "))
                plot_polars(lambda theta: epispiral(theta, a, b), label=f"Epispiral (a={a}, b={b})")
            except ValueError as e:
                print(f"Error: {e}")

        
        elif choice == "9":
            exit_program()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    



