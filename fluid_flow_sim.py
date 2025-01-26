# June-20-2024

import numpy as np
import matplotlib.pyplot as plt

plot_every = 50


def distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    # Define the grid
    x = 400
    y = 100
    tau = .53
    iterations = 100000

    # Lattice speeds and weights
    lattice_num = 9
    cxs = np.array([0, 0, 1, 1, 1, 0, -1, -1, -1])
    cys = np.array([0, 1, 1, 0, -1, -1, -1, 0, 1])
    weights = np.array([4 / 9, 1 / 9, 1 / 36, 1 / 9, 1 / 36, 1 / 9, 1 / 36, 1 / 9, 1 / 36])

    # Define the initial conditions
    F = np.ones((y, x, lattice_num)) + 0.1 * np.random.randn(y, x, lattice_num)
    F[:, :, 3] = 2.3

    # Define the obstacle in the flow fluid
    disk = np.full((y, x), False)

    # Define the borders of the obstacle
    center_x = x // 6
    center_y = y // 2
    radius = 13
    for i in range(x):
        for j in range(y):
            if distance(center_x, center_y, i, j) < radius:
                disk[j][i] = True

    # Main loop
    for t in range(iterations):
        print(t)

        # Applying the zou-he boundary conditions
        F[:, -1, [6, 7, 8]] = F[:, -2, [6, 7, 8]]
        F[:, 0, [2, 3, 4]] = F[:, 1, [2, 3, 4]]

        # Make the flow go from the left to the right
        for i, cx, cy in zip(range(lattice_num), cxs, cys):
            F[:, :, i] = np.roll(F[:, :, i], cx, axis=1)
            F[:, :, i] = np.roll(F[:, :, i], cy, axis=0)

        # Make the particles that collide with the boundary go in the opposite direction
        boundrF = F[disk, :]
        boundrF = boundrF[:, [0, 5, 6, 7, 8, 1, 2, 3, 4]]

        # Calculate the fluid variables
        rho = np.sum(F, 2)  # Density
        u = np.sum(F * cxs, 2) / rho  # Horizontal velocity
        v = np.sum(F * cys, 2) / rho  # Vertical velocity

        F[disk, :] = boundrF
        u[disk] = 0
        v[disk] = 0

        # Collision
        feq = np.zeros(F.shape)
        for i, cx, cy, w in zip(range(lattice_num), cxs, cys, weights):
            feq[:, :, i] = rho * w * (1 + 3*(cx * u + cy * v) + 9 * (cx * u + cy * v)**2 / 2 - 3 * (u**2 + v**2) / 2)

        F = F + -(1/tau) * (F - feq)

        if t % plot_every == 0:
            plt.imshow(np.sqrt(u**2 + v**2), cmap="jet")
            plt.pause(0.01)
            plt.cla()
    plt.show()


if __name__ == "__main__":
    main()
