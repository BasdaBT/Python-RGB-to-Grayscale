from __future__ import annotations

import argparse
from pathlib import Path

import cv2


def process_image(
    input_path: Path,
    output_dir: Path,
    threshold: int,
) -> tuple[Path, Path, Path]:
    """Create direct grayscale, converted grayscale and binary outputs."""
    color_image = cv2.imread(str(input_path), cv2.IMREAD_COLOR)
    direct_gray = cv2.imread(str(input_path), cv2.IMREAD_GRAYSCALE)

    if color_image is None or direct_gray is None:
        raise FileNotFoundError(f"Image could not be read: {input_path}")

    converted_gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(
        converted_gray,
        threshold,
        255,
        cv2.THRESH_BINARY,
    )

    # OpenCV stores color images as BGR. This conversion produces an RGB array
    # suitable for libraries such as Matplotlib.
    rgb_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
    print(f"BGR shape: {color_image.shape}; RGB shape: {rgb_image.shape}")

    output_dir.mkdir(parents=True, exist_ok=True)
    stem = input_path.stem
    direct_path = output_dir / f"{stem}_gray_direct.png"
    converted_path = output_dir / f"{stem}_gray_converted.png"
    binary_path = output_dir / f"{stem}_binary.png"

    cv2.imwrite(str(direct_path), direct_gray)
    cv2.imwrite(str(converted_path), converted_gray)
    cv2.imwrite(str(binary_path), binary_image)
    return direct_path, converted_path, binary_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create grayscale and binary versions of an image with OpenCV."
    )
    parser.add_argument("input", type=Path, help="Path to the source image")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory for generated images (default: outputs)",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=127,
        choices=range(256),
        metavar="0-255",
        help="Binary threshold value (default: 127)",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display the generated images in OpenCV windows",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_paths = process_image(args.input, args.output_dir, args.threshold)
    for path in output_paths:
        print(f"Saved: {path}")

    if args.show:
        color_image = cv2.imread(str(args.input), cv2.IMREAD_COLOR)
        gray_image = cv2.imread(str(output_paths[1]), cv2.IMREAD_GRAYSCALE)
        binary_image = cv2.imread(str(output_paths[2]), cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Original", color_image)
        cv2.imshow("Grayscale", gray_image)
        cv2.imshow("Binary", binary_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
