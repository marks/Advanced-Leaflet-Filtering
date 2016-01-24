import random

names = ["Erin", "Dustin", "Hannah", "Des", "Lance", "Tyler", "Jacob", "Heather", "Beth", "Nate"]
places = ["Bedroom", "Bathroom", "Kitchen", "Car", "Hair Stylist"]
yorn = ["y", "n"]

outfile = open("data.csv", 'w')
outfile.write("Name,lat,lng,A.C.,Bathroom,Food,\n")

markers = input("Enter number of markers:")
i =0
while (i < int(markers)):
    lat = random.uniform(46.698808,46.757938)
    lng = random.uniform(-117.214233,-117.102469)

    place = random.choice(names) + "'s " + random.choice(places)

    ac = random.choice(yorn)
    Bathroom = random.choice(yorn)
    Food = random.choice(yorn)
    
    line = place+","+str(lat)+","+str(lng)+"," + ac + "," + Bathroom + "," + Food + "\n"
    outfile.write(line)
    i += 1
    
outfile.close()    
