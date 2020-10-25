# Environemnt Setup

> Please take the time to setup your Python environment ahead of time.  Even seasoned experts of Python may run into a library problem and need more time to work it out.  Our timeline for this session won't allow me to help everyone personally so please take advantage of this guide prior to attending our session together.

It's ideal to setup a Python environment for each project you work on. Having a separate environment for each independent Python project or domain allows:

- Fewer library inconsistencies 
- Minimal library complexity
- Maximum project portability

For example, you might have a Python environment specifically for Jupyter and a specific analysis or one for a dashboard application. I recommend that you set up an environment, especially for this session, mainly for these reasons:

- We all run the same libraries and versions
- Any problems we encounter are more likely to be shared amongst everyone
- It's easier to support each other in chat when we have the same problems

So with this in mind, you can choose to install the following libraries in your own environment, but it's strongly recommended that you setup a new environment!


## 1. Anaconda Environments

It's recommended to use Anaconda to install the Python environment because it's easy to install a specific Python version along with the required packages in our [requirements.txt](./requirements.txt) file.  You can also use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/), but the setup is a bit trickier to use a specific version of Python with.
> If you're already hip to setting up and managing your Python environments, you can move on to the next step in setup and configuration.

### 1.1 Anaconda
Using [Anaconda Individual](https://www.anaconda.com/products/individual), create an environemnt called `odsc-dv` with the appropriate packages using Python `3.8.5` with the following command from this cloned repo:

```bash
conda create --name odsc-dv --file requirements.txt python=3.8.5
```

> After you create the environment `odsc-dv`, it will give you instructions on how to activate it.

Activate the environment prior to using Jupyter lab, Panel, or Flask:

```bash
conda activate odsc-dv
```

## 2. Enable Pyviz Extension For Jupyter Lab

We will be exploring the [Panel](https://panel.holoviz.org/getting_started/index.html) library with Jupyter and with Flask.

### 2.1 From Terminal

> _"JupyterLab extensions are npm packages (the standard package format in Javascript development). You can search for the keyword jupyterlab-extension on the npm registry to find extensions. For information about developing extensions, see the developer documentation."_ 

In order to install JupyterLab extensions, you need to have Node.js installed.  If you don't have nodejs, the labextension command below will not work.  So if you do have an issue, you might first try verifying that running `node` from the command line works:

![](https://snipboard.io/1ufWbF.jpg)

> You can type .exit in the node console to exit.


To use panel widgets in Jupyter, you need to enable them using the `labextension` command.  This only needs to be 1x when first setting up your environment:
```bash
jupyter labextension install @pyviz/jupyterlab_pyviz
```

If everything worked out ok, there should be no errors (red console text).  If you do run into errors, double check that node is in stalled (see above).  If you are having problems, please post in Slack prior to our session as there will be very limited time to address any issues once our session begins.


## 3. Run Test Notebook + App

### 3.1 Test Panel Notebook

If you made it this far, check the [prerequisite.ipynb](./notebooks/prerequisite.ipynb) from Jupyter Lab and ensure that the default widgets.  If everything instlled in your `odsc-dv` environment, you should be able to use Panel, Matplotlib, Pandas, and Flask.

![](https://snipboard.io/bquGBr.jpg)
> The prerequisites notebook has an exciting sine function to check your environment against.  If it runs, congrats!  Most of lifes problems are solved!


Also, check that the demo Panel server application works as well:

```bash
python demo.py
```

> Double check that you are in the `odsc-dv` environment!

![](https://snipboard.io/5D3pVB.jpg)

Then check that the application is running in your browser @ http://localhost:8080

![](https://snipboard.io/olYSFy.jpg)
>  You should see the 2 panel applications visible in the list and they should both load.

![](https://snipboard.io/jWO69G.jpg)

### 3.1 Test Flask App

> Double check that you are in the `odsc-dv` environment!
```bash
export FLASK_APP=flask-demo.py
flask run
```

![](https://snipboard.io/Whiduv.jpg)

If successful, you should be able to load the basic Flask app in your browser:

http://127.0.0.1:5000/

![](https://snipboard.io/lBEsRt.jpg)


## 4. Have a Code Editor Installed

This is hopefully the easiest step in all of this.  In our last session we will be coding outside of Jupyter Lab so it will be useful to have one of the following installed:

- [Microsoft VSC](https://code.visualstudio.com/)
- [Sublime Text](https://www.sublimetext.com/)
- [Atom](https://atom.io/)

We will be coding an app step-by-step and then stopping to check-in at various points.


















