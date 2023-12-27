required_amenities=[]
block_details=[]
amenities={"School":False,"Gym":False,"Pool":False,"Hospital":False,"Store":False}
print("Enter your requirements :(1-required/0-not required)")
for x in amenities.keys():
	k=int(input(x))
	if k==1:
		required_amenities.append(x)
