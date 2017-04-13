import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def plot_BPT_ell(cov, means, ax, col):
    """ Plot confidences interval at 68% and 95% (1 and 2 sigmas)
    in the BPT diagram.
    """
    v, w = np.linalg.eigh(cov[:2,:2])
    u = w[0] / np.linalg.norm(w[0])
    angle = np.arctan2(u[1], u[0])
    angle = 180 * angle / np.pi  # convert to degrees
    norm_1s = 2 * np.sqrt(2*v)
    norm_2s = 4 * np.sqrt(2*v)

    ell_2s = mpl.patches.Ellipse(xy=means[:2], width=norm_2s[0], height=norm_2s[1],
                                 angle=angle, color=col)
    ell_2s.set_clip_box(ax.bbox)
    ell_2s.set_alpha(0.15)
    ax.add_artist(ell_2s)
    ell_1s = mpl.patches.Ellipse(xy=means[:2], width=norm_1s[0], height=norm_1s[1],
                                 angle=angle, color=col)
    ell_1s.set_clip_box(ax.bbox)
    ell_1s.set_alpha(0.7)
    ax.add_artist(ell_1s)
    
def plot_WHAN_ell(cov, means, ax, col):
    """ Plot confidences interval at 68% and 95% (1 and 2 sigmas)
    in the WHAN diagram.
    """
    v, w = np.linalg.eigh(cov[0:3:2,0:3:2])
    u = w[0] / np.linalg.norm(w[0])
    angle = np.arctan2(u[1], u[0])
    angle = 180 * angle / np.pi  # convert to degrees
    norm_1s = 2 * np.sqrt(2*v)
    norm_2s = 4 * np.sqrt(2*v)
    
    ell_2s = mpl.patches.Ellipse(xy=means[0:3:2], width=norm_2s[0], height=norm_2s[1],
                                 angle=angle, color=col)
    ell_2s.set_clip_box(ax.bbox)
    ell_2s.set_alpha(0.15)
    ax.add_artist(ell_2s)
    ell_1s = mpl.patches.Ellipse(xy=means[0:3:2], width=norm_1s[0], height=norm_1s[1],
                                 angle=angle, color=col)
    ell_1s.set_clip_box(ax.bbox)
    ell_1s.set_alpha(0.7)
    ax.add_artist(ell_1s)


def set_plt_style():

    plt.subplot(121)
    plt.xlim(-1.5,1.25)
    plt.ylim(-1.5,1.6)
    plt.xlabel(r'$\log([\rm NII]/H\alpha)$', fontsize=18)
    plt.ylabel(r'$\log([\rm OIII]/H\beta)$', fontsize=18)
    plt.title('BPT Diagram', fontsize=20)

    plt.subplot(122)
    plt.xlim(-1.5,1.25)
    plt.ylim(-1.1,3.05)
    plt.xlabel(r'$\log([\rm NII]/H\alpha)$', fontsize=18)
    plt.ylabel(r'$\log(\rm W_{H\alpha})$', fontsize=18)
    plt.title('WHAN Diagram', fontsize=20)


def lda_bpt_plt_style():

    plt.subplot(3,4,1)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group1'], fontsize=10, loc=2)

    plt.subplot(3,4,2)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group2'], fontsize=10, loc=2)

    plt.subplot(3,4,3)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group3'], fontsize=10, loc=2)

    plt.subplot(3,4,4)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group4'], fontsize=10, loc=2)

    plt.subplot(3,4,5)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['Comp.','group1'], fontsize=10, loc=2)

    plt.subplot(3,4,6)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['Comp.','group2'], fontsize=10, loc=2)

    plt.subplot(3,4,7)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['Comp.','group3'], fontsize=10, loc=2)

    plt.subplot(3,4,8)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['Comp.','group4'], fontsize=10, loc=2)

    plt.subplot(3,4,9)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['AGN','group1'], fontsize=10, loc=2)

    plt.subplot(3,4,10)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['AGN','group2'], fontsize=10, loc=2)

    plt.subplot(3,4,11)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['AGN','group3'], fontsize=10, loc=2)

    plt.subplot(3,4,12)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['AGN','group4'], fontsize=10, loc=2)


def lda_whan_plt_style():
    
    plt.subplot(4,4,1)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group1'], fontsize=10, loc=2)

    plt.subplot(4,4,2)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group2'], fontsize=10, loc=2)

    plt.subplot(4,4,3)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group3'], fontsize=10, loc=2)

    plt.subplot(4,4,4)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['SF','group4'], fontsize=10, loc=2)

    plt.subplot(4,4,5)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['sAGN','group1'], fontsize=10, loc=2)

    plt.subplot(4,4,6)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['sAGN','group2'], fontsize=10, loc=2)

    plt.subplot(4,4,7)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['sAGN','group3'], fontsize=10, loc=2)

    plt.subplot(4,4,8)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['sAGN','group4'], fontsize=10, loc=2)

    plt.subplot(4,4,9)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['wAGN','group1'], fontsize=10, loc=2)

    plt.subplot(4,4,10)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['wAGN','group2'], fontsize=10, loc=2)

    plt.subplot(4,4,11)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['wAGN','group3'], fontsize=10, loc=2)

    plt.subplot(4,4,12)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['wAGN','group4'], fontsize=10, loc=2)

    plt.subplot(4,4,13)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['retired','group1'], fontsize=10, loc=2)

    plt.subplot(4,4,14)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['retired','group2'], fontsize=10, loc=2)

    plt.subplot(4,4,15)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['retired','group3'], fontsize=10, loc=2)

    plt.subplot(4,4,16)
    plt.xlim(-15,15)
    plt.ylim(0.0,0.8)
    plt.legend(['retired','group4'], fontsize=10, loc=2)

