import matplotlib.pyplot as plt

# Fungsi untuk melakukan refleksi terhadap sumbu y = -x
def reflect_over_y_minus_x(point):
    x, y = point
    reflected_x = -y
    reflected_y = -x
    return reflected_x, reflected_y

# Titik-titik segitiga
triangle_points = [(1, 1), (7, 1), (4, 5)]

# Melakukan refleksi pada setiap titik segitiga
reflected_triangle = [reflect_over_y_minus_x(point) for point in triangle_points]

# Menampilkan hasil
plt.plot(*zip(*triangle_points), 'bo-', label='Segitiga Asli')
plt.plot(*zip(*reflected_triangle), 'ro-', label='Segitiga yang Difleksi')
plt.axline((0, 0), slope=-1, color='gray', linestyle='--', label='Garis Refleksi $y = -x$')
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Refleksi Segitiga terhadap $y = -x$')
plt.grid(True)
plt.show()
