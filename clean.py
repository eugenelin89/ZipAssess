fname = "eugene.csv"
with open(fname, "r") as f:
    lines = f.readlines()
count = 0
clean = ""
for i in range(len(lines)):
    line = lines[i]
    count_i = 0
    for j in range(i+1, len(lines)):
        line_j = lines[j]
        if line == line_j:
            count += 1
            count_i += 1
    if count_i != 0:
        print(f"Line {i} duplicate: {count_i}")
    if count_i == 0:
        clean = clean + line


clean_file_name = fname + ".clean"
with open(clean_file_name, "a") as f:
    f.write(clean)
