import kq1
from pymc import MCMC, AdaptiveMetropolis, Matplot
from pylab import *

HISTORICAL, CONCURRENT = 0,1

iterations = 1000000
burn = 900000
thin = 10

hmod = kq1.generate_model(HISTORICAL)
cmod = kq1.generate_model(CONCURRENT)

H = MCMC(hmod, db="pickle", dbname="historical_model.pickle")

H.sample(iterations, burn, thin=thin, verbose=2)

C = MCMC(cmod, db="pickle", dbname="concurrent_model.pickle")

C.sample(iterations, burn, thin=thin, verbose=2)

conc = np.sum(C.trace("pred")[:], 0)/float((iterations-burn)/thin)
historical = np.sum(H.trace("pred")[:], 0)/float((iterations-burn)/thin)

x = np.arange(200,3200, 200)

colors = ('0.7', 'black')
markers = (False, True)

for i,p in enumerate((70,85)):
    plot(x, conc[i*-1][C.crit_pred==1], color=colors[i], marker='^'*markers[i])
    plot(x, historical[i*-1][H.crit_pred==1], color=colors[i], marker='o'*markers[i])
    plot(x, conc[i*-1][C.crit_pred==0], color=colors[i], marker='^'*markers[i], linestyle="dashed")
    plot(x, historical[i*-1][H.crit_pred==0], color=colors[i], marker='o'*markers[i], linestyle="dashed")
xlim(150, 3050)
ylim(0,1)

xlabel("Phe ($\mu$mol/L)")
ylabel("Pr(IQ < threshold)")
text(1400, 0.9, "critical period, historical", fontsize=12)
text(1700, 0.55, "non-critical period, historical", fontsize=12)
text(2000, 0.41, "non-critical period, concurrent", fontsize=12)
text(2000, 0.17, "critical period, concurrent", fontsize=12)