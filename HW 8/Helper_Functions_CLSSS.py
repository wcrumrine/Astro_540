import numpy as np
from classy import Class

def Get_LCDM_Cls(h, omega_b, omega_cdm, tau_reio, A_s, n_s):
    LCDM = Class()
    
    # pass input parameters
    LCDM.set({'h':h,'omega_b':omega_b,'omega_cdm':omega_cdm,'tau_reio':tau_reio,'A_s':A_s,'n_s':n_s})
    LCDM.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes'})
    
    # run class
    LCDM.compute()
    
    
    clM = LCDM.lensed_cl(2500)
    ll = clM['ell'][2:]
    clTT = clM['tt'][2:]
    clEE = clM['ee'][2:]
    clTE = clM['te'][2:]

    return ll, clTT, clEE, clTE


