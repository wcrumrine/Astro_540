import numpy as np
from classy import Class

def Get_LCDM_Cls(h, omega_b, omega_cdm, tau_reio, A_s, n_s, P_k_max, k_per_decade, N_ur, N_ncdm):
    LCDM = Class()
    
    # pass input parameters
    LCDM.set({'h':h,'omega_b':omega_b,'omega_cdm':omega_cdm,'tau_reio':tau_reio,'A_s':A_s,'n_s':n_s})
    LCDM.set({'N_ur':N_ur, 'N_ncdm':N_ncdm})
    LCDM.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes'})
    
    # run class
    LCDM.compute()
    
    
    clM = LCDM.lensed_cl(2500)
    ll = clM['ell'][2:]
    clTT = clM['tt'][2:]
    clEE = clM['ee'][2:]
    clTE = clM['te'][2:]

    return ll, clTT, clEE, clTE


def Get_PHO_Cls(h, omega_b, omega_cdm, tau_reio, A_s, n_s, P_k_max, k_per_decade, \
                                  f_idm, m_idm, u_idm_g, N_ur, N_ncdm):
    PHO = Class()
    
    # pass input parameters
    PHO.set({'h':h,'omega_b':omega_b,'omega_cdm':omega_cdm, 'tau_reio':tau_reio,'A_s':A_s,'n_s':n_s})
    PHO.set({'N_ur':N_ur, 'N_ncdm':N_ncdm})
    PHO.set({'f_idm':f_idm,'m_idm':m_idm,'u_idm_g':u_idm_g})
    PHO.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes'})
     
    # run class
    PHO.compute()
    
    clM_PHO = PHO.lensed_cl(2500)
    ll_PHO = clM_PHO['ell'][2:]
    clTT_PHO = clM_PHO['tt'][2:]
    clEE_PHO = clM_PHO['ee'][2:]
    clTE_PHO = clM_PHO['te'][2:]
             
    # output
    return ll_PHO, clTT_PHO, clEE_PHO, clTE_PHO


def Get_NU_Cls(h, omega_b, omega_cdm, tau_reio, A_s, n_s, P_k_max, k_per_decade, \
                                 f_nudm, u_ncdmdm_scale, N_ur, N_ncdm, m_ncdm, u_ncdmdm):
    NU = Class()
    
    # pass input parameters
    NU.set({'h':h, 'omega_b':omega_b, 'omega_cdm':omega_cdm, 'tau_reio':tau_reio, 'A_s':A_s, 'n_s':n_s})
    NU.set({'N_ur':N_ur, 'N_ncdm':N_ncdm})
    NU.set({'output':'tCl,pCl,lCl,mPk,mTk','lensing':'yes','gauge':'newtonian'})
    NU.set({'f_nudm':f_nudm, 'u_ncdmdm_scale':u_ncdmdm_scale})

    params1 = {}
    params1['m_ncdm']=m_ncdm
    NU.set(params1)  
    
    params2 = {}
    params2['u_ncdmdm']=u_ncdmdm
    NU.set(params2) 
     
    # run class
    NU.compute()
    
    clM_NU = NU.lensed_cl(2500)
    ll_NU = clM_NU['ell'][2:]
    clTT_NU = clM_NU['tt'][2:]
    clEE_NU = clM_NU['ee'][2:]
    clTE_NU = clM_NU['te'][2:]
             
    # output
    return ll_NU, clTT_NU, clEE_NU, clTE_NU


    
