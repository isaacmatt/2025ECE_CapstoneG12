from pathlib import Path
import csv
p = Path('.')

imgList = list(p.glob('**/*.jpeg')) + list(p.glob('**/*.jpg')) + list(p.glob('**/*.png')) # + and copy list portion to include new filetype if needed.

# Function that will extract GPS coordinates from file
def extract_gps_from_file(filename):
    try:
        # *Note modify this based on your actual filename format*
        # Check the filename format: IMG_123456_37.7749_-122.4194
        parts = filename.split('_')
        if len(parts) >= 3:
            lat = float(parts[-2])  # Second to last part
            lon = float(parts[-1])  # Last part
            return lat, lon
    except ValueError:
        print(f"Error parsing GPS data from filename: {filename}")

    return None
# Define CSV file to store extracted GPS coordinates
csv_filename = "G12_Gps_Coordinates.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Filename", "Latitude", "Longitude"])  # Header row

    for file in imgList: #iterate through all images added to the image list variable.
        filename = file.stem #Object is then accessed to get the filename without its extension.
        print(filename[3:]) #Modify this to include portion of filename that contains the GPS coordinates in the title.
    
    gps_coords = extract_gps_from_file(filename[3:])  # Matched to the filename slicing

    if gps_coords:
        writer.writerow([filename, gps_coords[0], gps_coords[1]])  # Writes extracted data to the CSV

print(f"GPS Coordinates Saved In: {csv_filename}")