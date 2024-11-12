def print_sums_from_file(file_name: str) -> None: #Opens a file with floats and prints the sum of the 2 floats on each line if possible -- else, prints an error message
    try:
        file = (open(file_name, "r"))
    except:
        print("Error opening file")
        exit()
    for line in file:
        if "," in line:
            floats = line.split(",")
        else:
            floats = line.split()
        if len(floats) != 2:
            print("There aren't 2 items in this line.")
        else:
            try:
                float_1 = float(floats[0])
                float_2 = float(floats[1])
                print(float_1 + float_2)
            except IndexError:
                print("There aren't 2 floats")
            except ValueError:
                print("Couldn't convert to float")
            except:
                print("Some error")
    file.close()

if __name__ == "__main__":
    print_sums_from_file("floats.txt")
    print_sums_from_file("What the heckers")