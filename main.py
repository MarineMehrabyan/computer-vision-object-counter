import cv2
import numpy as np

def count_objects(image_path):
    '''
    Function to count the number of coins in an image using computer vision techniques.
    Parameters:
        image_path (str): Path to the input image file.
    Returns:
        None
    '''
    # Use the "with" statement to open and close the image file
    with open(image_path, 'rb') as f:
        image_bytes = bytearray(f.read())

    # Load the image from the byte buffer
    image = cv2.imdecode(np.asarray(image_bytes, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    canny = cv2.Canny(gray, 20, 40)

    # Apply dilation
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(canny, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Display the result and print the number of coins
    cv2.imshow('Result', image)
    print('Objects in the image: ', len(contours))

    # Wait for user input and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function for multiple images
count_objects('image1.jpg')
count_objects('image3.png')
count_objects('image4.png')
count_objects('image2.jpg')

