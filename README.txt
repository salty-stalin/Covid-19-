Software to graph and sort Covid-19 Data


All data is graphed for daily cases and daily deaths per country

where possible fittings are done for the data. The cases can be split into 3 categories:
these cases are written doen in the subsequent .txt files

-very low number of cases (irrregular or linear pattern- #bad testing or lockdown working#) ==== e.g. Kyrgyztsan, uzbekistan
-exponential growth countries (countries where the deasease is starting to spread rapidly -#can be identified with exponential fitting) ==== e.g USA, UK
-Countries of peaking or past peaking (countries who have reached or passing the peak and a gaussian can be fitted) === e.g. Italy

Next to the countries apprpriete estimated parameters are written down

RUNNING SOFTWARE

1)to run the software execute the main.py file

this will run the 4 scripts:
-download_data.py (Downloads upto date Covid-19 Statistics from https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-04-03.xlsx)
-separate_files.py (sorts the excel file into appropriete .txt files per country)
-write_country_names.py (lists the appropriete countries to be analysed)
-plot_graphs.py (runs the soft ware for plotting and fitting)

2) Make sure the Control_parameters.txt is in the directory 
These are the parameters to control for the gaussian and exponential fitting
width = minimum width for data to be gaussian
distance = minimum distance for peak around data
height = minimum height of peak
exp_grad = minimal gradient for the exponential curve for it to be fitted
exp_grad_std = minimum startdard deviation of the fitted parameter to the actual data

3)Fitting

The Gaussian fitting assumes that a good estimate for data is amp1*(1/(sigma1*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x-cen1)/sigma1)**2)))
a standard gaussian curve. An estimates for the parameters is made if the data is approaching a gaussian distribution
estimate parameters made are for sigma, amplitude, centre
The estimate is made using find_peak where the gradient is analysed the surrounding points
when an estimate is made curve_fit is used where the fitting is optimised using the sum of least squared method between the fitting and data
This process follows the same method for exponential fitting for high increase countries
the form is of return a * np.exp((-b*x)) + c

The fitting is heavily reliant on the parameters which can be adjusted using the control_parameter.txt

4) Errors 
Most errors arrive from incorrect position of appripreite files in the directory-make sure all files are in same folder
make sure the control parameter is in the folder too with appropriete values
the excel file downloaded must not have spaces in country names! 
sometimesthe uploaded documents will have spaces instead of the usual _
this has to be edited by hand

if excel file is changed debugging can be done in the main.py file by commenting out uneeded modules