################################################################
# University of Amsterdam                                      #
# MSc Economics Thesis: Markets and Regulations                #
# 'CAOs, Costs & Competition:                                  #
#   Analyzing collective labor agreement bargaining &          #
#   their effect on competition in the Netherlands, a study    #
#   of the poldermodel in the case of the grocery market'      #
# Pedro Maroto de la Cruz                                      #
# 11618248                                                     #
################################################################

### Imports
import customtkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

### Embeded data & initializing variables 
gradient_shift_ratios = pd.DataFrame({
    'del_mon': [0.000000, 0.000000, 0.142857, 0.142857, 0.428571, 0.714286, 1.000000, 0.714286],
    'del_tue': [0.428571, 0.428571, 0.428571, 0.142857, 0.428571, 0.714286, 1.000000, 0.714286],
    'del_wed': [0.000000, 0.000000, 0.142857, 0.142857, 0.428571, 0.714286, 1.000000, 0.714286],
    'del_thu': [0.428571, 0.428571, 0.428571, 0.142857, 0.428571, 0.714286, 1.000000, 0.714286],
    'del_fri': [0.142857, 0.142857, 0.142857, 0.142857, 0.428571, 0.714286, 1.000000, 1.000000],
    'del_sat': [0.142857, 0.142857, 0.142857, 0.142857, 0.428571, 0.714286, 1.000000, 1.000000],
    'del_sun': [0.142857, 0.142857, 0.142857, 0.142857, 0.428571, 0.714286, 1.000000, 0.714286],
    'sup_mon': [0.333333, 0.333333, 0.666667, 1.000000, 0.666667, 0.333333, 0.000000, -1.000000],
    'sup_tue': [0.333333, 0.333333, 0.666667, 1.000000, 0.666667, 0.333333, 0.000000, -1.000000],
    'sup_wed': [0.333333, 0.333333, 0.666667, 1.000000, 0.666667, 0.333333, 0.000000, -1.000000],
    'sup_thu': [0.333333, 0.333333, 0.666667, 1.000000, 0.666667, 0.333333, 0.000000, -1.000000],
    'sup_fri': [0.333333, 0.333333, 0.666667, 1.000000, 0.666667, 0.666667, 0.666667, -1.000000],
    'sup_sat': [0.333333, 0.333333, 0.666667, 1.000000, 0.666667, 0.666667, 0.666667, -1.000000],
    'sup_sun': [0.333333, 0.333333, 0.666667, 1.000000, 0.666667, 0.666667, 0.333333, -1.000000],
})

bonus = pd.DataFrame({
    'shift': [8, 10, 12, 14, 16, 18, 20, 22],
    'vgl_d_mon': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.25, 1.5],
    'vgl_d_tue': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.25, 1.5],
    'vgl_d_wed': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.25, 1.5],
    'vgl_d_thu': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.25, 1.5],
    'vgl_d_fri': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.25, 1.5],
    'vgl_d_sat': [1.3, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.5],
    'vgl_d_sun': [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    'ecom_mon': [1, 1, 1, 1, 1, 1, 1, 1],
    'ecom_tue': [1, 1, 1, 1, 1, 1, 1, 1],
    'ecom_wed': [1, 1, 1, 1, 1, 1, 1, 1],
    'ecom_thu': [1, 1, 1, 1, 1, 1, 1, 1],
    'ecom_fri': [1, 1, 1, 1, 1, 1, 1, 1],
    'ecom_sat': [1, 1, 1, 1, 1, 1, 1, 1],
    'ecom_sun': [1, 1, 1, 1, 1, 1, 1, 1],
    'vgl_s_mon': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5],
    'vgl_s_tue': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5],
    'vgl_s_wed': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5],
    'vgl_s_thu': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5],
    'vgl_s_fri': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5],
    'vgl_s_sat': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5],
    'vgl_s_sun': [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
})

shift_ratio_c2 = pd.DataFrame({
    'shift': [8, 10, 12, 14, 16, 18, 20, 22],
    'del_mon': [1.0, 1.0, 1.2, 1.2, 1.6, 2.0, 2.4, 2.0],
    'del_tue': [1.6, 1.6, 1.6, 1.2, 1.6, 2.0, 2.4, 2.0],
    'del_wed': [1.0, 1.0, 1.2, 1.2, 1.6, 2.0, 2.4, 2.0],
    'del_thu': [1.6, 1.6, 1.6, 1.2, 1.6, 2.0, 2.4, 2.0],
    'del_fri': [1.2, 1.2, 1.2, 1.2, 1.6, 2.0, 2.4, 2.4],
    'del_sat': [1.2, 1.2, 1.2, 1.2, 1.6, 2.0, 2.4, 2.4],
    'del_sun': [1.2, 1.2, 1.2, 1.2, 1.6, 2.0, 2.4, 2.0],
    'sup_mon': [1.333333, 1.333333, 1.666667, 2.000000, 1.666667, 1.333333, 1.000000, 0.000000],
    'sup_tue': [1.333333, 1.333333, 1.666667, 2.000000, 1.666667, 1.333333, 1.000000, 0.000000],
    'sup_wed': [1.333333, 1.333333, 1.666667, 2.000000, 1.666667, 1.333333, 1.000000, 0.000000],
    'sup_thu': [1.333333, 1.333333, 1.666667, 2.000000, 1.666667, 1.333333, 1.000000, 0.000000],
    'sup_fri': [1.333333, 1.333333, 1.666667, 2.000000, 1.666667, 1.666667, 1.000000, 0.000000],
    'sup_sat': [1.333333, 1.333333, 1.666667, 2.000000, 1.666667, 1.666667, 1.666667, 0.000000],
    'sup_sun': [1.333333, 1.333333, 1.666667, 2.000000, 1.666667, 1.666667, 1.333333, 0.000000],
})

wages = pd.DataFrame({
    'wage_group': ['Y_15', 'Y_16', 'Y_17', 'Y_18', 'Y_19', 'Y_20', 'Y_21', 'Y_22'],
    'vgl_s': [3.81, 4.39, 5.02, 5.51, 6.44, 8.61, 10.76, 11.80],
    'ecom': [0.00, 5.23, 5.93, 7.57, 8.08, 9.28, 11.53, 11.53],
    'vgl_d': [3.81, 4.39, 5.02, 5.51, 6.44, 8.61, 10.76, 11.80],
    'ah': [3.66, 4.22, 4.82, 5.29, 6.19, 7.74, 9.68, 11.35],
    'flink': [0.0, 7.4, 7.8, 8.3, 9.5, 11.0, 12.1, 12.1],
    'ah_AI': [4.866702, 5.611334, 6.409154, 7.034113, 8.230843, 10.291878, 12.871496, 15.092095]
})

shift_slots = ['8-10', '10-12', '12-14', '14-16', '16-18', '18-20', '20-22', '22-24']
weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
labels_wage_groupings = ['p21', 'p18', 'u18']

provider = ['del_', 'sup_']

del_grad = gradient_shift_ratios.filter(regex=r'^del_')
sup_grad = gradient_shift_ratios.filter(regex=r'^sup_')
del_grad.index = shift_slots
sup_grad.index = shift_slots
del_grad.columns = weekdays
sup_grad.columns = weekdays
CAO_wage_list = wages.columns.tolist()

del_ratio = shift_ratio_c2.filter(regex=r'^del_')
sup_ratio = shift_ratio_c2.filter(regex=r'^sup_')
del_ratio.index = shift_slots
sup_ratio.index = shift_slots
bonus.index = shift_slots


contract_type = ['ft', 'pt']
labels_wage_groupings = ['p21', 'p18', 'u18']
provlabel = ['Deliverer', 'Supermarket']

prov_ct_gradq = {}
grad_q = {}
cao_bonus_ratio = {}
cao_bonus_wage = {}
cao_prov_age_pq = {}
week_q = {}
week_pq = {}
detailed_implicit_wagecosts_pac = {}

day_shifts = ['8-10', '10-12', '12-14', '14-16']
night_shifts = ['16-18', '18-20', '20-22', '22-24']

stats1 = None
stats2 = None
stats3 = None

age_bind = {
    '-18': 'u18',
    '18-20': 'p18',
    '+21': 'p21'
}

del_exp_lt = 0
del_imp_lt = 0
sup_exp_lt = 0
sup_imp_lt = 0

workercount_det = pd.DataFrame(index=provider)
workercount_sum = pd.DataFrame(index=provider)
quantity_costs = pd.DataFrame(index=provider) 
explicit_week_costs = pd.DataFrame(index=provider, columns=CAO_wage_list)
implicit_week_costs = pd.DataFrame(index=provider, columns=CAO_wage_list)

descriptive_stats = {}
d_stats = ['Real hourly cost', 'Total week cost', 'Avg weekday cost', 'Avg weekend cost', 'Avg day shift cost', 'Avg night shift cost']


dataset = [wages, bonus, shift_ratio_c2, del_ratio, sup_ratio]

for set in dataset:
    if 'wage_group' in set.columns:
        set.set_index('wage_group', inplace=True)

wages = wages.replace(0, np.nan)


age_groupings = ['-18', '18-20', '+21']

grouped_wages = pd.DataFrame(index=labels_wage_groupings, columns=CAO_wage_list)

labels_wage_groupings = ['p21', 'p18', 'u18']
for cao in CAO_wage_list:
    for wg in labels_wage_groupings:
        try:
            if wg == 'u18':
                grouped_wages.loc[wg, cao] = wages.loc[['Y_15', 'Y_16', 'Y_17'], cao].mean()
            if wg == 'p18':
                grouped_wages.loc[wg, cao] = wages.loc[['Y_18', 'Y_19', 'Y_20'], cao].mean()
            if wg == 'p21':
                grouped_wages.loc[wg, cao] = wages.loc[['Y_21', 'Y_22'], cao].mean()
        except KeyError:
            continue

# VGL - Supermarkets implicit costs
vgl_s_pension = 0.1964 # +21 complicated af
vgl_s_franchise = 7.9154
vgl_s_vac_pay = .08 # Total wage costs * 8%
vgl_s_socialfund = 0.0026  # On total wage costs
vgl_s_adv = 0.006075 # ADV normalized across wages
vgl_s_nvacdays = 0.092308  # As if at the end of every week paid vacation is taken

# VGL - Distribution center implicit costs
vgl_d_pension = 0.1964  # +21 complicated af
vgl_d_franchise = 7.9154  # hourly wage not included in pensionable wage
vgl_d_vac_pay = .08 # Total wage costs * 8%
vgl_d_socialfund = 0.0026 # On total wage costs
vgl_d_dinnerpay =  5.45
vgl_d_adv = 0.006075  # ADV normalized across wages
vgl_d_nvacdays = 0.092308  # As if at the end of every week paid vacation is taken

# eCom implicit costs
ecom_vac_pay = 0.08
ecom_nvacdays = 0.096153846
ecom_pension = 0
ecom_franchise = 0
ecom_socialfund = 0
ecom_adv = 0
ecom_dinnerpay = 0

imp_cost_source = ['ADV', 'Vac days', 'Vac pay', 'Sociaal fond', 'Pensions', 'Dinner pay', 'Vakbondstientje']


### Cost calculations
def calculate_values(c_del_cao, c_sup_cao, c_del_min, c_del_max, c_sup_max, c_sup_min, c_del_p21, c_del_u18, c_del_p18, c_sup_p21, c_sup_u18, c_sup_p18, c_del_p21ft, c_del_p18ft, c_del_u18ft, c_sup_p21ft, c_sup_p18ft, c_sup_u18ft, c_del_ftpref, c_sup_ftpref, c_del_ptavg, c_sup_ptavg):
    del_cao = c_del_cao
    sup_cao = c_sup_cao

    if not del_cao:
        del_cao = 'vgl_d'
    
    if not sup_cao:
        sup_cao = 'vgl_s'

    del_mingrad =  c_del_min
    sup_mingrad = c_sup_min
    del_maxgrad = c_del_max
    sup_maxgrad = c_sup_max
    p21_del_grad = c_del_p21
    u18_del_grad = c_del_u18
    p18_del_grad = c_del_p18

    p21_sup_grad = c_sup_p21
    u18_sup_grad = c_sup_u18
    p18_sup_grad = c_sup_p18

    p21_del_ft = c_del_p21ft
    p18_del_ft = c_del_p18ft
    u18_del_ft = c_del_u18ft

    p21_sup_ft = c_sup_p21ft
    p18_sup_ft = c_sup_p18ft    
    u18_sup_ft = c_sup_u18ft

    ft_del_daypref = c_del_ftpref
    ft_sup_daypref = c_sup_ftpref

    del_pt_avg_time = c_del_ptavg
    sup_pt_avg_time = c_sup_ptavg

    del_pt_factor = del_pt_avg_time / 40
    sup_pt_factor = sup_pt_avg_time / 40


    for prov in provider:
        prov_grloop = globals()[f'{prov}grad'].copy()
        prov_min = int(locals()[f'{prov}mingrad'])
        prov_max = int(locals()[f'{prov}maxgrad'])
        grad_q[f'{prov}gradq'] = pd.DataFrame(index=shift_slots, columns=weekdays)

        for shift in shift_slots:
            for day in weekdays:
                grad_q[f'{prov}gradq'].loc[shift, day] = (prov_grloop.loc[shift, day] * (prov_max - prov_min)) + prov_min
            if shift == '22-24' and prov.startswith('sup_'):
                grad_q[f'{prov}gradq'].loc[shift, :] = 0

    del_gradq = grad_q['del_gradq']
    sup_gradq = grad_q['sup_gradq']

    for prov in provider:
        prov_est_sch = grad_q[f'{prov}gradq'].copy()

        for ag in labels_wage_groupings:
            for ct in contract_type:
                if ct == 'ft':
                    ct_applied = prov_est_sch * locals()[f'{ag}_{prov}grad'] * locals()[f'{ag}_{prov}ft']
                    ft_pref_prov = locals()[f'ft_{prov}daypref']
                    
                    for time in 'day', 'night':
                        pref_check = globals()[f'{time}_shifts']
                        ftpref_ratio = locals()[f'ft_{prov}daypref'] if time == 'day' else 1 - locals()[f'ft_{prov}daypref']

                        for shift in pref_check:
                            ct_applied.loc[shift] *= ftpref_ratio

                elif ct == 'pt':
                    ct_applied = prov_est_sch * locals()[f'{ag}_{prov}grad'] * (1 - locals()[f'{ag}_{prov}ft'])
                    ft_pref_prov = 1 - locals()[f'ft_{prov}daypref']

                    for time in 'day', 'night':
                            pref_check = globals()[f'{time}_shifts']
                            ftpref_ratio = locals()[f'ft_{prov}daypref'] if time == 'day' else 1 - locals()[f'ft_{prov}daypref']

                            for shift in pref_check:
                                ct_applied.loc[shift] *= ftpref_ratio
                
                
                prov_ct_gradq[f'{ag}_{prov}{ct}'] = ct_applied

    for prov in provider:
        for wg in labels_wage_groupings:
            for ct in contract_type:
                if ct == 'ft': # Set to 40h
                    workercount_det.loc[prov, f'{wg}_{ct}'] = (prov_ct_gradq[f'{wg}_{prov}{ct}'].sum().sum() * 2) / 40
                elif ct == 'pt': # User sets average
                    workercount_det.loc[prov, f'{wg}_{ct}'] = (prov_ct_gradq[f'{wg}_{prov}{ct}'].sum().sum() * 2) / locals()[f'{prov}pt_avg_time']
                workercount_sum.loc[prov, ct] = workercount_det.loc[prov, [col for col in workercount_det.columns if f'{ct}' in col]].sum()
            workercount_sum.loc[prov, wg] = workercount_det.loc[prov, [col for col in workercount_det.columns if f'{wg}' in col]].sum()


    for prov in provider:
        for ct in contract_type:
            quantity_costs.loc[prov, 'vakbondstientje'] = workercount_sum.loc[prov, [col for col in workercount_sum.columns if f'{ct}' in col]].sum() * 22.71

    ############

    # (1)
    for cao in CAO_wage_list:
        cao_bonus_ratio[cao] = pd.DataFrame(index=shift_slots)
        cao_bonus_ratio[cao] = bonus.filter(regex=f'^{cao}')
        for cao, df in cao_bonus_ratio.items():
            if len(df.columns) == len(weekdays):
                df.columns = weekdays
    # (2) CBW
    for cao, df in cao_bonus_ratio.items():
        if len(df.columns) == len(weekdays):
            for age in labels_wage_groupings: 
                wage_brutto = grouped_wages.loc[age, cao] * 2 #Using 2h shift slots
                week_wage_b = df.mul(wage_brutto)
                week_wage_b.index = shift_slots
                week_wage_b.columns = weekdays
                cao_bonus_wage[f"{cao}_{age}"] = week_wage_b    
    # (3)  
    for prov in provider:
        for cao in CAO_wage_list:
            for ag in labels_wage_groupings:
                for ct in contract_type:
                    c_b_w = f"{cao}_{ag}"
                    cao_bonus_get = cao_bonus_wage.get(c_b_w, pd.DataFrame())
                    if not cao_bonus_get.empty:
                        age_pq = prov_ct_gradq[f'{ag}_{prov}{ct}']
                        cao_prov_age_pq[f"{cao}_{prov}{ag}_{ct}"] = pd.DataFrame(index=shift_slots, columns=weekdays)
                        if ag == 'u18':
                            cao_prov_age_pq[f"{cao}_{prov}{ag}_{ct}"] = age_pq * cao_bonus_get
                        elif ag == 'p18':
                            cao_prov_age_pq[f"{cao}_{prov}{ag}_{ct}"] = age_pq * cao_bonus_get
                        elif ag == 'p21':
                            cao_prov_age_pq[f"{cao}_{prov}{ag}_{ct}"] = age_pq * cao_bonus_get
                    continue   


    #######

    for prov in provider: 
        for cao in CAO_wage_list:
            for ag in labels_wage_groupings:
                wq_fill = f'{prov}{ag}'
                wpq_fill = f'{prov}{cao}_{ag}'
                try: 
                    week_q[wq_fill] = prov_ct_gradq[f'{ag}_{prov}ft'] + prov_ct_gradq[f'{ag}_{prov}pt']
                    week_pq[wpq_fill] = cao_prov_age_pq[f"{cao}_{prov}{ag}_ft"] + cao_prov_age_pq[f"{cao}_{prov}{ag}_pt"]
                except KeyError:
                    continue

    #######
    for prov in provider:
        for cao in CAO_wage_list:
            detailed_implicit_wagecosts_pac[f'{prov}{cao}'] = pd.DataFrame(index=labels_wage_groupings, columns=imp_cost_source)

            try:
                nvacpay = globals()[f'{cao}_vac_pay']
                nvacdays = globals()[f'{cao}_nvacdays']
                nadv = globals()[f'{cao}_adv']
                socialfund = globals()[f'{cao}_socialfund']
                pension = globals()[f'{cao}_pension']
                franchise = globals()[f'{cao}_franchise']

                for ag in labels_wage_groupings:    
                    detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, 'ADV'] = week_q[f'{prov}{ag}'].sum().sum() * 2 * grouped_wages.loc[ag, cao] * nadv
                    detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, 'Vac days'] = week_q[f'{prov}{ag}'].sum().sum() * (((1 + nadv) * 2 * grouped_wages.loc[ag, cao]) * nvacdays)
                    detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, 'Vac pay'] = week_q[f'{prov}{ag}'].sum().sum() * ((2 * grouped_wages.loc[ag, cao] * (1 + nadv)) * nvacpay)
                    detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, 'Sociaal fond'] = week_q[f'{prov}{ag}'].sum().sum() * (2 * grouped_wages.loc[ag, cao] * (1 + nadv)) * socialfund
                    detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, 'Vakbondstientje'] = workercount_sum.loc[prov, ag] * (22.71 / 52) # Must adjust part-time factor to it
                    if ag == 'p21':
                        detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, 'Pensions'] = week_q[f'{prov}{ag}'].sum().sum() * ((2 * grouped_wages.loc[ag, cao] * (1 + nadv)) - franchise) * pension
                    if cao == 'vgl_d':
                        detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, 'Dinner pay'] = (week_q[f'{prov}{ag}'].iloc[6, :].sum() * 5.45)
            except KeyError:
                continue
    ####
 
    
    
    for prov in provider:
        for cao in CAO_wage_list:
                try:
                    exp_temp = 0
                    imp_temp = detailed_implicit_wagecosts_pac[f'{prov}{cao}'].sum().sum()
                    for ag in labels_wage_groupings:
                        exp_temp += week_pq[f'{prov}{cao}_{ag}'].sum().sum()
                    explicit_week_costs.loc[prov, cao] = exp_temp
                    implicit_week_costs.loc[prov, cao] = imp_temp
                except KeyError:
                    continue
    

    for prov in provider:
        for cao in CAO_wage_list:
            descriptive_stats[f'{prov}{cao}'] = pd.DataFrame(index=labels_wage_groupings, columns=d_stats)
            for ag in labels_wage_groupings:
                try:
                    descriptive_stats[f'{prov}{cao}'].loc[ag, 'Real hourly cost'] = round(((week_pq[f'{prov}{cao}_{ag}'].sum().sum() + detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, :].sum()) / 2) / week_q[f'{prov}{ag}'].sum().sum() , 3)
                    descriptive_stats[f'{prov}{cao}'].loc[ag, 'Total week cost'] = round(week_pq[f'{prov}{cao}_{ag}'].sum().sum() + detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, :].sum(), 3)
                    descriptive_stats[f'{prov}{cao}'].loc[ag, 'Avg weekday cost'] = round(((week_pq[f'{prov}{cao}_{ag}'].iloc[:, :5].sum().sum() / 5) + detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, :].sum() * (5/7)) / week_q[f'{prov}{ag}'].iloc[:, :5].sum().sum(), 3)
                    descriptive_stats[f'{prov}{cao}'].loc[ag, 'Avg weekend cost'] = round(((week_pq[f'{prov}{cao}_{ag}'].iloc[:, 5:].sum().sum() / 2) + detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, :].sum() * (2/7)) / week_q[f'{prov}{ag}'].iloc[:, 5:].sum().sum(), 3)
                    descriptive_stats[f'{prov}{cao}'].loc[ag, 'Avg day shift cost'] = round(((week_pq[f'{prov}{cao}_{ag}'].iloc[:4, :].sum().sum() / 4) + (detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, :].sum() * (1/2))) / week_q[f'{prov}{ag}'].iloc[:4, :].sum().sum(), 3)
                    descriptive_stats[f'{prov}{cao}'].loc[ag, 'Avg night shift cost'] = round(((week_pq[f'{prov}{cao}_{ag}'].iloc[4:, :].sum().sum() / 4) + (detailed_implicit_wagecosts_pac[f'{prov}{cao}'].loc[ag, :].sum() * (1/2))) / week_q[f'{prov}{ag}'].iloc[4:, :].sum().sum(), 3)
                except KeyError:
                    continue
                


    ###

    del_exp1 = round(explicit_week_costs.loc['del_', del_cao], 4)
    del_imp1 = round(implicit_week_costs.loc['del_', del_cao], 4)
    sup_exp1 = round(explicit_week_costs.loc['sup_', sup_cao], 4)
    sup_imp1 = round(implicit_week_costs.loc['sup_', sup_cao], 4)

    explicit_costw = [del_exp1, sup_exp1]
    implicit_costw = [del_imp1, sup_imp1]

    explicit_costm = [del_exp1 * 4, sup_exp1 * 4]
    implicit_costm = [del_imp1 * 4, sup_imp1 * 4]


    for prov in provider:
        expc = locals()[f'{prov}exp1']
        impc = locals()[f'{prov}imp1']
        
        cao = locals()[f'{prov}cao']
        if cao == 'vgl_d' or cao == 'vgl_s':
            globals()[f'{prov}exp_lt'] = (expc * 21) + ((1.025)*expc * 38) + ((1.025)*(1.01)*expc * 17) + ((1.025)*(1.01)*(1.015)*expc * 13)
            globals()[f'{prov}imp_lt'] = (impc * 21) + ((1.025)*impc * 38) + ((1.025)*(1.01)*impc * 17) + ((1.025)*(1.01)*(1.015)*impc * 13)
        elif cao == 'ecom':
            globals()[f'{prov}exp_lt'] = (expc * 17) + ((1.03)*expc * 52) + ((1.03)*(1.03)*expc * 21)
            globals()[f'{prov}imp_lt'] = (impc * 17) + ((1.03)*impc * 52) + ((1.03)*(1.03)*impc * 21)


    impl_lt = [del_imp_lt, sup_imp_lt]
    expl_lt = [del_exp_lt, sup_exp_lt]

    ##### May need to correct for some costs x2 style
    del_brut_wage = [week_q['del_u18'].sum().sum() * grouped_wages.loc['u18', f'{del_cao}'], week_q['del_p18'].sum().sum() * grouped_wages.loc['p18', f'{del_cao}'], week_q['del_p21'].sum().sum() * grouped_wages.loc['p21', f'{del_cao}']]
    del_bon_wage = [(week_pq[f'del_{del_cao}_u18'].sum().sum() - (week_q['del_u18'].sum().sum() * 2 * grouped_wages.loc['u18', f'{del_cao}'])), (week_pq[f'del_{del_cao}_p18'].sum().sum() - (week_q['del_p18'].sum().sum() * 2 * grouped_wages.loc['p18', f'{del_cao}'])), (week_pq[f'del_{del_cao}_p21'].sum().sum() - (week_q['del_p21'].sum().sum() * 2 *grouped_wages.loc['p21', f'{del_cao}']))]
    del_adv = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'ADV'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'ADV'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'ADV']]
    del_vacd = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Vac days'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Vac days'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Vac days']]
    del_vacp = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Vac pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Vac pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Vac pay']]
    del_sf = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Sociaal fond'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Sociaal fond'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Sociaal fond']]
    del_pens = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Pensions'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Pensions'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Pensions']]
    del_dinp = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Dinner pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Dinner pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Dinner pay']]
    del_vb = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Vakbondstientje'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Vakbondstientje'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Vakbondstientje']]

    sup_brut_wage = [week_q['del_u18'].sum().sum() * grouped_wages.loc['u18', f'{del_cao}'], week_q['del_p18'].sum().sum() * grouped_wages.loc['p18', f'{del_cao}'], week_q['del_p21'].sum().sum() * grouped_wages.loc['p21', f'{del_cao}']]
    sup_bon_wage = [(week_pq[f'del_{del_cao}_u18'].sum().sum() - (week_q['del_u18'].sum().sum() * 2 * grouped_wages.loc['u18', f'{del_cao}'])), (week_pq[f'del_{del_cao}_p18'].sum().sum() - (week_q['del_p18'].sum().sum() * 2 *grouped_wages.loc['p18', f'{del_cao}'])), (week_pq[f'del_{del_cao}_p21'].sum().sum() - (week_q['del_p21'].sum().sum() * 2 *grouped_wages.loc['p21', f'{del_cao}']))]
    sup_adv = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'ADV'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'ADV'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'ADV']]
    sup_vacd = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Vac days'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Vac days'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Vac days']]
    sup_vacp = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Vac pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Vac pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Vac pay']]
    sup_sf = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Sociaal fond'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Sociaal fond'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Sociaal fond']]
    sup_pens = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Pensions'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Pensions'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Pensions']]
    sup_dinp = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Dinner pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Dinner pay'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Dinner pay']]
    sup_vb = [detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['u18', 'Vakbondstientje'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p18', 'Vakbondstientje'], detailed_implicit_wagecosts_pac[f'del_{del_cao}'].loc['p21', 'Vakbondstientje']]

    # Directly create new axes maximums
    #del_det_max = del_brut_wage + del_bon_wage + del_adv + del_vacd + del_vacp + del_sf + del_pens + del_dinp + del_vb
    #sup_det_max = sup_brut_wage + sup_bon_wage + sup_adv + sup_vacd + sup_vacp + sup_sf + sup_pens + sup_dinp + sup_vb

    return explicit_costw, implicit_costw, explicit_costm, implicit_costm, expl_lt, impl_lt, del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf, del_pens, del_dinp, del_vb, sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf, sup_pens, sup_dinp, sup_vb


### Chart creation
b1_w = 0.4
b1_pos = np.arange(len(provlabel))

b2_w = 0.2
b2_pos = np.arange(len(labels_wage_groupings)) # might be wrong

bar_del_u18 = np.arange(len(labels_wage_groupings))
bar_del_p18 = [i + b2_w for i in bar_del_u18]
bar_del_p21 = [i + b2_w for i in bar_del_p18]

bar_sup_u18 = np.arange(len(labels_wage_groupings))
bar_sup_p18 = [i + b2_w for i in bar_sup_u18]
bar_sup_p21 = [i + b2_w for i in bar_sup_p18]

def charts(explicit_costw, implicit_costw, explicit_costm, implicit_costm, expl_lt, impl_lt, del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf, del_pens, del_dinp, del_vb, sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf, sup_pens, sup_dinp, sup_vb):
    
    plt.style.use('seaborn')
    
    # Stats2
    fig1w, axw = plt.subplots(figsize=(3, 3))
    bar_explicit_costw = axw.bar(provlabel, explicit_costw, b1_w, label='Explicit costs')
    bar_implicit_costw = axw.bar(provlabel, implicit_costw, b1_w, bottom=explicit_costw, label='Implicit costs')
    for i in range(len(explicit_costw)):
        plt.text(provlabel[i], explicit_costw[i]/2, str(round(explicit_costw[i])), ha='center', va='center', fontsize=8)
    for i in range(len(implicit_costw)):
        plt.text(provlabel[i], explicit_costw[i] + implicit_costw[i]/2, str(round(implicit_costw[i])), ha='center', va='center', fontsize=8)
    axw.set_xlabel('Business model', fontsize=8)
    axw.set_ylabel('Total labor costs (€)', fontsize=8)
    axw.set_title('Total weekly labor costs by business model', fontsize=8)
    axw.legend(fontsize='small')
    axw.set_ylim(0, (max(explicit_costw) + max(implicit_costw))* 1.1)

    fig1m, axm = plt.subplots(figsize=(3, 3))
    bar_explicit_costm = axm.bar(provlabel, explicit_costm, b1_w, label='Explicit costs')
    bar_implicit_costm = axm.bar(provlabel, implicit_costm, b1_w, bottom=explicit_costm, label='Implicit costs')
    for i in range(len(explicit_costm)):
        plt.text(provlabel[i], explicit_costm[i]/2, str(round(explicit_costm[i])), ha='center', va='bottom', fontsize=8)
    for i in range(len(implicit_costm)):
        plt.text(provlabel[i], explicit_costm[i] + implicit_costm[i]/2, str(round(implicit_costm[i])), ha='center', va='bottom', fontsize=8)
    axm.set_xlabel('Business model', fontsize=8)   
    axm.set_ylabel('Total labor costs (€)', fontsize=8)
    axm.set_title('Total monthly labor costs by business model', fontsize=8)
    axm.legend(fontsize='small')
    axm.set_ylim(0, (max(explicit_costm) + max(implicit_costm))* 1.1)

    fig1lt, axlt = plt.subplots(figsize=(3, 3))
    bar_explicit_costlt = axlt.bar(provlabel, expl_lt, b1_w, label='Explicit costs')
    bar_implicit_costlt = axlt.bar(provlabel, impl_lt, b1_w, bottom=expl_lt, label='Implicit costs')
    for i in range(len(expl_lt)):
        plt.text(provlabel[i], expl_lt[i]/2, str(round(expl_lt[i])), ha='center', va='bottom', fontsize=8)
    for i in range(len(impl_lt)):
        plt.text(provlabel[i], expl_lt[i] + impl_lt[i]/2, str(round(impl_lt[i])), ha='center', va='bottom', fontsize=8)
    axlt.set_xlabel('Business model', fontsize=8)
    axlt.set_ylabel('Total labor costs (€)', fontsize=8)
    axlt.set_title('90w costs (Jan22-Oct23) by business model', fontsize=8)
    axlt.legend(fontsize='small')
    axlt.set_ylim(0, (max(expl_lt) + max(impl_lt))* 1.1)

    #height_2d = [sum(x) for x in zip(del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf, del_pens, del_dinp, del_vb)]
    #max_height2d = max(height_2d)
    #max_height2d = (max(del_brut_wage) + max(del_bon_wage) + max(del_adv) + max(del_vacd) + max(del_vacp) + max(del_sf) + max(del_pens) + max(del_dinp) + max(del_vb))
    #print(max_height2d)

    # Stats3
    fig2d, axd = plt.subplots(figsize=(3, 3))
    bar_del_brut = axd.bar(bar_del_u18, del_brut_wage, b2_w, label='Brutto wage')
    bar_del_bon = axd.bar(bar_del_u18, del_bon_wage, b2_w, bottom=del_brut_wage, label='Bonuses')
    bar_del_adv = axd.bar(bar_del_u18, del_adv, b2_w, bottom=[i+j for i,j in zip(del_brut_wage, del_bon_wage)], label='ADV')
    bar_del_vacd = axd.bar(bar_del_u18, del_vacd, b2_w, bottom=[i+j+k for i,j,k in zip(del_brut_wage, del_bon_wage, del_adv)], label='Vacation days')
    bar_del_vacp =axd.bar(bar_del_u18, del_vacp, b2_w, bottom=[i+j+k+l for i,j,k,l in zip(del_brut_wage, del_bon_wage, del_adv, del_vacd)], label='Vacation pay')
    bar_del_sf = axd.bar(bar_del_u18, del_sf, b2_w, bottom=[i+j+k+l+m for i,j,k,l,m in zip(del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp)], label='Sociaal fond')
    bar_del_pens = axd.bar(bar_del_u18, del_pens, b2_w, bottom=[i+j+k+l+m+n for i,j,k,l,m,n in zip(del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf)], label='Pensions')
    bar_del_dinp = axd.bar(bar_del_u18, del_dinp, b2_w, bottom=[i+j+k+l+m+n+o for i,j,k,l,m,n,o in zip(del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf, del_pens)], label='Dinner pay')
    bar_del_vb = axd.bar(bar_del_u18, del_vb, b2_w, bottom=[i+j+k+l+m+n+o+p for i,j,k,l,m,n,o,p in zip(del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf, del_pens, del_dinp)], label='Vakbondstientje')
    axd.set_xlabel('Age', fontsize=8)
    axd.set_ylabel('Costs', fontsize=8)
    axd.set_title('Deliverer costs per age group', fontsize=8)
    axd.legend(fontsize='small')
    axd.set_xticks(bar_del_u18, ['-18', '18-21', '+21'], fontsize=8)
    axd.set_ylim(0, (max(explicit_costw) + max(implicit_costw))* 1.1 * .6)

    #height_2s = [sum(x) for x in zip(sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf, sup_pens, sup_dinp, sup_vb)]
    #max_height2s = max(height_2s)
    #max_height2s = (max(sup_brut_wage) + max(sup_bon_wage) + max(sup_adv) + max(sup_vacd) + max(sup_vacp) + max(sup_sf) + max(sup_pens) + max(sup_dinp) + max(sup_vb))
    #print(max_height2s)

    fig2s, axs = plt.subplots(figsize=(3, 3))
    bar_sup_brut = axs.bar(bar_sup_u18, sup_brut_wage, b2_w, label='Brutto wage')
    bar_sup_bon = axs.bar(bar_sup_u18, sup_bon_wage, b2_w, bottom=sup_brut_wage, label='Bonuses')
    bar_sup_adv = axs.bar(bar_sup_u18, sup_adv, b2_w, bottom=[i+j for i,j in zip(sup_brut_wage, sup_bon_wage)], label='ADV')
    bar_sup_vacd = axs.bar(bar_sup_u18, sup_vacd, b2_w, bottom=[i+j+k for i,j,k in zip(sup_brut_wage, sup_bon_wage, sup_adv)], label='Vacation days')
    bar_sup_vacp = axs.bar(bar_sup_u18, sup_vacp, b2_w, bottom=[i+j+k+l for i,j,k,l in zip(sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd)], label='Vacation pay')
    bar_sup_sf = axs.bar(bar_sup_u18, sup_sf, b2_w, bottom=[i+j+k+l+m for i,j,k,l,m in zip(sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp)], label='Sociaal fond')
    bar_sup_pens = axs.bar(bar_sup_u18, sup_pens, b2_w, bottom=[i+j+k+l+m+n for i,j,k,l,m,n in zip(sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf)], label='Pensions')
    bar_sup_dinp = axs.bar(bar_sup_u18, sup_dinp, b2_w, bottom=[i+j+k+l+m+n+o for i,j,k,l,m,n,o in zip(sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf, sup_pens)], label='Dinner pay')
    bar_sup_vb = axs.bar(bar_sup_u18, sup_vb, b2_w, bottom=[i+j+k+l+m+n+o+p for i,j,k,l,m,n,o,p in zip(sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf, sup_pens, sup_dinp)], label='Vakbondstientje')
    axs.set_xlabel('Age', fontsize=8)
    axs.set_ylabel('Costs', fontsize=8)
    axs.set_title('Supermarket costs per age group', fontsize=8)
    axs.legend(fontsize='small')
    axs.set_xticks(bar_sup_u18, ['-18', '18-21', '+21'], fontsize=8)
    axs.set_ylim(0, (max(explicit_costw) + max(implicit_costw))* 1.1 * .6)

    chart_bars = {
        'ew': bar_explicit_costw,
        'iw': bar_implicit_costw,
        'em': bar_explicit_costm,
        'im': bar_implicit_costm,
        'elt': bar_explicit_costlt,
        'ilt': bar_implicit_costlt,
        'del_brut': bar_del_brut,
        'd_bon': bar_del_bon,
        'd_adv': bar_del_adv,
        'd_vacd': bar_del_vacd,
        'd_vacp': bar_del_vacp,
        'd_sf': bar_del_sf,
        'd_pens': bar_del_pens,
        'd_dinp': bar_del_dinp,
        'd_vb': bar_del_vb,
        's_brut': bar_sup_brut,
        's_bon': bar_sup_bon,
        's_adv': bar_sup_adv,
        's_vacd': bar_sup_vacd,
        's_vacp': bar_sup_vacp,
        's_sf': bar_sup_sf,
        's_pens': bar_sup_pens,
        's_dinp': bar_sup_dinp,
        's_vb': bar_sup_vb,
    }

    chart_axes = {
        'ax_w': axw,
        'ax_m': axm,
        'ax_lt': axlt,
        'ax_d': axd,
        'ax_s': axs,
    }


    return fig1w, fig1m, fig1lt, fig2d, fig2s, chart_bars, chart_axes


### Input interface
def cost_input_interface(calculator):

    calc_frame =tk.Frame(calculator)
    calc_frame.pack()

    ### Deliverer factors
    del_input_frame = tk.LabelFrame(calc_frame, text='Deliverer cost inputs', font=('Times New Roman', 10))
    del_input_frame.grid(row=0,column=0)

    # Del cost frames
    del_base_frame = tk.LabelFrame(del_input_frame, text='Base cost factors', font=('Times New Roman', 10))
    del_base_frame.grid(row=0, column=0)

    del_prop_frame = tk.LabelFrame(del_input_frame, text='Proportions cost factors', font=('Times New Roman', 10))
    del_prop_frame.grid(row=1, column=0)

    del_pref_frame = tk.LabelFrame(del_input_frame, text='Worker preference cost factors', font=('Times New Roman', 10))
    del_pref_frame.grid(row=2, column=0)


    # Del labels
    del_cao_l = tk.Label(del_base_frame, text='Which CAO to test?', font=('Times New Roman', 10))
    del_cao_l.grid(row=0, column=0)
    del_min_l = tk.Label(del_base_frame, text='Minimum number of workers in a shift', font=('Times New Roman', 10))
    del_min_l.grid(row=0, column=1)
    del_max_l = tk.Label(del_base_frame, text ='Maximum number of workers in a shift', font=('Times New Roman', 10))
    del_max_l.grid(row=0,column=2)

    del_p21_l = tk.Label(del_prop_frame, text='Proportion of +21 workers', font=('Times New Roman', 10))
    del_p21_l.grid(row=0,column=0)
    del_u18_l = tk.Label(del_prop_frame, text='Proportion of -18 workers', font=('Times New Roman', 10))
    del_u18_l.grid(row=0, column=1)
    del_ft_l = tk.Label(del_prop_frame, text='Proportion +21 employees working fulltime', font=('Times New Roman', 10))
    del_ft_l.grid(row=0,column=2)

    del_ft_pref_l = tk.Label(del_pref_frame, text='Proportion of hours fulltimers work during the day', font=('Times New Roman', 10))
    del_ft_pref_l.grid(row=0,column=0)
    del_pt_avgh_l = tk.Label(del_pref_frame, text='Average weekly hours worked by part-time workers', font=('Times New Roman', 10))
    del_pt_avgh_l.grid(row=0,column=1)

    # Del entries
    del_cao_entry = ttk.Combobox(del_base_frame, values=['vgl_s', 'vgl_d', 'ecom'], textvariable=tk.StringVar(value='vgl_d'), font=('Times New Roman', 10))
    del_cao_entry.grid(row=1,column=0)
    del_min = tk.Entry(del_base_frame)
    del_min.insert(0, '7')
    del_min.grid(row=1,column=1)
    del_max = tk.Entry(del_base_frame)
    del_max.insert(0, '20')
    del_max.grid(row=1, column=2)

    del_p21 = tk.Scale(del_prop_frame, from_=0, to=100) ##
    del_p21.set(60)
    del_p21.grid(row=1, column=0)
    del_u18 = tk.Scale(del_prop_frame, from_=0, to=100) ##
    del_u18.set(25)
    del_u18.grid(row=1,column=1)
    del_ft = tk.Scale(del_prop_frame, from_=0, to=100) ##
    del_ft.set(40)
    del_ft.grid(row=1,column=2)

    del_ft_pref = tk.Scale(del_pref_frame, from_=0, to=100)
    del_ft_pref.set(70)
    del_ft_pref.grid(row=1, column=0)
    del_pt_avgh = tk.Entry(del_pref_frame)
    del_pt_avgh.insert(0, '20')
    del_pt_avgh.grid(row=1, column=1)

    ### Supermarket factors
    sup_input_frame = tk.LabelFrame(calc_frame, text='Supermarket cost inputs', font=('Times New Roman', 10))
    sup_input_frame.grid(row=0,column=1)

    # Sup cost frames
    sup_base_frame = tk.LabelFrame(sup_input_frame, text='Base cost factors', font=('Times New Roman', 10))
    sup_base_frame.grid(row=0, column=0)

    sup_prop_frame = tk.LabelFrame(sup_input_frame, text='Proportions cost factors', font=('Times New Roman', 10))
    sup_prop_frame.grid(row=1, column=0)

    sup_pref_frame = tk.LabelFrame(sup_input_frame, text='Worker preference cost factors', font=('Times New Roman', 10))
    sup_pref_frame.grid(row=2, column=0)

    # Sup labels
    sup_cao_l = tk.Label(sup_base_frame, text='Which CAO to test?', font=('Times New Roman', 10))
    sup_cao_l.grid(row=0, column=0)
    sup_min_l = tk.Label(sup_base_frame, text='Minimum number of workers in a shift', font=('Times New Roman', 10))
    sup_min_l.grid(row=0, column=1)
    sup_max_l = tk.Label(sup_base_frame, text ='Maximum number of workers in a shift', font=('Times New Roman', 10))
    sup_max_l.grid(row=0,column=2)

    sup_p21_l = tk.Label(sup_prop_frame, text='Proportion of +21 workers', font=('Times New Roman', 10))
    sup_p21_l.grid(row=0,column=0)
    sup_u18_l = tk.Label(sup_prop_frame, text='Proportion of -18 workers', font=('Times New Roman', 10))
    sup_u18_l.grid(row=0, column=1)
    sup_ft_l = tk.Label(sup_prop_frame, text='Proportion +21 employees working fulltime', font=('Times New Roman', 10))
    sup_ft_l.grid(row=0,column=2)

    sup_ft_pref_l = tk.Label(sup_pref_frame, text='Proportion of hours fulltimers work during the day', font=('Times New Roman', 10))
    sup_ft_pref_l.grid(row=0,column=0)
    sup_pt_avgh_l = tk.Label(sup_pref_frame, text='Average weekly hours worked by part-time workers', font=('Times New Roman', 10))
    sup_pt_avgh_l.grid(row=0,column=1)

    # Sup entries
    sup_cao_entry = ttk.Combobox(sup_base_frame, values=['vgl_s', 'vgl_d', 'ecom'], textvariable=tk.StringVar(value='vgl_s'))
    sup_cao_entry.grid(row=1,column=0)
    sup_min = tk.Entry(sup_base_frame)
    sup_min.insert(0, "8")
    sup_min.grid(row=1,column=1)
    sup_max = tk.Entry(sup_base_frame)
    sup_max.insert(0, "16")
    sup_max.grid(row=1, column=2)

    sup_p21 = tk.Scale(sup_prop_frame, from_=0, to=100) ##
    sup_p21.set(50)
    sup_p21.grid(row=1, column=0)
    sup_u18 = tk.Scale(sup_prop_frame, from_=0, to=100) ##
    sup_u18.set(30)
    sup_u18.grid(row=1,column=1)
    sup_ft = tk.Scale(sup_prop_frame, from_=0, to=100) ##
    sup_ft.set(60)
    sup_ft.grid(row=1,column=2)

    sup_ft_pref = tk.Scale(sup_pref_frame, from_=0, to=100)
    sup_ft_pref.set(80)
    sup_ft_pref.grid(row=1, column=0)
    sup_pt_avgh = tk.Entry(sup_pref_frame)
    sup_pt_avgh.insert(0, "16")
    sup_pt_avgh.grid(row=1, column=1)

    return calc_frame, del_cao_entry, del_min, del_max, del_p21, del_u18, del_ft, del_ft_pref, del_pt_avgh, sup_cao_entry, sup_min, sup_max, sup_p21, sup_u18, sup_ft, sup_ft_pref, sup_pt_avgh


### Cost dashboard
def dashboard(dash_board, fig1w, fig1m, fig1lt, fig2d, fig2s, del_cao_entry, sup_cao_entry):

    dashframe = tk.Frame(dash_board)
    dashframe.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)



    if del_cao_entry is not ['vgl_d', 'vgl_s', 'ecom']:
        del_c_fill = 'vgl_d'
    else:
        del_c_fill = del_cao_entry.get()

    if sup_cao_entry is not ['vgl_d', 'vgl_s', 'ecom']:
        sup_c_fill = 'vgl_s'
    else:    
        sup_c_fill = sup_cao_entry.get()

    des_st_del = descriptive_stats[f'del_{del_c_fill}']
    des_st_sup = descriptive_stats[f'sup_{sup_c_fill}']

    # Stats1
    stats1 = tk.Frame(dashframe, height=400, width=800)
    stats1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
    stats1_labels = {}

    # Labels
    stats1_labels['lrhc'] = tk.Label(stats1, text='Real hourly costs', font=('Times New Roman', 10))
    stats1_labels['lrhc'].grid(row=2, column=0, sticky='nsew')
    stats1_labels['ltwc'] = tk.Label(stats1, text='Total weekly costs', font=('Times New Roman', 10))
    stats1_labels['ltwc'].grid(row=3, column=0, sticky='nsew')
    stats1_labels['lawdc'] = tk.Label(stats1, text='Avg weekday costs', font=('Times New Roman', 10))
    stats1_labels['lawdc'].grid(row=4, column=0, sticky='nsew')
    stats1_labels['lawec'] = tk.Label(stats1, text='Avg weekend costs', font=('Times New Roman', 10))
    stats1_labels['lawec'].grid(row=5, column=0, sticky='nsew')
    stats1_labels['ladsc'] = tk.Label(stats1, text='Avg day shift costs', font=('Times New Roman', 10))
    stats1_labels['ladsc'].grid(row=6, column=0, sticky='nsew')
    stats1_labels['lansc'] = tk.Label(stats1, text='Avg night shift costs', font=('Times New Roman', 10))
    stats1_labels['lansc'].grid(row=7, column=0, sticky='nsew')
    
    stats1_labels['lst1del'] = tk.Label(stats1, text='Deliverers', font=('Times New Roman', 10))
    stats1_labels['lst1del'].grid(row=0, column=1, sticky='nsew')
    stats1_labels['ldu18'] = tk.Label(stats1, text='-18', font=('Times New Roman', 10))
    stats1_labels['ldu18'].grid(row=1, column=1, sticky='nsew')
    stats1_labels['ldp18'] = tk.Label(stats1, text='18-21', font=('Times New Roman', 10))
    stats1_labels['ldp18'].grid(row=1, column=2, sticky='nsew')
    stats1_labels['ldp21'] = tk.Label(stats1, text='+21', font=('Times New Roman', 10))
    stats1_labels['ldp21'].grid(row=1, column=3, sticky='nsew')
    stats1_labels['lst1sup'] = tk.Label(stats1, text='Supermarkets', font=('Times New Roman', 10))
    stats1_labels['lst1sup'].grid(row=0, column=4, sticky='nsew')
    stats1_labels['lsu18'] = tk.Label(stats1, text='-18', font=('Times New Roman', 10))
    stats1_labels['lsu18'].grid(row=1, column=4, sticky='nsew')
    stats1_labels['lsp18'] = tk.Label(stats1, text='18-21', font=('Times New Roman', 10))
    stats1_labels['lsp18'].grid(row=1, column=5, sticky='nsew')
    stats1_labels['lsp21'] = tk.Label(stats1, text='+21', font=('Times New Roman', 10))
    stats1_labels['lsp21'].grid(row=1, column=6, sticky='nsew')

    # Deliverer stats
    stats1_labels['delrhcu18'] = tk.Label(stats1, text=des_st_del.loc['u18', 'Real hourly cost'], font=('Times New Roman', 10))
    stats1_labels['delrhcu18'].grid(row=2, column=1, sticky='nsew')
    stats1_labels['deltwcu18'] = tk.Label(stats1, text=des_st_del.loc['u18', 'Total week cost'], font=('Times New Roman', 10))
    stats1_labels['deltwcu18'].grid(row=3, column=1, sticky='nsew')
    stats1_labels['delawdcu18'] = tk.Label(stats1, text=des_st_del.loc['u18', 'Avg weekday cost'], font=('Times New Roman', 10))
    stats1_labels['delawdcu18'].grid(row=4, column=1, sticky='nsew')
    stats1_labels['delawecu18'] = tk.Label(stats1, text=des_st_del.loc['u18', 'Avg weekend cost'], font=('Times New Roman', 10))
    stats1_labels['delawecu18'].grid(row=5, column=1, sticky='nsew')
    stats1_labels['deladscu18'] = tk.Label(stats1, text=des_st_del.loc['u18', 'Avg day shift cost'], font=('Times New Roman', 10))    
    stats1_labels['deladscu18'].grid(row=6, column=1, sticky='nsew')
    stats1_labels['delanscu18'] = tk.Label(stats1, text=des_st_del.loc['u18', 'Avg night shift cost'], font=('Times New Roman', 10))
    stats1_labels['delanscu18'].grid(row=7, column=1, sticky='nsew')

    stats1_labels['delrhcp18'] = tk.Label(stats1, text=des_st_del.loc['p18', 'Real hourly cost'], font=('Times New Roman', 10))
    stats1_labels['delrhcp18'].grid(row=2, column=2, sticky='nsew')
    stats1_labels['deltwcp18'] = tk.Label(stats1, text=des_st_del.loc['p18', 'Total week cost'], font=('Times New Roman', 10))
    stats1_labels['deltwcp18'].grid(row=3, column=2, sticky='nsew')
    stats1_labels['delawdcp18'] = tk.Label(stats1, text=des_st_del.loc['p18', 'Avg weekday cost'], font=('Times New Roman', 10))
    stats1_labels['delawdcp18'].grid(row=4, column=2, sticky='nsew')
    stats1_labels['delawecp18'] = tk.Label(stats1, text=des_st_del.loc['p18', 'Avg weekend cost'], font=('Times New Roman', 10))
    stats1_labels['delawecp18'].grid(row=5, column=2, sticky='nsew')
    stats1_labels['deladscp18'] = tk.Label(stats1, text=des_st_del.loc['p18', 'Avg day shift cost'], font=('Times New Roman', 10))
    stats1_labels['deladscp18'].grid(row=6, column=2, sticky='nsew')
    stats1_labels['delanscp18'] = tk.Label(stats1, text=des_st_del.loc['p18', 'Avg night shift cost'], font=('Times New Roman', 10))
    stats1_labels['delanscp18'].grid(row=7, column=2, sticky='nsew')

    stats1_labels['delrhcp21'] = tk.Label(stats1, text=des_st_del.loc['p21', 'Real hourly cost'], font=('Times New Roman', 10))
    stats1_labels['delrhcp21'].grid(row=2, column=3, sticky='nsew')
    stats1_labels['deltwcp21'] = tk.Label(stats1, text=des_st_del.loc['p21', 'Total week cost'], font=('Times New Roman', 10))
    stats1_labels['deltwcp21'].grid(row=3, column=3, sticky='nsew')
    stats1_labels['delawdcp21'] = tk.Label(stats1, text=des_st_del.loc['p21', 'Avg weekday cost'], font=('Times New Roman', 10))
    stats1_labels['delawdcp21'].grid(row=4, column=3, sticky='nsew')  
    stats1_labels['delawecp21'] = tk.Label(stats1, text=des_st_del.loc['p21', 'Avg weekend cost'], font=('Times New Roman', 10))
    stats1_labels['delawecp21'].grid(row=5, column=3, sticky='nsew')
    stats1_labels['deladscp21'] = tk.Label(stats1, text=des_st_del.loc['p21', 'Avg day shift cost'], font=('Times New Roman', 10))
    stats1_labels['deladscp21'].grid(row=6, column=3, sticky='nsew')
    stats1_labels['delanscp21'] = tk.Label(stats1, text=des_st_del.loc['p21', 'Avg night shift cost'], font=('Times New Roman', 10))
    stats1_labels['delanscp21'].grid(row=7, column=3, sticky='nsew')

    # Supermarket stats
    stats1_labels['suprhcu18'] = tk.Label(stats1, text=des_st_sup.loc['u18', 'Real hourly cost'], font=('Times New Roman', 10))
    stats1_labels['suprhcu18'].grid(row=2, column=4, sticky='nsew')
    stats1_labels['suptwcu18'] = tk.Label(stats1, text=des_st_sup.loc['u18', 'Total week cost'], font=('Times New Roman', 10))
    stats1_labels['suptwcu18'].grid(row=3, column=4, sticky='nsew')
    stats1_labels['supawdcu18'] = tk.Label(stats1, text=des_st_sup.loc['u18', 'Avg weekday cost'], font=('Times New Roman', 10))
    stats1_labels['supawdcu18'].grid(row=4, column=4, sticky='nsew')
    stats1_labels['supawecu18'] = tk.Label(stats1, text=des_st_sup.loc['u18', 'Avg weekend cost'], font=('Times New Roman', 10))
    stats1_labels['supawecu18'].grid(row=5, column=4, sticky='nsew')
    stats1_labels['supadscu18'] = tk.Label(stats1, text=des_st_sup.loc['u18', 'Avg day shift cost'], font=('Times New Roman', 10))
    stats1_labels['supadscu18'].grid(row=6, column=4, sticky='nsew')
    stats1_labels['supanscu18'] = tk.Label(stats1, text=des_st_sup.loc['u18', 'Avg night shift cost'], font=('Times New Roman', 10))
    stats1_labels['supanscu18'].grid(row=7, column=4, sticky='nsew')

    stats1_labels['suprhcp18'] = tk.Label(stats1, text=des_st_sup.loc['p18', 'Real hourly cost'], font=('Times New Roman', 10))
    stats1_labels['suprhcp18'].grid(row=2, column=5, sticky='nsew')
    stats1_labels['suptwcp18'] = tk.Label(stats1, text=des_st_sup.loc['p18', 'Total week cost'], font=('Times New Roman', 10))
    stats1_labels['suptwcp18'].grid(row=3, column=5, sticky='nsew')
    stats1_labels['supawdcp18'] = tk.Label(stats1, text=des_st_sup.loc['p18', 'Avg weekday cost'], font=('Times New Roman', 10))
    stats1_labels['supawdcp18'].grid(row=4, column=5, sticky='nsew')
    stats1_labels['supawecp18'] = tk.Label(stats1, text=des_st_sup.loc['p18', 'Avg weekend cost'], font=('Times New Roman', 10))
    stats1_labels['supawecp18'].grid(row=5, column=5, sticky='nsew')
    stats1_labels['supadscp18'] = tk.Label(stats1, text=des_st_sup.loc['p18', 'Avg day shift cost'], font=('Times New Roman', 10))
    stats1_labels['supadscp18'].grid(row=6, column=5, sticky='nsew')
    stats1_labels['supanscp18'] = tk.Label(stats1, text=des_st_sup.loc['p18', 'Avg night shift cost'], font=('Times New Roman', 10))
    stats1_labels['supanscp18'].grid(row=7, column=5, sticky='nsew')


    stats1_labels['suprhcp21'] = tk.Label(stats1, text=des_st_sup.loc['p21', 'Real hourly cost'], font=('Times New Roman', 10))
    stats1_labels['suprhcp21'].grid(row=2, column=6, sticky='nsew')
    stats1_labels['suptwcp21'] = tk.Label(stats1, text=des_st_sup.loc['p21', 'Total week cost'], font=('Times New Roman', 10))
    stats1_labels['suptwcp21'].grid(row=3, column=6, sticky='nsew') 
    stats1_labels['supawdcp21'] = tk.Label(stats1, text=des_st_sup.loc['p21', 'Avg weekday cost'], font=('Times New Roman', 10))
    stats1_labels['supawdcp21'].grid(row=4, column=6, sticky='nsew')
    stats1_labels['supawecp21'] = tk.Label(stats1, text=des_st_sup.loc['p21', 'Avg weekend cost'], font=('Times New Roman', 10))
    stats1_labels['supawecp21'].grid(row=5, column=6, sticky='nsew')
    stats1_labels['supadscp21'] = tk.Label(stats1, text=des_st_sup.loc['p21', 'Avg day shift cost'], font=('Times New Roman', 10))
    stats1_labels['supadscp21'].grid(row=6, column=6, sticky='nsew')
    stats1_labels['supanscp21'] = tk.Label(stats1, text=des_st_sup.loc['p21', 'Avg night shift cost'], font=('Times New Roman', 10))
    stats1_labels['supanscp21'].grid(row=7, column=6, sticky='nsew')


    # Stats2
    stats2 = tk.Frame(dashframe, bg='blue')
    stats2.grid(row=0, column=1, rowspan=2, sticky='nsew')

    stats2_coord = []

    f1w = FigureCanvasTkAgg(fig1w, stats2)
    f1w.draw()
    f1w.get_tk_widget().grid(row=0, column=0, sticky='nsew')
    stats2_coord.append((f1w, (0, 0)))

    f1m = FigureCanvasTkAgg(fig1m, stats2)
    f1m.draw()
    f1m.get_tk_widget().grid(row=1, column=0, sticky='nsew')
    stats2_coord.append((f1m, (1, 0)))

    f1y = FigureCanvasTkAgg(fig1lt, stats2)
    f1y.draw()
    f1y.get_tk_widget().grid(row=2, column=0, sticky='nsew')
    stats2_coord.append((f1y, (2, 0)))


    # Stats3
    stats3 = tk.Frame(dashframe, height=400, width=800)
    stats3.grid(row=1, column=0, sticky='nsew')

    stats3_coord = []

    det_del = FigureCanvasTkAgg(fig2d, stats3)
    det_del.draw()
    det_del.get_tk_widget().grid(row=0, column=0, sticky='nsew')
    stats3_coord.append((det_del, (0, 0)))

    det_sup = FigureCanvasTkAgg(fig2s, stats3)
    det_sup.draw()
    det_sup.get_tk_widget().grid(row=0, column=1, sticky='nsew')
    stats3_coord.append((det_sup, (0, 1)))

    return dashframe, stats1, stats2, stats3, stats1_labels, stats2_coord, stats3_coord


### Update calls
def stats_config(c_del_cao, c_sup_cao):

    d_stat_abbr = {
        'rhc': 'Real hourly cost',
        'twc': 'Total week cost',
        'awdc': 'Avg weekday cost',
        'awec': 'Avg weekend cost',
        'adsc': 'Avg day shift cost',
        'ansc': 'Avg night shift cost'
    }

    provlab = ['del', 'sup']

    for prov in provlab:
        if prov == 'del':
            checked_cao = c_del_cao
        elif prov == 'sup':
            checked_cao = c_sup_cao
        des_st = descriptive_stats[f'{prov}_{checked_cao}']
        for ag in labels_wage_groupings:
            for abr, name in d_stat_abbr.items():
                stats1_labels[f'{prov}{abr}{ag}'].configure(text=des_st.loc[ag, name], font=('Times New Roman', 10))

def bar_config(chart_bars, config_chart_bars, chart_axes, config_chart_axes):
    for bar_name, new_item in config_chart_bars.items():
        for bar, item in zip(chart_bars[bar_name], new_item):
            bar.set_height(item)
    for ax, new_ax in config_chart_axes.items():
        chart_axes[ax].set_ylim(0, new_ax())
        chart_axes[ax].figure.canvas.draw_idle()
        chart_axes[ax].figure.canvas.flush_events()


##### MAIN
def main_gui():
    global stats1, stats2, stats3, stats1_labels
    calculator = tk.Tk()
    calculator.geometry('600x600')
    calculator.title('Cost inputs')

    dash_board = tk.Toplevel(calculator)
    dash_board.title('Cost Dashboard')
    dash_board.geometry('600x600')
    dash_board.state('zoomed')

    calc_frame, del_cao_entry, del_min, del_max, del_p21, del_u18, del_ft, del_ft_pref, del_pt_avgh, sup_cao_entry, sup_min, sup_max, sup_p21, sup_u18, sup_ft, sup_ft_pref, sup_pt_avgh = cost_input_interface(calculator)

    if del_cao_entry is None:
        del_cao_entry = 'vgl_d'

    if sup_cao_entry is None:
        sup_cao_entry = 'vgl_s'

    ###
    upd_del_cao = del_cao_entry
    upd_sup_cao = sup_cao_entry

    upd_del_min = del_min
    upd_sup_min = sup_min

    upd_del_max = del_max
    upd_sup_max = sup_max

    upd_del_p21 = del_p21
    upd_del_u18 = del_u18

    upd_sup_p21 = sup_p21
    upd_sup_u18 = sup_u18

    upd_del_p21ft = del_ft
    upd_del_u18ft = 0
    
    upd_sup_p21ft = sup_ft
    upd_sup_u18ft = 0

    upd_del_ftpref = del_ft_pref
    upd_sup_ftpref = sup_ft_pref

    upd_del_ptavg = del_pt_avgh
    upd_sup_ptavg = sup_pt_avgh

    c_del_cao = ''
    c_sup_cao = ''

    c_del_min = 0
    c_sup_min = 0

    c_del_max = 0
    c_sup_max = 0 

    c_del_p21 = 0
    c_del_u18 = 0
    c_del_p18 = 0

    c_sup_p21 = 0
    c_sup_u18 = 0
    c_sup_p18 = 0

    c_del_p21ft = 0
    c_del_p18ft = 0
    c_del_u18ft = 0

    c_sup_p21ft = 0
    c_sup_p18ft = 0
    c_sup_u18ft = 0

    c_del_ftpref = 0
    c_sup_ftpref = 0

    c_del_ptavg = 0
    c_sup_ptavg = 0

    upd_del_cao = del_cao_entry.get()
    upd_sup_cao = sup_cao_entry.get()

    upd_del_min = del_min.get()
    upd_sup_min = sup_min.get()

    upd_del_max = del_max.get()
    upd_sup_max = sup_max.get()

    upd_del_p21 = del_p21.get()
    upd_del_u18 = del_u18.get()

    upd_sup_p21 = sup_p21.get()
    upd_sup_u18 = sup_u18.get()

    upd_del_p21ft = del_ft.get()
    upd_del_u18ft = 0
    
    upd_sup_p21ft = sup_ft.get() 
    upd_sup_u18ft = 0

    upd_del_ftpref = del_ft_pref.get()
    upd_sup_ftpref = sup_ft_pref.get()

    upd_del_ptavg = int(del_pt_avgh.get())
    upd_sup_ptavg = int(sup_pt_avgh.get())

    c_del_cao = upd_del_cao
    c_sup_cao = upd_sup_cao

    c_del_min = upd_del_min
    c_sup_min = upd_sup_min

    c_del_max = upd_del_max
    c_sup_max = upd_sup_max

    c_del_p21 = upd_del_p21 / 100
    c_del_u18 = upd_del_u18 / 100
    c_del_p18 = 1 - c_del_p21 - c_del_u18

    c_sup_p21 = upd_sup_p21 / 100
    c_sup_u18 = upd_sup_u18 / 100
    c_sup_p18 = 1 - c_sup_p21 - c_sup_u18

    c_del_p21ft = upd_del_p21ft / 100
    c_del_p18ft = c_del_p21ft / 2
    c_del_u18ft = 0

    c_sup_p21ft = upd_sup_p21ft / 100
    c_sup_p18ft = c_sup_p21ft / 2
    c_sup_u18ft = 0

    c_del_ftpref = upd_del_ftpref / 100
    c_sup_ftpref = upd_sup_ftpref / 100

    c_del_ptavg = upd_del_ptavg
    c_sup_ptavg = upd_sup_ptavg

    c_del_cao = 'vgl_d' if c_del_cao is None else c_del_cao
    c_sup_cao = 'vgl_s' if c_sup_cao is None else c_sup_cao

    ### 
    values = calculate_values(c_del_cao, c_sup_cao, c_del_min, c_del_max, c_sup_max, c_sup_min, c_del_p21, c_del_u18, c_del_p18, c_sup_p21, c_sup_u18, c_sup_p18, c_del_p21ft, c_del_p18ft, c_del_u18ft, c_sup_p21ft, c_sup_p18ft, c_sup_u18ft, c_del_ftpref, c_sup_ftpref, c_del_ptavg, c_sup_ptavg)
    fig1w, fig1m, fig1lt, fig2d, fig2s, chart_bars, chart_axes  = charts(*values)
    figs = [fig1w, fig1m, fig1lt, fig2d, fig2s]

    canvases = []
    for fig in figs:
        canvas = FigureCanvasTkAgg(fig, master=dash_board)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')
        canvases.append(canvas)

    dashframe, stats1, stats2, stats3, stats1_labels, stats2_coord, stats3_coord = dashboard(dash_board, fig1w, fig1m, fig1lt, fig2d, fig2s, sup_cao_entry, del_cao_entry)

    def update_widgets():
        global stats1, stats2, stats3
        # Maybe must include in global the figs to be updated

        upd_del_cao = del_cao_entry.get()
        upd_sup_cao = sup_cao_entry.get()

        upd_del_min = del_min.get()
        upd_sup_min = sup_min.get()

        upd_del_max = del_max.get()
        upd_sup_max = sup_max.get()

        upd_del_p21 = del_p21.get()
        upd_del_u18 = del_u18.get()

        upd_sup_p21 = sup_p21.get()
        upd_sup_u18 = sup_u18.get()

        upd_del_p21ft = del_ft.get()
        upd_del_u18ft = 0
        
        upd_sup_p21ft = sup_ft.get() 
        upd_sup_u18ft = 0

        upd_del_ftpref = del_ft_pref.get()
        upd_sup_ftpref = sup_ft_pref.get()

        upd_del_ptavg = (int(del_pt_avgh.get()))
        upd_sup_ptavg = (int(sup_pt_avgh.get()))

        c_del_cao = upd_del_cao
        c_sup_cao = upd_sup_cao

        c_del_min = upd_del_min
        c_sup_min = upd_sup_min

        c_del_max = upd_del_max
        c_sup_max = upd_sup_max

        c_del_p21 = upd_del_p21 / 100
        c_del_u18 = upd_del_u18 / 100
        c_del_p18 = 1 - c_del_p21 - c_del_u18

        c_sup_p21 = upd_sup_p21 / 100
        c_sup_u18 = upd_sup_u18 / 100
        c_sup_p18 = 1 - c_sup_p21 - c_sup_u18

        c_del_p21ft = upd_del_p21ft / 100
        c_del_p18ft = c_del_p21ft / 2
        c_del_u18ft = 0

        c_sup_p21ft = upd_sup_p21ft / 100
        c_sup_p18ft = c_sup_p21ft / 2
        c_sup_u18ft = 0

        c_del_ftpref = upd_del_ftpref / 100
        c_sup_ftpref = upd_sup_ftpref / 100

        c_del_ptavg = upd_del_ptavg
        c_sup_ptavg = upd_sup_ptavg

        explicit_costw, implicit_costw, explicit_costm, implicit_costm, expl_lt, impl_lt, del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf, del_pens, del_dinp, del_vb, sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf, sup_pens, sup_dinp, sup_vb = calculate_values(c_del_cao, c_sup_cao, c_del_min, c_del_max, c_sup_max, c_sup_min, c_del_p21, c_del_u18, c_del_p18, c_sup_p21, c_sup_u18, c_sup_p18, c_del_p21ft, c_del_p18ft, c_del_u18ft, c_sup_p21ft, c_sup_p18ft, c_sup_u18ft, c_del_ftpref, c_sup_ftpref, c_del_ptavg, c_sup_ptavg)

        # Update stats1
        stats_config(c_del_cao, c_sup_cao)


        # Update stats2 and stats3 (charts)
        config_chart_bars = {
            'ew': explicit_costw,
            'iw': implicit_costw,
            'em': explicit_costm,
            'im': implicit_costm,
            'elt': expl_lt,
            'ilt': impl_lt,
            'del_brut': del_brut_wage,
            'd_bon': del_bon_wage,
            'd_adv': del_adv,
            'd_vacd': del_vacd,
            'd_vacp': del_vacp,
            'd_sf': del_sf,
            'd_pens': del_pens,
            'd_dinp': del_dinp,
            'd_vb': del_vb,
            's_brut': sup_brut_wage,
            's_bon': sup_bon_wage,
            's_adv': sup_adv,
            's_vacd': sup_vacd,
            's_vacp': sup_vacp,
            's_sf': sup_sf,
            's_pens': sup_pens,
            's_dinp': sup_dinp,
            's_vb': sup_vb,
        }

        config_chart_axes = {
        'ax_w': lambda: (max(explicit_costw) + max(implicit_costw)) * 1.1,
        'ax_m': lambda: (max(explicit_costm) + max(implicit_costm)) * 1.1,
        'ax_lt': lambda: (max(expl_lt) + max(impl_lt)) * 1.1,
        'ax_d': lambda: (explicit_costw[0] + implicit_costw[0]) * 1.1, # Del first
        'ax_s': lambda: (explicit_costw[1] + implicit_costw[1]) * 1.1, # Sup second
        }


        # stats2_coord, stats3_coord

        upfig1w, upfig1m, upfig1lt, upfig2d, upfig2s, chart_bars, chart_axes  = charts(explicit_costw, implicit_costw, explicit_costm, implicit_costm, expl_lt, impl_lt, del_brut_wage, del_bon_wage, del_adv, del_vacd, del_vacp, del_sf, del_pens, del_dinp, del_vb, sup_brut_wage, sup_bon_wage, sup_adv, sup_vacd, sup_vacp, sup_sf, sup_pens, sup_dinp, sup_vb)
        upfigs2 = [upfig1w, upfig1m, upfig1lt]
        upfigs3 = [upfig2d, upfig2s]

        # Update stats2
        for (old_canv, location), new_fig in zip(stats2_coord, upfigs2):
            old_canv.get_tk_widget().grid_remove()
            new_canv = FigureCanvasTkAgg(new_fig, stats2)
            new_canv.draw()
            new_canv.get_tk_widget().grid(row=location[0], column=location[1])
            stats2_coord[stats2_coord.index((old_canv, location))] = (new_canv, location)

        # Update stats3
        for (old_canv, location), new_fig in zip(stats3_coord, upfigs3):
            old_canv.get_tk_widget().grid_remove()
            new_canv = FigureCanvasTkAgg(new_fig, stats3)
            new_canv.draw()
            new_canv.get_tk_widget().grid(row=location[0], column=location[1])
            stats3_coord[stats3_coord.index((old_canv, location))] = (new_canv, location)

        dashframe.update_idletasks()


    submit_trigger = tk.Button(calc_frame, text='Submit', command=update_widgets, font=('Times New Roman', 10))
    submit_trigger.grid(row=3, column=0)

    calculator.mainloop()

main_gui()
