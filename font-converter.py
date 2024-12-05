import json

def convert_font_to_gitfiti():
    # Initialize result dictionary
    font_dict = {}

    # Read the header file content from local directory
    with open('font.h', 'r') as f:
        lines = f.readlines()

    current_char = None
    current_pattern = []

    for line in lines:
        line = line.strip()

        # Look for character definition start
        if line.startswith("{'") and '",' not in line:
            # Extract the character
            if "', {" in line:
                current_char = line.split("'")[1]
        # Look for pattern lines
        elif line.startswith('"') and (line.endswith('",') or line.endswith('}},')):
            # Convert the pattern line to numbers
            # Remove quotes and comma
            pattern = line[1:-2]
            # Convert to numeric values (# = 4, space = 0)
            numeric_pattern = [4 if c == '#' else 0 for c in pattern][:5]
            current_pattern.append(numeric_pattern)


        # Check if we've completed a character pattern
        if "}}," in line and current_char is not None:
            print("termianting")
            # Store the completed pattern
            if current_pattern:
                font_dict[current_char] = current_pattern
            # Reset for next character
            current_char = None
            current_pattern = []

    return font_dict

# Convert the font
font_dict = convert_font_to_gitfiti()

# Save to JSON file
with open('font_gitfiti.json', 'w') as f:
    json.dump(font_dict, f)

# Print a sample character to verify format
print("Example 'A' character representation:")
if 'A' in font_dict:
    for row in font_dict['A']:
        print(row)

print("\nFont dictionary has been saved to 'font_gitfiti.json'")
print(f"Total characters converted: {len(font_dict)}")
