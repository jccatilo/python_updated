reference https://www.youtube.com/watch?v=xl0N7tHiwlw

Setting up your conda-python environment

1. Create a folder for your project.
2. Open the folder in the anaconda terminal.
3. Create your conda environment using the command below. Answer **y** when asked to proceed. this might take some time.

```
conda create -n <environment_name> python=3.9
```
4. Activate your environment using the **activate** command.
```
conda activate <environment_name>
```
5. Install the libraries using **conda install**.
- streamlit
- numpy
- pandas
- matplotlib
- scikit-learn

6. Install a kernel for your environment
```
ipython kernel install --user --name=<environment_name>
```
7. Start your jupiter notebook.


