from src.utils import load_image
from src.kmeans_quantization import quantization
from src.visualization import show_comparison


def main():
    input_path = "images/image_one.jpg"

    k_values = [2, 4, 8, 16, 32]

    original_image = load_image(input_path)

    quantized_images = []

    for k in k_values:
        quantized_image, centers = quantization(original_image, k)
        quantized_images.append((k, quantized_image))

    show_comparison(original_image, quantized_images)


if __name__ == "__main__":
    main()