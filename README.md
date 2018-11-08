# tensorflow-atom
Testing what, if anything, can be accomplished with Tensorflow on an Intel Atom processor.

The default builds of Tensorflow do not support the Atom CPU
It must be built from source. Here is a guide for that https://software.intel.com/en-us/articles/intel-optimization-for-tensorflow-installation-guide

The Atom machine did not have enouph memory or power to build from source so I used an other Intel machine with same OS (Ubuntu 18.04) and compiled without AVX support
