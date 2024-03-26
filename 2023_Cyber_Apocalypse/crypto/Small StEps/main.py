from Crypto.Util.number import long_to_bytes


ct = 70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
N = 7553724917178776446351158413775481699655359242186469122936217179893107586932408504417037444253401210131378477132162160534902516763621008292182841879647607
e = 3

low = 0
high = ct

mid = (low+high)//2
mid3 = mid**3
        
while mid3 != ct:

    mid = (low+high)//2
    mid3 = mid**3
            
    if mid3 < ct: 
        
        low = mid+1
    
    elif mid3 > ct: 

        high = mid-1

m = mid
m = long_to_bytes(m)
m = m.decode()

print(m)