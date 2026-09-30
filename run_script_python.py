# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:05:34 2026

@author: emartinez
"""

from f import Data_processing

#-Data info
data_name = 'MZS_O2'
conditions = ['Light', 'Dark']
measurement_by_type = {'ICE': ['o2_mid_mean'],
                       'WATER': ['o2_mid_mean'],
                       'CCO': ['o2_top_mean', 'o2_mid_mean', 'o2_bottom_mean'],
                       'DRY SOIL': ['o2_mid_mean', 'o2_bottom_mean'],
                       'WET SOIL': ['o2_mid_mean', 'o2_bottom_mean']}
max_time = 5.5 # [h] | 5.5 or 999 (for full experiment)
var1 = 'O2'
var1_label = '[Oxygen] (%)' 
var2 = 'sample_temperature'
var2_label = 'Temperature (°C)'
#-Plotting properties
## Plotting colors
var1_colors = {'ICE': ['#4499AD'],
               'WATER': ['#4499AD'],
               'CCO': ['#4499AD', '#A7B78D', '#2A4B42'],
               'DRY SOIL': ['#4499AD', '#2A4B42'],
               'WET SOIL': ['#4499AD', '#2A4B42']}
var2_color = '#d2554a'
## Legend labels
legend_labels = {'ICE': ['Water'],
                 'WATER': ['Water'],
                 'CCO': ['Water', 'Interface', 'Cryoconite'],
                 'DRY SOIL': ['Air', 'Soil'],
                 'WET SOIL': ['Air', 'Soil']}
## Position of statistics labels ('ns', '*', '**', '***')
y_plus_texts = {'ICE': [1.02],
                'WATER': [1.02],
                'CCO': [1.14, 1.08, 1.02],
                'DRY SOIL': [1.08, 1.02],
                'WET SOIL': [1.08, 1.02]}
show_legend = True
legend_orientation = 'horizontal'
save_fig = False
## Set limits of x-coordinates
xlim = [-0.2, 5.7] # [-0.2, 5.7] or [None, None] (for full experiment)
## Set limits of y-coordinates
ylim_var1 = [0, 27]
ylim_var2 = [0, 13]
x_ticker_format = "{x:.1f}"
ns_label = True
ns_label_fontsize = 9
#-Statistics
stats_dark_vs_light = True
stats_coefficient_of_variation = True
significant_difference_times = False
significant_difference_t0 = True
CV_method = 'RSD' # 'RSD' or 'QCD' | RSD - Relative Standard deviaiton; QCD - Quartile coefficient of dispersion

#-Execute function
Data_processing.process_and_stats(data_name = data_name, 
                                  conditions = conditions, 
                                  measurement_by_type = measurement_by_type, 
                                  var1_colors = var1_colors, 
                                  legend_labels = legend_labels, 
                                  y_plus_texts = y_plus_texts, 
                                  var1 = var1, 
                                  var1_label = var1_label, 
                                  var2 = var2,
                                  var2_label = var2_label,
                                  var2_color = var2_color,
                                  max_time = max_time, 
                                  show_legend = show_legend, 
                                  legend_orientation = legend_orientation, 
                                  save_fig = save_fig, 
                                  xlim = xlim, 
                                  ylim_var1 = ylim_var1, 
                                  ylim_var2 = ylim_var2, 
                                  ns_label = ns_label,
                                  ns_label_fontsize = ns_label_fontsize, 
                                  x_ticker_format = x_ticker_format, 
                                  stats_dark_vs_light = stats_dark_vs_light, 
                                  stats_coefficient_of_variation = stats_coefficient_of_variation, 
                                  CV_method = CV_method, 
                                  significant_difference_times = significant_difference_times,
                                  significant_difference_t0 = significant_difference_t0)
