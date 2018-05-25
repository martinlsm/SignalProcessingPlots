import numpy as np
import matplotlib.pyplot as plt
import math

unity_xs = np.array([math.cos(x) for x in np.linspace(0, 2 * math.pi, 1000)])
unity_ys = np.array([math.sin(y) for y in np.linspace(0, 2 * math.pi, 1000)])

def plot_poles_zeros(poles, zeros, subplot):
    subplot.axis('equal')
    subplot.plot(unity_xs, unity_ys, color='gray', linestyle='--', zorder=0)
    subplot.plot(np.array([-1,1]), np.array([0,0]), color='gray', zorder=0)
    subplot.plot(np.array([0,0]), np.array([-1,1]), color='gray', zorder=0)
    subplot.set_title('Pole/zero plot')
    subplot.set_xlabel('real(z)')
    subplot.set_ylabel('imag(z)')
    for p in poles:
        subplot.scatter(p.real, p.imag, marker='x', color='red')
    for z in zeros:
        subplot.scatter(z.real, z.imag, marker='o', color='blue',zorder=5)
        subplot.scatter(z.real, z.imag, marker='.', color='white',zorder=10)
