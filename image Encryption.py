import cv2
import numpy as np
import argparse

def encrypt_image(image_path, output_path, key):
    image = cv2.imread()
    if image is None:
        print("Error: Could not read the image.")
        return
    
    encrypted_image = (image + key) % 256  # Simple pixel manipulation
    cv2.imwrite(output_path, encrypted_image)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(encrypted_path, output_path, key):
    encrypted_image = cv2.imread(encrypted_path)
    if encrypted_image is None:
        print("Error: Could not read the encrypted image.")
        return
    
    decrypted_image = (encrypted_image - key) % 256  # Reverse operation
    cv2.imwrite(output_path, decrypted_image)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument("output", help="Output file path")
    parser.add_argument("key", type=int, help="Encryption key (integer value)")
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        encrypt_image(args.image, args.output, args.key)
    else:
        decrypt_image(args.image, args.output, args.key)
