import matplotlib.pyplot as plt

dots = []
with open("DS0.txt", "r") as file:
    for line in file:
        i = line.index("\n")
        dots.append(line[0:i].split(" "))

file.close()

for el in dots:
    el[0] = int(el[0])
    el[1] = int(el[1])


x = [x[0] for x in dots]
y = [y[1] for y in dots]

fig = plt.figure(figsize = (10,5.625))
plt.title("Lab2", fontsize = 12)
plt.xlabel('X', fontsize=12, color='blue')
plt.ylabel('Y', fontsize=12, color='blue')
plt.plot(y, x, "ro")
fig.savefig('saved_figure.png')