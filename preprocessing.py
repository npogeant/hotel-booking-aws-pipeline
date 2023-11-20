
import argparse
import pathlib
import boto3
import os
import pandas as pd
import logging
from sklearn.model_selection import train_test_split

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--validation-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    args, _ = parser.parse_known_args()
    logger.info("Received arguments {}".format(args))
    
    # Set local path prefix in the processing container
    local_dir = "/opt/ml/processing"    
    
    input_data_path = os.path.join("/opt/ml/processing/bookings", "bookings.csv")
    
    logger.info("Reading data from {}".format(input_data_path))
    df = pd.read_csv(input_data_path)
    
    # Split into train, validation, and test sets
    train_ratio = args.train_ratio
    val_ratio = args.validation_ratio
    test_ratio = args.test_ratio
    
    logger.debug("Splitting data into train, validation, and test sets")
    
    y = df['is_canceled']
    X = df.drop(['is_canceled'], axis = 1)
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=val_ratio, random_state=42)

    train_df = pd.concat([y_train, X_train], axis = 1)
    val_df = pd.concat([y_val, X_val], axis = 1)
    test_df = pd.concat([y_test, X_test], axis = 1)
    dataset_df = pd.concat([y, X], axis = 1)
    
    logger.info("Train data shape after preprocessing: {}".format(train_df.shape))
    logger.info("Validation data shape after preprocessing: {}".format(val_df.shape))
    logger.info("Test data shape after preprocessing: {}".format(test_df.shape))
    
    # Save processed datasets to the local paths in the processing container.
    # SageMaker will upload the contents of these paths to S3 bucket
    logger.debug("Writing processed datasets to container local path.")
    train_output_path = os.path.join(f"{local_dir}/train", "train.csv")
    validation_output_path = os.path.join(f"{local_dir}/val", "validation.csv")
    test_output_path = os.path.join(f"{local_dir}/test", "test.csv")
    full_processed_output_path = os.path.join(f"{local_dir}/full", "dataset.csv")

    logger.info("Saving train data to {}".format(train_output_path))
    train_df.to_csv(train_output_path, index=False)
    
    logger.info("Saving validation data to {}".format(validation_output_path))
    val_df.to_csv(validation_output_path, index=False)

    logger.info("Saving test data to {}".format(test_output_path))
    test_df.to_csv(test_output_path, index=False)
    
    logger.info("Saving full processed data to {}".format(full_processed_output_path))
    dataset_df.to_csv(full_processed_output_path, index=False)
