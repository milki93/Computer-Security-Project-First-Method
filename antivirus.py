import glob, re

def check_for_signatures():
    # get all programs in the directory
    programs = glob.glob("*.py")
    for p in programs:
        if p == "antivirus.py" or p == "virus.py" :
            continue
        file = open(p, "r")
        lines = file.readlines()
        file.close()

        begin = 0
        end = 0
        for i,line in enumerate(lines):
            if (re.search("^# starting virus code",line)):
                begin = i
            if (re.search("^# end of virus", line)):
                end = i
        lines = lines[:begin] + lines[end+1:]
        print(lines)
        file = open(p,'w')
        file.writelines(lines)
        file.close()

check_for_signatures()
