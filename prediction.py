import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit

date=np.loadtxt('C:\\Users\\User\\Desktop\\Covid-19 Data\\Countries File\\Italy.txt' ,dtype=np.str,usecols=(0,))
daily_cases=np.loadtxt('C:\\Users\\User\\Desktop\\Covid-19 Data\\Countries File\\Italy.txt' ,usecols=(2,))
daily_deaths=np.loadtxt('C:\\Users\\User\\Desktop\\Covid-19 Data\\Countries File\\Italy.txt' ,usecols=(3,))

flip_cases=np.flip(daily_cases)
flip_deaths=np.flip(daily_deaths)


print(date)
x_values=np.arange(len(date))
max_val=np.amax(daily_cases)

def _1gaussian(x, amp1,cen1,sigma1):
    return amp1*(1/(sigma1*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x-cen1)/sigma1)**2)))
amp1=6000
cen1=80
sigma1=19
popt_gauss, pcov_gauss = scipy.optimize.curve_fit(_1gaussian, x_values, flip_cases, p0=[amp1, cen1, sigma1])
perr_gauss = np.sqrt(np.diag(pcov_gauss))

x_fitting=np.arange(len(date)+50)
fitting_values=_1gaussian(x_fitting,popt_gauss[0],popt_gauss[1],popt_gauss[2])



print(x_values)

print(x_fitting)
print(fitting_values)




fig, ax = plt.subplots()

ax.plot(x_fitting,fitting_values)
#plt.gca().invert_xaxis()
ax.set_title('France')
ax.set_xlabel('Date')
ax.set_ylabel('Number of cases')
plt.show()
print(perr_gauss)