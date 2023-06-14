import re

def make_variable_names_consistent(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expressions to find variable names
    variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    variables = re.findall(variable_pattern, content)

    # Create a mapping of old names to new names
    variable_map = {}
    for variable in variables:
        if variable not in variable_map:
            new_variable = convert_to_consistent_name(variable)
            variable_map[variable] = new_variable

    # Replace variable names in the content
    for variable, new_variable in variable_map.items():
        content = re.sub(r'\b{}\b'.format(re.escape(variable)), new_variable, content)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

def convert_to_consistent_name(variable_name):
    # Apply your desired naming convention here
    # This example converts variable names to lowercase
    return variable_name.lower()

def main():
    python_file_path = input("Enter the path to the Python file: ")
    make_variable_names_consistent(python_file_path)
    print("Variable names have been made consistent in the file.")

if __name__ == "__main__":
    main()
