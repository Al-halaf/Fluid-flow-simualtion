# Fluid Flow Simulation Using Lattice Boltzmann Method (LBM)

This project implements a fluid flow simulation using the Lattice Boltzmann Method (LBM). It simulates fluid dynamics over a defined grid with an obstacle, providing a visual representation of velocity fields as the fluid interacts with the object.

## Features

- **Lattice Boltzmann Method:** Implements LBM to model fluid dynamics with collision and streaming steps.
- **Boundary Conditions:** Applies Zou-He boundary conditions for the simulation.
- **Obstacle Interaction:** Simulates fluid flow around a circular obstacle.
- **Visualization:** Generates real-time visualizations of fluid velocity magnitudes.

## Requirements

To run the project, ensure the following dependencies are installed:

- **Python**
- Libraries:
  - `numpy`
  - `matplotlib`

## Workflow

1. **Grid Initialization:**
   - Define the simulation grid dimensions and lattice parameters (speeds, weights).
   - Initialize the particle distribution function `F` with random perturbations for fluid flow.

2. **Obstacle Definition:**
   - Create a circular obstacle at a specified location within the grid.

3. **Main Simulation Loop:**
   - Apply Zou-He boundary conditions at the grid edges.
   - Stream particles across the grid according to lattice velocities.
   - Handle collisions with the obstacle by reversing particle directions.
   - Compute macroscopic variables such as density (`rho`), horizontal velocity (`u`), and vertical velocity (`v`).
   - Perform collision calculations using equilibrium distribution (`feq`).

4. **Visualization:**
   - Display the magnitude of the velocity field at specified intervals (`plot_every`) during the simulation.

## Applications

This project can be applied to:

- Computational Fluid Dynamics (CFD) studies.
- Education and demonstration of fluid flow concepts.
- Simulating flows around various shapes to study drag and flow patterns.

## Example Simulation

The simulation models fluid flowing from left to right across a grid containing a circular obstacle. Real-time visualizations illustrate how the fluid interacts with the obstacle, creating wake regions and flow dynamics.

---

Feel free to explore and modify the code for additional features or scenarios!
