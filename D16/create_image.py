import numpy as np
from PIL import Image
from answer import p

a = [*map(lambda c : (int(c.real), int(c.imag)), p)]
def maze_to_image(maze_text, cell_size=10):
    """
    Convert a text-based maze to an RGB image.
    
    Parameters:
    - maze_text: String representation of the maze
    - cell_size: Size of each cell in pixels (default 10)
    
    Returns:
    - PIL Image object
    """
    # Remove any leading/trailing whitespace and split into rows
    maze_rows = maze_text.strip().split('\n')
    
    # Create a numpy array for the image
    height = len(maze_rows)
    width = len(maze_rows[0])
    
    # Create an RGB image
    image = np.zeros((height * cell_size, width * cell_size, 3), dtype=np.uint8)
    
    # Color mapping
    colors = {
        '#': [0, 0, 0],       # Black walls
        '.': [255, 255, 255], # White paths
        'S': [0, 255, 0],     # Green start
        'E': [255, 0, 0],
        '*' : [0, 255, 0]
    }
    
    # Fill the image
    for y, row in enumerate(maze_rows):
        for x, cell in enumerate(row):
            # Get the color for this cell
            if (y, x) in a:
                if cell == "#":
                    color = [255,128,0]
                else:
                    cell = '*'
                    color = colors.get(cell, [128, 128, 128])  # Default to gray if unknown
            else:
                color = colors.get(cell, [128, 128, 128])
            
            # Fill the cell with the corresponding color
            y_start = y * cell_size
            x_start = x * cell_size
            image[y_start:y_start+cell_size, 
                  x_start:x_start+cell_size] = color
    
    # Convert to PIL Image
    return Image.fromarray(image)

# Example usage
maze_text = open('in.txt').read()
# Create and save the image
maze_image = maze_to_image(maze_text, cell_size=20)
maze_image.save('maze_visualization.png')

# Optional: display the image (requires matplotlib)
# import matplotlib.pyplot as plt
# plt.imshow(maze_image)
# plt.axis('off')
# plt.show()