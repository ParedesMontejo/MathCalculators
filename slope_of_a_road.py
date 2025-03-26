# (c) 2025 Ma. Womah S. Montejo and Denise Laureen Paredes
# Slope of a Road

def slope_of_a_road():
    rise = float(input("Enter the rise of the road (m):"))
    run  = float(input("Enter the run of the road(m):")) 
    
    
    slope = rise/run * 100
    
    print(f"So, the slope of the road is {slope:.2f}s%.") 
    
if __name__== "__main__":
    slope_of_a_road()  