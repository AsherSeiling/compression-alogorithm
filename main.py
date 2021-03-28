import regular_expression
import random
# The data for the file storage
file_adress = "fileTest.txt"
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = alpha.upper()

# Arrays
encoded_text = []
abreviation_array = ["/-/"]
reference_array = ["\n"]
# Function to make a id for the thing
def id_gen():
    random_num = random.randint(0, 25)
    random_num2 = random.randint(0, 25)
    random_num3 = random.randint(0, 9)
    if random_num == random_num2:
        random_num2 = random.randint(0, 25)
        if random_num == random_num2:
            random_num2 = random.randint(0, 25)
    return f"{alpha[random_num]}{random_num3}{alpha_upper[random_num2]}"

# Compession for the file
def compress(margin):
    # Import file
    text_data = open(file_adress, "r")
    text_data = [x.rstrip("\n") for x in text_data.readlines()]

    # Analize margin the file
    for i in text_data:
        temp_buffer = ""
        counter = 0
        for x in i:
            temp_buffer += x
            if len(temp_buffer) >= margin or (len(i) - counter) < margin:
                counter += margin
                if temp_buffer in reference_array:
                    index1 = reference_array.index(temp_buffer)
                    encoded_text.append(abreviation_array[index1])
                else:
                    random_id = id_gen()
                    if random_id in abreviation_array:
                        random_id = id_gen()
                        if random_id in abreviation_array:
                            random_id = id_gen()
                            if random_id in abreviation_array:
                                random_id = id_gen()
                    abreviation_array.append(random_id)
                    reference_array.append(temp_buffer)
                    encoded_text.append(random_id)
                temp_buffer = ""
        encoded_text.append("/n/")
    save_compresed()
def save_compresed():
    print("Input the name of the file")
    #`file_name = input()
    file_name = "test"
    new_file = open(file_name + "_compressed.txt", "w+")
    buffer = ""
    #for i in abreviation_array:
    #    buffer += i + ","
    #new_file.write(f"{buffer}\n")
    #for i in reference_array:
    #    new_file.write(i + "\n")
    #buffer = ""
    for i in encoded_text:
        buffer += i
    new_file.write(f"{buffer}\n")

# Class for importing files to compress
class import_files:
    def import_code():
        print("What is the adress of the file that you want to compress")
        file_adress = input()
    def import_compresed_file():
        print("Place the adress of the file that you want to decompress")
        file_adress = input()

def decompress():
    pass
# Main function that runs on startup
def main():
    print("Do you want to compress or decompress(comp:decomp)")
    input_select = input().lower()
    if input_select == "decomp":
        import_files.import_compresed_file()
    elif input_select == "comp":
        import_files.import_code()
    else:
        main()
    print("What is the margin that you want to compress your file with")
    margin = int("Input")
    if input_select == "decomp":
        pass
    elif input_select == "comp":
        compress(margin)

# Start of the file run
if __name__=='__main__':
    compress(6)