from PIL import Image
import imageio.v3 as iio

filenames = [
    r"C:\Users\shani\OneDrive\Desktop\mini practice projects\image1.png",
    r"C:\Users\shani\OneDrive\Desktop\mini practice projects\image2.jpeg",
]

# Step 1: Read images using PIL
pil_images = [Image.open(f) for f in filenames]

# Step 2: Resize all to the size of the first image
base_size = pil_images[0].size
pil_images = [img.resize(base_size) for img in pil_images]

# Step 3: Convert to numpy arrays for imageio
images = [iio.imread(f) for f in filenames]

# Overwrite with resized arrays
images = [iio.imread(f).astype('uint8') for f in filenames]

# Step 4: Save GIF using PIL (better)
pil_images[0].save(
    "output.gif",
    save_all=True,
    append_images=pil_images[1:],
    duration=500,
    loop=0
)

print("GIF created successfully!")
