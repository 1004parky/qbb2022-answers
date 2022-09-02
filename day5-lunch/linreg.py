import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.formula.api as smf
from scipy import stats

data = np.genfromtxt('final_data.txt', dtype=int, names=True)
# columns:
# ('proband_ID', 'father_age', 'mother_age', 'n_father', 'n_mother')
# print(data.dtype.names)

plt.scatter(data['mother_age'], data['n_mother'])
plt.ylabel('Number of maternal de novo mutations')
plt.xlabel('Mother age')
plt.title('Mother')
plt.savefig('ex2_a.png')
plt.clf()

plt.scatter(data['father_age'], data['n_father'])
plt.ylabel('Number of paternal de novo mutations')
plt.xlabel('Father age')
plt.title('Father')
plt.savefig('ex2_b.png')

# Exercise 6 + 7
model = smf.ols(formula='n_mother ~ mother_age + 1', data=data)
results = model.fit()

print(results.summary())

model = smf.ols(formula='n_father ~ father_age + 1', data=data)
results = model.fit()

print(results.summary())

# Exercise 8
plt.clf()
plt.hist(data['n_mother'], label='maternal', alpha=0.5, bins=10)
plt.hist(data['n_father'], label='paternal', alpha=0.5, bins=10)
plt.ylabel('Number of probands')
plt.xlabel('number of de novo mutations per proband')
plt.legend()
plt.title('Histogram')
plt.savefig('ex2_c.png')

# Exercise 9 
print(stats.ttest_ind(data['n_mother'], data['n_father']))

# Exercise 10 
sample = data[0]
sample.fill(0)
sample['father_age'] = 50.5
print(results.predict(sample))
