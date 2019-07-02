# Load libraries
import pandas as pd
import numpy as np
# %matplotlib notebook
import matplotlib.pylab as plt
from statsmodels.tsa.stattools import adfuller
# from statsmodels.tsa.seasonal import seasonal_decompose
# from statsmodels.tsa.arima_model import ARIMA
import warnings

warnings.filterwarnings('ignore')


## Definitions of selected functions

# Test stationarity
def test_stationarity(timeseries, figsizeIn):
    # Determing rolling statistics
    rolmean = timeseries.rolling(window=12).mean()  # rolling_mean(timeseries, window=12)
    rolstd = timeseries.rolling(window=12).std()  # rolling_std(timeseries, window=12)

    # Plot rolling statistics:
    plt.figure(figsize=figsizeIn)
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')

    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)


# Estimate hurst parameter
def hurst(ts):
    """Returns the Hurst Exponent of the time series vector ts"""

    # Create the range of lag values
    lags = range(2, 100)

    # Calculate the array of the variances of the lagged differences
    tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # Use a linear fit to estimate the Hurst Exponent
    poly = np.polyfit(np.log(lags), np.log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0] * 2.0


# Compute fractional differnce
# x = np.array([1,2,3,4,5,6,7,8,9,10])
# d = 0.3
# dfx = fractionalDiff(x,d)
# print (dfx)
def fractionalDiff(x, d):
    """Returns fractionally differentiated time series """

    # Get coefficients
    N = len(x)
    c = np.zeros(N)
    # j = 1.0
    c[0] = 1.0
    for k in range(1, N):  # Shifted index 1:N to 0:N-1
        pp = 1.0 * d
        for a in range(1, k):
            pp *= (d - a) / (a + 1.0)
        c[k] = pp * ((-1) ** k)

    c = c[::-1]  # Reverse them
    # print '\n Forv cc =', c

    dfx = np.zeros(N);
    for k in range(N):
        dfx[k] = np.dot(c[N - k - 1:N], x[0:k + 1])

    return dfx


# Compute inverse fractional differnce
# x = np.array([1,2,3,4,5,6,7,8,9,10])
# d = 0.3
# dfx = fractionalDiff(x,d)
# print (dfx)
def fractionalInvDiff(x, d):
    """ Returns fractionally differentiated time series """

    # Get coefficients
    N = len(x)
    aa = np.zeros(N)
    aa[0] = 1.0
    for n in range(1, N):
        aa_c = 0.0
        for k in range(1, n + 1):
            pp = 1.0 * d
            for a in range(1, k):
                pp *= (d - a) / (a + 1.0)
            aa_c += aa[n - k] * ((-1) ** (k - 1)) * pp
            # aa_c += aa[n-k-1]*((-1)**(k-1))*sc.special.binom(d,k)
        aa[n] = aa_c

    aa = aa[::-1]  # Reverse them
    # print '\n Inv aa = ', aa

    idfx = np.zeros(N);
    for k in range(N):
        idfx[k] = np.dot(aa[N - k - 1:N], x[0:k + 1])

    return idfx
