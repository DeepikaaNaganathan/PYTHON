file1 = open(r"C:\Users\Deepikaa Naganathan\Desktop\SAYUR\Python\File_Handling\Input_file.txt","r")
file2 = open(r"C:\Users\Deepikaa Naganathan\Desktop\SAYUR\Python\File_Handling\Output_file.txt","w")
for line in file1:
    file2.write(line)

file1.close()
file2.close()

file2 = open(r"C:\Users\Deepikaa Naganathan\Desktop\SAYUR\Python\File_Handling\Output_file.txt","r")
print(file2.read())
file2.close()

"""

OUTPUT
Hai this is Deepikaa_Naganathan.This is an input file

"""
