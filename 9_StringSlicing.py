name = "Raj kushwaha"
# 'name([index1:index2])' is used to print the specific number of character in the string
# NOTE: index1 include hoti hai par index2 nahi hoti
print(name[0:3])
# 'len' function is used to find out the length of the string
print(len(name))
print(name[:5]) # Agar ham index1 ki jagah kuch na lagae to python automatically 0 laga lega 
print(name[0:-4]) # Negetive ke case me python negetive value ke aage length of the number include kar leta hai
# for example:
print(name[0:len(name)-4])
n = "Harry"
print(n[-4:-2])