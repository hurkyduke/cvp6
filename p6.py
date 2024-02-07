import cv2
import matplotlib.pyplot as plt

# Load an image in RGB format
image = cv2.imread('/Users/venkateshsanwal/Desktop/ml/computer_vision/Pi7_Tool_100-VENKETESHPHOTO-hadbomb_com.jpg', cv2.IMREAD_COLOR)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Convert RGB to Grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and converted images
    plt.figure(figsize=(10, 5))

    plt.subplot(121)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image (RGB)')

    plt.subplot(122)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Grayscale Image')

    plt.show()
