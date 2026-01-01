import random

print("Generating...")
def main():
    # Generate 1000 unique hex colours using a different method
    colours = []
    
    # Avoid duplicates
    while len(colours) < 20000:
        # Random hex colour
        colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if colour not in colours:
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
    print(f"HEX colours saved to colours.txt, RGB saved to coloursrgb.txt")
if __name__ == "__main__":
    main()