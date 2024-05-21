def convert_to_layered_list(filename):
    layered_list = []
    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace characters
            line = line.strip()
            # Split the line at the first occurrence of " - "
            if " - " in line:
                number, location = line.split(" - ", 1)
                # Append the [number, location] pair to the layered list
                layered_list.append([number, location])
    return layered_list

def main():
    filename = 'codes.txt'
    layered_list = convert_to_layered_list(filename)
    for n in layered_list:
        print(n)

if __name__ == "__main__":
    main()
