srcs=( "scimark2.c" "FFT.c" "kernel.c" "Stopwatch.c" "Random.c" "SOR.c" "SparseCompRow.c" "array.c" "MonteCarlo.c" "LU.c" )

# compile all source files
for src in "${srcs[@]}"
do
  clang "../../"$src -I../../ -Xclang -disable-O0-optnone -fomit-frame-pointer -momit-leaf-frame-pointer -S -emit-llvm
done