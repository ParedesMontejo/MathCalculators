# (c) 2025 Ma. Womah S. Montejo and Denise Laureen Paredes
# Concrete Volume Calculation

def concrete_volume_calculation():
    L = float(input("Enter the length of the sidewalk (m):"))
    W = float(input("Enter the width of the sidewalk (m):")) 
    D = float(input("Enter the depth of the sidewalk (m):"))
    
    
    V = L*W*D
    
    print(f"So, you need {V:.2f}cubic meter of concrete.\n") 
    
if __name__== "__main__":
    concrete_volume_calculation()     