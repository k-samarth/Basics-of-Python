# Appending file:
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# Open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
