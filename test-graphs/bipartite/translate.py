def parse(value):
    if value.find('r') != -1:
        value = int(value.replace('r', ''))
        return str(value + 100)
    else:
        return value

with open('old.txt', 'r') as file:
    file1 = open("bipartite100-10-percent-pp.txt", "w")
    for line in file:
        # count = file.readlines()
        values = line.split()
        if values:
            file1.write(parse(values[0]) + " " + parse(values[1]) + " " + values[2] + "\n")
