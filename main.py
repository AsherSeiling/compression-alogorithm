import regular_expression
import random

# The data for the file storage
file_adress = "fileTest.py"

# Arrays
encoded_text = []
abreviation_array = []
reference_array = []

# Compession for the file
def compress(margin):
    # Import file
    text_data = open(file_adress, "r")
    text_data = [x.rstrip("\n") for x in text_data.readlines()]

    # Analize margin the file
    for i in text_data:
        counter = 0
        run = True
        while run == True:
            var_buffer = i[counter:(counter + 4)]
            if i in reference_array:
                encoded_text.append(abreviation_array[reference_array.index(var_buffer)])
            else:
                pass



# Class for importing files to compress
class import_files:
    def import_code():
        print("What is the adress of the file that you want to compress")
        file_adress = input()
    def import_compresed_file():
        print("Place the adress of the file that you want to decompress")
        file_adress = input()

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
    #main()
    compress(4)
