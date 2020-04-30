rm -rf *.bc *.ll *.o *.s

srcs=( "smallpt.cpp" )

# compile all source files
for src in "${srcs[@]}"
do
  clang++ "../../"$src -I../../ -Wno-c++11-narrowing -fopenmp -I/opt/intel/compilers_and_libraries_2020.1.217/linux/compiler/include/omp.h  -Xclang -disable-O0-optnone -fomit-frame-pointer -momit-leaf-frame-pointer -S -emit-llvm
done