#!/usr/bin/env python3
"""
Solve the Lemur XOR challenge by XORing two images encrypted with the same key.
When two images are XORed with the same key, XORing them together cancels out the key.
"""

from PIL import Image
import numpy as np

def xor_images(image1_path, image2_path, output_path):
    """XOR the RGB bytes of two images and save the result."""
    # Load the images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    
    # Convert to numpy arrays for easy manipulation
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    # Ensure images have the same dimensions
    if arr1.shape != arr2.shape:
        print(f"Warning: Image dimensions don't match!")
        print(f"Image 1: {arr1.shape}, Image 2: {arr2.shape}")
        # Crop to the smaller dimensions
        min_height = min(arr1.shape[0], arr2.shape[0])
        min_width = min(arr1.shape[1], arr2.shape[1])
        arr1 = arr1[:min_height, :min_width]
        arr2 = arr2[:min_height, :min_width]
    
    # XOR the RGB bytes (element-wise XOR)
    xor_result = np.bitwise_xor(arr1, arr2)
    
    # Convert back to image
    result_img = Image.fromarray(xor_result.astype('uint8'))
    
    # Save the result
    result_img.save(output_path)
    print(f"XOR result saved to: {output_path}")
    
    return result_img

if __name__ == "__main__":
    # XOR the two encrypted images
    result = xor_images(
        "flag_7ae18c704272532658c10b5faad06d74.png",
        "lemur_ed66878c338e662d3473f0d98eedbd0d.png",
        "xor_result.png"
    )
    
    print("\nThe XOR of the two images reveals the combined visual information!")
    print("Check xor_result.png to see the flag and lemur images combined.")
