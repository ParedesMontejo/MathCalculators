# (c) 2025 Ma. Womah S. Montejo and Denise Laureen Paredes
# Cement Slurry Calculator


def cement_slurry_dilution():
    V2 = 1
    C1 = 200
    C2 = 50
    
    V1 = (V2 * C2) / C1 
    
    print(f"So, you need { V1:.2f} liters of the original slurry.")
    
if __name__== "__main__":
    cement_slurry_dilution() 
 