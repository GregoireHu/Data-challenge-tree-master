import argparse
import logging
import os
import warnings
from data_processing.engine import preprocessing_engine
from  machine_learning.engine import ml_processing
warnings.filterwarnings('ignore')

#from machine_learning.engine import machine_learning_engine
#from eda.engine import eda_engine


# Set up logging
logging.basicConfig(level=logging.INFO)

def parse_file_path(path):
    if not os.path.exists(path):
        # raise an error if the path does not exist
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    elif os.path.isdir(path):
        # if the path is a directory, return all CSV files in the directory
        return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]
    elif os.path.isfile(path):
        # if the path is a file, return the file path as a list
        return [path]
    else:
        # raise an error if the path is neither a file nor a directory
        raise ValueError(f"Invalid input: '{path}' is not a file or directory")



def main():
    parser = argparse.ArgumentParser(description='Run the machine learning project engines.')

    parser.add_argument('--preprocess', metavar='data_path', nargs='+', type=str,
                        help='path(s) of the raw data file(s) to be preprocessed. You can use wildcards such as * to specify multiple files.')
    parser.add_argument('--ml', dest='ml', action='store_true',
                        help='run the machine learning engine')
    parser.add_argument('--eda', action='store_true',
                        help='run the exploratory data analysis engine')

    args = parser.parse_args()

    if args.preprocess:
        file_paths = [path for pattern in args.preprocess for path in parse_file_path(pattern)]
        logging.info(f"Running the pre-processing engine on files: {', '.join(file_paths)}")
        preprocessing_engine(file_paths)
        logging.info("Pre-processing complete. You can find the processed files in the 'processed' directory.")
    

    elif args.ml:
       logging.info('Running the machine learning engine')
       ml_processing()
    #elif args.eda:
     #   logging.info('Running the exploratory data analysis engine')
      #  eda_engine()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()




