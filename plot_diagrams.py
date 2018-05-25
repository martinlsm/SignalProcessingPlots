import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style
from scipy import signal
import plot_poles_zeros
from read_file import PolesAndZeros

def plot_amplitude(poles, zeros, subplot):
    w, h = signal.freqz_zpk(zeros, poles, 1)
    subplot.plot(w/(2*math.pi), abs(h), color='blue')
    subplot.set_title('Frequency response')
    subplot.set_ylabel('Amplitude')
    subplot.set_xlabel('Frequency [f]')

def plot_argument(poles, zeros, subplot):
    w, h = signal.freqz_zpk(zeros, poles, 1)
    subplot.plot(w/(2*math.pi), np.angle(h), color='blue')
    subplot.set_title('Phase Response')
    subplot.set_ylabel('Phase [rad]')
    subplot.set_xlabel('Frequency [f]')

def plot_impulse_response(poles, zeros, subplot):
    lti = signal.dlti(zeros, poles, 1)
    t, y = signal.dimpulse(lti, n=10)
    y = y[0]
    subplot.plot(np.array([0, 0]), np.array([min(1.2 * min(y), 0), max(1.2 * max(y), 0)]), color='gray', zorder=0)
    subplot.plot(np.array([0, t[-1]]), np.array([0, 0]), color='gray', zorder=0)
    subplot.set_title('Impulse Response')
    subplot.set_xlabel('Index n')
    subplot.set_ylabel('h(n)')
    for i in range(len(t)):
        subplot.scatter(t[i], y[i], color='blue')
        subplot.plot(np.array([t[i], t[i]]), np.array([0, y[i]]), color='blue')

if __name__ == '__main__':
    poz = PolesAndZeros('poles_and_zeros.txt')
    fig, subplots = plt.subplots(nrows=2, ncols=2)
    fig.tight_layout(pad=4)
    plot_argument(poz.poles, poz.zeros, subplots[0,0])
    plot_amplitude(poz.poles, poz.zeros, subplots[0,1])
    plot_impulse_response(poz.poles, poz.zeros, subplots[1,0])
    plot_poles_zeros.plot_poles_zeros(poz.poles, poz.zeros, subplots[1,1])
    plt.show()
