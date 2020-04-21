myPasses=-O3
rm -rf *.bc *.ll *.o *.s exe    
clang ../c-ray-mt.c  -Xclang -disable-O0-optnone -fomit-frame-pointer -Xclang -vectorize-loops -Xclang -vectorize-slp -momit-leaf-frame-pointer -S -emit-llvm
for filename in $(ls | grep .ll)
do
    opt ${filename::-3}.ll $myPasses -o ${filename::-3}.bc
    llc ${filename::-3}.bc -O3  -o ${filename::-3}.s
    clang -c ${filename::-3}.s
done
clang *.o -lm -lpthread -o exe -mno-relax-all
