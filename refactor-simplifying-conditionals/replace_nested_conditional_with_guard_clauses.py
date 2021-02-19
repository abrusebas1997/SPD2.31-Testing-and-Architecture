
def extract_position(line):
    if 'x:' in line:
        start_index = line.find('x:',) + 2
        return line[start_index:]
    return None

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)
