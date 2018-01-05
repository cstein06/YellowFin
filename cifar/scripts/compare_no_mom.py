import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def compare_losses(niter = 50, log_dir='../results/'):
  def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / N

  plt.figure()

  losses = np.loadtxt(log_dir+'with_mom/loss_full.txt')
  plt.semilogy(range(0,len(losses),30),losses[::30], 'r.', alpha=0.1)
  plt.semilogy(running_mean(losses,300), 'r', lw=2, alpha=0.5, label="With momentum")

  losses = np.loadtxt(log_dir+'no_mom/loss_full.txt')
  plt.semilogy(range(0,len(losses),30),losses[::30], 'b.', alpha=0.1)
  plt.semilogy(running_mean(losses,300), 'b', lw=2, alpha=0.5, label="No momentum")

  plt.xlabel('Iterations')
  plt.ylabel('Loss')
  plt.legend()
  plt.grid()
  ax = plt.subplot(111)
  ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
        ncol=3, fancybox=True, shadow=True)

  #plt.savefig(log_dir + "/compare_losses_" + str(niter) + ".pdf")
  plt.savefig(log_dir + "/compare_losses.pdf")
  print "figure plotted"

  #plt.close()
  plt.show()

if __name__ == "__main__":
  compare_losses()