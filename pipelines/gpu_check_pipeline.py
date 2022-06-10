import kfp
from kfp import dsl

def gpu_check_op():
    return dsl.ContainerOp(
        name='Test GPU',
        image='tensorflow/tensorflow:latest-gpu',
        command=['sh', '-c'],
        arguments=['nvidia-smi']
    ).set_gpu_limit(1)

@dsl.pipeline(
    name='GPU Test',
    description='Check if GPU is available.'
)
def gpu_pipeline():
    gpu_check = gpu_check_op()

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(gpu_pipeline, 'gpu_check.yaml')