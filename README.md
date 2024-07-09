# Infinitesimal Dipole Antenna Simulator

This project simulates the behavior of an infinitesimal dipole antenna. It provides a graphical user interface (GUI) to visualize the current distribution, electric field, and magnetic field of the antenna based on user-defined parameters.

## Features

- **Current Distribution Plot**: Visualizes the current distribution along the dipole.
- **Electric Field Plot**: Displays the electric field magnitude in a polar plot.
- **Magnetic Field Plot**: Shows the magnetic field magnitude in a polar plot.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Matplotlib
- NumPy

## Installation

1. Clone the repository:
    ```sh
     git clone https://github.com/17himanshu/Antenna-Project.git
    cd Antenna-Project
    ```

2. Install the required Python packages:
    ```sh
    pip install matplotlib numpy
    ```

## Running the Simulator

1. Ensure that you have the required images (`infinitesimal.png` and `image2.png`) in the same directory as `antenna.py`.

2. Run the simulator:
    ```sh
    python antenna.py
    ```

## Usage

1. **Dipole Length (m)**: Enter the length of the dipole in meters.
2. **Current Amplitude (A)**: Enter the current amplitude in amperes.
3. **Frequency (Hz)**: Enter the operating frequency in hertz.
4. **Distance (m)**: Enter the distance from the dipole in meters.

### Buttons

- **Plot Current**: Generates a plot of the current distribution along the dipole.
- **Plot Electric Field**: Generates a polar plot of the electric field magnitude.
- **Plot Magnetic Field**: Generates a polar plot of the magnetic field magnitude.

## Example

Here's an example of how to use the simulator:

1. Open the simulator by running `python antenna.py`.
2. Enter the following values:
    - Dipole Length: `0.5`
    - Current Amplitude: `1`
    - Frequency: `3e8`
    - Distance: `1`
3. Click on the "Plot Current" button to see the current distribution.
4. Click on the "Plot Electric Field" button to see the electric field magnitude.
5. Click on the "Plot Magnetic Field" button to see the magnetic field magnitude.

## Notes

- Ensure that the image files `infinitesimal.png` and `image2.png` are available in the same directory. If not, the simulator will not display the images but will still function.
- This project is for educational purposes to demonstrate the visualization of an infinitesimal dipole antenna.

  
![WhatsApp Image 2024-07-09 at 11 02 42_a3d2f002](https://github.com/17himanshu/Antenna-Project/assets/96365482/9ddcdf4a-812f-4dfb-b109-2bf7567c56b9)
![image](https://github.com/17himanshu/Antenna-Project/assets/96365482/26bd77c1-57b4-45d9-a0f2-d20cee16cd41)
![image](https://github.com/17himanshu/Antenna-Project/assets/96365482/abc9b460-e757-4329-afe6-a46a538fe054)


