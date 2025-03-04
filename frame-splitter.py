from PIL import Image
import os
import sys

def extract_frames(input_path):
    """Extract frames from PNG/GIF file"""
    img = Image.open(input_path)
    frames = []
    try:
        while True:
            # Copy the current frame
            frames.append(img.copy())
            img.seek(img.tell() + 1)
    except EOFError:
        pass
    return frames

def create_atlas(frames, output_path):
    """Create horizontal atlas from frames"""
    if not frames:
        print("No frames found in the input file")
        return False
    
    frame_width = frames[0].width
    frame_height = frames[0].height
    
    # Calculate atlas dimensions
    num_frames = len(frames)
    atlas_width = num_frames * frame_width
    atlas_height = frame_height
    
    # Create new image for atlas
    atlas = Image.new('RGBA', (atlas_width, atlas_height), (0, 0, 0, 0))
    
    # Place frames horizontally
    for i, frame in enumerate(frames):
        atlas.paste(frame, (i * frame_width, 0))
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save atlas
    atlas.save(output_path)
    print(f"Created atlas with {num_frames} frames")
    print(f"Atlas dimensions: {atlas_width}x{atlas_height} pixels")
    print(f"Saved to: {output_path}")
    return True

def process_file(input_path):
    """Process a single file"""
    try:
        # Generate output path by adding _atlas to the original filename
        file_name = os.path.splitext(input_path)[0]
        output_path = f"{file_name}_atlas.png"
        
        frames = extract_frames(input_path)
        if create_atlas(frames, output_path):
            return 1
        return 0
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return 0

def process_directory(directory):
    """Process all PNG files in a directory"""
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} not found")
        return
    
    # Create output directory if needed
    output_dir = os.path.join(directory, "atlas_output")
    os.makedirs(output_dir, exist_ok=True)
    
    successful = 0
    total = 0
    
    # Process all PNG files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                total += 1
                input_path = os.path.join(root, file)
                
                # Create relative output path
                rel_path = os.path.relpath(root, directory)
                output_subdir = os.path.join(output_dir, rel_path)
                os.makedirs(output_subdir, exist_ok=True)
                
                file_name = os.path.splitext(file)[0]
                output_path = os.path.join(output_subdir, f"{file_name}_atlas.png")
                
                try:
                    frames = extract_frames(input_path)
                    if create_atlas(frames, output_path):
                        successful += 1
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed {successful} out of {total} PNG files")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frame-splitter.py <input_file.png/.gif or directory>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    # Check if input exists
    if not os.path.exists(input_path):
        print(f"Error: Path {input_path} not found")
        sys.exit(1)
    
    # Process either a single file or a directory
    if os.path.isfile(input_path):
        process_file(input_path)
    else:
        process_directory(input_path) 