import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
#            MASUKKAN GAYA (UBAH SESUKA ANDA)
# ==========================================================

forces = {
    "F1": np.array([10, 4]),
    "F2": np.array([-6, 4]),
     "F3": np.array([0, -12]),
    # "F4": np.array([5, 0])
}

# ==========================================================
#      HITUNG RESULTAN (HUKUM NEWTON 1)
# ==========================================================

sumF = np.sum(list(forces.values()), axis=0)

print("=== HUKUM NEWTON 1: Resultan Gaya ===")
for name, F in forces.items():
    print(f"{name} = {F}")

print("\nResultan ∑F =", sumF)

if np.allclose(sumF, [0,0]):
    print("➡ Benda SETIMBANG (diam / GLB).")
else:
    print("➡ Benda TIDAK SETIMBANG (ada percepatan).")

# ==========================================================
#              FUNGSI GAMBAR PANAH GAYA
# ==========================================================

def draw_force(ax, F, label, origin=(0,0), color="red"):
    ox, oy = origin
    ax.arrow(ox, oy, F[0], F[1],
             head_width=0.5,
             head_length=0.7,
             length_includes_head=True,
             linewidth=2.5,
             color=color)
    ax.text(ox + F[0]*1.05, oy + F[1]*1.05,
            label, fontsize=14, color=color, weight="bold")

# ==========================================================
#            GAMBAR FBD (VERSI LEBIH LUAS)
# ==========================================================

fig, ax = plt.subplots(figsize=(10, 10))  # <<< BESARKAN KANVAS

# Warna otomatis (looping)
colors = ["red", "blue", "green", "orange", "purple", "brown"]

for (name, F), col in zip(forces.items(), colors):
    draw_force(ax, F, name, color=col)

# Gambar resultan dari titik berbeda
draw_force(ax, sumF, "Resultan (ΣF)", origin=(0, -3), color="purple")

# ==========================================================
#            SETTING AREA GAMBAR (AUTO SCALE)
# ==========================================================

# Cari gaya terbesar → untuk menentukan batas grafik otomatis
max_range = np.max(np.abs(np.array(list(forces.values())))) * 2.5

ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)

# Sumbu bantu
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.5)

ax.set_title("Free Body Diagram – Versi Diperbesar", fontsize=18, weight="bold")

plt.show()
