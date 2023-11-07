"""
Utilities for plotting neural activity.
"""
from matplotlib import pyplot as plt

def spike_raster_plot(t,data,colors=None,offset=0) -> None:
    """
    Plot spike rasters of spiking data.
    :param t:   vector of timesteps.
    :type t:    List, np.ndarray, or torch.tensor
    :param data:    2D vector of spiking data. Each row corresponds to a different neuron.
    :type data:     np.ndarray or torch.tensor
    :param colors:  List of colors to plot each neuron, default is every neuron is blue.
    :type colors:   List of str, optional
    :param offset:  Constant vertical offset for all spikes, default is 0.
    :type offset:   Number, optional
    :return:        None
    :rtype:         N/A
    """

    if colors is None:
        colors = ['blue']
    if data.ndim > 1:
        for neuron in range(len(data)):
            spike_locs = []
            for step in range(len(t)):
                if data[neuron][step] > 0:
                    spike_locs.append(t[step])
            if len(colors) == 1:
                plt.eventplot(spike_locs,lineoffsets=neuron+1+offset, colors=colors[0],linelengths=0.8)
            else:
                plt.eventplot(spike_locs, lineoffsets=neuron + 1+offset, colors=colors[neuron], linelengths=0.8)
    else:
        spike_locs = []
        for step in range(len(t)):
            if data[step] > 0:
                spike_locs.append(t[step])
        plt.eventplot(spike_locs, lineoffsets=1+offset, colors=colors[0], linelengths=0.8)
