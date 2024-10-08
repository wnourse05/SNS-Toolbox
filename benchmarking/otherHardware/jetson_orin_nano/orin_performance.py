import matplotlib.pyplot as plt
import numpy as np
import pickle

def plot_graph(data, threshold, title, linestyle, lower=5, upper=95):
    numNeurons = data['shape']

    torchCPURawTimes = data['torchCPU']
    torchCPUAvgTimes = np.mean(torchCPURawTimes[:,1:], axis=1) * 1000
    torchCPUVar = np.std(torchCPURawTimes[:,1:], axis=1) * 1000
    torchCPULow = np.percentile(torchCPURawTimes[:,1:], lower, axis=1) * 1000
    torchCPUHigh = np.percentile(torchCPURawTimes[:,1:], upper, axis=1) * 1000

    torchGPURawTimes = data['torchGPU']
    torchGPUAvgTimes = np.mean(torchGPURawTimes[:,1:], axis=1) * 1000
    torchGPUVar = np.std(torchGPURawTimes[:,1:], axis=1) * 1000
    torchGPULow = np.percentile(torchGPURawTimes[:,1:], lower, axis=1) * 1000
    torchGPUHigh = np.percentile(torchGPURawTimes[:,1:], upper, axis=1) * 1000

    """
    ########################################################################################################################
    PLOTTING
    """
    plt.plot(numNeurons, torchCPUAvgTimes, color='C1', label='Torch CPU', linestyle=linestyle)
    plt.fill_between(numNeurons, torchCPULow, torchCPUHigh + torchCPUVar, color='C1', alpha=0.2, linestyle=linestyle)
    plt.plot(numNeurons, torchGPUAvgTimes, color='C2', label='Torch GPU', linestyle=linestyle)
    plt.fill_between(numNeurons, torchGPULow, torchGPUHigh, color='C2', alpha=0.2, linestyle=linestyle)
    plt.axhline(y=threshold, color='black', label='Real-Time Boundary', linestyle='--')
    plt.xlim([numNeurons[0], numNeurons[-1]])
    plt.xlabel('Number of Neurons')
    plt.ylabel('Step Time (ms)')
    plt.yscale('log')
    plt.xscale('log')
    # plt.xlim([10,3000])
    plt.title(title)
    plt.legend()

data_sparse_nonspiking_orin = pickle.load(open('dataJetsonNanoNonspikingSparseLarge.p', 'rb'))
data_dense_nonspiking_orin = pickle.load(open('dataJetsonNonspikingDenseLarge.p', 'rb'))

plt.figure()
plt.subplot(1,2,1)
plot_graph(data_dense_nonspiking_orin,1,'Dense Nonspiking', '-.')

plt.subplot(1,2,2)
plot_graph(data_sparse_nonspiking_orin,1,'Sparse Nonspiking', '-.')

plt.show()
