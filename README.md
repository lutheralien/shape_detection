# Real-Time Shape and Color Detection

## Project Overview
This project implements a system for detecting different shapes (circles, squares, triangles) and their respective colors in images. The current implementation focuses on Phase 1: Basic Image Processing, which includes image loading, preprocessing, and edge detection.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
  - [Using Conda (Recommended)](#using-conda-recommended)
  - [Using pip](#using-pip)
- [Usage](#usage)
  - [Running the Program](#running-the-program)
  - [Program Options](#program-options)
- [Features](#features)
- [Code Structure](#code-structure)
- [Output Examples](#output-examples)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

## Requirements
- Python 3.8 or higher
- OpenCV (4.5.0 or higher)
- NumPy (1.20.0 or higher)
- Matplotlib (3.4.0 or higher)

## Installation

### Using Conda (Recommended)

#### Creating a New Environment
```bash
# Create a new conda environment named 'shape_detection'
conda create -n shape_detection python=3.10

# Activate the environment
conda activate shape_detection

# Install required packages
conda install -c conda-forge opencv numpy matplotlib
```

#### Installing from environment.yml
```bash
# Create the environment from the provided environment.yml file
conda env create -f environment.yml

# Activate the environment
conda activate shape_detection
```

### Using pip
```bash
# Option 1: Install in your current Python environment
pip install opencv-python numpy matplotlib

# Option 2: Create a virtual environment first (recommended)
python -m venv shape_detection_env
source shape_detection_env/bin/activate  # On Windows: shape_detection_env\Scripts\activate
pip install opencv-python numpy matplotlib

# Option 3: Install from the provided requirements.txt
pip install -r requirements.txt
```

### Verifying Installation
To verify that all dependencies are installed correctly:
```bash
python -c "import cv2, numpy, matplotlib; print(f'OpenCV: {cv2.__version__}, NumPy: {numpy.__version__}, Matplotlib: {matplotlib.__version__}')"
```

## Usage

### Running the Program
1. Ensure your environment is activated:
   ```bash
   conda activate shape_detection  # If using conda
   # OR
   source shape_detection_env/bin/activate  # If using venv on Unix/MacOS
   # OR
   shape_detection_env\Scripts\activate  # If using venv on Windows
   ```

2. Run the script:
   ```bash
   python shape_detection.py
   ```

### Program Options
When you run the program, you will be prompted with several options:

1. **Create test image or use your own?**
   - Enter `y` to create a test image with predefined shapes
   - Enter `n` to use your own image (you'll be asked for the path)

2. **Adjust edge detection parameters?**
   - Enter `y` to manually set the Canny edge detection thresholds
   - Enter `n` to use default values (low threshold = 50, high threshold = 150)

## Features
- Image loading and preprocessing
- Noise reduction using Gaussian blur
- Edge detection using Canny algorithm
- Visualization of original, preprocessed, and edge-detected images
- Option to create test images with basic shapes
- Interactive adjustment of edge detection parameters
- Automatic saving of results

## Code Structure
The code is organized into the following functions:

1. `load_image()`: Loads an image from a specified path
2. `preprocess_image()`: Converts to grayscale and applies blur
3. `detect_edges()`: Applies Canny edge detection
4. `display_results()`: Visualizes and saves the images
5. `create_test_image()`: Creates an image with basic shapes
6. `main()`: Orchestrates the entire process

## Output Examples
The program generates the following outputs in the `results` folder:

1. **original.jpg**: The original input image
2. **preprocessed.jpg**: The grayscale, blurred image
3. **edge_detected.jpg**: The final edge-detected image
4. **edge_detection_results.png**: A combined view of all three images

Expected visual results:
- For the test image, you should see clear edge outlines of a circle, square, and triangle
- For custom images, the quality of edge detection depends on the image clarity and the chosen parameters

## Troubleshooting

### Common Issues

1. **"ImportError: No module named 'cv2'"**
   - OpenCV is not installed correctly
   - Solution: Run `conda install -c conda-forge opencv` or `pip install opencv-python`

2. **"Error loading image"**
   - The specified image path is incorrect or the file is corrupted
   - Solution: Check the file path and ensure the image is valid

3. **Poor edge detection results**
   - Try adjusting the Canny thresholds:
     - Lower the values to detect more edges (may include noise)
     - Increase the values to detect fewer edges (may miss important features)

4. **Matplotlib display issues on macOS**
   - If using macOS and encountering GUI errors, try adding this before importing matplotlib:
     ```python
     import matplotlib
     matplotlib.use('TkAgg')
     ```

### Getting Help
For additional help or to report issues, please open an issue on the GitHub repository.

## Future Enhancements
Planned features for Phase 2 and beyond:

1. Real-time video processing
2. Shape classification (detecting specific shapes)
3. Color detection and classification
4. Object tracking
5. Improved edge detection algorithms

---

## Project Information
- **Author**: [Your Name]
- **Version**: 1.0.0
- **License**: MIT
- **Last Updated**: March 16, 2025