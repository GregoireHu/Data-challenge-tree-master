## House Price Predictions

This project includes a command-line interface to run engines for exploratory data analysis and machine learning on real estate data.

### Installation

To use this project, first clone the repository

```
git clone https://github.com/salahmouslih/data-challenge.git
cd data-challenge
```

Next, create and activate a virtual environment then install the required packages using pip:

```
python3 -m venv env 
source env/bin/activate # activate the virtual environment (Unix)
env\Scripts\activate    # activate the virtual environment (Windows)
```

```
pip install -r requirements.txt
```

### Usage

#### Download data

Before running the preprocessing engine, you need to make sure that the required data is available in the correct directory. 

Specifically, you need to download and unzip the raw data file(s) available at [raw_data](https://drive.google.com/file/d/1DvGKiCj-ywh_SthmYUayIZ7W5onqwJF-/view?usp=share_link) then place the extracted files in the `data/raw` directory.
Similarily, download and unzip public data available at [public_data](https://drive.google.com/file/d/1HQUMVZtvtxghBXzWahRg8CDM5oh1vJIB/view?usp=share_link) then place the extracted files in the `data/open_data` directory. 

Once the data is in the correct directory, you can proceed with running the main.py script with the desired command line arguments. The available options are:

- **preprocess** : preprocess the specified raw data file(s).
- **ml** : run the machine learning engine.
- **eda** : run the exploratory data analysis engine.

#### Pre-processing Engine
To preprocess the raw data, run the following command:

``` python src/main.py --preprocess path/to/raw/data.csv ```

You can also preprocess multiple files at once using wildcards:

``` python src/main.py --preprocess path/to/directory/*.csv ```

The preprocessed files will be stored in the `processed` directory.

#### Machine Learning Engine
To run the machine learning engine on the processed data, use the following command:

``` python src/main.py --ml ```

This engine trains machine learning models on the preprocessed data and saves the evaluation metrics in the `output/models` directory.
Note that you need to run the preprocessing engine first.

#### Exploratory Data Analysis Engine

To run the exploratory data analysis engine, use the following command:

```python src/main.py --eda path/to/processed/data.csv```

This engine generates exploratory data analysis visualizations and saves them in the `plots` directory.

#### Help

To see the available command-line arguments, run the following command:

``` python src/main.py --help``` 

## Notebooks
The original notebooks can be found at the `notebooks` folder.

## Documentation
The project documentation can be found at `docs/documentation/index.html`.

## General structure

```
├── README.md
├── data
│   ├── open_data
│   ├── processed  
│   └── raw
├── docs
├── models
├── notebooks
│   ├── processing_notebook.py
│   ├── eda_notebook.py
│   └── ml_notebook.py
├── output
│   ├── models
│   └── plots
├── requirements.txt
├── setup.py
├── screenshots
├── src
│   ├── data_processing
│   │   ├── amenities.py
│   │   ├── clean.py
│   │   ├── clean.pyc
│   │   ├── discount.py
│   │   ├── education.py
│   │   ├── engine.py
│   │   ├── engine.pyc
│   │   ├── filters.py
│   │   ├── stats.py
│   │   └── utilities.py
│   ├── eda
│   │   ├── core.py
│   │   ├── eda_engine.py
│   │   └── utilities.py
│   ├── machine_learning
│   │   ├── engine.py
│   │   ├── preprocess.py
│   │   ├── scores.py
│   │   └── utilities.py
│   ├── main.py
│   └── utils
└── tests
```


## Licence
## Acknowledgments 
