#!/usr/bin/env python3
"""
Image optimization script for portfolio website
Compresses images while maintaining quality
"""

from PIL import Image
import os

def optimize_image(input_path, output_path=None, max_width=1200, quality=85):
    """
    Optimize an image by resizing and compressing
    
    Args:
        input_path: Path to input image
        output_path: Path to save optimized image (defaults to input_path)
        max_width: Maximum width in pixels
        quality: JPEG quality (1-100)
    """
    if output_path is None:
        output_path = input_path
    
    try:
        # Open image
        img = Image.open(input_path)
        
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        
        # Resize if too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Get file size before
        size_before = os.path.getsize(input_path)
        
        # Save optimized image
        if output_path.lower().endswith('.png'):
            img.save(output_path, 'PNG', optimize=True)
        else:
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        # Get file size after
        size_after = os.path.getsize(output_path)
        reduction = ((size_before - size_after) / size_before) * 100
        
        print(f"✓ {os.path.basename(input_path)}: {size_before/1024:.1f}KB → {size_after/1024:.1f}KB ({reduction:.1f}% reduction)")
        
    except Exception as e:
        print(f"✗ Error optimizing {input_path}: {e}")

def main():
    assets_dir = "assets"
    
    # Images to optimize
    images = [
        "cv_image.jpg",
        "cv_image.png",
        "3D Position Estimation with Deep Learning.png",
        "Autonomous Delivery Robot.png",
        "Autonomous Logistics Robot.png",
        "Fashion MNIST.png",
        "Gesture-Controlled Quadruped Robot.png",
        "Gesture-based Intelligent Appliance Control.png",
        "Pipe Climbing Robot.png",
        "SwasthyaLogs AI - Medical Record System.png",
        "VLM Robotic Manipulation.png"
    ]
    
    print("Optimizing images...\n")
    
    for img_name in images:
        img_path = os.path.join(assets_dir, img_name)
        if os.path.exists(img_path):
            # Use higher quality for hero image
            quality = 90 if "cv_image" in img_name else 85
            optimize_image(img_path, quality=quality)
        else:
            print(f"⚠ {img_name} not found")
    
    print("\n✓ Optimization complete!")

if __name__ == "__main__":
    main()
