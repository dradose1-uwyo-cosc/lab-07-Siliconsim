from pathlib import Path

key_value_pairs = []
mappings = {
    "w": " ",
    "*": "*"
}

contents = ""
cleaned_contents = ""
output_string = ""
debug = ""

def output_char(pair):
    if (len(pair) <= 1):
        return
    global output_string
    output_char = mappings[pair[0]]
    
    times_to_output = int(pair[1])
    output_string += output_char * times_to_output
    
    #for i in range(times_to_output + 1):
        #output_string += output_char

try:
    path = Path("prompt.txt")
    contents = path.read_text()
except FileNotFoundError:
    print("File not found!")

# Remove whitespaces and tabs from string
cleaned_contents = contents.replace("\n", "")
cleaned_contents = cleaned_contents.split("\t")

# Split each key value pair in the list into separate individual lists 
for i in range(0, len(cleaned_contents)):
    output_char(cleaned_contents[i].split(":"))
Path("out.txt").write_text(output_string)