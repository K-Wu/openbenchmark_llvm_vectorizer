myPasses=-O3
rm -rf *.bc *.ll *.o *.s exe    
clang++ ../*.cpp -Wno-c++11-narrowing -fopenmp -I/opt/intel/compilers_and_libraries_2020.1.217/linux/compiler/include/omp.h  -Xclang -disable-O0-optnone -fomit-frame-pointer -Xclang -vectorize-loops -Xclang -vectorize-slp -momit-leaf-frame-pointer -S -emit-llvm
for filename in $(ls | grep .ll)
do
    opt ${filename::-3}.ll $myPasses -o ${filename::-3}.bc
    llc ${filename::-3}.bc -O3  -o ${filename::-3}.s
    clang++ -c ${filename::-3}.s
done
clang++ *.o -lm  -fopenmp -L/opt/intel/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64/libiomp5.so -o exe -mno-relax-all
