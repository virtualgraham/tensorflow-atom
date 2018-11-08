# tensorflow-atom
Testing what, if anything, can be accomplished with Tensorflow on an Intel Atom processor.

The default builds of Tensorflow do not support the Atom CPU.

It must be built from source. Here is a guide for that: https://www.tensorflow.org/install/source and https://software.intel.com/en-us/articles/intel-optimization-for-tensorflow-installation-guide

The Atom machine did not have enouph memory or power to build from source so I used another Intel machine with same OS (Ubuntu 18.04 64bit) and compiled without AVX but with MKL support.

Here is how the build was configured using ./configure. The important part is where the eoptimization flags are set to `-march=atom -mtune=atom` 

```
Please specify the location of python. [Default is /usr/bin/python]: 
Found possible Python library paths:
  /usr/local/lib/python2.7/dist-packages
  /usr/lib/python2.7/dist-packages
Please input the desired Python library path to use.  Default is [/usr/local/lib/python2.7/dist-packages]
Do you wish to build TensorFlow with jemalloc as malloc support? [Y/n]: y
jemalloc as malloc support will be enabled for TensorFlow.
Do you wish to build TensorFlow with Google Cloud Platform support? [Y/n]: n
No Google Cloud Platform support will be enabled for TensorFlow.
Do you wish to build TensorFlow with Hadoop File System support? [Y/n]: n
No Hadoop File System support will be enabled for TensorFlow.
Do you wish to build TensorFlow with Amazon AWS Platform support? [Y/n]: n
No Amazon AWS Platform support will be enabled for TensorFlow.
Do you wish to build TensorFlow with Apache Kafka Platform support? [Y/n]: n
No Apache Kafka Platform support will be enabled for TensorFlow.
Do you wish to build TensorFlow with XLA JIT support? [y/N]: n
No XLA JIT support will be enabled for TensorFlow.
Do you wish to build TensorFlow with GDR support? [y/N]: n
No GDR support will be enabled for TensorFlow.
Do you wish to build TensorFlow with VERBS support? [y/N]: n
No VERBS support will be enabled for TensorFlow.
Do you wish to build TensorFlow with nGraph support? [y/N]: n
No nGraph support will be enabled for TensorFlow.
Do you wish to build TensorFlow with OpenCL SYCL support? [y/N]: n
No OpenCL SYCL support will be enabled for TensorFlow.
Do you wish to build TensorFlow with CUDA support? [y/N]: n
No CUDA support will be enabled for TensorFlow.
Do you wish to download a fresh release of clang? (Experimental) [y/N]: n
Clang will not be downloaded.
Do you wish to build TensorFlow with MPI support? [y/N]: n
No MPI support will be enabled for TensorFlow.
Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]: -march=atom -mtune=atom
Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]: n
```
Here is the build command with `--config=mkl` set

```
nohup bazel build --config=mkl --config=opt //tensorflow/tools/pip_package:build_pip_package &
```

This wheel seems to perform better than the one I built here:
https://github.com/yaroslavvb/tensorflow-community-wheels/issues/86

## Results

#### Google Compute with single Intel Broadwell vCPU:

```
60000/60000 [==============================] - 95s 2ms/step - loss: 0.1688 - acc: 0.9459
Epoch 2/5
60000/60000 [==============================] - 93s 2ms/step - loss: 0.0470 - acc: 0.9851
Epoch 3/5
60000/60000 [==============================] - 94s 2ms/step - loss: 0.0323 - acc: 0.9899
Epoch 4/5
60000/60000 [==============================] - 94s 2ms/step - loss: 0.0240 - acc: 0.9925
Epoch 5/5
60000/60000 [==============================] - 94s 2ms/step - loss: 0.0200 - acc: 0.9937
10000/10000 [==============================] - 5s 467us/step
0.9908
```

#### Google Compute with Tesla P4 GPU:

```

```

#### Intel Atom x5-Z8300 CPU:

```

```
