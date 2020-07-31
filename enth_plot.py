from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

#level of enthusiasm during NMA 
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('center')
#ax.set_title('Focus')
ax.set_ylabel('Level of enthusiasm')
ax.set_xlabel('Time')
plt.xticks([])
plt.yticks([])
fig.text(0.7, 0.04, 'Despina, 2020', ha='left', va='center', fontsize=9)

plt.annotate('NMA starts! Yey!',xy=(0, 0.98), arrowprops=dict(arrowstyle='->'), xytext=(0.03, 1.1))
plt.annotate('GLM day',xy=(0.12, 0.2), arrowprops=dict(arrowstyle='->'), xytext=(0.17, 0.27))
plt.annotate('Organizers say it is OK \n to be overwhelmed',xy=(0.11, 0.9), arrowprops=dict(arrowstyle='->'), xytext=(0.14, 0.94))
plt.annotate('No error in the\n project script!',xy=(0.62, 0.9), arrowprops=dict(arrowstyle='->'), xytext=(0.62, 1))
plt.annotate('That didnt last long...',xy=(0.67, 0.5), arrowprops=dict(arrowstyle='->'), xytext=(0.6, 0.4))
plt.annotate('Meet your superpod \n and chitchat',xy=(0.99, 0.95), arrowprops=dict(arrowstyle='->'), xytext=(0.8, 0.6))

x = np.linspace(0,1,1000)

SIGMA = 0.02
MU = 1
TAU = 17
TAU2 = -10

def power(x, tau):
	return np.exp(-tau * x)

def power2(x, tau, b):
	return (b - np.exp(-tau * x)) / b

def gauss(x, sigma, mu):
	return 0.03* 1 / np.sqrt(2 * np.pi) / sigma * np.exp(-(x - mu) ** 2 / 2. / sigma ** 2)

def calc_y(x, sigma, mu, tau):
  step = 0.7*np.append(np.zeros((100,1)), np.ones((len(x)-100,1)))
  return gauss(x, sigma, mu) + power(x, tau) + step + 0.3*gauss(x, sigma, 0.61) - 0.25*gauss(x, sigma, 0.67)

def calc_students(x, sigma, mu, tau, b):
  return (power2(x, tau, b) + 0.4*gauss(x, sigma, mu)) - 0.3

y = calc_y(x, SIGMA, MU, TAU)
y2 = 61*np.linspace(0.02,0.02,1000)

plt.plot(x,y, label='Average NMA participant')
plt.plot(x,y2, label='Konrad', color='r')

ax.set_xlim(-0.02,1)
plt.legend(loc='lower right',frameon='False')
plt.savefig('NMA.png', dpi=300)
plt.title('Enthusiasm dynamics at NMA 2020')
plt.show()
