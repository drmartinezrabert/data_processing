# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:13:21 2026

@author: emartinez
"""

import pandas as pd
import numpy as np
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.image as mpimg
import datetime

class Data_processing:
    path_data = 'data/'
    path_save = 'results/'
    plt.rcParams['figure.dpi'] = 400
    plt.rcParams['savefig.dpi'] = 400
    plt.rcParams['font.family'] = 'Arial'
    
    def process_and_stats(data_name, conditions, measurement_by_type, legend_labels, y_plus_texts, var1, var1_label, var1_colors, max_time = 9999,  
                          var2 = None, var2_label = None, var2_color = '#d2554a', show_legend = True, legend_orientation = 'horizontal', 
                          xlim = [None, None], ylim_var1 = [0, 27], ylim_var2 = [0, 13], ns_label = True, ns_label_fontsize = 9, save_fig = True,
                          x_ticker_format = "{x:.1f}", stats_dark_vs_light = True, stats_coefficient_of_variation = False, CV_method = 'RSD', 
                          significant_difference_times = False, significant_difference_t0 = False, show_icon = False):
        """
        Function to process and do statistics of data from Folder `data/`.

        Parameters
        ----------
        data_name : STR
            Name of file with data to be processed (from Folder `data/`). Name of file without format (i.e., without `.csv`).
        conditions : LIST of STR
            List of conditions. These must coincide with the names given in the column 'Condition' of `{data_name}.csv`.
        measurement_by_type : DICT
            Description of measurements taken for each sample type. Format: {'Sample type': ['Measurement name 1', 'Measurement name 2']}.
            'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.
            'Measurement name #' corresponds to the column(s) with the data of variable 1 of `{data_name}.csv`.
        var1 : STR
            Name of primary variable, corresponding to data defined in `measurement_by_type`.
        var1_label : STR
            Label of primary variable in primary y-axis of plot (left axis).
        var1_colors : DICT
            Plotting colors of primary variable. Format: {'Sample type': ['Color 1', 'Color 2']}.
            'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.
            Color list must have the same length as measurements defined in `measurement_by_type`.
        legend_labels : DICT
            Label of measurements in plot legend. Format: {'Sample type': ['Label name 1', 'Label name 2']}.
            'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.
            Label list must have the same length as measurements defined in `measurement_by_type`. 
        y_plus_texts : DICT
            Position of stastics labels over the top of plots. Format: {'Sample type': [1.08, 1.02]}.
            'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.
            Position list must have the same length as measurements defined in `measurement_by_type`. 
        max_time : FLOAT, optional
            Maximum measurement time considered for processing. The default is 9999.
        var2 : STR, optional
            Name of secundary variable. The name must coincide with a column of `{data_name}.csv`. The default is None.
        var2_label : STR, optional
            Label of secundary variable in secundary y-axis of plot (right axis). The default is None.
        var2_color : STR, optional
            Plotting color of secundary variable. The default is '#d2554a'.
        show_legend : BOOL, optional
            Set whether legend is shown in plots. The default is True.
        legend_orientation : STR, optional
            Set orientation of legend ('horizontal' or 'vertical'). The default is 'horizontal'.
        xlim : LIST, optional
            Set limits of x-axis with floats ([left limit, right limit]). The default is [None, None].
        ylim_var1 : LIST, optional
            Set limits of primary y-axis (left axis) with floats ([bottom limit, top limit]). The default is [0, 27].
        ylim_var2 : LIST, optional
            Set limits of secundary y-axis (right axis) with floats ([bottom limit, top limit]). The default is [0, 13].
        ns_label : BOOL, optional
            Set whether not significant labels ('ns') are shown in plots. The default is True.
        ns_label_fontsize : FLOAT, optional
            Size of statistics labels ('ns', '*', '**', '***') over the plots. The default is 9.
        save_fig : BOOL, optional
            Set whether the plots are saved in Folder `results/`. The default is True.
        x_ticker_format : STR, optional
            Set x-ticker format. The default is "{x:.1f}".
        stats_dark_vs_light : BOOL, optional
            Run stastics comparing dark vs light conditions and save them in an Excel (Folder `results/`. The default is True.
        stats_coefficient_of_variation : BOOL, optional
            Calculate coefficient of variation of measurements and save them in an Excel (Folder `results/`). The default is False.
        CV_method : STR, optional
            Set method to calculate coefficient of variation. The default is 'RSD'.
                - 'RSD': Relative Standard Deviaiton
                - 'QCD': Quartile Coefficient of Dispersion
        significant_difference_times : BOOL, optional
            Calculate and show in plot significant differences between t_n and t_n+1. The default is False.
        significant_difference_t0 : BOOL, optional
            Calculate and show in plot significant differences between t_0 and t_n. The default is False.
        show_icon : BOOL, optional
            Set wheteher icons are shown in right-top of plots. The default is False.

        Returns
        -------
        Plots shown in Console/Cell output and saved in Folder `results/` (if `save_fig = True`)
        Statistics outcome saved in Folder `results/`

        """
        data = pd.read_csv(f'{Data_processing.path_data}{data_name}.csv')
        data_IDs = data['ID'].unique()
        if significant_difference_times and significant_difference_t0:
            raise ValueError('Choose one of significant difference method: significant difference between t_n and t_n+1 (`significant_difference_times = True`) or between t_0 and t_n (`significant_difference_t0 = True`).')
        if stats_dark_vs_light:
            # Difference between light and night
            time_now = datetime.datetime.now()
            time_now_strf = time_now.strftime('%Y-%m-%d_%H%M%S')
            file = f'{var1}_pval_{time_now_strf}.xlsx'
            full_path_save = Data_processing.path_save + file
            if not os.path.isfile(full_path_save):
                introRowDGr = pd.DataFrame(np.array(['Oxygen measurements. Light vs Dark (p-values)']))
                with pd.ExcelWriter(full_path_save) as writer:
                    introRowDGr.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', index = False, header = False)
            else:
                raise ValueError(f'Error 404: Save folder {full_path_save} not found.')
            sRow = 1
        if stats_coefficient_of_variation:
            if CV_method == 'RSD':
                CV_method_name = 'Relative Standard Deviation, RSD'
            elif CV_method == 'QCD': # It doesn't make sense with low amount of replicates
                CV_method_name = 'Quartile Coefficient of Dispersion, QCD'
            else:
                raise ValueError(f"Method ({CV_method_name}) not found. Please use 'RSD' (Relative Standard Deviation) or 'QCD' (Quartile Coefficient of Dispersion)'")
            # Coefficient of variation of replicates
            time_now = datetime.datetime.now()
            time_now_strf = time_now.strftime('%Y-%m-%d_%H%M%S')
            file_CV = f'CV_replicates_{time_now_strf}_{CV_method}.xlsx'
            full_path_save_CV = Data_processing.path_save + file_CV
            if not os.path.isfile(full_path_save_CV):
                introRowDGr = pd.DataFrame(np.array([f'Coefficeint of variation of replicates ({CV_method_name})']))
                with pd.ExcelWriter(full_path_save_CV) as writer:
                    introRowDGr.to_excel(writer, sheet_name = 'CV replicates', index = False, header = False)
            else:
                raise ValueError(f'Error 404: Save folder {full_path_save} not found.')
        sRow_CV = 1
        for sample_id in data_IDs:
            if stats_coefficient_of_variation:
                # Write Excel
                sample_array = pd.DataFrame(np.array([sample_id]))
                with pd.ExcelWriter(full_path_save_CV, engine='openpyxl', mode = 'a', if_sheet_exists='overlay') as writer:
                    sample_array.to_excel(writer, sheet_name = 'CV replicates', startrow = sRow_CV,
                                          index = False, header = False)
                sRow_CV += 1
            for condition in conditions:
                iData = data[(data['ID'] == sample_id) & (data['Condition'] == condition) & (data['Time'] <= max_time)]
                if iData.empty:
                    continue
                iType = iData['Sample type'].unique()[0]
                if isinstance(var2, str):
                    var2_ = iData.groupby('Time')[var2].mean()
                x = iData['Time'].unique()
                descr = iData.groupby('Time')[measurement_by_type[iType]].describe()
                if stats_coefficient_of_variation:
                    for id_meas, meas in enumerate(measurement_by_type[iType]):
                        CV_site = legend_labels[iType][id_meas]
                        CV_name = pd.DataFrame(np.array([f'CV ({CV_site} - {condition}):']))
                        if CV_method == 'RSD':
                            # Within-subject standard deviation method (or relative standard deviation, RSD)
                            CV = descr[meas]['std'] / descr[meas]['mean']
                        elif CV_method == 'QCD':
                            # Quartile coefficient of dispersion (QCD)
                            CV = (descr[meas]['75%'] - descr[meas]['25%']) / (descr[meas]['75%'] + descr[meas]['25%'])
                        CV_array = pd.DataFrame(np.array(CV)).transpose()
                        with pd.ExcelWriter(full_path_save_CV, engine='openpyxl', mode = 'a', if_sheet_exists='overlay') as writer:
                            CV_name.to_excel(writer, sheet_name = 'CV replicates', startrow = sRow_CV, 
                                                     startcol = 0, index = False, header = False)
                            CV_array.to_excel(writer, sheet_name = 'CV replicates', startrow = sRow_CV, 
                                                      startcol = 1, index = False, header = False)
                        sRow_CV += 1
                if significant_difference_times:
                    pval_time_diff = np.empty((len(measurement_by_type[iType]), len(x)), dtype = '<U10')
                    for id_site, site in enumerate(measurement_by_type[iType]):
                        site_data = iData[['Time', 'Replicate', site]]
                        site_data_times = site_data['Time'].unique()
                        pval_time_diff_ = ['ns']
                        for id_time, time in enumerate(site_data_times):
                            if id_time > 0:
                                t1 = site_data_times[id_time-1]
                                t2 = site_data_times[id_time]
                                site_data_t1 = np.array(site_data[site_data['Time'] == t1][site].values, dtype='d')
                                site_data_t2 = np.array(site_data[site_data['Time'] == t2][site].values, dtype='d')
                                _, pvalue = stats.ttest_ind(site_data_t1, site_data_t2, nan_policy = 'omit')
                                if pvalue > 0.05:
                                    pvalue = ['ns']
                                elif (pvalue < 0.05) and (pvalue > 0.01):
                                    pvalue = ['*']
                                elif (pvalue < 0.01) and (pvalue > 0.001):
                                    pvalue = ['**']
                                else:
                                    pvalue = ['***']
                                pval_time_diff_ += pvalue
                        pval_time_diff[id_site, :] = pval_time_diff_
                    if np.ndim(pval_time_diff) == 1: pval_time_diff = np.array([pval_time_diff])
                if significant_difference_t0:
                    pval_time_diff_t0 = np.empty((len(measurement_by_type[iType]), len(x)), dtype = '<U10')
                    for id_site, site in enumerate(measurement_by_type[iType]):
                        site_data = iData[['Time', 'Replicate', site]]
                        site_data_times = site_data['Time'].unique()
                        pval_time_diff_t0_ = ['ns']
                        t1 = site_data_times[0]
                        for id_time, time in enumerate(site_data_times):
                            if id_time > 0:
                                t2 = site_data_times[id_time]
                                site_data_t1 = np.array(site_data[site_data['Time'] == t1][site].values, dtype='d')
                                site_data_t2 = np.array(site_data[site_data['Time'] == t2][site].values, dtype='d')
                                _, pvalue = stats.ttest_ind(site_data_t1, site_data_t2, nan_policy = 'omit')
                                if pvalue > 0.05:
                                    pvalue = ['ns']
                                elif (pvalue < 0.05) and (pvalue > 0.01):
                                    pvalue = ['*']
                                elif (pvalue < 0.01) and (pvalue > 0.001):
                                    pvalue = ['**']
                                else:
                                    pvalue = ['***']
                                pval_time_diff_t0_ += pvalue
                        pval_time_diff_t0[id_site, :] = pval_time_diff_t0_ 
                    if np.ndim(pval_time_diff_t0) == 1: pval_time_diff = np.array([pval_time_diff_t0])
                x = descr.index.values
                count = int(descr[measurement_by_type[iType][0]]['count'].unique()[0])
                title = f'{sample_id} ({iType}) | n = {count}'
                full_path_figsave = Data_processing.path_save + f'{sample_id}_{condition}_{iType}.tiff'
                if show_icon:
                    if condition == 'Light':
                        icon = mpimg.imread('data/light_icon.png')
                        zoom = 0.060
                    elif condition == 'Dark':
                        icon = mpimg.imread('data/dark_icon.png')
                        zoom = 0.085
                #-Plotting
                x_formatter = ticker.StrMethodFormatter(x_ticker_format)
                fig, ax1 = plt.subplots()
                for id_meas, meas in enumerate(measurement_by_type[iType]):
                    y_plus_text = y_plus_texts[iType]
                    ax1.errorbar(x, descr[meas]['mean'], yerr=descr[meas]['std'], fmt='o', 
                                 linestyle = '-', color = var1_colors[iType][id_meas],
                                 ecolor = 'black', elinewidth = 0.75, barsabove = False, capsize = 3)
                    if significant_difference_times:
                        pval_array = pval_time_diff[id_meas, :]
                        for id_time, time in enumerate(x):
                            if not ns_label:
                                pval_array = [p.replace('ns' , '') for p in pval_array]
                            if not id_time == 0:
                                ax1.text(time, ylim_var1[1]*y_plus_text[id_meas], pval_array[id_time], ha = 'center',
                                         fontfamily = 'Arial', c = var1_colors[iType][id_meas], weight = 650, fontsize = ns_label_fontsize)
                    elif significant_difference_t0:
                        pval_array = pval_time_diff_t0[id_meas, :]
                        for id_time, time in enumerate(x):
                            if not ns_label:
                                pval_array = [p.replace('ns' , '') for p in pval_array]
                            if not id_time == 0:
                                ax1.text(time, ylim_var1[1]*y_plus_text[id_meas], pval_array[id_time], ha = 'center', 
                                         fontfamily = 'Arial', c = var1_colors[iType][id_meas], weight = 650, fontsize = ns_label_fontsize)
                if show_icon:
                    imagebox = OffsetImage(icon, zoom = zoom)
                    if not xlim[1]:
                        x_icon = max(x)*0.98
                    else:
                        x_icon = xlim[1]*0.93
                    ab = AnnotationBbox(imagebox, (x_icon, ylim_var1[1]*0.91), frameon = False)
                    ax1.add_artist(ab)
                if significant_difference_times or significant_difference_t0:
                    plt.title(title, y = y_plus_text[0]*1.04, weight = 650)
                else:
                    plt.title(title, weight = 650)
                ax1.set_ylabel(var1_label)
                ax1.set_xlim(left = xlim[0], right = xlim[1])
                ax1.set_ylim(bottom = ylim_var1[0], top = ylim_var1[1])
                ax1.xaxis.set_major_formatter(x_formatter)
                ax1.minorticks_on()
                legend = list(legend_labels[iType])
                plt.xlabel('Time (h)')
                if isinstance(var2, str):
                    ax2 = ax1.twinx()
                    ax2.plot(x, var2_, color = '#d2554a', linestyle = '-', marker = 's', alpha = 0.5)
                    ax2.set_ylabel(var2_label, color = var2_color)
                    ax2.set_ylim(bottom = ylim_var2[0], top = ylim_var2[1])
                    ax2.yaxis.set_major_formatter(x_formatter)
                    ax2.minorticks_on()
                    legend += [var2]
                if show_legend:
                    if legend_orientation == 'vertical':
                        fig.legend(legend, bbox_to_anchor = (1.27, 0.6))
                    elif legend_orientation == 'horizontal':
                        fig.legend(legend, bbox_to_anchor = (0.95, 0), ncol = len(legend))
                if save_fig:
                    plt.savefig(full_path_figsave, bbox_inches='tight')
                plt.show()
            sRow_CV += 1
            if stats_dark_vs_light:
                # Difference between light and night
                lightData = data[(data['ID'] == sample_id) & (data['Condition'] == 'Light')]
                darkData = data[(data['ID'] == sample_id) & (data['Condition'] == 'Dark')]
                if lightData.empty or darkData.empty:
                    continue
                else:
                    iType = lightData['Sample type'].unique()[0]
                    light_times = lightData['Time'].unique()
                    dark_times = darkData['Time'].unique()
                    measurement_sites = measurement_by_type[iType]
                    # Write Excel
                    sample_array = pd.DataFrame(np.array([sample_id]))
                    light_time_name = pd.DataFrame(np.array(['Time (Light):']))
                    light_time_array = pd.DataFrame(np.array(light_times)).transpose()
                    dark_time_name = pd.DataFrame(np.array(['Time (Dark):']))
                    dark_time_array = pd.DataFrame(np.array(dark_times)).transpose()
                    with pd.ExcelWriter(full_path_save, engine='openpyxl', mode = 'a', if_sheet_exists='overlay') as writer:
                        sample_array.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow,
                                              index = False, header = False)
                        light_time_name.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow+1, 
                                                 startcol = 0, index = False, header = False)
                        light_time_array.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow+1, 
                                                  startcol = 1, index = False, header = False)
                        dark_time_name.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow+2, 
                                                startcol = 0, index = False, header = False)
                        dark_time_array.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow+2, 
                                                 startcol = 1, index = False, header = False)
                    sRow += 3
                    for id_site, site in enumerate(measurement_sites):
                        lData = lightData[['Time', 'Replicate', site]]
                        dData = darkData[['Time', 'Replicate',  site]]
                        pval = []
                        abs_diff = []
                        if len(light_times) <= len(dark_times):
                            times = light_times
                            what_times = 'Light'
                        else:
                            times = dark_times
                            what_times = 'Dark'
                        for id_time, time in enumerate(times):
                            if what_times == 'Light':
                                l_time = time
                                d_time = dark_times[id_time]
                            else:
                                l_time = light_times[id_time]
                                d_time = time
                            lData_t = lData[lData['Time'] == l_time][site].values
                            dData_t = dData[dData['Time'] == d_time][site].values
                            _, pvalue = stats.ttest_ind(lData_t, dData_t)
                            pval += [pvalue]
                            abs_diff += [abs(np.average(lData_t) - np.average(dData_t))]
                        # Write Excel
                        site_name = legend_labels[iType][id_site]
                        pvalue_name = pd.DataFrame(np.array([f'pvalue ({site_name}):']))
                        abs_diff_name = pd.DataFrame(np.array([f'Abs. diff. ({site_name}):']))
                        abs_diff_array = pd.DataFrame(np.array(abs_diff)).transpose()
                        pvalue_array = pd.DataFrame(np.array(pval)).transpose()
                        with pd.ExcelWriter(full_path_save, engine='openpyxl', mode = 'a', if_sheet_exists='overlay') as writer:
                            abs_diff_name.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow, startcol=0,
                                                 index = False, header = False)
                            abs_diff_array.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow, startcol=1,
                                                  index = False, header = False)
                            pvalue_name.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow+1, startcol=0,
                                                 index = False, header = False)
                            pvalue_array.to_excel(writer, sheet_name = f'{var1}. Light vs Dark', startrow = sRow+1, startcol=1,
                                                  index = False, header = False)
                        sRow += 2
                sRow += 1