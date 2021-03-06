"""
This type stub file was generated by pyright.
"""

from scipy._lib.doccer import extend_notes_in_docstring, replace_notes_in_docstring
from ._distn_infrastructure import rv_continuous

class ksone_gen(rv_continuous):
    r"""Kolmogorov-Smirnov one-sided tes"""
    ...


ksone = ...
class kstwo_gen(rv_continuous):
    r"""Kolmogorov-Smirnov two-sided tes"""
    ...


kstwo = ...
class kstwobign_gen(rv_continuous):
    r"""Limiting distribution of scaled """
    ...


kstwobign = ...
_norm_pdf_C = ...
_norm_pdf_logC = ...
class norm_gen(rv_continuous):
    r"""A normal continuous random varia"""
    @_call_super_mom
    @replace_notes_in_docstring(rv_continuous, notes="""\
        For the normal distrib""")
    def fit(self, data, **kwds): # -> tuple[Any | Unknown, Any | Unknown]:
        ...
    


norm = ...
class alpha_gen(rv_continuous):
    r"""An alpha continuous random varia"""
    _support_mask = ...


alpha = ...
class anglit_gen(rv_continuous):
    r"""An anglit continuous random vari"""
    ...


anglit = ...
class arcsine_gen(rv_continuous):
    r"""An arcsine continuous random var"""
    ...


arcsine = ...
class FitDataError(ValueError):
    def __init__(self, distr, lower, upper) -> None:
        ...
    


class FitSolverError(RuntimeError):
    def __init__(self, mesg) -> None:
        ...
    


class beta_gen(rv_continuous):
    r"""A beta continuous random variabl"""
    @_call_super_mom
    @extend_notes_in_docstring(rv_continuous, notes="""\
        In the special case wh""")
    def fit(self, data, *args, **kwds):
        ...
    


beta = ...
class betaprime_gen(rv_continuous):
    r"""A beta prime continuous random v"""
    _support_mask = ...


betaprime = ...
class bradford_gen(rv_continuous):
    r"""A Bradford continuous random var"""
    ...


bradford = ...
class burr_gen(rv_continuous):
    r"""A Burr (Type III) continuous ran"""
    ...


burr = ...
class burr12_gen(rv_continuous):
    r"""A Burr (Type XII) continuous ran"""
    ...


burr12 = ...
class fisk_gen(burr_gen):
    r"""A Fisk continuous random variabl"""
    ...


fisk = ...
class cauchy_gen(rv_continuous):
    r"""A Cauchy continuous random varia"""
    ...


cauchy = ...
class chi_gen(rv_continuous):
    r"""A chi continuous random variable"""
    ...


chi = ...
class chi2_gen(rv_continuous):
    r"""A chi-squared continuous random """
    ...


chi2 = ...
class cosine_gen(rv_continuous):
    r"""A cosine continuous random varia"""
    ...


cosine = ...
class dgamma_gen(rv_continuous):
    r"""A double gamma continuous random"""
    ...


dgamma = ...
class dweibull_gen(rv_continuous):
    r"""A double Weibull continuous rand"""
    ...


dweibull = ...
class expon_gen(rv_continuous):
    r"""An exponential continuous random"""
    @_call_super_mom
    @replace_notes_in_docstring(rv_continuous, notes="""\
        When `method='MLE'`,
 """)
    def fit(self, data, *args, **kwds): # -> tuple[float, float]:
        ...
    


expon = ...
class exponnorm_gen(rv_continuous):
    r"""An exponentially modified Normal"""
    ...


exponnorm = ...
class exponweib_gen(rv_continuous):
    r"""An exponentiated Weibull continu"""
    ...


exponweib = ...
class exponpow_gen(rv_continuous):
    r"""An exponential power continuous """
    ...


exponpow = ...
class fatiguelife_gen(rv_continuous):
    r"""A fatigue-life (Birnbaum-Saunder"""
    _support_mask = ...


fatiguelife = ...
class foldcauchy_gen(rv_continuous):
    r"""A folded Cauchy continuous rando"""
    ...


foldcauchy = ...
class f_gen(rv_continuous):
    r"""An F continuous random variable."""
    ...


f = ...
class foldnorm_gen(rv_continuous):
    r"""A folded normal continuous rando"""
    ...


foldnorm = ...
class weibull_min_gen(rv_continuous):
    r"""Weibull minimum continuous rando"""
    ...


weibull_min = ...
class weibull_max_gen(rv_continuous):
    r"""Weibull maximum continuous rando"""
    ...


weibull_max = ...
class genlogistic_gen(rv_continuous):
    r"""A generalized logistic continuou"""
    ...


genlogistic = ...
class genpareto_gen(rv_continuous):
    r"""A generalized Pareto continuous """
    ...


genpareto = ...
class genexpon_gen(rv_continuous):
    r"""A generalized exponential contin"""
    ...


genexpon = ...
class genextreme_gen(rv_continuous):
    r"""A generalized extreme value cont"""
    ...


genextreme = ...
class gamma_gen(rv_continuous):
    r"""A gamma continuous random variab"""
    @extend_notes_in_docstring(rv_continuous, notes="""\
        When the location is f""")
    def fit(self, data, *args, **kwds):
        ...
    


gamma = ...
class erlang_gen(gamma_gen):
    """An Erlang continuous random vari"""
    def fit(self, data, *args, **kwds):
        ...
    
    if fit.__doc__:
        ...


erlang = ...
class gengamma_gen(rv_continuous):
    r"""A generalized gamma continuous r"""
    ...


gengamma = ...
class genhalflogistic_gen(rv_continuous):
    r"""A generalized half-logistic cont"""
    ...


genhalflogistic = ...
class genhyperbolic_gen(rv_continuous):
    r"""A generalized hyperbolic continu"""
    ...


genhyperbolic = ...
class gompertz_gen(rv_continuous):
    r"""A Gompertz (or truncated Gumbel)"""
    ...


gompertz = ...
class gumbel_r_gen(rv_continuous):
    r"""A right-skewed Gumbel continuous"""
    @_call_super_mom
    def fit(self, data, *args, **kwds): # -> tuple[Unknown, ...] | tuple[Unknown, Unknown]:
        ...
    


gumbel_r = ...
class gumbel_l_gen(rv_continuous):
    r"""A left-skewed Gumbel continuous """
    @_call_super_mom
    def fit(self, data, *args, **kwds): # -> tuple[Unknown, Unknown]:
        ...
    


gumbel_l = ...
class halfcauchy_gen(rv_continuous):
    r"""A Half-Cauchy continuous random """
    ...


halfcauchy = ...
class halflogistic_gen(rv_continuous):
    r"""A half-logistic continuous rando"""
    ...


halflogistic = ...
class halfnorm_gen(rv_continuous):
    r"""A half-normal continuous random """
    ...


halfnorm = ...
class hypsecant_gen(rv_continuous):
    r"""A hyperbolic secant continuous r"""
    ...


hypsecant = ...
class gausshyper_gen(rv_continuous):
    r"""A Gauss hypergeometric continuou"""
    ...


gausshyper = ...
class invgamma_gen(rv_continuous):
    r"""An inverted gamma continuous ran"""
    _support_mask = ...


invgamma = ...
class invgauss_gen(rv_continuous):
    r"""An inverse Gaussian continuous r"""
    _support_mask = ...
    def fit(self, data, *args, **kwds): # -> tuple[Unknown, ...] | tuple[Any | Unknown, Unknown, Any | Unknown]:
        ...
    


invgauss = ...
class geninvgauss_gen(rv_continuous):
    r"""A Generalized Inverse Gaussian c"""
    ...


geninvgauss = ...
class norminvgauss_gen(rv_continuous):
    r"""A Normal Inverse Gaussian contin"""
    _support_mask = ...


norminvgauss = ...
class invweibull_gen(rv_continuous):
    u"""An inverted Weibull continuous r"""
    _support_mask = ...


invweibull = ...
class johnsonsb_gen(rv_continuous):
    r"""A Johnson SB continuous random v"""
    _support_mask = ...


johnsonsb = ...
class johnsonsu_gen(rv_continuous):
    r"""A Johnson SU continuous random v"""
    ...


johnsonsu = ...
class laplace_gen(rv_continuous):
    r"""A Laplace continuous random vari"""
    @_call_super_mom
    @replace_notes_in_docstring(rv_continuous, notes="""\
        This function uses exp""")
    def fit(self, data, *args, **kwds): # -> tuple[Unknown, Any | Unknown]:
        ...
    


laplace = ...
class laplace_asymmetric_gen(rv_continuous):
    r"""An asymmetric Laplace continuous"""
    ...


laplace_asymmetric = ...
class levy_gen(rv_continuous):
    r"""A Levy continuous random variabl"""
    _support_mask = ...


levy = ...
class levy_l_gen(rv_continuous):
    r"""A left-skewed Levy continuous ra"""
    _support_mask = ...


levy_l = ...
class levy_stable_gen(rv_continuous):
    r"""A Levy-stable continuous random """
    ...


levy_stable = ...
class logistic_gen(rv_continuous):
    r"""A logistic (or Sech-squared) con"""
    @_call_super_mom
    def fit(self, data, *args, **kwds): # -> tuple[Unknown, ...]:
        ...
    


logistic = ...
class loggamma_gen(rv_continuous):
    r"""A log gamma continuous random va"""
    ...


loggamma = ...
class loglaplace_gen(rv_continuous):
    r"""A log-Laplace continuous random """
    ...


loglaplace = ...
class lognorm_gen(rv_continuous):
    r"""A lognormal continuous random va"""
    _support_mask = ...
    @_call_super_mom
    @extend_notes_in_docstring(rv_continuous, notes="""\
        When `method='MLE'` an""")
    def fit(self, data, *args, **kwds):
        ...
    


lognorm = ...
class gilbrat_gen(rv_continuous):
    r"""A Gilbrat continuous random vari"""
    _support_mask = ...


gilbrat = ...
class maxwell_gen(rv_continuous):
    r"""A Maxwell continuous random vari"""
    ...


maxwell = ...
class mielke_gen(rv_continuous):
    r"""A Mielke Beta-Kappa / Dagum cont"""
    ...


mielke = ...
class kappa4_gen(rv_continuous):
    r"""Kappa 4 parameter distribution.
"""
    ...


kappa4 = ...
class kappa3_gen(rv_continuous):
    r"""Kappa 3 parameter distribution.
"""
    ...


kappa3 = ...
class moyal_gen(rv_continuous):
    r"""A Moyal continuous random variab"""
    ...


moyal = ...
class nakagami_gen(rv_continuous):
    r"""A Nakagami continuous random var"""
    ...


nakagami = ...
class ncx2_gen(rv_continuous):
    r"""A non-central chi-squared contin"""
    ...


ncx2 = ...
class ncf_gen(rv_continuous):
    r"""A non-central F distribution con"""
    ...


ncf = ...
class t_gen(rv_continuous):
    r"""A Student's t continuous random """
    ...


t = ...
class nct_gen(rv_continuous):
    r"""A non-central Student's t contin"""
    ...


nct = ...
class pareto_gen(rv_continuous):
    r"""A Pareto continuous random varia"""
    @_call_super_mom
    def fit(self, data, *args, **kwds): # -> tuple[Unknown, ...] | tuple[Any | Unknown, Unknown, Unknown]:
        ...
    


pareto = ...
class lomax_gen(rv_continuous):
    r"""A Lomax (Pareto of the second ki"""
    ...


lomax = ...
class pearson3_gen(rv_continuous):
    r"""A pearson type III continuous ra"""
    @_call_super_mom
    @extend_notes_in_docstring(rv_continuous, notes="""\
        Note that method of mo""")
    def fit(self, data, *args, **kwds):
        ...
    


pearson3 = ...
class powerlaw_gen(rv_continuous):
    r"""A power-function continuous rand"""
    ...


powerlaw = ...
class powerlognorm_gen(rv_continuous):
    r"""A power log-normal continuous ra"""
    _support_mask = ...


powerlognorm = ...
class powernorm_gen(rv_continuous):
    r"""A power normal continuous random"""
    ...


powernorm = ...
class rdist_gen(rv_continuous):
    r"""An R-distributed (symmetric beta"""
    ...


rdist = ...
class rayleigh_gen(rv_continuous):
    r"""A Rayleigh continuous random var"""
    _support_mask = ...
    @_call_super_mom
    @extend_notes_in_docstring(rv_continuous, notes="""\
        Notes specifically for""")
    def fit(self, data, *args, **kwds): # -> tuple[Unknown, Any] | tuple[Unknown, Unknown]:
        ...
    


rayleigh = ...
class reciprocal_gen(rv_continuous):
    r"""A loguniform or reciprocal conti"""
    ...


loguniform = ...
reciprocal = ...
class rice_gen(rv_continuous):
    r"""A Rice continuous random variabl"""
    ...


rice = ...
class recipinvgauss_gen(rv_continuous):
    r"""A reciprocal inverse Gaussian co"""
    ...


recipinvgauss = ...
class semicircular_gen(rv_continuous):
    r"""A semicircular continuous random"""
    ...


semicircular = ...
class skewcauchy_gen(rv_continuous):
    r"""A skewed Cauchy random variable."""
    ...


skewcauchy = ...
class skew_norm_gen(rv_continuous):
    r"""A skew-normal random variable.

"""
    ...


skewnorm = ...
class trapezoid_gen(rv_continuous):
    r"""A trapezoidal continuous random """
    ...


trapezoid = ...
trapz = ...
if trapz.__doc__:
    ...
class triang_gen(rv_continuous):
    r"""A triangular continuous random v"""
    ...


triang = ...
class truncexpon_gen(rv_continuous):
    r"""A truncated exponential continuo"""
    ...


truncexpon = ...
TRUNCNORM_TAIL_X = ...
TRUNCNORM_MAX_BRENT_ITERS = ...
class truncnorm_gen(rv_continuous):
    r"""A truncated normal continuous ra"""
    ...


truncnorm = ...
class tukeylambda_gen(rv_continuous):
    r"""A Tukey-Lamdba continuous random"""
    ...


tukeylambda = ...
class FitUniformFixedScaleDataError(FitDataError):
    def __init__(self, ptp, fscale) -> None:
        ...
    


class uniform_gen(rv_continuous):
    r"""A uniform continuous random vari"""
    @_call_super_mom
    def fit(self, data, *args, **kwds): # -> tuple[float, float]:
        """
        Maximum likelihood esti"""
        ...
    


uniform = ...
class vonmises_gen(rv_continuous):
    r"""A Von Mises continuous random va"""
    ...


vonmises = ...
vonmises_line = ...
class wald_gen(invgauss_gen):
    r"""A Wald continuous random variabl"""
    _support_mask = ...


wald = ...
class wrapcauchy_gen(rv_continuous):
    r"""A wrapped Cauchy continuous rand"""
    ...


wrapcauchy = ...
class gennorm_gen(rv_continuous):
    r"""A generalized normal continuous """
    ...


gennorm = ...
class halfgennorm_gen(rv_continuous):
    r"""The upper half of a generalized """
    ...


halfgennorm = ...
class crystalball_gen(rv_continuous):
    r"""
    Crystalball distribution

 """
    ...


crystalball = ...
class argus_gen(rv_continuous):
    r"""
    Argus distribution

    %(b"""
    ...


argus = ...
class rv_histogram(rv_continuous):
    """
    Generates a distribution gi"""
    _support_mask = ...
    def __init__(self, histogram, *args, **kwargs) -> None:
        """
        Create a new distributi"""
        ...
    


class studentized_range_gen(rv_continuous):
    r"""A studentized range continuous r"""
    ...


studentized_range = ...
pairs = ...
__all__ = _distn_names + _distn_gen_names + ['rv_histogram']
