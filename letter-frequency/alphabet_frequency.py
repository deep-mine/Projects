#alphabet frequency
import matplotlib.pyplot as plt

def count_char(text, char):
    count = 0
    for c in text:
        c = c.lower()
        if c == char:
            count += 1
    return count

filename1 = input("Enter a filename: ")
with open(filename1) as f1:
    text1 = f1.read()
    
frq1 = []
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text1, char) / len(text1)
    print("{0} - {1}%".format(char, round(perc, 2)))    
    frq1.append(round(perc,2))

filename2 = input("Enter a filename: ")
with open(filename2) as f2:
    text = f2.read()
    
frq2 = []
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))    
    frq2.append(round(perc,2))
    
x=[]
for i in range(1,27):
    x.append(i)
xa = []
for i in range(0,27):
    xa.append(chr(i+97))

plt.plot(x,frq1)
#plt.scatter(x,frq1)

plt.plot(x,frq2)
#plt.scatter(x,frq2)


plt.xticks(x,xa)
plt.xlabel("alphabet--->")
plt.ylabel("percentage of occurrence--->")
plt.title("Alphabet frequency in "+filename1+" and "+filename2)
plt.grid()
plt.show()