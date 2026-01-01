import random
import re

def load_existing_colours(filename):
    existing_colours = set()
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # both # and x work as hex prefix 
                hex_matches = re.findall(r'[#x]([0-9a-fA-F]{6})', line)
                for match in hex_matches:
                    # Converting to # prefix
                    existing_colours.add(f"#{match}")
                
                # Extract RGB colours, both , and ; valid separators
                rgb_matches = re.findall(r'(\d+)[,;](\d+)[,;](\d+)', line)
                for r, g, b in rgb_matches:
                    # RGB to hex
                    hex_colour = "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
                    existing_colours.add(hex_colour)
    except FileNotFoundError:
        print(f"No input file named '{filename}' found. Generating colours without input.")
    
    return existing_colours

def hex_to_rgb(hex_colour):
    hex_colour = hex_colour.lstrip('#')
    return tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))

#Check that RGB colours are valid then convert to hex
def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return f"#{r:02x}{g:02x}{b:02x}"

def main():
    # Load input
    print("Input must be named 'input.txt'. Input must only have one colour per line. Can read HEX with x or # prefix, can read RGB with ; or , separator.")
    use_input = input("Load existing colours from 'input.txt'? (y/n): ").lower().strip()
    
    existing_colours = set()
    if use_input in ['y', 'yes', 'ok']:
        existing_colours = load_existing_colours('input.txt')
        print(f"Loaded {len(existing_colours)} existing colours from input.txt")

    colours = []
    
    # Avoid duplicates
    while len(colours) < 20000:
        # Random hex colour
        colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        
        # Check if duplicate and add if not
        if colour not in existing_colours and colour not in colours:
            colours.append(colour)
            print("Generated: " + colour)
    
    with open("colours.txt", "w") as file:
        for colour in colours:
            file.write(f"{colour}\n")

    with open("coloursrgb.txt", "w") as file:
        for colour in colours:
            # Converting to RGB
            hex_colour = colour[1:]
            r = int(hex_colour[0:2], 16)
            g = int(hex_colour[2:4], 16)
            b = int(hex_colour[4:6], 16)
            file.write(f"{r};{g};{b}\n")
    
    print(f"Successfully generated {len(colours)} unique colours.")
    print(f"{len(colours)} HEX colours saved to colours.txt, {len(colours)} RGB colours saved to coloursrgb.txt")

if __name__ == "__main__":
    main()