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

1. **Suggested:** In case you cannot install Python locally on your computer, you may run the codes through [Google Colab](https://colab.research.google.com/) by clicking on the links to the jupyter notebooks below, then clicking on the "Open in Colab" button at the top of the notebook. This will work on any computer, mobile or tablet that has internet access and a standard web browser like Google Chrome, Microsoft Edge, Firefox or whatever. However, these codes will run on colab servers, rather than locally on your computer. This is usually not a problem, although the servers might be slow.

2. In order to run these programs locally in your computer (instead of Google Colab), perform the following steps.

     * Install GitHub Desktop after downloading it from its website @ [desktop.github.com](https://desktop.github.com/)
       
     * Then, download this repository by cloning it using GitHub Desktop (see [this doc](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)  for details).
       
     * Finally, download and install the anaconda python distribution (anaconda @ https://www.anaconda.com/). Anaconda includes [Jupyter notebooks](https://jupyter.org/) and the [Spyder IDE](https://www.spyder-ide.org/), either of which can be readily used for designing and running python code. Also, see [this blog entry](https://fangohr.github.io/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html) on how to install anaconda.

3. If you're having problems with Git, and do not want to use Google Colab, you can simply copy-paste the codes individually into your local python setup:
   
   * Click on the "Copy raw contents" button on the top-right corner of the github page of a particular code (to the right of the 'Blame' button).
   
   * Then, paste it into a text editor or a running python IDE like [Spyder](https://www.spyder-ide.org/) or [Pydroid](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) in order to execute it. 
   
   * **However**, this will only work for regular Python, not for Jupyter notebooks. For the latter, you can either run them in Google Colab, or copy-paste each code cell from the jupyter notebook to a local Python file in your device. This should work well on Android devices, where it is difficult to run jupyter locally. Note, however, that IPython magics won't work in regular Python, and you'll have to delete or rewrite them.

List of Tutorials and Codes
=========================

Use the following links:

## Scientific Python Tutorials:

* [Scientific Python Tutorials (including numpy and matplotlib)](https://github.com/hariseldon99/scientific-python-lectures)

* [Quick Introduction to polynomials in NumPy](https://kitchingroup.cheme.cmu.edu/blog/2013/01/22/Polynomials-in-python/)

* [Quantum Harmonic Oscillator using NumPy and Matplotlib](https://github.com/hariseldon99/Quantum-Harmonic-Numpy)

## Computational Physics in Python, Lecture Slides:


## Computational Physics in Python, Example Codes:

* [Examples of Partial Differential Equations using Finite Difference Method](PDE_FDM.ipynb)
* [Examples of Quantum Physics using QutiP](QUTIP.ipynb)
* [Examples of Fast Fourier Transforms (FFT)](FFT.ipynb)
* [Examples of the Monte carlo Method](MC.ipynb)

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
