#open the file names.txt in read mode. 
# 2. read all lines from the file into a list name lines. 
# 3. define the variable nametoserach with the value lee. 
# 4. For each line in line. 
#   * chekc if name_to_serach is in the current line 
#   * if ture, print the line

with open("names.txt") as f:
    lines = f.readlines()

names_to_search = "Mahdi"
for line in lines:
    if names_to_search in line:
        print(line)
        