# data_processing
Script for data processing of measurement replicates (calculating average and standard deviation), do statistics (p-value between measurements and coefficient of variation between replicates), and plotting the results.

*· Contributors: Eloi Martinez-Rabert*.<br>
> [!NOTE]
> To open the links in a new tab: right click on the link + "Open link in new tab".
____________________________

## README Contents
· **Setup PC:**
- Before having fun with **Anaconda/Spyder**... | [GO](#before-having-fun-with-anacondaspyder)
    - Anaconda Python installation | [GO](#gear-anaconda-python-installation)
    - Anaconda Navigator | [GO](#anaconda-navigator)
    - Anaconda Prompt or Terminal | [GO](#anaconda-prompt-or-terminal)
    - Spyder | [GO](#spyder)
    - Python packages | [GO](#python-packages)
    - Installation of packages using Anaconda Navigator | [GO](#installation-of-packages-using-anaconda-navigator)
    - Installation of packages using pip | [GO](#installation-of-packages-using-pip)
- Before having fun with **Jupyter Notebook**... | [GO](#before-having-fun-with-jupyter-notebook)
    - Jupyter Notebook installation | [GO](#gear-jupyter-notebook-installation)
        - Installing Jupyter using Anaconda and Conda | [GO](#installing-jupyter-using-anaconda-and-conda)
        - Installing Jupyter with pip | [GO](#installing-jupyter-with-pip)
- Before having fun with **JupyterLab**... | [GO](#before-having-fun-with-jupyterlab)
    - JupyterLab installation | [GO](#gear-jupyterlab-installation)
        - Installing JupyterLab with pip | [GO](#installing-jupyterlab-with-pip)

· **Dowloading script:**
- Instructions for downloading and setting up data_processing script | [GO](#clipboard-instructions-for-downloading-and-setting-up-data_processing-script)
    - Data formating instructions | [GO](#data-formating-instructions)

· **Instruction of use:**
- Instruction to use data_processing via Spyder | [GO](#clipboard-instruction-to-use-data_processing-via-spyder)
- Instruction to use data_processing via Jupyter Notebook | [GO](#clipboard-instruction-to-use-data_processing-via-jupyter-notebook)
- Instruction to use data_processing via JupyterLab | [GO](#clipboard-instruction-to-use-data_processing-via-jupyterlab)
- Script guidelines | [GO](#script-guidelines)
    - Data_processing.process_and_stats | [GO](#data_processingprocess_and_stats)

· **Contact**:
- Contact | [GO](#contact)
____________________________

## Before having fun with **Anaconda/Spyder**...

### :gear: Anaconda Python installation
This script is built up in Python. You can execute this script in Python with **Anaconda**. **Anaconda Python** is a free, open-source platform that allows to write and execute code in the programming language Python ([Python Tutorial](https://docs.python.org/3/tutorial/index.html)). This platform simplifies package installation, managment and development, and alos comes with a large number of libraries/packages that can be you for your projects. To install **Anaconda**, just head to the [Anaconda Documentation website](https://docs.anaconda.com/free/anaconda/install/index.html) and follow the instructions to download teh installer for your operating system.

[🔼 Back to **Contents**](#readme-contents)

### Anaconda Navigator
Anaconda Navigator is a desktop graphical user interface that allows you to launch applications and efficiently manage conda packages, environments, and channels without using command-line commands. For more info, click [here](https://docs.anaconda.com/free/navigator/).

[🔼 Back to **Contents**](#readme-contents)

### Anaconda Prompt or Terminal
Anaconda Prompt is a command line interface with Anaconda Distribution. Terminal is a command line interface that comes with macOS and Linux. To open it in **Windows**: Click Start, search for _"Anaconda Prompt"_ and click to open. In **macOS**: use Cmd+Space to open Spotlight Search and type _"Navigator"_ to open the program. In **Linux-CentOS**: open Applications > System Tools > Terminal.

[🔼 Back to **Contents**](#readme-contents)

### Spyder
Spyder is a Python development environment with many features for working with Python code, such as a text editor, debugger, profiler, and interactive console. You can launch **Spyder** using the **Anaconda Navigator**. For Spyder Tutorials, click [here](https://www.youtube.com/watch?v=E2Dap5SfXkI&list=PLPonohdiDqg9epClEcXoAPUiK0pN5eRoc&ab_channel=SpyderIDE).

[🔼 Back to **Contents**](#readme-contents)

### Python packages
A **Python package** is a collection of files containing Python code (i.e., modules). To execute **EcoSysEM platform**, the following packages must to be installed:
- **<ins>NumPy</ins>** (≥2.3.5). NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more. For more info and tutorials, click [here](https://numpy.org/).
- **<ins>SciPy</ins>** (≥1.17.1). SciPy is a collection of mathematical algorithms and convenience functions built on NumPy . It adds significant power to Python by providing the user with high-level commands and classes for manipulating and visualizing data. For more info and tutorials, click [here](https://scipy.github.io/devdocs/tutorial/index.html).
- **<ins>Matplotlib</ins>** (≥3.10.8). Matplotlib is a library for creatinc static, animated and interactive visualizations in Python. For more info and tutorials, click [here](https://matplotlib.org/).

[🔼 Back to **Contents**](#readme-contents)

### Installation of packages using Anaconda Navigator
You can install any Python package using the **Anaconda Navigator**. For this, execute the navigator and click to **Environments**. In this section you can install new packages and delete the already installed. For more info, click [here](https://docs.anaconda.com/free/navigator/).

[🔼 Back to **Contents**](#readme-contents)

### Installation of packages using pip
**pip** is the package installer for Python. In general, pip installs the minimal instalation requirements automatically, but not the optionals requirements. To install the mentioned packages using pip, you have only to write the following command lines in **Anaconda Prompt or Terminal**:
#### · <ins>Anaconda Prompt</ins>
**NumPy**:
```
pip install numpy
```
**SciPy**:
```
pip install scipy
```
**Matplotlib**:
```
pip install matplotlib
```
____________________________

#### · <ins>Windows Terminal</ins>
**NumPy**:
```
python -m pip install numpy
```
**SciPy**:
```
python -m pip install scipy
```
**Matplotlib**:
```
python -m pip install matplotlib
```

[🔼 Back to **Contents**](#readme-contents)

____________________________

## Before having fun with **Jupyter Notebook**...

### :gear: Jupyter Notebook installation
This script is built up in Python. You can execute this script in Python with **Jupyter Notebook**. **Jupyter Notebook** is a free software, open standards, and web services for interactive computing across all programming languages. This platform simplifies the creation, sharing and execution of program scripts. Python is a requirement for installing Jupyter Notebook. We **highly recommend installing [Anaconda](#gear-anaconda-python-installation)**. Anaconda installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science. The required Python packages to execute the code can be installed previously (see [Installation of packages using pip](#installation-of-packages-using-pip)) or run the first Cell of `run_script_jupyter.ipynb`.

#### Installing Jupyter using Anaconda and Conda
1. Download [Anaconda](https://www.anaconda.com/download). We recommend downloading Anaconda’s latest Python 3 version (currently Python 3.9).
2. Install the version of Anaconda which you downloaded, following the instructions on the download page.
3. Run the notebook using Command Prompt (Windows/Mac) or Anaconda Prompt - [Run script with Jupyter Notebook](#).

#### Installing Jupyter with pip
As an exisiting Python user, you can install Jupyter using Python's pacakgae manager pip, instead of Anaconda. 
1. Ensure that you have the latest pip version (olver versions may have trouble with some dependencies.
```
pip3 install --upgrade pip
```
2. Install the Jupyter Notebook using:
```
pip3 install jupyter
```
> [!NOTE]
> Use `pip` if using legacy Python 2.)

[🔼 Back to **Contents**](#readme-contents)

____________________________

## Before having fun with **JupyterLab**...

### :gear: JupyterLab installation
This script is built up in Python. You can execute this script in Python with **JupyterLab**. **JupyterLab** is the lastest web-based interactive development environment for notebooks, code and data (an improved version of **Jupyter Notebook**). Python is a requirement for installing JupyterLab. **highly recommend installing [Anaconda](#gear-anaconda-python-installation)**. Anaconda installs Python and other commonly used packages for scientific computing and data science. The required Python packages to execute the code can be installed previously (see [Installation of packages using pip](#installation-of-packages-using-pip)) or run the first Cell of `run_script_jupyter.ipynb`. 

#### Installing JupyterLab with pip
JupyterLab is not installed with Anaconda, and this can be installed with pip.
1. Open Anaconda Prompt (or Command Prompt if you have already installed Python in your PC).
2. Write the line code:
```
pip3 install jupyterlab
```
> [!NOTE]
> Use `pip` if using legacy Python 2.)

[🔼 Back to **Contents**](#readme-contents)

____________________________

## :clipboard: Instructions for downloading and setting up data_processing script
1. Download .zip code. Last version: `v1.0.0`. [Download release]([https://github.com/](https://github.com/drmartinezrabert/data_processing/archive/refs/tags/v1.0.0.zip)).
2. Extract files to a destination (Recommendation - Desktop).
3. Open extracted files and copy data  to be processed (format `.csv`) into Folder `data_processing-1.0.0/data/`.
4. Execute script via Spyder (see [Instruction to use data_processing via Spyder](#clipboard-instructions-to-use-data_processing-via-spyder) section), Jupyter Notebook (see [Instruction to use data_processing via Jupyter Notebook](#clipboard-instructions-to-use-data_processing-via-jupyter-notebook) section) or JupyterLab (see [Instruction to use data_processing via JupyterLab](#clipboard-instructions-to-use-data_processing-via-jupyterlab) section).

### Data formating instructions
The script `data_processing` only reads files in `.csv` format. In it, some column names are required:
- **ID**. Identifier of sample (the user can choose any).
- **Sample type**. Description of sample type (the user can choose any).
- **Condition**. Condition of incubation (for now 'Light' or 'Dark').
- **Replicate**. Replicate number (_integer_ format - 1, 2, 3...).
- **Time**. Time of measurement (_float_ format - 0.00, 1.00, 1.502...).
- **Measurement(s)** (the user can choose any name(s)). Measurement data (_float_ format - 18.30, 8.02, 10.52...). It can be more than one variable/column.

[🔼 Back to **Contents**](#readme-contents)

____________________________

## :clipboard: Instruction to use data_processing via Spyder
1. Launch **Spyder**. For Spyder Tutorials, click [here](https://www.youtube.com/watch?v=E2Dap5SfXkI&list=PLPonohdiDqg9epClEcXoAPUiK0pN5eRoc&ab_channel=SpyderIDE).
2. Set (at least) the following panes in Spyder (most are selected by default): `Files`, `Editor`, `IPython Console`, `Plots`, `Help`, `Historial`.
   From Spyder taskbar: <ins>V</ins>iew / Panes ▸.
3. Go to the **Code folder<sup>2</sup>** using the `Files` pane and open `run_script_python.py` file.
    &#09;<br><sup><sup>2</sup>Code folder: folder with `run_script_jupyter.ipynb` file (Folder: `data_processing-1.0.0`). </sup>
4. Modify arguments of script (see [Data_processing.process_and_stats](#data_processingprocess_and_stats)).
5. Run `run_script_python.py` script with Ctrl + Intro, F5 or Play symbol of _Run toolbar_.

[🔼 Back to **Contents**](#readme-contents)

____________________________

## :clipboard: Instruction to use data_processing via Jupyter Notebook
1. Open **Anaconda Prompt** or **Command Prompt** of Windows/Mac.
2. Go to the **Code folder<sup>2</sup>** using `cd` command (more info about [Using Terminal](https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/use-terminal/?highlight=Using%20Terminal)).
    &#09;<br><sup><sup>2</sup>Code folder: folder with `run_script_jupyter.ipynb` file (Folder: `data_processing-1.0.0`).</sup>
3. Open **Jupyter Notebook** with the command line:
   · Command Prompt (Windows):
   ```
   python -m notebook
   ```
   · Anaconda Prompt:
   ```
   jupyter notebook
   ```
4. Install required Python packages running the first cell (if necessary).
5. Modify arguments of script (see [Data_processing.process_and_stats](#data_processingprocess_and_stats)) and run the cell.
6. Run cell script with `Data_processing.process_and_stats()`.

[🔼 Back to **Contents**](#readme-contents)

____________________________

## :clipboard: Instruction to use data_processing via JupyterLab
1. Open **Anaconda Prompt or Terminal**.
2. Go to the **Code folder<sup>2</sup>** using `cd` command (more info about [Using Terminal](https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/use-terminal/?highlight=Using%20Terminal)).
    &#09;<br><sup><sup>2</sup>Code folder: folder with `run_script_jupyter.ipynb` file (Folder: `data_processing-1.0.0`). </sup>
3. Open **JupyterLab** with the command line:
   · Command Prompt (Windows):
   ```
   python -m jupyterlab
   ```
   · Anaconda Prompt:
   ```
   jupyter lab
   ```
4. Install required Python packages running the first cell (if necessary).
5. Modify arguments of script (see [Data_processing.process_and_stats](#data_processingprocess_and_stats)) and run the cell..
6. Run cell script with `Data_processing.process_and_stats()`.

[🔼 Back to **Contents**](#readme-contents)

____________________________

## Script guidelines
This section is an overview and explanation of important features of data_processing script. For now, only one function is run `Data_processing.process_and_stats()`.

### Data_processing.process_and_stats
```python
Data_processing.process_and_stats(data_name, conditions, measurement_by_type, legend_labels, y_plus_texts, var1, var1_label, var1_colors, max_time=9999,  
                                  var2=None, var2_label=None, var2_color='#d2554a', show_legend=True, legend_orientation='horizontal', xlim=[None, None],
                                  ylim_var1=[0, 27], ylim_var2=[0, 13], ns_label=True, ns_label_fontsize=9, save_fig=True, x_ticker_format="{x:.1f}",
                                  stats_dark_vs_light=True, stats_coefficient_of_variation=False, CV_method='RSD', significant_difference_times=False,
                                  significant_difference_t0=False, show_icon=False)
```
Function to process and do statistics of data from Folder `data/`.<p>
**Parameters:**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **data_name : _str_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Name of file with data to be processed (from Folder `data/`). Name of file without format (i.e., without `.csv`).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **conditions : _list of str_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; List of conditions. These must coincide with the names given in the column 'Condition' of `{data_name}.csv`. For now, only 'Light' or 'Dark'.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **measurement_by_type : _dict_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Description of measurements taken for each sample type. Format: {'Sample type': ['Measurement name 1', 'Measurement name 2']}.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Measurement name #' corresponds to the column(s) with the data of variable 1 of `{data_name}.csv`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **var1 : _str_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Name of primary variable, corresponding to data defined in `measurement_by_type`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **var1_label : _str_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Label of primary variable in primary y-axis of plot (left axis).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **var1_colors : _dict_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Plotting colors (HEX code) of primary variable. Format: {'Sample type': ['Color 1', 'Color 2']}.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Color list must have the same length as measurements defined in `measurement_by_type`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **legend_labels : _dict_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Label of measurements in plot legend. Format: {'Sample type': ['Label name 1', 'Label name 2']}.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Label list must have the same length as measurements defined in `measurement_by_type`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **y_plus_texts : _dict_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Position of stastics labels over the top of plots. Format: {'Sample type': [1.08, 1.02]}.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Sample type' must coincide with the names given in the column 'Sample type' of `{data_name}.csv`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Position list must have the same length as measurements defined in `measurement_by_type`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **max_time : _int_ or _float_, _optional, default: 9999_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Maximum measurement time considered for processing.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **var2 : _str_, _optional, default: None_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Name of secundary variable. The name must coincide with a column of `{data_name}.csv`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **var2_label : _str_, _optional, default: None_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Label of secundary variable in secundary y-axis of plot (right axis).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **var2_color : _str_, _optional, default: '#d2554a'_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Plotting color (HEX code) of secundary variable.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **show_legend : _bool_, _optional, default: True_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set whether legend is shown in plots.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **legend_orientation : _str_, _optional, default: 'horizontal'_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set orientation of legend ('horizontal' or 'vertical'). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **xlim : _list_, _optional, default: [None, None]_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set limits of x-axis with floats ([left limit, right limit]).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ylim_var1 : _list_, _optional, default: [0, 27]_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set limits of primary y-axis (left axis) with floats ([bottom limit, top limit]).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ylim_var2 : _list_, _optional, default: [0, 13]_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set limits of secundary y-axis (right axis) with floats ([bottom limit, top limit]).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ns_label : _bool_, _optional, default: True_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set whether not significant labels ('ns') are shown in plots.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **ns_label_fontsize : _float_, _optional, default: 9_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Size of statistics labels ('ns', '*', '**', '***') over the plots.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **save_fig : _bool_, _optional, default: True_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set whether the plots are saved in Folder `results/`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **x_ticker_format : _str_, _optional, default: '{x:.1f}'_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set x-ticker format.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **stats_dark_vs_light : _bool_, _optional, default: False_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Run stastics comparing dark vs light conditions and save them in an Excel (Folder `results/`).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **stats_coefficient_of_variation : _bool_, _optional, default: False_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calculate coefficient of variation of measurements and save them in an Excel (Folder `results/`).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **CV_method : _str_, _optional, default: RSD_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set method to calculate coefficient of variation.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 'RSD': Relative Standard Deviaiton.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 'QCD': Quartile Coefficient of Dispersion.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **significant_difference_times : _bool_, _optional, default: False_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calculate and show in plot significant differences between t_n and t_n+1.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **significant_difference_t0 : _bool_, _optional, default: False_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calculate and show in plot significant differences between t_0 and t_n.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **show_icon : _bool_, _optional, default: False_** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set wheteher icons are shown in right-top of plots.<br>
**Returns:** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Plots shown in Console/Cell output and saved in Folder `results/` (if `save_fig = True`).**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Statistics outcome in Excel format saved in Folder `results/`.**<br>

[🔼 Back to **Contents**](#readme-contents)

____________________________

## Contact

**Eloi Martinez-Rabert**. :envelope: eloi.mrp@gmail.com

[🔼 Back to **Contents**](#readme-contents)
