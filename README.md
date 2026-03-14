# Kvantizacija boja slike pomoću K-Means algoritma

Ovaj projekt demonstrira primjenu K-Means algoritma za kvantizaciju boja na digitalnim slikama. Svaki piksel slike promatra se kao točka u RGB prostoru boja te se grupira u K klastera. Nakon klasteriranja, originalne boje piksela zamjenjuju se bojama centara klastera čime se smanjuje ukupan broj boja u slici.

Projekt je implementiran u programskom jeziku Python koristeći biblioteke NumPy, OpenCV, Matplotlib i scikit-learn. Rezultati prikazuju usporedbu originalne slike i kvantiziranih verzija za različite vrijednosti parametra K.