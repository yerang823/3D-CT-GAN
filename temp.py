import numpy as np
from utils.equalizer import *

instances=np.load('data/instances.npy')

# Histogram Equalization:
print("equalizing the data...")
eq = histEq(instances)
instances = eq.equalize(instances) #killed here maybe.....
#os.makedirs('tmp',exist_ok=True)
eq.save('equalization__.pkl')

# -1 1 Normalization
print("normalizing the data...")
min_v = np.min(instances)
max_v = np.max(instances)
mean_v = np.mean(instances)
norm_data = np.array([mean_v, min_v, max_v])
instances = (instances - mean_v) / (max_v - min_v)
np.save('normalization__.npy',norm_data)


print("saving the dataset")
np.save('unhealthy_samples_201210.npy',instances)

