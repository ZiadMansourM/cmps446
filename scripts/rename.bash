#!/bin/bash

# Change the directory path to your image directory
image_dir="/Users/ziadh/Desktop/playgroud/image-processing/cmps446/dev-docs/static/assets/datasets/potato/Potato___Late_blight"

# Counter for renaming
count=0

# Iterate over the files in the directory
for file in "$image_dir"/*; do
    # Check if the item is a file
    if [ -f "$file" ]; then
        # Format the new filename with leading zeros
        new_filename=$(printf "%04d.JPG" "$count")
        
        # Rename the file
        mv "$file" "$image_dir/$new_filename"
        
        # Increment the count
        count=$((count + 1))
    fi
done