
#FILE HANDLING
---------------
-> File handler is an object of file to manitain several function of file like,creating,reading,updating and deleting the file.

-->opening a file is in two ways
1.open()
2.with open()
name=open('filename','mode') as name
------
name.close()

modes
-----
'r' --> is used to reading the file,error if file does not exist..
'a'-->is used to add text into file at last index,if file does not exist..
'w'-->is used to add the text into file but it will override of all text inside file..
'x'-->used to create the file ,but will throw error if we are used

method
-------
write()
read()
------
-->This method can read entire file chunk by chunk where we can specify the
readline()
-->can read only one line at a time in a file..
readlines
-->It will read entire file and gives in a list where each line is each index in the list.



so=open('demo.txt','r')
print(so.read())
so.close

so=open('demo.txt','w')
print(so.write('python'))
so.close

with open('demo.txt','w') as so:
    print(so.write('python'))


with open('demo.txt','w') as any_:
    any_.write('hello')
    
any_=open('demo.txt','r')
print(any_.read(3))
any_.close()



any_=open('demo.txt','r')
print(any_.readline())
any_.close()

any_=open('demo.txt','r')
print(any_.readlines())
any_.close()


















    

