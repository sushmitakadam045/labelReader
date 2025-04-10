import cv2
import numpy as np


def increase_contrast_clahe(image, alpha = 2.0, beta = 0):
    # Convert the image to grayscale
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image

def isImageBlurred(roi, threshold = 1000):
    laplacianVar = cv2.Laplacian(roi, cv2.CV_64F).var()
    if laplacianVar < 1000:
        return True
    return False


def detect_sticker_label(image):
    image = increase_contrast_clahe(image, 1.25, 0)
    if image is None:
        print("Error: Could not load image")
        return None

    # Convert to HSV color space for better color-based segmentation
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color range for the white sticker
    # White in HSV: high value (brightness), low saturation
    lower_white = np.array([0, 0, 200])  # Adjust these values if needed
    upper_white = np.array([180, 50, 255])

    # Create a mask for white regions
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Apply morphological operations to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.erode(mask, kernel, iterations=1)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours to find the sticker
    sticker_contour = None
    max_area = 0

    for contour in contours:
        # Approximate the contour to a polygon
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # Check if the contour is roughly rectangular and has significant area
        area = cv2.contourArea(contour)
        if len(approx) == 4 and area > 150000:  # Lowered area threshold #TODO fetch this area from the config file
            if area > max_area:
                max_area = area
                sticker_contour = approx

    if sticker_contour is not None:
        # Draw the detected sticker contour on the original image
        cv2.drawContours(image, [sticker_contour], -1, (0, 255, 0), 2)

        # Calculate bounding rectangle
        x, y, w, h = cv2.boundingRect(sticker_contour)
        roi = image[y:y + h, x:x + w] # selecting region of interest i.e. label area
        if(isImageBlurred(roi, threshold=1000)):
            return

        # Display area information
        print(f"Sticker detected at: x={x}, y={y}")
        print(f"Width: {w}, Height: {h}")
        print(f"Area: {w * h} pixels")

        # Show the result
        cv2.imshow("Detected Sticker", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return x, y, w, h
    return None, None, None, None


"""
video_path = "b.mp4"
cap = cv2.VideoCapture(video_path)
fc = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break # video ended
    if fc % 5 == 0:
       detect_sticker_label(frame)
    fc = fc + 1

cap.release()
cv2.destroyAllWindows()
# Provide the path to the image you want to test
image_path = "C:\\users\\sk6813\\Downloads\\imageC2.png"

"""