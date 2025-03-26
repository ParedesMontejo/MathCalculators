# (c) 2025 Ma. Womah S. Montejo and Denise Laureen Paredes
# Material Strength Calculation for Steel

def material_strength_calculation_for_steel():
    F = float(input("Enter the force applied to the beam (N):"))
    A = float(input("Enter the cross-sectional area of the beam (mm^2):")) 
    
    stress = F/A
    
    print(f"So, the stress on the beam is {stress:.2f}Pa.\n") 
    
if __name__== "__main__":
    material_strength_calculation_for_steel()     