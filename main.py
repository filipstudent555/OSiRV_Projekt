import os
import matplotlib.pyplot as plt

from src.utils import load_image, save_image
from src.kmeans_quantization import quantization
from src.visualization import show_comparison


def main():
    output_folder = "results"
    os.makedirs(output_folder, exist_ok=True)

    k_values = [2, 4, 8, 16, 32]

    image_paths = {
        "Ptica": "images/image_one.jpg",
        "Vodopad": "images/image_two.jpg",
        "Grafiti": "images/image_three.jpg"
    }

    all_analysis_results = {}

    for image_name, input_path in image_paths.items():

        original_image = load_image(input_path)
        quantized_images = []
        analysis_results = []

        image_output_folder = os.path.join(output_folder, image_name.lower())
        os.makedirs(image_output_folder, exist_ok=True)

        for k in k_values:
            quantized_image, centers, inertia = quantization(original_image, k)

            output_path = os.path.join(image_output_folder, f"quantized_k{k}.png")
            save_image(quantized_image, output_path)

            file_size_bytes = os.path.getsize(output_path)
            file_size_kb = file_size_bytes / 1024

            quantized_images.append((k, quantized_image))
            analysis_results.append((k, inertia, file_size_kb))

        all_analysis_results[image_name] = analysis_results

        show_comparison(original_image, quantized_images)

        print("-" * 55)
        print(f"{'K':<10}{'SSE':<20}{'PNG size (KB)':<20}")
        print("-" * 55)

        for k, inertia, file_size_kb in analysis_results:
            print(f"{k:<10}{inertia:<20.2f}{file_size_kb:<20.2f}")

    plt.figure(figsize=(10, 6))

    for image_name, analysis_results in all_analysis_results.items():
        k_list = [item[0] for item in analysis_results]
        inertia_list = [item[1] for item in analysis_results]

        plt.plot(k_list, inertia_list, marker='o', label=image_name)

    plt.xlabel("K")
    plt.ylabel("SSE (Inertia)")
    plt.title("Ovisnost SSE vrijednosti o broju klastera K")
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(output_folder, "graf.png"))
    plt.show()


if __name__ == "__main__":
    main()