import numpy as np
from sklearn.cluster import KMeans

def prepare_data(image_np):
    h, w, _ = image_np.shape
    pixels = image_np.reshape((-1, 3))
    return pixels, h, w


def quantization(image_np, k):
    pixels, h, w = prepare_data(image_np)

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(pixels)

    centers = np.round(kmeans.cluster_centers_).astype(np.uint8)
    quantized_pixels = centers[labels]
    quantized_image = quantized_pixels.reshape((h, w, 3))

    return quantized_image, centers


def print_palette(centers):
    print("\nDetected colors (RGB cluster centers):")
    for i, color in enumerate(centers, start=1):
        print(f"Color {i}: {tuple(color)}")