from PIL import Image

def convert_image(image_path, output_format):
  try:
    # Open the image using Pillow
    image = Image.open(image_path)
    # Convert the image to the desired format
    image.save(f"converted_image.{output_format}", output_format)
    print(f"Image converted to {output_format} format successfully!")
  except OSError:
    print(f"Error: Could not open image file {image_path}")

# Get user input for image path and desired output format
image_path = input("Enter the path to the image file: ")
output_format = input("Enter the desired output format (JPEG, PNG, BMP): ").upper()

# Check for valid output format
valid_formats = ["JPEG", "PNG", "BMP"]
if output_format not in valid_formats:
  print(f"Invalid output format. Please choose from {', '.join(valid_formats)}")
  exit()

convert_image(image_path, output_format)
