"""
Analyze the data we collected in the component comparison test
William Nourse
December 16th 2021
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt

test_params = pickle.load(open('test_params.p','rb'))
num_neurons = test_params['numNeurons']

data = []
data.append(pickle.load(open('10_neurons.p', 'rb')))
data.append(pickle.load(open('11_neurons.p', 'rb')))
data.append(pickle.load(open('13_neurons.p', 'rb')))
data.append(pickle.load(open('15_neurons.p', 'rb')))
data.append(pickle.load(open('17_neurons.p', 'rb')))
data.append(pickle.load(open('20_neurons.p', 'rb')))
data.append(pickle.load(open('23_neurons.p', 'rb')))
data.append(pickle.load(open('26_neurons.p', 'rb')))
data.append(pickle.load(open('30_neurons.p', 'rb')))
data.append(pickle.load(open('35_neurons.p', 'rb')))
data.append(pickle.load(open('40_neurons.p', 'rb')))
data.append(pickle.load(open('47_neurons.p', 'rb')))
data.append(pickle.load(open('54_neurons.p', 'rb')))
data.append(pickle.load(open('62_neurons.p', 'rb')))
data.append(pickle.load(open('71_neurons.p', 'rb')))
data.append(pickle.load(open('82_neurons.p', 'rb')))
data.append(pickle.load(open('95_neurons.p', 'rb')))
data.append(pickle.load(open('109_neurons.p', 'rb')))
data.append(pickle.load(open('126_neurons.p', 'rb')))
data.append(pickle.load(open('145_neurons.p', 'rb')))
data.append(pickle.load(open('167_neurons.p', 'rb')))
data.append(pickle.load(open('193_neurons.p', 'rb')))
data.append(pickle.load(open('222_neurons.p', 'rb')))
data.append(pickle.load(open('255_neurons.p', 'rb')))
data.append(pickle.load(open('294_neurons.p', 'rb')))
data.append(pickle.load(open('339_neurons.p', 'rb')))
data.append(pickle.load(open('390_neurons.p', 'rb')))
data.append(pickle.load(open('449_neurons.p', 'rb')))
data.append(pickle.load(open('517_neurons.p', 'rb')))
data.append(pickle.load(open('596_neurons.p', 'rb')))
data.append(pickle.load(open('686_neurons.p', 'rb')))
data.append(pickle.load(open('790_neurons.p', 'rb')))
data.append(pickle.load(open('910_neurons.p', 'rb')))
data.append(pickle.load(open('1048_neurons.p', 'rb')))
data.append(pickle.load(open('1206_neurons.p', 'rb')))
data.append(pickle.load(open('1389_neurons.p', 'rb')))
data.append(pickle.load(open('1599_neurons.p', 'rb')))
data.append(pickle.load(open('1842_neurons.p', 'rb')))
data.append(pickle.load(open('2120_neurons.p', 'rb')))
data.append(pickle.load(open('2442_neurons.p', 'rb')))
data.append(pickle.load(open('2811_neurons.p', 'rb')))
data.append(pickle.load(open('3237_neurons.p', 'rb')))
data.append(pickle.load(open('3727_neurons.p', 'rb')))
data.append(pickle.load(open('4291_neurons.p', 'rb')))
data.append(pickle.load(open('4941_neurons.p', 'rb')))
data.append(pickle.load(open('5689_neurons.p', 'rb')))
data.append(pickle.load(open('6551_neurons.p', 'rb')))
data.append(pickle.load(open('7543_neurons.p', 'rb')))
data.append(pickle.load(open('8685_neurons.p', 'rb')))
data.append(pickle.load(open('10000_neurons.p', 'rb')))

full_spiking_mean = np.zeros(len(num_neurons))
full_no_delay_mean = np.zeros(len(num_neurons))
full_non_spiking_mean = np.zeros(len(num_neurons))
realistic_spiking_mean = np.zeros(len(num_neurons))
realistic_no_delay_mean = np.zeros(len(num_neurons))
realistic_non_spiking_mean = np.zeros(len(num_neurons))

full_spiking_var = np.zeros(len(num_neurons))
full_no_delay_var = np.zeros(len(num_neurons))
full_non_spiking_var = np.zeros(len(num_neurons))
realistic_spiking_var = np.zeros(len(num_neurons))
realistic_no_delay_var = np.zeros(len(num_neurons))
realistic_non_spiking_var = np.zeros(len(num_neurons))

full_spiking_std = np.zeros(len(num_neurons))
full_no_delay_std = np.zeros(len(num_neurons))
full_non_spiking_std = np.zeros(len(num_neurons))
realistic_spiking_std = np.zeros(len(num_neurons))
realistic_no_delay_std = np.zeros(len(num_neurons))
realistic_non_spiking_std = np.zeros(len(num_neurons))

for i in range(len(num_neurons)):
    full_spiking_mean[i] = np.mean(data[i]['fullSpiking'])
    full_no_delay_mean[i] = np.mean(data[i]['fullNoDelay'])
    full_non_spiking_mean[i] = np.mean(data[i]['fullNonSpiking'])
    realistic_spiking_mean[i] = np.mean(data[i]['realisticSpiking'])
    realistic_no_delay_mean[i] = np.mean(data[i]['realisticNoDelay'])
    realistic_non_spiking_mean[i] = np.mean(data[i]['realisticNonSpiking'])

    full_spiking_var[i] = np.var(data[i]['fullSpiking'])
    full_no_delay_var[i] = np.var(data[i]['fullNoDelay'])
    full_non_spiking_var[i] = np.var(data[i]['fullNonSpiking'])
    realistic_spiking_var[i] = np.var(data[i]['realisticSpiking'])
    realistic_no_delay_var[i] = np.var(data[i]['realisticNoDelay'])
    realistic_non_spiking_var[i] = np.var(data[i]['realisticNonSpiking'])

    full_spiking_std[i] = np.std(data[i]['fullSpiking'])
    full_no_delay_std[i] = np.std(data[i]['fullNoDelay'])
    full_non_spiking_std[i] = np.std(data[i]['fullNonSpiking'])
    realistic_spiking_std[i] = np.std(data[i]['realisticSpiking'])
    realistic_no_delay_std[i] = np.std(data[i]['realisticNoDelay'])
    realistic_non_spiking_std[i] = np.std(data[i]['realisticNonSpiking'])

plt.figure()
plt.plot(num_neurons,full_spiking_mean,color='blue',label='Full Spiking Model')
plt.fill_between(num_neurons,full_spiking_mean-full_spiking_std,full_spiking_mean+full_spiking_std,color='blue',alpha=0.1)
plt.plot(num_neurons,full_no_delay_mean,color='orange',label='Full No Delay Model')
plt.fill_between(num_neurons,full_no_delay_mean-full_no_delay_std,full_no_delay_mean+full_no_delay_std,color='orange',alpha=0.1)
plt.plot(num_neurons,full_non_spiking_mean,color='green',label='Full Non Spiking Model')
plt.fill_between(num_neurons,full_non_spiking_mean-full_non_spiking_std,full_non_spiking_mean+full_non_spiking_std,color='green',alpha=0.1)
plt.legend()
plt.xlabel('Number of Neurons')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Average Time per Step (s)')
plt.title('Fully Connected Networks')

plt.figure()
plt.plot(num_neurons,realistic_spiking_mean,color='blue',label='Realistic Spiking Model')
plt.fill_between(num_neurons,realistic_spiking_mean-realistic_spiking_std,realistic_spiking_mean+full_spiking_std,color='blue',alpha=0.1)
plt.plot(num_neurons,realistic_no_delay_mean,color='orange',label='Realistic No Delay Model')
plt.fill_between(num_neurons,realistic_no_delay_mean-realistic_no_delay_std,realistic_no_delay_mean+realistic_no_delay_std,color='orange',alpha=0.1)
plt.plot(num_neurons,realistic_non_spiking_mean,color='green',label='Realistic Non Spiking Model')
plt.fill_between(num_neurons,realistic_non_spiking_mean-realistic_non_spiking_std,realistic_non_spiking_mean+realistic_non_spiking_std,color='green',alpha=0.1)
plt.legend()
plt.xlabel('Number of Neurons')
plt.ylabel('Average Time per Step (s)')
plt.yscale('log')
plt.xscale('log')
plt.title('Realistically Connected Networks')

plt.show()

plt.show()