from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def polynomial_2(x, a, b, c):
     return a*x**2+b*x+c

class ReadExcel:
     def __init__(self,energy_top,energy_bottom):
          self.energy_top=energy_top
          self.energy_bottom=energy_bottom
          self.nazwa=f"{self.energy_top}_{self.energy_bottom}.xlsx"
          
          tau_nb=pd.read_excel(self.nazwa,sheet_name='Dane',header=None,usecols='B,D,G,I',skiprows=6,nrows=1,names=['tt','ut','tb','ub'])
          tau_top=pd.read_excel(self.nazwa,sheet_name='Dane',header=None,usecols='A,H,I',skiprows=9,nrows=4,names=['x','y','u'])
          tau_bottom=pd.read_excel(self.nazwa,sheet_name='Dane',header=None,usecols='A,H,I',skiprows=15,nrows=4,names=['x','y','u'])

          self.top=[self.energy_top,np.array(tau_nb['tt']),np.array(tau_nb['ut']),
                             np.array(tau_top['x']),np.array(tau_top['y']),np.array(tau_top['u'])]
          self.bottom=[self.energy_bottom,np.array(tau_nb['tb']),np.array(tau_nb['ub']),
                       np.array(tau_bottom['x']),np.array(tau_bottom['y']),np.array(tau_bottom['u'])]
     def plot_top(self):
          a_b_c, ua_ub_uc=curve_fit(polynomial_2, self.top[3], self.top[4], sigma=self.top[5], absolute_sigma=True)
          a,b,c=a_b_c
          ua,ub,uc=np.sqrt(np.diag(ua_ub_uc))

          residuals=self.top[4]-polynomial_2(self.top[3],a,b,c)
          variance_residuals=np.sum(residuals**2)/(len(self.top[4])-len(a_b_c))
          std_residuals=np.sqrt(variance_residuals)
          total_variance=np.mean(self.top[5]**2)
          total_std=np.sqrt(std_residuals**2+total_variance)
          two_std_dev=total_std
          #std_dev=np.std(residuals,ddof=1)
          #two_std_dev=2*std_dev

          print(f"Energy {self.energy_top} fitted:")
          print(f"a = {a}, b = {b}, c = {c}")
          print(f"u(a) = {ua}, u(b) = {ub}, u(c) = {uc}")
          print(f"Tau with background: {polynomial_2(self.top[0],a,b,c)}+-{two_std_dev}")#np.sqrt(ua**2+ub**2+uc**2)}")

          x=np.linspace(min(self.top[3])-1.0, max(self.top[3])+1.0,1000)
          plt.errorbar(self.top[0],self.top[1], yerr=self.top[2], fmt='o', label=f"Energy {self.energy_top}", capsize=5)
          plt.errorbar(self.top[3], self.top[4], yerr=self.top[5], fmt='o', label='Background', capsize=5)
          plt.plot(x,polynomial_2(x,a,b,c),"-", label='Polynomial fitting')
          plt.errorbar(self.top[0],polynomial_2(self.top[0],a,b,c), yerr=two_std_dev, fmt='o', label=f"Energy {self.energy_top} with background", capsize=5)
          plt.title(f"Energy {self.energy_top} fitted:")
          plt.xlabel("Energy [keV]")
          plt.ylabel("Time tau [ps]")
          plt.legend()
          plt.savefig(f"{self.energy_bottom}_{self.energy_top}.png", format='png', dpi=300)
          plt.show()
     def plot_bottom(self):
          a_b_c, ua_ub_uc=curve_fit(polynomial_2, self.bottom[3], self.bottom[4], sigma=self.bottom[5], absolute_sigma=True)
          a,b,c=a_b_c
          ua,ub,uc=np.sqrt(np.diag(ua_ub_uc))

          residuals=self.bottom[4]-polynomial_2(self.bottom[3],a,b,c)
          variance_residuals=np.sum(residuals**2)/(len(self.bottom[4])-len(a_b_c))
          std_residuals=np.sqrt(variance_residuals)
          total_variance=np.mean(self.bottom[5]**2)
          total_std=np.sqrt(std_residuals**2+total_variance)
          two_std_dev=total_std
          #std_dev=np.std(residuals,ddof=1)
          #two_std_dev=2*std_dev

          print(f"Energy {self.energy_bottom} fitted:")
          print(f"a = {a}, b = {b}, c = {c}")
          print(f"u(a) = {ua}, u(b) = {ub}, u(c) = {uc}")
          print(f"Tau with background: {polynomial_2(self.bottom[0],a,b,c)}+-{two_std_dev}")#np.sqrt(ua**2+ub**2+uc**2)}")

          x=np.linspace(min(self.bottom[3])-1.0, max(self.bottom[3])+1.0,1000)
          plt.errorbar(self.bottom[0],self.bottom[1], yerr=self.bottom[2], fmt='o', label=f"Energy {self.energy_bottom}", capsize=5)
          plt.errorbar(self.bottom[3], self.bottom[4], yerr=self.bottom[5], fmt='o', label='Background', capsize=5)
          plt.plot(x,polynomial_2(x,a,b,c),"-", label='Polynomial fitting')
          plt.errorbar(self.bottom[0],polynomial_2(self.bottom[0],a,b,c), yerr=two_std_dev, fmt='o', label=f"Energy {self.energy_bottom} with background", capsize=5)
          plt.title(f"Energy {self.energy_bottom} fitted:")
          plt.xlabel("Energy [keV]")
          plt.ylabel("Time tau [ps]")
          plt.legend()
          plt.savefig(f"{self.energy_top}_{self.energy_bottom}.png", format='png', dpi=300)
          plt.show()
          
#ReadExcel(1223,147).plot_top()
#ReadExcel(1223,147).plot_bottom()
#ReadExcel(809,122).plot_top()
#ReadExcel(809,122).plot_bottom()
#ReadExcel(530,122).plot_top()
#ReadExcel(530,122).plot_bottom()
#ReadExcel(279,530).plot_top()
#ReadExcel(279,530).plot_bottom()
          
ReadExcel(1277,686).plot_top()
ReadExcel(1277,686).plot_bottom()
#ReadExcel(261,827).plot_top()
#ReadExcel(261,827).plot_bottom()
          
#ReadExcel(382,919).plot_top()
#ReadExcel(382,919).plot_bottom()
#ReadExcel(1577,837).plot_top()
#ReadExcel(1577,837).plot_bottom()
#ReadExcel(770,432).plot_top()
#ReadExcel(770,432).plot_bottom()

#ReadExcel(168,590).plot_top()
#ReadExcel(168,590).plot_bottom()
#ReadExcel(710,590).plot_top()
#ReadExcel(710,590).plot_bottom()
#ReadExcel(260,876).plot_top()
#ReadExcel(260,876).plot_bottom()
#ReadExcel(1699,876).plot_top()
#ReadExcel(1699,876).plot_bottom()
#ReadExcel(346,710).plot_top()
#ReadExcel(346,710).plot_bottom()
#ReadExcel(1270,710).plot_top()
#ReadExcel(1270,710).plot_bottom()

