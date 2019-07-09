# Analysis of Mobile Network Measurement Data

This repository contains code that was used to perform data analysis on a dataset which was the result of mobile network measurements. Measurements were performed in a LTE network using several identical measurement devices, and more than 200 parameters were observed at the time of each measurement. The period between measurements was not constant, thus the results in datasets are represented as unevenly sampled time series.

The analysis was performed using Python and pandas. Please refer to my masters thesis (available [here](https://repozitorij.uni-lj.si/Dokument.php?id=119570&lang=slv)) for detailed information on the experiments and the course of the analysis.

Jupyter notebooks are organized as follows:
  - *feature_selection*: feature space of raw iperf measurement data is shrunk by using a heuristic feature selection process.
  - *iperf_data*: detailed iperf measurement data is parsed from JSON to a new dataframe. Another dataframe is created with iperf test duration information. A split-apply-combine approach is used in order to convert time series which contain measurement data to become evenly sampled. Results of the base station stress test are compared to regular beavior in the same time frame. Finally, seasonal component is analyzed in the time series using statsmodels' seasonal decompose implementation and FFT.
  - *iperf_data_detailed*: detailed iperf dataset which was generated in *iperf_data.ipynb* is analyzed for each second of the duration of the iperf test.
  - *frequent_radio_data*: iperf duration dataset which was generated in *iperf_data.ipynb* is used to search for correlation between the number of active devices in a cell and RSRQ.
