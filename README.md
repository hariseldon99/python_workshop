Python Workshop
============================================

Python lectures and codes for the National Workshop on Python in Scientific Computing, taught at the University Science Instrumentation Centre (USIC), The University of Burdwan

A repository of all my codes, tutorial lectures and simulations used to teach [Computational Physics in Python](https://www.buruniv.ac.in/usic/Python%20Flyer2023.pdf) to students at the 
[USIC](https://www.buruniv.ac.in/usic/index.html) in [The University of Burdwan](https://www.buruniv.ac.in/)

The simulations are written in the [Python programming language](https://www.python.org/about/gettingstarted/).

Background
=========================

* For a quick introduction to the Python programming language, as well as [Numerical Python](https://numpy.org), [Scientific Python](https://scipy.org) and [Matplotlib](https://matplotlib.org), see [this tutorial](https://cs231n.github.io/python-numpy-tutorial/)

* For a more detailed introduction to the abovementioned topics, see Robert Johansson's [Scientific Python Lectures](https://github.com/jrjohansson/scientific-python-lectures).

# Instructions

You can run these python codes by installing the requisite software in your computer, or online through [Google Colab](https://colab.research.google.com/).

1. **Suggested:** If you can't install Python locally, you can run the codes through [Google Colab](https://colab.research.google.com/) by clicking on the links to the jupyter notebooks below and then hitting "Open in Colab" at the top. This works on any computer, smartphone, or tablet with internet connectivity and a web browser like Chrome, Edge, Firefox, etc. These scripts will execute on colab servers, not your machine. Although servers may be slow, this is usually not a problem.

2. In order to run these programs locally in your computer (instead of Google Colab), perform the following steps.

     * Install GitHub Desktop after downloading it from its website @ [desktop.github.com](https://desktop.github.com/)
       
     * Then, download this repository by cloning it using GitHub Desktop (see [this doc](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)  for details).
       
     * Anaconda (https://www.anaconda.com/) should be downloaded and installed last. [Jupyter notebooks](https://jupyter.org/) or the [Spyder IDE](https://www.spyder-ide.org/) can be used to design and run Python code in Anaconda. See [this blog post](https://fangohr.github.io/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html) for anaconda installation instructions.
            
     * Optionally, if you need to do the Finite Element Method (FEM) computations, you might want to install the [SfePy](https://sfepy.org/) package.
Load a shell with the anaconda base environment activated.  

		On Windows, this can be done by opening the "Anaconda PowerShell Prompt" from "Start Menu". See the image below for details.

		[![Alt text](https://shaileshjha.com/wp-content/uploads/2020/03/windows_start_menu_anaconda_powershell_prompt.jpg)](https://shaileshjha.com/wp-content/uploads/2020/03/windows_start_menu_anaconda_powershell_prompt.jpg)
	
		On Linux, simply start a [terminal emulator](https://www.linfo.org/terminal_window.html) like [gnome-terminal](https://help.ubuntu.com/community/GnomeTerminal) and activate anaconda with the shell command
		```console
		$ conda activate base
		```
		
 		Next, run the commands given below:
		```console
		(base) PS C:\Users~1> conda config --add channels conda-forge
		(base) PS C:\Users~1> conda install sfepy
		```
		**Note that** you might want to install sfepy in a fresh conda environment. [See this link for details](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
   
	* **Recommended:** The default version of python in anaconda can be a little old. I would suggest that you update the python to at least [version 3.11](https://www.python.org/downloads/release/python-3110/) in a fresh conda environment. To check if the default version is older than 3.11, open the Anaconda PowerShell Prompt as described above and run the following command
	```console
	(base) PS C:\Users~1> python --version
	```
	If the version is older than 3.11, then run the following commands to create an environment (named 'exercises') with python version 3.11 inside it, then install all necessary packages and activate the environment for use.
	```console
	(base) PS C:\Users~1> conda config --add channels conda-forge
	(base) PS C:\Users~1> conda create -n exercises python=3.11 numpy scipy matplotlib qutip sfepy
	(base) PS C:\Users~1> conda activate exercises
	```
3. If you're having problems with Git, and do not want to use Google Colab, you can simply copy-paste the codes individually into your local python setup:
   
   * Click on the "Copy raw contents" button on the top-right corner of the github page of a particular code (to the right of the 'Blame' button).
   
   * Then, paste it into a text editor or a running python IDE like [Spyder](https://www.spyder-ide.org/) or [IDLE](https://docs.python.org/3.11/library/idle.html) in order to execute it. 
   
   * **However**, this only works for normal Python, not Jupyter notebooks. You can run them in Google Colab or copy-paste each code cell from the jupyter notebook to a local Python file on your device. In standard Python, IPython magics won't work, so delete or rewrite them.

List of Tutorials and Codes
=========================

Use the following links:

## Computational Physics in Python: Learning Materials:

* [Lecture Notes (ODP with animations)](Lecture_Notes.odp) 
* [Lecture Notes (PDF without animations)](Lecture_Notes.pdf)


## Computational Physics in Python, Example Codes:

* [Examples of Partial Differential Equations using Finite Difference Method](PDE_FDM.ipynb)
* [Examples of Partial Differential Equations using Finite Element Method](PDE_FEM.ipynb)
* [Examples of Quantum Physics using QutiP](QUTIP.ipynb)
* [Examples of Fast Fourier Transforms (FFT)](FFT.ipynb)
* [Examples of the Monte Carlo Method](MC.ipynb)


## Computational Physics in Python: Background Materials:

* [Scientific Python Tutorials (including numpy and matplotlib)](https://github.com/hariseldon99/scientific-python-lectures)

* [Quick Introduction to polynomials in NumPy](https://kitchingroup.cheme.cmu.edu/blog/2013/01/22/Polynomials-in-python/)

* [Quantum Harmonic Oscillator using NumPy and Matplotlib](https://github.com/hariseldon99/Quantum-Harmonic-Numpy)

* [SfePy: Simple Finite Elements in Python](https://sfepy.org/), including [extensive documentation](https://sfepy.org/doc-devel/documentation.html) and [theoretical background](https://sfepy.org/doc-devel/theory.html).

License
=======

This work is licensed under a [MIT License](LICENSE)

Author
=======

Analabha Roy  
Assistant Professor,  
[Department of Physics](https://sites.google.com/a/phys.buruniv.ac.in/physics/),  
[The University of Burdwan](https://www.buruniv.ac.in/)  
[Bardhaman](https://en.wikivoyage.org/wiki/Bardhaman), India 713104  
Webpage: https://www.ph.utexas.edu/~daneel
