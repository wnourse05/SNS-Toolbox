"""
Neurons are the computational nodes of an SNS, and can be either spiking or non-spiking.
"""

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
IMPORTS
"""

from typing import Dict, Any
import warnings
import numbers

from sns_toolbox.design.design_utilities import valid_color, set_text_color

import numpy as np

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
BASE CLASS
"""

class Neuron:
    """
    Parent class of all neurons.

    :param name:                    Name of this neuron preset, default is 'Neuron'.
    :type name:                     str, optional
    :param color:                   Background fill color for the neuron, default is 'white'.
    :type color:                    str, optional
    :param membrane_capacitance:    Neural membrane capacitance, default is 5.0. Units are nanofarads (nF).
    :type membrane_capacitance:     Number, optional
    :param membrane_conductance:    Neural membrane conductance, default is 1.0. Units are microsiemens (uS).
    :type membrane_conductance:     Number, optional
    :param bias:                    Internal bias current, default is 0.0. Units are nanoamps (nA).
    :type bias:                     Number, optional
    """
    def __init__(self, name: str = 'Neuron',
                 color: str = 'white',
                 membrane_capacitance: float = 5.0,
                 membrane_conductance: float = 1.0,
                 bias: float = 0.0) -> None:

        self.params: Dict[str, Any] = {}
        if valid_color(color):
            self.color = color
        else:
            warnings.warn('Specified color is not in the standard SVG set. Defaulting to white.')
            self.color = 'white'
        if isinstance(name,str):
            self.name = name
        else:
            raise TypeError('Neuron name must be a string')
        if isinstance(membrane_capacitance, numbers.Number):
            self.params['membrane_capacitance'] = membrane_capacitance
        else:
            raise TypeError('Membrane capacitance must be a number (int, float, double, etc.)')
        if isinstance(membrane_conductance, numbers.Number):
            self.params['membrane_conductance'] = membrane_conductance
        else:
            raise TypeError('Membrane conductance must be a number (int, float, double, etc.)')
        if isinstance(bias,numbers.Number):
            self.params['bias'] = bias
        else:
            raise TypeError('Bias must be a number (int, float, double, etc.')
        self.params['spiking'] = False
        self.params['gated'] = False

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
SPECIFIC MODELS
"""

class NonSpikingNeuron(Neuron):
    """
    Classic non-spiking neuron model, whose dynamics are as follows:
    membrane_capacitance*dU/dt = -membrane_conductance*u + bias current + synaptic current + external current.
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class NonSpikingNeuronWithGatedChannels(NonSpikingNeuron):
    """
    Iion = sum_j[Gj * A_(inf,j)^Pa * Bj^Pb * Cj^Pc * (Ej - U)]
    """
    def __init__(self, g_ion=None, e_ion=None,
                 pow_a=None, k_a=None, slope_a=None, e_a=None,
                 pow_b=None, k_b=None, slope_b=None, e_b=None, tau_max_b=None,
                 pow_c=None, k_c=None, slope_c=None, e_c=None, tau_max_c=None, **kwargs) -> None:
        super().__init__(**kwargs)

        inputs = [g_ion, e_ion,                         # Channel params
                  pow_a, k_a, slope_a, e_a,             # A gate params
                  pow_b, k_b, slope_b, e_b, tau_max_b,  # B gate params
                  pow_c, k_c, slope_c, e_c, tau_max_c]  # C gate params
        if all(len(x) == len(g_ion) for x in inputs) is False:
            raise ValueError('All channel parameters must be the same dimension (len(g_ion) = len(e_ion) = ...)')
        self.params['gated'] = True
        self.params['Gion'] = g_ion
        self.params['Eion'] = e_ion
        self.params['numChannels'] = len(g_ion)
        self.params['paramsA'] = {'pow': pow_a, 'k': k_a, 'slope': slope_a, 'reversal': e_a}
        self.params['paramsB'] = {'pow': pow_b, 'k': k_b, 'slope': slope_b, 'reversal': e_b, 'TauMax': tau_max_b}
        self.params['paramsC'] = {'pow': pow_c, 'k': k_c, 'slope': slope_c, 'reversal': e_c, 'TauMax': tau_max_c}


class SpikingNeuron(Neuron):
    """
    Generalized leaky integrate-and-fire neuron model, whose dynamics are as follows:
    membrane_capacitance*dU/dt = -membrane_conductance*u + bias current + synaptic current + external current;
    threshold_time_constant*dTheta/dt = -Theta + threshold_initial_value + threshold_proportionality_constant*u;
    if u > Theta, u->0.

    :param threshold_time_constant: Rate that the firing threshold moves to the baseline value, default is 5.0. Units
        are milliseconds (ms).
    :type threshold_time_constant:  Number, optional
    :param threshold_initial_value: Baseline value of the firing threshold, default is 1.0. Units are millivolts (mV).
    :type threshold_initial_value:  Number, optional
    :param threshold_proportionality_constant:  Constant which determines spiking behavior.
        In response to constant stimulus, negative values cause the firing rate to decrease, positive values cause the
        rate to increase, and zero causes the rate to remain constant. Default is 0.0.
    :param threshold_proportionality constant:  Number, optional
    """
    def __init__(self, threshold_time_constant: float = 5.0,
                 threshold_initial_value: float = 1.0,
                 threshold_proportionality_constant: float = 0.0,
                 **kwargs) -> None:

        super().__init__(**kwargs)
        self.params['threshold_time_constant'] = threshold_time_constant
        self.params['threshold_initial_value'] = threshold_initial_value
        self.params['threshold_proportionality_constant'] = threshold_proportionality_constant
        self.params['spiking'] = True
