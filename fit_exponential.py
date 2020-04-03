# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import time

date=np.loadtxt('C:\\Users\\User\\Desktop\\Covid-19 Data\\Countries File\\United_Kingdom.txt' ,dtype=np.str,usecols=(0,))

daily_cases=np.loadtxt('C:\\Users\\User\\Desktop\\Covid-19 Data\\Countries File\\United_Kingdom.txt' ,usecols=(2,))
daily_deaths=np.loadtxt('C:\\Users\\User\\Desktop\\Covid-19 Data\\Countries File\\United_Kingdom.txt' ,usecols=(3,))
flip_cases=np.flip(daily_cases)
flip_deaths=np.flip(daily_deaths)
flip_date=np.flip(date)
x_values=np.arange(len(date))
def func(x, a, b, c):
    return a * np.exp((-b*x)) + c


#,
popt, pcov = curve_fit(func, x_values, flip_cases,p0=[1,1e-6,1])
perr = np.sqrt(np.diag(pcov))

print(popt)
fitting_values=func(x_values, popt[0],popt[1],popt[2])
plt.figure()
plt.plot(x_values, flip_cases, 'ko', label="Original Noised Data")
plt.plot(x_values, fitting_values, 'r-', label="Fitted Curve")
plt.legend()
plt.show()
print(perr)