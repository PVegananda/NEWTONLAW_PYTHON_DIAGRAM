import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
#              MASUKKAN GAYA (UBAH SESUKA ANDA)
# ==========================================================

F1 = np.array([10, 4])   # gaya pertama
F2 = np.array([-6, 4])   # gaya kedua
#F3 = np.array([0, 0])    # gaya ketiga (opsional)

forces = {
    "F1": F1,
    "F2": F2,
    #"F3": F3
}

# ==========================================================
#      HUKUM NEWTON 1 → cek apakah ∑F = 0 ?
# ==========================================================

sumF = np.sum(list(forces.values()), axis=0)

print("=== HUKUM NEWTON 1: Resultan Gaya ===")
print("F1 =", F1)
print("F2 =", F2)
#print("F3 =", F3)
print("\nResultan ∑F =", sumF)

if np.allclose(sumF, [0,0]):
    print("➡ Benda SETIMBANG (diam / GLB).")
else:
    print("➡ Benda TIDAK SETIMBANG (ada percepatan).")


# ==========================================================
#                    GAMBAR FREE BODY DIAGRAM
# ==========================================================

def draw_force(ax, F, label, color, origin=(0,0)):
    ox, oy = origin
    ax.arrow(ox, oy, F[0], F[1],
             head_width=0.2,
             head_length=0.3,
             length_includes_head=True,
             linewidth=2,
             color=color)
    ax.text(ox + F[0]*1.1, oy + F[1]*1.1, label, fontsize=12, color=color)

fig, ax = plt.subplots(figsize=(7,7))

colors = ["red", "blue", "green"]
for (name, F), col in zip(forces.items(), colors):
    draw_force(ax, F, name, col)

# Resultan digambar dari titik yang berbeda
draw_force(ax, sumF, "Resultan (∑F)", "purple", origin=(0, -2))

# Sumbu bantu
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

ax.set_title("Free Body Diagram – Resultan Gaya (Hukum Newton 1)", fontsize=14)
ax.set_aspect("equal")
ax.grid(True, linestyle=":")

ax.set_xlim(-20, 20)
ax.set_ylim(-10, 10)

plt.show()
