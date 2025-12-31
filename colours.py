import random

print("Generating...")
def main():
    # Generate 1000 unique hex colours using a different method
    colours = []
    
    # Avoid duplicates
    while len(colours) < 100000:
        # Random hex colour
        colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if colour not in colours:
            colours.append(colour)
            print("Generated: " + colour)
    
    with open("colours.txt", "w") as file:
        for colour in colours:
            file.write(f"{colour}\n")
    
    print(f"Successfully generated {len(colours)} unique colours and saved them to colours.txt")

if __name__ == "__main__":
    main()