from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    training_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str
    drift_message:str
@dataclass
class DataTransformationArtifact:
    transformed_dir:str
    trasformed_trained_file:str
    transformed_test_file:str
   