import kq1
from pymc import *

HISTORICAL, CONCURRENT = 0,1

db_hist = database.pickle.load('historical_model.pickle')
hmod = kq1.generate_model(HISTORICAL)
H = MCMC(hmod, db=db_hist)

db_conc = database.pickle.load('concurrent_model.pickle')
cmod = kq1.generate_model(CONCURRENT)
C = MCMC(cmod, db=db_conc)

