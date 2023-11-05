from Graph import cities

file_in = open("input.txt", "r")
n = int(file_in.readline())
cts = cities(n)
points = []
for i in range(n):
    points.append(tuple(map(float, file_in.readline().split())))
for i in range(n):
    for j in range(i + 1, n):
        cts[i, j] = round(((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5, 3)
cts.draw_graph('images of cities/my_city.png')
print(cts)

d = [[float('inf')] * (2**n) for _ in range(n)]
d[0][0] = 0.0
print(f'The shortest way is {round(cts.tsp_dp(0, 1, d), 3)}')

