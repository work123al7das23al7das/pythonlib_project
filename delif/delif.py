#delete empty lines in file
import glob, os , pathlib

os.chdir("change")
file_names = [] 
for file in glob.glob("*.asm"):
    file_names.append(file)
for file in glob.glob("*.inc"):
    file_names.append(file)    

print(file_names)             

empty_lines = 0
for i in range(len(file_names)):
    with open(file_names[i], 'r', encoding='utf-8') as inf, open( "new/"+file_names[i],'w', encoding='utf-8') as out:
        for line in inf:
            if line.strip():            
                if empty_lines>1:
                    out.write("\n")
                empty_lines = 0
                out.write(line)
            else:
                empty_lines=empty_lines+1
