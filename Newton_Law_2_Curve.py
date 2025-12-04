import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# ==========================================================
#                1. MASSA DAN GAYA-GAYA
# ==========================================================

m = 2.0  # massa benda (kg)

# Gaya-gaya dalam bentuk vektor
forces = {
    "F1": np.array([10, 4]),
    "F2": np.array([-6, 4]),
    # "F3": np.array([5, -3]),
    # "F4": np.array([-8, 6]),
}

# Hitung resultan gaya (vektor)
sumF_vector = np.sum(list(forces.values()), axis=0)

# Besar gaya total (magnitudo)
sumF = np.linalg.norm(sumF_vector)

# Percepatan sesuai Hukum Newton 2
a = sumF / m

print(f"Resultan Gaya = {sumF:.2f} N")
print(f"Percepatan    = {a:.2f} m/s²")

# ==========================================================
#                 2. PERHITUNGAN GERAK MOBIL
# ==========================================================

t = np.linspace(0, 5, 200)        # waktu 0–5 detik
x = 0.5 * a * t**2                # persamaan GLBB
v = a * t                         # kecepatan

# Batasi posisi agar tidak keluar layar
x = np.clip(x, 0, 20)

# ==========================================================
#                3. ANIMASI GERAK MOBIL
# ==========================================================

fig, ax = plt.subplots(figsize=(8, 6))

def animate(frame):
    ax.clear()

    # Grafik hanya kuadran positif
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 10)

    ax.set_title("Simulasi Hukum Newton 2 — Gerak dengan Percepatan",
                 fontsize=14, weight="bold")

    # Gambar lintasan
    ax.plot([0, 20], [0, 0], color="black", linewidth=1)

    # Jejak mobil
    ax.plot(x[:frame], np.zeros(frame), color="blue", linewidth=2)

    # Mobil sebagai lingkaran
    ax.scatter(x[frame], 0, s=500, color="royalblue")

    # Informasi fisika
    ax.text(1, 8,
            f"Massa           = {m} kg\n"
            f"Gaya Total     = {sumF:.1f} N\n"
            f"Percepatan     = {a:.2f} m/s²\n"
            f"Kecepatan      = {v[frame]:.2f} m/s",
            fontsize=12,
            bbox=dict(facecolor="white", alpha=0.85))

anim = FuncAnimation(fig, animate, frames=len(t), interval=30)

plt.close(fig)
HTML(anim.to_jshtml())
