# Ferrography — Image-Based Particle Analysis

A legacy Python/OpenCV prototype for inspecting ferrography images and extracting particle-like regions. It combines interactive threshold adjustment, contour-based detection, approximate size grouping, and simple summaries.

**Status:** Historical experimental implementation. The measurement accuracy and reproducibility have not been independently validated. The project is a candidate for a manual rewrite focused on numerical correctness and evaluation.

## Existing code

- `mainUI.py`: Tkinter desktop interface.
- `spalingIdentify.py`: HSV thresholding, contours, region annotations, and size grouping.
- `blkWhite.py`: grayscale thresholding experiment.
- `graphData.py`: Matplotlib visualization.
- `spectroUI.py`, `getFilePath.py`: supporting UI and state.

The source uses Python, OpenCV, NumPy, Matplotlib, Pillow, and Tkinter. Some local paths and desktop assumptions are environment-specific; there is no verified one-command setup.

## Important limitations

- The existing code uses bounding-box geometry as a size proxy. Physical size in micrometers **cannot be trusted** without verified pixel-to-distance calibration.
- Fixed thresholds can be sensitive to contrast, lighting, scale, and overlapping particles.
- No documented, independently labeled evaluation set or established precision/recall and measurement-error results are provided.
- Output is exploratory and must not be relied on for engineering or maintenance decisions.

## Planned rebuild

1. Separate image processing from the desktop UI.
2. Implement a minimal, testable classical segmentation baseline.
3. Use authorized labeled images to evaluate count and segmentation error.
4. Validate physical calibration and uncertainty.
5. Only consider supervised ML after benchmarking simpler approaches.

The aim is a smaller, reproducible scientific-computing project whose assumptions and results can be defended.
