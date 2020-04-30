rm -rf *.bc *.ll *.o *.s

srcs=( "himenobmtxpa.c" )

# compile all source files
for src in "${srcs[@]}"
do
  clang "../../"$src -I../../ -Xclang -disable-O0-optnone -fomit-frame-pointer -momit-leaf-frame-pointer -S -emit-llvm
done