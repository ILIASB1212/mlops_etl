from dataclasses import dataclass
import databricks


@dataclass
class DataIngestionArtifactes:
    train_file_path:str
    test_file_path:str