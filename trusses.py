import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of input file")
parser.add_argument("k", help="number of trusses",
                    type=int, default=2)

args = parser.parse_args()

f = open(args.filename)
span = []
for line in f:
    nodes = []
    parts = line.rstrip()
    yolo1 = parts.split(' ')
    nodes = [yolo1[0], yolo1[1]]
    span.append(nodes)
#print(span)
#Η συνάρτηση neibhors παίρνει σαν παραμέτρους την λίστα span και εναν κόμβο.
#Διατρέχει την λίστα span και αν ο κόμβος-παράμετρος ισούται με κάποιον κόμβο της λίστας
#προσθέτει στην λίστα γειτνίασης του κόμβου όρισμα τον γειτονικό κόμβο
#επιστρέφει μία λίστα neig που περίεχει τους γείτονες του κόμβου j
def neighbors(whole, j):
    neig=[]
    for egde in whole:
        if (j==egde[0]):
            neig.append(egde[1])
        elif (j==egde[1]):
            neig.append(egde[0])
    return neig

#Η συνάρτηση size_inter παίρνει ως παραμέτρους 2 λίστες οι οποίες περιέχουν τους
#γείτονες 2 κόμβων και επιστρέφει το μέγεθος της τομής τους
def size_inter(b , m):
    w=0
    for i in b:
        for j in m:
            if (i==j):
                w=w+1
    return w



# Διατρέχω την λίστα span και αν κάποιο i ικανοποιεί την συνθήκη το προσθέτω
#στην λίστα removals, η οποία στο τέλος του loop θα περιέχει όλους τους κόμβους
#που πρέπει να αφαιρεθούν
removals=[]
for i in span:
    if (size_inter(neighbors(span, i[0]), neighbors(span, i[1])) < (args.k - 2)):
        removals.append(i)

#αφαιρώ την removals από την span
for item in removals:
    while span.count(item) > 0:
        span.remove(item)


z=0
for i in span:
    if (z%args.k==0): #συνθήκη για να τυπώνεται μόνο μία φορά το κάθε δικτύωμα
        dikt= neighbors(span, i[0])
        dikt.append(i[0])
        #μετατρέπω τα elements σε int
        for j in range(len(dikt)):
            dikt[j] = int(dikt[j])

        show=tuple(dikt)
        print(show)
    z=z+1


f.close()
