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
- easyocr
- googletrans
- gtts
- PIL
- numpy

doing the steps above makes sure that your current pip installs wont interfere with my required python libs.


Run the app by....

```
streamlit run app.py
```

disclaimer: not yet perfect. to be further modified.
