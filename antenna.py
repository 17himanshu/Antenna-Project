import tkinter as tk
from tkinter import PhotoImage
import matplotlib.pyplot as plt
import numpy as np

def plot_current(dipole_length, current_amplitude):
    x_min = -dipole_length / 2
    x_max = dipole_length / 2
    num_points = 100
    x = np.linspace(x_min, x_max, num_points)
    current = current_amplitude * np.sin(2 * np.pi * x / dipole_length)
    plt.plot(x, current)
    plt.xlabel('Position (x)')
    plt.ylabel('Current (A)')
    plt.title('Current Distribution of Infinitesimal Dipole')
    plt.show()

def plot_electric_field(dipole_length, frequency, distance, current_amplitude):
    theta = np.linspace(0, np.pi, 100)
    mu_0 = 4 * np.pi * 1e-7
    c = 3e8
    ni = 377
    k = 2 * np.pi * frequency / c
    sigma = 0
    E_r = (ni * current_amplitude * dipole_length * (1 / (2 * np.pi * distance * distance)) * np.exp(-1j * k * distance) * np.cos(theta) * (1 + 1 / (1j * k * distance)))
    E_theta = (1j * ni * dipole_length * current_amplitude * (k / (4 * np.pi * distance)) * np.exp(-1j * k * distance) * np.sin(theta) * (1 + (1 / (1j * k * distance)) - 1 / (k * distance) ** 2))
    magnitude = np.sqrt(np.abs(E_theta) ** 2 + np.abs(E_r) ** 2)
    plt.polar(theta, magnitude)
    plt.title('Electric Field Magnitude of Infinitesimal Dipole')
    plt.show()

def plot_magnetic_field(dipole_length, frequency, distance, current_amplitude):
    theta = np.linspace(0, np.pi, 100)
    mu_0 = 4 * np.pi * 1e-7
    c = 3e8
    k = 2 * np.pi * frequency / c
    sigma = 0
    H_phi = (1j * dipole_length * current_amplitude * (k / (4 * np.pi * distance)) * np.exp(-1j * k * distance) * np.sin(theta) * (1 + 1 / (1j * k * distance)))
    magnitude = abs(H_phi)
    plt.polar(theta, magnitude)
    plt.title('Magnetic Field Magnitude of Infinitesimal Dipole')
    plt.show()

def create_label(parent, text, font_size=14):
    return tk.Label(parent, text=text, font=('Helvetica', font_size))

def create_button(parent, text, command, font_size=14):
    return tk.Button(parent, text=text, command=command, font=('Helvetica', font_size))

window = tk.Tk()
window.title('Infinitesimal Dipole Antenna Simulator')

headline_label = create_label(window, 'Antenna Simulation', font_size=25)
headline_label.pack(pady=10)

image_path1 = "infinitesimal.png"
try:
    image1 = PhotoImage(file="infinitesimal.png")
    image_label1 = tk.Label(window, image=image1)
    image_label1.pack(side=tk.LEFT, padx=50)
except tk.TclError:
    print(f"Error: Unable to load image from {image_path1}")

image_path2 = "image2.png"
try:
    image2 = PhotoImage(file="image2.png")
    image_label2 = tk.Label(window, image=image2)
    image_label2.pack(side=tk.RIGHT, padx=35)
except tk.TclError:
    print(f"Error: Unable to load image from {image_path2}")

labels_and_entries = [
    ('Dipole Length (m):', tk.Entry(window)),
    ('Current Amplitude (A):', tk.Entry(window)),
    ('Frequency (Hz):', tk.Entry(window)),
    ('Distance (m):', tk.Entry(window)),
]

for label_text, entry in labels_and_entries:
    label_widget = create_label(window, label_text)
    label_widget.pack(pady=5)
    entry.pack(pady=5)

plot_current_button = create_button(window, 'Plot Current', lambda: plot_current(float(labels_and_entries[0][1].get()), float(labels_and_entries[1][1].get())))
plot_current_button.pack(pady=10)

plot_electric_field_button = create_button(window, 'Plot Electric Field', lambda: plot_electric_field(float(labels_and_entries[0][1].get()), float(labels_and_entries[2][1].get()), float(labels_and_entries[3][1].get()), float(labels_and_entries[1][1].get())))
plot_electric_field_button.pack(pady=10)

plot_magnetic_field_button = create_button(window, 'Plot Magnetic Field', lambda: plot_magnetic_field(float(labels_and_entries[0][1].get()), float(labels_and_entries[2][1].get()), float(labels_and_entries[3][1].get()), float(labels_and_entries[1][1].get())))
plot_magnetic_field_button.pack(pady=10)

window.mainloop()