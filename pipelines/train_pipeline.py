import os
import sys
from functools import partial

import kfp
from kfp import dsl

assert len(sys.argv) == 3, "three CLI arguments required: <output_file>, <image>, <components_dir>"
OUTPUT_FILE, COMPONENTS_PATH = sys.argv[1:]

training_component = kfp.components.load_component_from_url("https://github.com/kedarw/kubeflow-demo/blob/main/components/train.yaml")

if __name__ == "__main__":
    print(f"creating training pipeline for image {IMAGE}")

    kfp.compiler.Compiler().compile( pipeline_func=training_component, package_path=OUTPUT_FILE)
