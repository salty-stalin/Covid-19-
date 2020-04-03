import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import time

read_variables=np.loadtxt('Control_Parameters.txt' ,usecols=(2,))

time.sleep(10)
width1=int(read_variables[0])
distance1=int(read_variables[1])
height1=int(read_variables[2])
exp_grad = float(read_variables[3])
exp_grad_std = float(read_variables[4])

print(width1)
print(distance1)
print(height1)
print(exp_grad)
print(exp_grad_std)
country_names=np.loadtxt('country_names.txt',dtype=np.str)
print(country_names)
for j in country_names:
    print(j)
    date=np.loadtxt('Countries File\\'+j ,dtype=np.str,usecols=(0,))
    if date.size>5:
        daily_cases=np.loadtxt('Countries File\\'+j ,usecols=(2,))
        daily_deaths=np.loadtxt('Countries File\\'+j ,usecols=(3,))
        flip_cases=np.flip(daily_cases)
        flip_deaths=np.flip(daily_deaths)
        flip_date=np.flip(date)
        print(date)
        x_values=np.arange(len(date))
        
        
        
        def find_nearest(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return array[idx]
        
        
        
        
        
        peaks,properties = find_peaks(flip_cases,width=width1,distance=distance1,height=height1)
        
        print((peaks))
        print(properties)
        print(flip_cases[peaks])
        j = j[:-4]
    
    
        if peaks.size:
            max_val=np.amax(peaks)
            half_max_estimate=flip_cases[max_val]/2
            half_max_actual=find_nearest(flip_cases,half_max_estimate)
            where_half_max=np.where(flip_cases == half_max_actual)
            FWHM=abs(max_val-where_half_max)*2
            print(half_max_estimate)
            print(half_max_actual)
            print(max_val)
            print(where_half_max)
            print(FWHM)
            def _1gaussian(x, amp1,cen1,sigma1):
                return amp1*(1/(sigma1*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x-cen1)/sigma1)**2)))
            amp1=flip_cases[max_val]
            cen1=max_val
            sigma1=int(FWHM/2.35482004503)
            
            popt_gauss, pcov_gauss = scipy.optimize.curve_fit(_1gaussian, x_values, flip_cases, p0=[amp1, cen1, sigma1])
            perr_gauss = np.sqrt(np.diag(pcov_gauss))
            
            x_fitting=np.arange(len(date)+50)
            fitting_values=_1gaussian(x_fitting,popt_gauss[0],popt_gauss[1],popt_gauss[2])
        
        
            
            print(x_values)
            
            print(x_fitting)
            print(fitting_values)
        
        
        
        
            fig, ax = plt.subplots()
            ax.scatter(flip_date, flip_cases,s=2)
            ax.scatter(flip_date, flip_deaths,s=2 ,c='red')
            ax.plot(x_fitting,fitting_values)
            ax.set_title(j)
            ax.set_xlabel('Date')
            ax.tick_params(axis='x', which='major', labelsize=8)
            ax.set_ylabel('Number of cases')
            ax.xaxis.set_major_locator(plt.MaxNLocator(10))
            plt.savefig('Country Graphs\\' +j + '.png')
            gaussian_filename='gaussian_countries.txt'
            file = open(gaussian_filename,'a') 
            file.write(j+" " + str(popt_gauss)+"\n")
            file.write(j+" " + str(perr_gauss)+"\n")
        else :
            
            def func(x, a, b, c):
                return a * np.exp((-b*x)) + c


            try:
                popt, pcov = curve_fit(func, x_values, flip_cases,p0=[1,0.01,1])
                perr = np.sqrt(np.diag(pcov))
                print(popt)
                if popt[1]<exp_grad and perr[1]<exp_grad_std:
                    
                    fitting_values_exp=func(x_values, popt[0],popt[1],popt[2])
                    
                    
                    fig, ax = plt.subplots()
                    ax.scatter(flip_date, flip_cases,s=2)
                    ax.scatter(flip_date, flip_deaths,s=2 ,c='red')
                    ax.set_title(j)
                    ax.set_xlabel('Date')
                    ax.tick_params(axis='x', which='major', labelsize=8)
                    ax.set_ylabel('Number of cases')
                    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
                    ax.plot(x_values,fitting_values_exp)
                    plt.savefig('Country Graphs\\'+j + '.png')
                    exponential_filename='exponetial_countries.txt'
                    file = open(exponential_filename,'a') 
                    file.write(j+" " + str(popt)+"\n")
                    
    
                else:
                
                
                    fig, ax = plt.subplots()
                    ax.scatter(flip_date, flip_cases,s=2)
                    ax.scatter(flip_date, flip_deaths,s=2 ,c='red')
                    ax.set_title(j)
                    ax.set_xlabel('Date')
                    ax.tick_params(axis='x', which='major', labelsize=8)
                    ax.set_ylabel('Number of cases')
                    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
                    plt.savefig('Country Graphs\\'+j + '.png')
                    irregular_filename='irregular_countries.txt'
                    file = open(irregular_filename,'a') 
                    file.write(j+"\n")
            except:
                    fig, ax = plt.subplots()
                    ax.scatter(flip_date, flip_cases,s=2)
                    ax.scatter(flip_date, flip_deaths,s=2 ,c='red')
                    ax.set_title(j)
                    ax.set_xlabel('Date')
                    ax.tick_params(axis='x', which='major', labelsize=8)
                    ax.set_ylabel('Number of cases')
                    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
                    plt.savefig('Country Graphs\\'+j + '.png')
                    irregular_filename='irregular_countries.txt'
                    file = open(irregular_filename,'a') 
                    file.write(j+"\n")
        
