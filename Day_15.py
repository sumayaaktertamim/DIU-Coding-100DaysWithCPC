# A. Anton and Polyhedrons-800
n=int(input())
polyhedron={
"Icosahedron" :20,
"Cube"        : 6,
"Tetrahedron" : 4,
"Dodecahedron":12,
"Octahedron"  : 8
}
total_faces=0
for i in range(n):
    poly=input()
    total_faces+=polyhedron[poly]
print(total_faces)
    