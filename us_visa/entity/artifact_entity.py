# the outputs we get from data ingestion : test.csv & train.csv
from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 