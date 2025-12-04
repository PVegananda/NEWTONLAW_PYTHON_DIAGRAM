import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# ==========================================================
#                PARAMETER FISIKA (NEWTON 2)
# ==========================================================

m = 2.0  # massa mobil (kg)

forces = {
    "F1": np.array([10, 0]),
    "F2": np.array([-2, 0]),
    "F3": np.array([3, 0]),
    "F4": np.array([-1, 0]),
}

# hitung ΣF dan percepatan
sumF = np.sum(list(forces.values()), axis=0)
acc = sumF / m  # percepatan mobil (m/s²)

# ==========================================================
#                    STATE SIMULASI
# ==========================================================

pos = 0.0         # posisi awal mobil
vel = 0.0         # kecepatan awal mobil
dt = 0.1          # timestep
trail_x = []      # jejak posisi mobil
trail_y = []      # posisinya di sumbu y tetap 0

max_speed = 2.0   # batas kecepatan
max_pos = 20      # batas grafik kanan

# ==========================================================
#                   SETUP FIGURE
# ==========================================================

fig, ax = plt.subplots(figsize=(12, 5))

# ==========================================================
#                    ANIMASI
# ==========================================================

def animate(frame):
    global pos, vel
    
    ax.clear()

    # batas grafik
    ax.set_xlim(0, 20)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", alpha=0.3)
    
    ax.set_title("Simulasi Mobil Mengalami Percepatan (Hukum Newton 2)", fontsize=16)

    # ------------------------------------------------------
    # PERBARUI FISIKA (a, v, x)
    # ------------------------------------------------------

    vel += acc[0] * dt
    vel = np.clip(vel, -max_speed, max_speed)   # batasi kecepatan

    pos += vel * dt
    pos = np.clip(pos, 0, max_pos)              # batasi posisi agar tidak keluar layar

    # simpan jejak
    trail_x.append(pos)
    trail_y.append(0)

    # ------------------------------------------------------
    # GAMBAR JEJAK MOBIL
    # ------------------------------------------------------
    ax.plot(trail_x, trail_y, color="cyan", linewidth=2, label="Jejak Lintasan")

    # ------------------------------------------------------
    # GAMBAR MOBIL (LINGKARAN)
    # ------------------------------------------------------
    mobil = plt.Circle((pos, 0), 0.8, color="black", fill=False, linewidth=3)
    ax.add_patch(mobil)

    # ------------------------------------------------------
    # GAMBAR VEKTOR PERCEPATAN (TANPA LABEL)
    # ------------------------------------------------------
    ax.arrow(pos, 0.5, acc[0]*1.2, 0,
             head_width=0.15,
             head_length=0.25,
             linewidth=2,
             color="purple")

    # ------------------------------------------------------
    # INFO FISIKA
    # ------------------------------------------------------
    ax.text(0.5, 2.3, f"ΣF = {sumF[0]:.2f} N", fontsize=12)
    ax.text(0.5, 1.8, f"a = {acc[0]:.2f} m/s²", fontsize=12)
    ax.text(0.5, 1.3, f"v = {vel:.2f} m/s (dibatasi)", fontsize=12)
    ax.text(0.5, 0.8, f"x = {pos:.2f} m", fontsize=12)

anim = FuncAnimation(fig, animate, frames=400, interval=50)

plt.close(fig)
HTML(anim.to_jshtml())
