import numpy as np
from matplotlib import animation, pyplot as plt

plt.rc('animation', html='jshtml')

class traceplot:
    def __init__(self, fig, axes, sample, nframes=200, nbins=25):
        self.sample = sample
        self.axes = axes
        self.axes[0].clear()
        self.axes[1].clear()
        self.fig = fig
        self.nframes = nframes
        self.nbins = nbins
        N = np.size(sample)
        self.N = N
        self.xrange = np.arange(N)
        blim = round(max(sample)*1.15)
        alim = round(min(sample)*1.15)
        self.blim = blim
        self.alim = alim
        line, = self.axes[1].plot([], [])
        self.line = line
        self.anim = animation.FuncAnimation(fig, self.update, init_func=self.initanim, frames=nframes, interval=40)
        
    def initanim(self):
        self.axes[0].clear()
        #fig, axs = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 4]}, figsize=(16, 4))
        self.axes[0].set_title('Гистограмма')
        self.axes[0].yaxis.tick_right()
        self.axes[0].get_xaxis().set_visible(False)
        self.axes[0].invert_xaxis()
        self.axes[1].set_title('Trace plot')
        self.axes[1].set_ylabel(r'$\theta$')
        self.axes[1].set_xlim((0, self.N))
        self.axes[0].set_ylim((self.alim, self.blim))
        self.axes[1].set_ylim((self.alim, self.blim))
        self.fig.tight_layout()
        self.axes[0].hist([])
        self.line.set_data([], [])
        return self.line
    
    def update(self, i):
        step = int(self.N / self.nframes)
        self.axes[0].clear()
        self.axes[0].set_title('Гистограмма')
        self.axes[0].hist(self.sample[:i*step], orientation='horizontal', bins=(np.arange(self.nbins+1) / self.nbins * (self.blim - self.alim) + self.alim))
        self.axes[0].set_ylim((self.alim, self.blim))
        self.axes[0].invert_xaxis()
        self.line.set_data(self.xrange[:i*step], self.sample[:i*step])
        return self.line,
