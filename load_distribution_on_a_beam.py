# (c) 2025 Ma. Womah S. Montejo and Denise Laureen Paredes
# Load Distribution on a Beam

def load_distribution_on_a_beam():
    w = float(input("Enter the load per unit (N/m):"))
    L = float(input("Enter the length of the beam (m):")) 
    
    
    F = w * L
    
    print(f"So, the total load actingt on the beam is {F:.2f}N.\n") 
    
if __name__== "__main__":
    load_distribution_on_a_beam()     
