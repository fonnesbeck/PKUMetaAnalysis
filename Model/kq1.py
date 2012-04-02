from get_kq1_data import *
from pymc import Normal, Uniform, Lambda, deterministic, stochastic, normal_like, potential, MvNormal, rtruncated_normal, rnormal, Uninformative
import numpy as np

def generate_model(subset = CONCURRENT):
    """Generate a model for a given subset of data"""

    data = get_data(subset)

    obs_indiv = data["obs_indiv"]
    obs_summ = data["obs_summ"]

    # =========================
    # = Individual-level data =
    # =========================

    if subset is HISTORICAL:
        # Impute Phe for individuals with only range given
        phe_isnan = np.isnan(obs_indiv['phe'])
        phe_low_missing = obs_indiv['phe_low'][phe_isnan]
        phe_high_missing = obs_indiv['phe_high'][phe_isnan]
        phe_missing = Uniform('phe_missing', lower=phe_low_missing, upper=phe_high_missing, plot=False)

    else:
        phe_missing = None

    # Study unit random effect for intercept

    # Mean intercept
    mu_int = Normal('mu_int', mu=100, tau=0.01, value=100)
    # SD of intercepts
    sigma_int = Uniform('sigma_int', lower=0, upper=100, value=10.)
    tau_int = Lambda('tau_int', lambda s=sigma_int: s**-2)
    # Intecepts by study
    beta0 = Normal('beta0', mu=mu_int, tau=tau_int, value=np.zeros(len(data["unique_papers"])))

    # Study unit random effect for slope

    # Mean slope
    mu_slope = Normal('mu_slope', mu=0, tau=0.1, value=-0.01)
    # SD of slopes
    sigma_slope = Uniform('sigma_slope', lower=0, upper=10, value=1.)
    tau_slope = Lambda('tau_slope', lambda s=sigma_slope: s**-2)

    # Random slopes by study
    alpha0 = Normal('alpha0', mu=mu_slope, tau=tau_slope, value=np.zeros(len(data["unique_papers"])))
    alpha1 = Normal('alpha1', mu=0, tau=0.01, value=0.0)

    @deterministic
    def beta1_indiv(a0=alpha0, a1=alpha1, crit=obs_indiv['critical_period']):
        """Calculate Phe effect (slope) for each individual"""
        return a0[data["paper_id_indiv"]] + a1*crit

    @deterministic
    def mu_iq(b0=beta0, b1=beta1_indiv, phe=obs_indiv['phe'], phe_m=phe_missing):
        """Expected IQ"""

        if subset is HISTORICAL:
            # Insert values for missing phe
            phe[phe_isnan] = phe_m

        return b0[data["paper_id_indiv"]] + b1*phe

    # Process noise (variance of observations about predicted mean)
    sigma_iq = Uniform('sigma_iq', lower=0, upper=100, value=1)
    tau_iq = Lambda('tau_iq', lambda s=sigma_iq: s**-2)

    # Data likelihood
    iq_like = Normal('iq_like', mu=mu_iq, tau=tau_iq, value=obs_indiv['iq'], observed=True)

    @deterministic
    def iq_pred(mu=mu_iq, tau=tau_iq):
        """Simulated data for posterior predictive checks"""
        return rnormal(mu, tau, size=len(obs_indiv['iq']))

    # ====================================================
    # = Infer slope from correlations of summarized data =
    # ====================================================

    # Means and stdevs of phe and IQ
    stdev_phe = obs_summ['phe_sd']
    stdev_iq = obs_summ['iq_sd']
    mean_phe = obs_summ['phe']
    mean_iq = obs_summ['iq']

    @deterministic(cache_depth=0)
    def beta1_summ(a0=alpha0, a1=alpha1, crit=obs_summ['critical_period']):
        """Calculate mean of slope for summarized data"""
        return a0[data["paper_id_summ"]] + a1*crit

    @potential
    def r_like(b1=beta1_summ, n=obs_summ['n']):
        """Likelihood for correlation coefficients of summarized data"""
        # Convert slope to r
        rho = b1*stdev_phe/stdev_iq

        # Fisher transformation to allow for normality assumption
        eps = np.arctan(rho) - np.arctan(obs_summ['correlation'])
        # Difference should be mean-zero
        return normal_like(eps, mu=np.zeros(len(n)), tau=n-3)


    # Calculate probabilites of IQ<85

    # Generate combinations of predictors
    crit_pred, phe_pred = np.transpose([[crit, phe] for crit in [0,1] for phe in np.arange(200,3200, 200)])

    @deterministic(cache_depth=0)
    def pred(a1=alpha1, mu_int=mu_int, tau_int=tau_int, mu_slope=mu_slope, tau_slope=tau_slope, tau_iq=tau_iq, values=(70,75,80,85)):
        """Estimate the probability of IQ<85 for different covariate values"""
        b0 = rnormal(mu_int, tau_int, size=len(phe_pred))
        a0 = rnormal(mu_slope, tau_slope, size=len(phe_pred))

        b1 = a0 + a1*crit_pred

        iq = rnormal(b0 + b1*phe_pred, tau_iq)

        return [iq<v for v in values]

    return locals()
