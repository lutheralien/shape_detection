import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_image(image_path):
    """
    Load an image from the specified path.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        numpy.ndarray: Loaded image in BGR format
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Check if image was loaded successfully
    if image is None:
        raise ValueError(f"Could not load image from {image_path}")
        
    return image

def preprocess_image(image):
    """
    Preprocess the image for better edge detection.
    
    Args:
        image (numpy.ndarray): Input image in BGR format
        
    Returns:
        tuple: (RGB image for display, grayscale image, blurred grayscale image)
    """
    # Create a copy to avoid modifying the original
    processed = image.copy()
    
    # Convert to RGB for display purposes
    image_rgb = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
    
    # Convert to grayscale for edge detection
    gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Return all three images: RGB, grayscale, and blurred
    return image_rgb, gray, blurred

def detect_edges(image, low_threshold=50, high_threshold=150):
    """
    Detect edges in the image using Canny edge detector.
    
    Args:
        image (numpy.ndarray): Grayscale image
        low_threshold (int): Lower threshold for the Canny edge detector
        high_threshold (int): Higher threshold for the Canny edge detector
        
    Returns:
        numpy.ndarray: Binary image with detected edges
    """
    # Apply Canny edge detection
    edges = cv2.Canny(image, low_threshold, high_threshold)
    
    return edges

def display_results(original, grayscale, blurred, edges, output_folder="results"):
    """
    Display the original, grayscale, blurred, and edge-detected images and save screenshots.
    
    Args:
        original (numpy.ndarray): Original RGB image
        grayscale (numpy.ndarray): Grayscale image
        blurred (numpy.ndarray): Blurred grayscale image
        edges (numpy.ndarray): Edge-detected binary image
        output_folder (str): Folder to save the output images
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Create a figure with 4 subplots
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    
    # Display original image
    axs[0].imshow(original)
    axs[0].set_title('Original Image')
    axs[0].axis('off')
    
    # Display grayscale image
    axs[1].imshow(grayscale, cmap='gray')
    axs[1].set_title('Grayscale Image')
    axs[1].axis('off')
    
    # Display blurred image
    axs[2].imshow(blurred, cmap='gray')
    axs[2].set_title('Blurred Image')
    axs[2].axis('off')
    
    # Display edge-detected image
    axs[3].imshow(edges, cmap='gray')
    axs[3].set_title('Edge Detection')
    axs[3].axis('off')
    
    # Adjust layout and save figure
    plt.tight_layout()
    plt.savefig(f'{output_folder}/edge_detection_results.png')
    
    # Save individual images
    cv2.imwrite(f'{output_folder}/original.jpg', cv2.cvtColor(original, cv2.COLOR_RGB2BGR))
    cv2.imwrite(f'{output_folder}/grayscale.jpg', grayscale)
    cv2.imwrite(f'{output_folder}/blurred.jpg', blurred)
    cv2.imwrite(f'{output_folder}/edge_detected.jpg', edges)
    
    print(f"Screenshots saved in the '{output_folder}' folder")
    
    # Show the plot
    plt.show()

def create_test_image(output_path="test_shapes.jpg", width=800, height=600):
    """
    Create a test image with basic shapes of different colors.
    
    Args:
        output_path (str): Path to save the test image
        width (int): Width of the image
        height (int): Height of the image
    
    Returns:
        numpy.ndarray: The created test image
    """
    # Create a white background
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    # Draw a red circle
    cv2.circle(image, (200, 200), 100, (0, 0, 255), -1)
    
    # Draw a green square
    cv2.rectangle(image, (400, 100), (600, 300), (0, 255, 0), -1)
    
    # Draw a blue triangle
    triangle_pts = np.array([[700, 300], [600, 500], [800, 500]], dtype=np.int32)
    cv2.fillPoly(image, [triangle_pts], (255, 0, 0))
    
    # Save the image
    cv2.imwrite(output_path, image)
    print(f"Test image created and saved to {output_path}")
    
    return image

def main():
    """
    Main function to execute the image processing pipeline.
    """
    # Create an output folder for results
    output_folder = "results"
    os.makedirs(output_folder, exist_ok=True)
    
    # Ask user if they want to create a test image
    use_test_image = input("Do you want to create a test image with basic shapes? (y/n): ").lower() == 'y'
    
    if use_test_image:
        # Create and use a test image
        test_image_path = f"{output_folder}/test_shapes.jpg"
        original_image = create_test_image(test_image_path)
    else:
        # Use user-provided image
        image_path = input("Enter the path to your image: ")
        
        try:
            # Load the image
            print("Loading image...")
            original_image = load_image(image_path)
        except Exception as e:
            print(f"Error loading image: {e}")
            print("Creating a test image instead.")
            test_image_path = f"{output_folder}/test_shapes.jpg"
            original_image = create_test_image(test_image_path)
    
    # Preprocess the image
    print("Preprocessing image...")
    rgb_image, gray_image, blurred_image = preprocess_image(original_image)
    
    # Let user adjust edge detection parameters (optional)
    adjust_params = input("Do you want to adjust edge detection parameters? (y/n): ").lower() == 'y'
    
    if adjust_params:
        try:
            low_threshold = int(input("Enter low threshold (10-100 recommended): "))
            high_threshold = int(input("Enter high threshold (100-200 recommended): "))
        except ValueError:
            print("Invalid input. Using default values.")
            low_threshold = 50
            high_threshold = 150
    else:
        # Default values
        low_threshold = 50
        high_threshold = 150
    
    # Detect edges
    print("Detecting edges...")
    edges = detect_edges(blurred_image, low_threshold, high_threshold)
    
    # Display and save results
    print("Displaying and saving results...")
    display_results(rgb_image, gray_image, blurred_image, edges, output_folder)
    
    print("Processing completed!")
    print(f"All output files are saved in the '{output_folder}' directory")

if __name__ == "__main__":
    main()