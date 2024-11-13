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

def concat_char(pair):
    global output_string
    if (len(pair) <= 1):
        return
    elif (pair[0] == "\nw"):
        output_string += "\n"
        pair[0] = "w"
    
    output_char = mappings[pair[0]]
    times_to_output = int(pair[1])
    for i in range(times_to_output + 1):
        output_string += output_char

try:
    path = Path("prompt.txt")
    contents = path.read_text()
except FileNotFoundError:
    print("File not found!")

# Remove tabs from string
cleaned_contents = contents.split("\t")

# Split each key value pair in the list into separate individual lists and write to the file once completed
for kvp in cleaned_contents:
    concat_char(kvp.split(":"))
Path("out.txt").write_text(output_string)