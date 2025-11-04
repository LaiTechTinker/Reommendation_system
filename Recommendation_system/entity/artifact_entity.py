from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    training_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str
    drift_message:str
   