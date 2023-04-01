import argparse
from pre_processing.engine import pre_process
from machine_learning.engine import machine_learning_engine
from eda.engine import eda_engine


# Set up logging
logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description='Run the machine learning project engines.')

    parser.add_argument('--pre-processing', dest='pre', action='store_true',
                        help='run the pre-processing engine')
    parser.add_argument('--machine-learning', dest='ml', action='store_true',
                        help='run the machine learning engine')
    parser.add_argument('--eda', action='store_true',
                        help='run the exploratory data analysis engine')

    args = parser.parse_args()

    if args.pre:
        logging.info('Running the pre-processing engine')
        pre_processing_engine()
    elif args.ml:
        logging.info('Running the machine learning engine')
        machine_learning_engine()
    elif args.eda:
        logging.info('Running the exploratory data analysis engine')
        eda_engine()
    else:
        parser.print_help()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f"Error: {e}")




