____Count Objects in an Image____
This is a Python script that counts the number of objects in an image using computer vision techniques.

____Dependencies____
1. OpenCV (cv2)
2. NumPy

____Usage____
Install the required dependencies using pip:
    _pip install opencv-python numpy_

Save your input images in a folder and set the image path in the count_objects() function.

Run the script
    _python3 count_objects.py_

The script will display the result and print the number of objects in each image.


____Algorithm____

Read the input image using the cv2.imread() function.

Convert the image to grayscale using the cv2.cvtColor() function.

Apply Canny edge detection to the grayscale image using the cv2.Canny() function.

Apply dilation to the Canny image using a kernel of size 3x3 and two iterations, using the cv2.dilate() function.

Find the contours in the dilated image using the cv2.findContours() function.

Draw the contours on the original image using the cv2.drawContours() function.

Display the resulting image using the cv2.imshow() function.

Print the number of objects found in the image using the len() function on the contours list.

Wait for user input and close the window using the cv2.waitKey() and cv2.destroyAllWindows() functions.


_The algorithm uses the fact that objects have distinct edges to detect and count them in the image. The Canny edge detection algorithm is used to detect the edges, and the dilation operation is used to enhance the edges and connect any disconnected edges. The contours of the connected edges are then found and used to count the number of objects in the image._
