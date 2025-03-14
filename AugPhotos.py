import os
import cv2
import matplotlib.pyplot as plt

# Specify the folder containing images
image_folder = 'G:\CAPSTONE\AugmentPhotoTest'

# Get all image file paths in the folder
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png'))]

# Loop through each image file
for i, image_file in enumerate(image_files):
    # Read the image
    image = cv2.imread(image_file)
    
    # Convert the image to RGB for matplotlib
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Apply augmentations
    aug_img_V_Flip = cv2.flip(image, 0)  # Vertical flipping
    aug_img_H_Flip = cv2.flip(image, 1)  # Horizontal flipping
    aug_img_HV_Flip = cv2.flip(image, -1)  # Horizontal and vertical flipping
    
    # Create a grid to display the images
    fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, figsize=(25, 25))
    
    # Display the original and augmented images
    ax[0][0].set_title("Original Image", fontsize=25)
    ax[0][0].imshow(image)
    
    ax[0][1].set_title("Horizontal and Vertical Flip", fontsize=25)
    ax[0][1].imshow(aug_img_HV_Flip)
    
    ax[1][0].set_title("Horizontal Flip", fontsize=25)
    ax[1][0].imshow(aug_img_H_Flip)
    
    ax[1][1].set_title("Vertical Flip", fontsize=25)
    ax[1][1].imshow(aug_img_V_Flip)
    
    # Hide axes for all subplots
    for row in ax:
        for col in row:
            col.axis('off')
    
    # Display the grid
    plt.show()
