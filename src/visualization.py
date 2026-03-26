import matplotlib.pyplot as plt


def show_comparison(original, quantized_images):

    total_images = len(quantized_images) + 1

    plt.figure(figsize=(15, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(original)
    plt.title("Original")
    plt.axis("off")

    for i, (k, img) in enumerate(quantized_images, start=2):

        plt.subplot(2, 3, i)
        plt.imshow(img)
        plt.title(f"K = {k}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()