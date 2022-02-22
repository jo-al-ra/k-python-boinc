import numpy as np
import matplotlib.pyplot as plt

# time
dt = 0.01
t = np.arange(0, 30, dt) # 3k time points

signal = np.genfromtxt('data_set_obfuscated.csv', delimiter=",")

s1=signal[0]
s2=signal[1]

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('coherence')

fig.tight_layout()
# plt.show()
out_filename = "/results_vibration.pdf"
plt.savefig('{}/results_vibration.pdf'.format("."))

