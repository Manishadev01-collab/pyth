# python can be used to perform opewrations in a file .(read & write data)

# Type of all file 
# 1. Text files : txt,.docx , .log etc.
# binary files : mp4, .mov4, .png,.jpeg etc.
 

f=open("demo.txt", "r")
# data = f.read(5)
# print(data)
data = f.read()
print(data)
print(type(data))
f.close()



f = open("demo.txt", "r")
line1 = f.readline()
print(line1)


line2 = f.readline()
print(line2)


line3 = f.readline()
print(line3)
f.close()


# Writing  to a file 
f = open("demo.txt","w")
f.write("this is a new line")    # overwrites the entire file















# // Character               Meaning 
# 'r'            open for reading (default)        
# 'w'            open for writing ,truncting the file first
# 'x'            create a new file and open it for writing
# 'a'            open for writing , appending to the end of the file
# 'b'             binary mode
# 't'              text mode(default)
# '+'               open a disk file for updating (reading and writing)


# write mode  'w'   apppend mode 'a'

f = open("demo.txt", "w")
f = open("demo.txt", "a")

# f.write("Then I'LL MOVE TO react Js ")
f.write()
f.close()
























