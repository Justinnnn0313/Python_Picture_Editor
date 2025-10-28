# PyImageStudio

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/yourusername/pyimagestudio)
[![Maintenance](https://img.shields.io/maintenance/yes/2025.svg)](https://github.com/yourusername/pyimagestudio)
[![Code style: PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A professional-grade command-line image editing application built with Python, featuring advanced image processing capabilities and intuitive selection tools.

## Overview

PyImageStudio is a feature-rich image manipulation tool designed for developers and image processing enthusiasts. It provides essential editing functions through an interactive command-line interface, making it ideal for batch processing, automation scripts, and educational purposes.

## ✨ Key Features

### Image Processing
- **Brightness Adjustment** - Fine-tune image luminosity with values ranging from -255 to +255
- **Contrast Enhancement** - Modify image contrast using advanced mathematical formulas (-255 to +255)
- **Grayscale Conversion** - Convert RGB images to grayscale using standard luminance coefficients (0.3R + 0.59G + 0.11B)
- **Gaussian Blur** - Apply professional-grade blur effects using 3×3 convolution kernels
- **Edge Detection** - Identify and highlight image boundaries with Laplacian operators
- **Emboss Effect** - Create stylized 3D embossed visuals for artistic effects

### Advanced Selection Tools
- **Rectangle Select** - Define rectangular regions with precise coordinate input
- **Magic Wand Select** - Color-based intelligent selection using Delta-E color distance algorithm

### File Management
- **Multi-Format Support** - Works with PNG, JPG, and other common image formats
- **Smart Image Loading** - Automatic alpha channel removal and format normalization
- **High-Quality Export** - Save processed images with full quality preservation
- **Mask-Based Editing** - Apply effects selectively to designated regions

## 📋 Requirements

- Python 3.6 or higher
- NumPy >= 1.18
- Matplotlib >= 3.0

## 🚀 Installation

### Clone Repository
```bash
git clone https://github.com/yourusername/pyimagestudio.git
cd pyimagestudio
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy matplotlib
```

## 💻 Usage

### Quick Start
```bash
python image_editor.py
```

### Interactive Workflow

1. **Load Image** - Start by loading your source image file
2. **Make Selections** - Use rectangle or magic wand tools to select regions
3. **Apply Effects** - Choose from various editing operations
4. **Preview Changes** - View real-time results immediately
5. **Export Results** - Save your edited image with a new filename

### Command Reference

| Command | Description |
|---------|-------------|
| `e` | Exit application |
| `l` | Load image file |
| `s` | Save current image |
| `1` | Adjust brightness |
| `2` | Adjust contrast |
| `3` | Apply grayscale |
| `4` | Apply blur effect |
| `5` | Perform edge detection |
| `6` | Apply emboss effect |
| `7` | Rectangle selection |
| `8` | Magic wand selection |

## 🔧 API Reference

### Core Functions

**Image I/O**
- `load_image(filename)` - Load and normalize image file
- `save_image(filename, image)` - Export processed image

**Brightness & Contrast**
- `change_brightness(image, value)` - Adjust brightness (-255 to +255)
- `change_contrast(image, value)` - Modify contrast using contrast stretching formula

**Color Processing**
- `grayscale(image)` - Convert RGB to grayscale

**Filtering & Effects**
- `blur_effect(image)` - Apply Gaussian blur (3×3 kernel)
- `edge_detection(image)` - Detect edges using Laplacian kernel
- `embossed(image)` - Create emboss effect

**Selection Tools**
- `rectangle_select(image, x, y)` - Generate rectangular selection mask
- `magic_wand_select(image, starting_pixel, thres)` - Color-based selection using BFS

**Utilities**
- `compute_edge(mask)` - Calculate mask boundary
- `display_image(image, mask)` - Render image with selection overlay

## 🏗️ Technical Architecture

### Implementation Details
- **Array Processing**: NumPy-based pixel-level operations for optimal performance
- **Convolution Kernels**: 3×3 matrix operations for spatial filtering
- **Selection Algorithm**: Breadth-first search (BFS) for flood-fill operations
- **Color Distance**: Delta-E (CIE 76) metric for perceptually accurate color matching
- **Mask System**: Binary masks enable non-destructive region-specific editing

### Algorithm Highlights
```
Blur Kernel:        Edge Detection:     Emboss Kernel:
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ 0.0625 0.125  │   │  -1   -1   -1 │   │  -1   -1    0 │
│  0.125 0.25   │   │  -1    8   -1 │   │  -1    0    1 │
│ 0.0625 0.125  │   │  -1   -1   -1 │   │   0    1    1 │
└───────────────┘   └───────────────┘   └───────────────┘
```

## 📝 Example Usage

### Scenario: Edit and Export
```
1. Load image → my_photo.jpg
2. Apply rectangle select → (50, 50) to (200, 200)
3. Apply grayscale effect
4. Save as → my_photo_edited.jpg
```

### Scenario: Batch Processing
Combine with shell scripts for automated image processing:
```bash
for image in *.jpg; do
  python image_editor.py --input "$image" --effect grayscale --output "gray_$image"
done
```

## ⚠️ Important Notes

- **Spyder IDE**: Configure Graphics Backend to "inline" via Tools → Preferences → IPython console → Graphics → Graphics Backend
- **PNG Handling**: Alpha channel is automatically removed during loading
- **Format Normalization**: Float-type images (0.0-1.0) are converted to integer format (0-255)
- **Memory**: Large images may require significant memory for processing operations

## 📈 Performance Considerations

- Blur and edge detection operations iterate through pixels sequentially
- For very large images (>4000×4000), consider using image downsampling first
- Magic wand with strict thresholds may process large regions

## 🔍 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Please load an image first" | Use option `l` to load an image before editing |
| No visualization | Ensure Matplotlib backend is configured correctly |
| Slow performance | Try with smaller images or reduce image resolution |
| Invalid coordinates | Ensure coordinates are within image bounds |

## 📜 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

**Guidelines**:
- Fork the repository
- Create a feature branch (`git checkout -b feature/improvement`)
- Commit changes (`git commit -am 'Add improvement'`)
- Push to branch (`git push origin feature/improvement`)
- Submit Pull Request

## 📧 Contact & Support

For questions, bug reports, or feature suggestions, please open an issue on GitHub.

## 🎓 Educational Use

This project is perfect for learning image processing fundamentals, including:
- Convolution operations
- Color space transformations
- Flood-fill algorithms
- Mask-based image manipulation

---

**Status**: ✅ Active Development | **Last Updated**: 2025 | **Contributors**: Welcome
