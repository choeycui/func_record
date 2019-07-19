# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:21:29 2019

@author: choey cui
"""

import numpy as np
import statsmodels.api as sm
from scipy import stats,special

def stepwise_reg(Y,X,sig):
    df = X.iloc[:,0].size
    df_old = 0
    df_new = 0
    x_cols = X.columns.to_list()
    remain = x_cols
    x_fin = []
    f_max = -1
    f_min = 9999999
    p_ftest = 0
    x_in1 = ''
    # pick the first variables into model
    for i in range(0,len(remain)-1):
        X_buffer = X[remain[i]]
        X_buffer = sm.add_constant(X_buffer, has_constant='add')
        model_buffer = sm.OLS(Y,X_buffer).fit()
        f_value = model_buffer.fvalue
        p_value = model_buffer.f_pvalue
        if (f_max < f_value) & (p_value < sig):
            f_max = f_value
            x_in1 = remain[i]
            mse_before = model_buffer.mse_model
    x_fin.append(x_in1)
    remain.remove(x_in1)
    df_old = df-len(x_fin)-1
    while (len(remain) > 0):
        remain = list(set(remain))
        x_fin = list(set(x_fin))
        f_max = -1
        # compare the rest variables if there are some appreciable ones
        for j in range(0,len(remain)):
            X_buffer = X[x_fin + [remain[j]]]
            X_buffer = sm.add_constant(X_buffer, has_constant='add')
            model_buffer = sm.OLS(Y,X_buffer).fit()
            # calculate each model's Fvlaue and Pvalue
            f_value = model_buffer.fvalue
            p_value = model_buffer.f_pvalue
            if (f_max < f_value) & (p_value < sig):
                f_max = f_value
                x_in = remain[j]
                mse_after = model_buffer.mse_model # retain the variable who has the greatest contribution to SSR(or SSE reduced)
        df_new = df_old - 1 # update the degree of freedom of the former and the latter model
        # verify if there is a significant reduction of model's mse via the max likelihood variable
        F = mse_before/mse_after
        p_ftest = 1-stats.f.cdf(F,df_old,df_new)
        mse_before = mse_after
        df_old = df_new
        # add the variable if significant
        if p_ftest < sig:
            x_fin.append(x_in)
            remain.remove(x_in)
        else:
            break
        # check if there is any existing variable become inappreciable and drop it
        for x in x_fin:
            buffer1 = list(set(x_fin).difference(set([x])))
            X_buffer1 = X[buffer1]
            X_buffer1 = sm.add_constant(X_buffer1, has_constant='add')
            model_test = sm.OLS(Y,X_buffer1).fit()
            mse_drop = model_test.mse_model
            F1 = mse_drop/mse_after
            if F1<f_min:
                f_min = F1
                x_out = x
        p1 = 1-stats.f.cdf(F1,df_new+1,df_new)
        if p1 > sig:
            x_fin.remove(x_out)
            remain.append(x_out)
    X_fin = X[x_fin]
    X_fin = sm.add_constant(X_fin, has_constant='add')
    model = sm.OLS(Y,X_fin).fit()
    #return the model and chosen variables         
    return model,X_fin

# box cox transformation thourgh lamda estimated by the boxcox log-likelihood function
def box_cox(datacol,lam_min,lam_max,grain):
    lam_range = np.linspace(lam_min,lam_max,grain)
    llf = np.zeros(lam_range.shape, dtype=float)
    for i,lam in enumerate(lam_range):
        llf[i] = stats.boxcox_llf(lam, datacol)
    lam_best = lam_range[llf.argmax()]
    y = special.boxcox1p(datacol, lam_best)
    #return the transformed y and the best lamda
    return y,lam_best

#test the consistency between two dataset, length can be different.
def homotest(y1,y2,grain):
    lower = max(y1.min(),y2.min())
    upper = min(y1.max(),y2.max())
    coef_ = y1.count()/y2.count()
    chi2 = 0
    df = 0
    block = np.linspace(lower,upper,grain)
    for i in range(len(block)-1):
        f0 = y1[(y1>block[i])&(y1<block[i+1])].count()
        fe = y2[(y2>block[i])&(y2<block[i+1])].count()*coef_
        chi2 += (f0-fe)**2/(fe+1)
        df += 1
    p = 1-stats.chi2.cdf(chi2,df-1)
    return p 
