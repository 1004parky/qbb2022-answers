from bdg_loader import *
import matplotlib.pyplot as plt

# Making plot like 6K from paper
# Part 1, step 5

files = 'D2_Sox2_R1_treat_pileup_scaled_cropped.bdg D2_Klf4_treat_scaled_cropped.bdg D0_H3K27ac_treat_scaled_cropped.bdg D2_H3K27ac_treat_scaled_cropped.bdg'.split()
fig, axs = plt.subplots(4)
for i in range(len(files)):
  data = load_data(files[i])
  axs[i].fill_between(data['X'], data['Y'])
  axs[i].set_ylabel(files[i].split('_')[1])

plt.xlabel('position')
plt.suptitle('ChIP data')
plt.tight_layout()
plt.savefig('hw5.1.png')
plt.show()