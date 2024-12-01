import scipy.stats as sps

#Define the parameters and upper limits
mu_ = 3.0
sigma_ = 0.3
beta_ = 1.0
m_ = 1.4
f_ = 0.6
lmbda_ = 0.3
mu_b_ = 0.0
sigma_b_ = 2.5

#define upper and lower limits
X_ulim_ = 5.0
X_llim_ = 0.0
Y_ulim_ = 10.0
Y_llim_ = 0.0

#define the functions using scipy stats
def g_s(X, beta = beta_, m = m_, mu = mu_, sigma = sigma_, X_ulim = X_ulim_, X_llim = X_llim_):
    return sps.crystalball.pdf(X, beta, m, mu, sigma) / (sps.crystalball.cdf(X_ulim, beta, m, mu, sigma) - sps.crystalball.cdf(X_llim, beta, m, mu, sigma))

def h_s(Y, Y_ulim = Y_ulim_, Y_llim = Y_llim_, lmbda = lmbda_):
    trunc_b = (Y_ulim - Y_llim)*lmbda
    return sps.truncexpon.pdf(Y, trunc_b, Y_llim, 1/lmbda)

def g_b(X, X_ulim =  X_ulim_, X_llim = X_llim_):
    return sps.uniform.pdf(X, X_llim, X_ulim)

def h_b(Y, mu_b = mu_b_, sigma_b = sigma_b_, Y_ulim = Y_ulim_, Y_llim = Y_llim_):
    a = (mu_b - Y_llim)/sigma_b
    b = (Y_ulim - mu_b)/sigma_b
    return sps.truncnorm.pdf(Y, a, b, mu_b, sigma_b)

def p_X(x, f = f_):
    return (1-f) * g_b(x) + f * g_s(x)

def p_Y(y, f = f_):
    return (1-f) * h_b(y) + f * h_s(y)