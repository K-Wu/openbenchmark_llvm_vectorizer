clang ../../*.c -fopenmp -I/opt/intel/compilers_and_libraries_2020.1.217/linux/compiler/include/omp.h  -Xclang -disable-O0-optnone -fomit-frame-pointer -momit-leaf-frame-pointer -S -emit-llvm
