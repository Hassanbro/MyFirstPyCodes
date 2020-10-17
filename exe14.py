#Strings

a = "Hello"

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#print the total number of characters (length)
print(len(a))

name = "Hassan Hamadu"
b = "I am an engineer"
c = "I want to be a big time consultant"
print(len(name))

#lower case conversion
k = name.lower()

l = b.lower()

print(k)
print(l)

#UPPER CASE CONVERSION

m = c.upper()

print(m)

n = b.upper()

print(n)

#Replace function

Definition = """
Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer programming languages, such as JavaScript, Python, and C++.
"""
y = Definition.replace("process", "method")

m = y.replace("Programming", "Coding")

l = m.replace("computer", "PC")

k = l.replace("JavaScript", "Fortran 22").replace("Python", "Anaconda").replace("C++", "Visual Studio")


print(y)
print(m)
print(l)
print(k)
