attendance = [18, 20, 19, 15, 21]


full=0
name=0
for views in attendance:
    name=name+views
    if views >= 20:
        print("Class Full")
        
        
        full = full+1
        
    
    else:
        print("Not Full")
        

print(full)
print(name)
        
