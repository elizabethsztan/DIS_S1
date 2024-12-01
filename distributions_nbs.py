from numba_stats import crystalball, truncexpon, uniform, truncnorm
from numba import njit, float64
import numpy as np

"""
Store of background and signal PDFs for X and Y.
Unlike the distributions.py store, these functions are optimised using numba for quicker sampling
and optmisation.

"""

@njit(float64(float64, float64, float64, float64, float64, float64, float64))
def g_s_nb(X, beta, m, mu, sigma, X_llim, X_ulim):
    """
    Signal PDF for X - truncated crystal ball

    Args:
        X (float64): _description_
        beta (float64): _description_
        m (float64): _description_
        mu (float64): _description_
        sigma (float64): _description_
        X_llim (float64): _description_
        X_ulim (float64): _description_

    Returns:
        float64: _description_
    """
    return crystalball.pdf(np.array([X], dtype=np.float64), beta, m, mu, sigma)[0] / (
       crystalball.cdf(np.array([X_ulim], dtype=np.float64), beta, m, mu, sigma)[0] 
       - crystalball.cdf(np.array([X_llim], dtype=np.float64), beta, m, mu, sigma)[0])

@njit(float64[:](float64[:], float64, float64, float64, float64, float64, float64))
def g_s_nb_(X_array, beta, m, mu, sigma, X_llim, X_ulim):
   result = np.zeros_like(X_array)
   for i in range(len(X_array)):
       result[i] = g_s_nb(X_array[i], beta, m, mu, sigma, X_llim, X_ulim)
   return result

@njit(float64(float64, float64, float64, float64))
def h_s_nb(Y, lmbda, Y_llim, Y_ulim):
   if Y <= Y_ulim and Y >= Y_llim:
       return truncexpon.pdf(np.array([Y], dtype=np.float64), Y_llim-1e-10, Y_ulim+1e-10, 0.0, 1/lmbda)[0]
   return 0.0

@njit(float64[:](float64[:], float64, float64, float64))
def h_s_nb_(Y_array, lmbda, Y_llim, Y_ulim):
   result = np.zeros_like(Y_array)
   for i in range(len(Y_array)):
       result[i] = h_s_nb(Y_array[i], lmbda, Y_llim, Y_ulim)
   return result

@njit(float64(float64, float64, float64))
def g_b_nb(X, X_llim, X_ulim):
   return uniform.pdf(np.array([X], dtype=np.float64), X_llim, X_ulim-X_llim)[0]

@njit(float64[:](float64[:], float64, float64))
def g_b_nb_(X_array, X_llim, X_ulim):
   result = np.zeros_like(X_array)
   for i in range(len(X_array)):
       result[i] = g_b_nb(X_array[i], X_llim, X_ulim)
   return result

@njit(float64(float64, float64, float64, float64, float64))
def h_b_nb(Y, mu_b, sigma_b, Y_llim, Y_ulim):
   if Y <= Y_ulim and Y >= Y_llim:
       return truncnorm.pdf(np.array([Y], dtype=np.float64), Y_llim-1e-10, Y_ulim+1e-10, mu_b, sigma_b)[0]
   return 0.0

@njit(float64[:](float64[:], float64, float64, float64, float64))
def h_b_nb_(Y_array, mu_b, sigma_b, Y_llim, Y_ulim):
   result = np.zeros_like(Y_array)
   for i in range(len(Y_array)):
       result[i] = h_b_nb(Y_array[i], mu_b, sigma_b, Y_llim, Y_ulim)
   return result