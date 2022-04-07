from os import sys
from PIL import Image

# PATTERN ROWS MUST HAVE THE SAME LENGTH!!!
pattern = [
    [0, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1]
]

# Get the image path
if (len(sys.argv[1:]) > 0):
    image_path = sys.argv[1]
else:
    image_path = input("Image path : ")

# Open the image
with Image.open(image_path) as img:
    img_width, img_height = img.size
    pattern_width, pattern_height = len(pattern[0]), len(pattern)
    pixel_map = img.load() # Extract the pixel map

    cpt = 0

    # Loop through the pixels
    for y in range(img_height - pattern_height + 1):
        for x in range(img_width - pattern_width + 1):
            colors = [[], None]
            found = True

            # Loop through the chunk
            for j in range(pattern_height):
                for i in range(pattern_width):
                    cur_color = pixel_map[i + x, j + y]
                    cur_pattern = pattern[j][i]

                    if (cur_pattern == 0):
                        if (colors[0]):
                            colors[0].append(cur_color)
                        else:
                            colors[0] = [cur_color]
                    elif (cur_pattern == 1):
                        # TODO: Adapt later, in order to support more than 1
                        if (cur_color in colors[0]): # If a foreground color is also found AMONG the background colors
                            found = False
                            break
                        elif (colors[1] and colors[1] != cur_color): # If we find a foreground pixel that's not identical to the others
                            found = False
                            break
                        else: # If it matches the pattern
                            colors[1] = cur_color
                    else:
                        found = False
                        break
                if (not found):
                    break
            
            if (found):
                cpt += 1
    
    print(cpt, "occurrences" if cpt > 1 else "occurrence", "du motif", "trouvées." if cpt > 1 else "trouvée.")