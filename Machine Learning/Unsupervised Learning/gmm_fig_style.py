import matplotlib.pyplot as plt


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


def lba_bpt_plt_style():

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


def lba_whan_plt_style():
    
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

