import numpy as np
import matplotlib.pyplot as plt




data_04 = np.loadtxt("data/Translation_04mm/epi_mc.par")

t = np.arange(data_04.shape[0])

# Extract translations
x = data_04[:,3]
y = data_04[:,4]
z = data_04[:,5]

# Shift so minimum = 0
x = (x - x.min())
y = (y - y.min())
z = (z - z.min())

plt.figure(figsize=(10,4))
# plt.plot(t, x, label="X (mm)")
# plt.plot(t, y, label="Y (mm)")
plt.plot(t*2, z, label="Z (mm)")
plt.xlabel("Timepoint (s)")
plt.ylabel("Translation (mm)")
plt.legend()
plt.title("Head motion from MCFLIRT, 4mm")
plt.tight_layout()
plt.savefig("results/motion_04mm.png")
plt.show()




data_08 = np.loadtxt("data/Translation_08mm/epi_mc.par")

t = np.arange(data_08.shape[0])

# Extract translations
x = data_08[:,3]
y = data_08[:,4]
z = data_08[:,5]

# Shift so minimum = 0
x = (x - x.min())
y = (y - y.min())
z = (z - z.min())

plt.figure(figsize=(10,4))
# plt.plot(t, x, label="X (mm)")
# plt.plot(t, y, label="Y (mm)")
plt.plot(t*2, z, label="Z (mm)")
plt.xlabel("Timepoint (s)")
plt.ylabel("Translation (mm)")
plt.legend()
plt.title("Head motion from MCFLIRT, 8mm")
plt.tight_layout()
plt.savefig("results/motion_08mm.png")
plt.show()




data_12 = np.loadtxt("data/Translation_12mm/epi_mc.par")

t = np.arange(data_04.shape[0])

# Extract translations
x = data_12[:,3]
y = data_12[:,4]
z = data_12[:,5]

# Shift so minimum = 0
x = (x - x.min())
y = (y - y.min())
z = (z - z.min())

plt.figure(figsize=(10,4))
# plt.plot(t, x, label="X (mm)")
# plt.plot(t, y, label="Y (mm)")
plt.plot(t*2, z, label="Z (mm)")
plt.xlabel("Timepoint (s)")
plt.ylabel("Translation (mm)")
plt.legend()
plt.title("Head motion from MCFLIRT, 12mm")
plt.tight_layout()
plt.savefig("results/motion_12mm.png")
plt.show()





data_20 = np.loadtxt("data/Translation_20mm/epi_mc.par")

t = np.arange(data_04.shape[0])

# Extract translations
x = data_20[:,3]
y = data_20[:,4]
z = data_20[:,5]

# Shift so minimum = 0
x = (x - x.min())
y = (y - y.min())
z = (z - z.min())

plt.figure(figsize=(10,4))
# plt.plot(t, x, label="X (mm)")
# plt.plot(t, y, label="Y (mm)")
plt.plot(t*2, z, label="Z (mm)")
plt.xlabel("Timepoint (s)")
plt.ylabel("Translation (mm)")
plt.legend()
plt.title("Head motion from MCFLIRT, 20mm")
plt.tight_layout()
plt.savefig("results/motion_20mm.png")
plt.show()




data_pattern_02 = np.loadtxt("data/motion_pattern_02/epi_mc.par")

t = np.arange(data_04.shape[0])

# Extract translations
x = data_pattern_02[:,3]
y = data_pattern_02[:,4]
z = data_pattern_02[:,5]

# Shift so minimum = 0
x = (x - x.min())
y = (y - y.min())
z = (z - z.min())

plt.figure(figsize=(10,4))
# plt.plot(t, x, label="X (mm)")
# plt.plot(t, y, label="Y (mm)")
plt.plot(t*2, z, label="Z (mm)")
plt.xlabel("Timepoint (s)")
plt.ylabel("Translation (mm)")
plt.legend()
plt.title("Head motion from MCFLIRT, motion pattern 2")
plt.tight_layout()
plt.savefig("results/motion_pattern_02.png")
plt.show()
