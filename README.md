# Image Editor

A comprehensive command-line image editing tool built with Python, offering a wide range of image processing capabilities.

## Features

### Image Editing
- **Brightness Adjustment** - Increase or decrease image brightness (-255 to +255)
- **Contrast Adjustment** - Modify image contrast (-255 to +255)
- **Grayscale Conversion** - Convert color images to grayscale
- **Blur Effect** - Apply Gaussian blur filter
- **Edge Detection** - Detect and highlight image edges
- **Emboss Effect** - Create a 3D embossed visual effect

### Selection Tools
- **Rectangle Select** - Select rectangular regions by coordinates
- **Magic Wand Select** - Intelligent selection tool based on color similarity

### File Operations
- **Load Images** - Support for common formats (PNG, JPG, etc.)
- **Save Images** - Export edited images to new files
- **Mask System** - Apply effects only to selected regions

## Requirements

- Python 3.6+
- NumPy
- Matplotlib

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/image-editor.git
cd image-editor
```

2. Install dependencies
```bash
pip install numpy matplotlib
```

## Usage

Run the program:
```bash
python image_editor.py
```

### Interactive Menu

The program launches an interactive command-line menu:

1. **First Launch** - Load an image file
2. **Select Operation** - Choose an operation from the menu
3. **Input Parameters** - Follow prompts to enter relevant parameters
4. **Real-time Preview** - View edited effects immediately
5. **Save Results** - Save the final result to a file

### Menu Options

| Option | Function |
|--------|----------|
| e | Exit program |
| l | Load new image |
| s | Save current image |
| 1 | Adjust brightness |
| 2 | Adjust contrast |
| 3 | Convert to grayscale |
| 4 | Apply blur |
| 5 | Edge detection |
| 6 | Emboss effect |
| 7 | Rectangle select |
| 8 | Magic wand select |

## Core Functions

- `load_image(filename)` - Load image file
- `save_image(filename, image)` - Save image file
- `change_brightness(image, value)` - Adjust brightness
- `change_contrast(image, value)` - Adjust contrast
- `grayscale(image)` - Convert to grayscale
- `blur_effect(image)` - Apply blur effect
- `edge_detection(image)` - Detect edges
- `embossed(image)` - Apply emboss effect
- `rectangle_select(image, x, y)` - Rectangle selection
- `magic_wand_select(image, starting_pixel, thres)` - Magic wand selection

## Technical Details

- Efficient pixel operations using NumPy arrays
- 3×3 convolution kernels for filter effects
- BFS-based algorithm for magic wand selection
- Mask system for region-specific editing

## Example Workflow
```
Load Image → Select Rectangle Region → Apply Grayscale → Save Image
```

## Notes

- If using Spyder IDE, configure "Tools → Preferences → IPython console → Graphics → Graphics Backend" to "inline"
- PNG images automatically have their alpha channel removed
- Float-type images are automatically converted to integer type (0-255 range)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

## Contact

For questions or suggestions, please reach out through GitHub Issues.
