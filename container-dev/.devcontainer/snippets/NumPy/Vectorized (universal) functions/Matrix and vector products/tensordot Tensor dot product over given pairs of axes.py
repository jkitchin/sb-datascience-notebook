a = np.arange(24).reshape((3,4,2))
axes_a = (2, 0)
b = np.arange(30).reshape((2,3,5))
axes_b = (0, 1)
np.tensordot(a, b, (axes_a, axes_b))