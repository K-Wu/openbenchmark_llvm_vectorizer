import os
import sys
import subprocess
def compiler_and_run_dir(dir, ours=False):
    myPasses = "-load ../../../build/pass/libSLPVectorizer-kdw.so -tti -tbaa -scoped-noalias -assumption-cache-tracker -targetlibinfo -verify -ee-instrument -simplifycfg -domtree -sroa -early-cse -lower-expect -targetlibinfo -tti -tbaa -scoped-noalias -assumption-cache-tracker -profile-summary-info -forceattrs -inferattrs -domtree -callsite-splitting -ipsccp -called-value-propagation -globalopt -domtree -mem2reg -deadargelim -domtree -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -simplifycfg -basiccg -globals-aa -prune-eh -inline -functionattrs -argpromotion -domtree -sroa -basicaa -aa -memoryssa -early-cse-memssa -speculative-execution -basicaa -aa -lazy-value-info -jump-threading -correlated-propagation -simplifycfg -domtree -aggressive-instcombine -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -libcalls-shrinkwrap -loops -branch-prob -block-freq -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -pgo-memop-opt -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -tailcallelim -simplifycfg -reassociate -domtree -loops -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -loop-rotate -licm -loop-unswitch -simplifycfg -domtree -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -loop-simplify -lcssa-verification -lcssa -scalar-evolution -indvars -loop-idiom -loop-deletion -loop-unroll -mldst-motion -phi-values -basicaa -aa -memdep -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -gvn -phi-values -basicaa -aa -memdep -memcpyopt -sccp -demanded-bits -bdce -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -lazy-value-info -jump-threading -correlated-propagation -basicaa -aa -phi-values -memdep -dse -loops -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -licm -postdomtree -adce -simplifycfg -domtree -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -barrier -elim-avail-extern -basiccg -rpo-functionattrs -globalopt -globaldce -basiccg -globals-aa -float2int -domtree -loops -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -loop-rotate -loop-accesses -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -loop-distribute -branch-prob -block-freq -scalar-evolution -basicaa -aa -loop-accesses -demanded-bits -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -loop-vectorize -loop-simplify -scalar-evolution -aa -loop-accesses -loop-load-elim -basicaa -aa -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -simplifycfg -domtree -loops -scalar-evolution -basicaa -aa -demanded-bits -lazy-branch-prob -lazy-block-freq -opt-remark-emitter %s -opt-remark-emitter -instcombine -loop-simplify -lcssa-verification -lcssa -scalar-evolution -loop-unroll -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -loop-simplify -lcssa-verification -lcssa -scalar-evolution -licm -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -transform-warning -alignment-from-assumptions -strip-dead-prototypes -globaldce -constmerge -domtree -loops -branch-prob -block-freq -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -branch-prob -block-freq -loop-sink -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instsimplify -div-rem-pairs -simplifycfg"%'-slpvect-kdw' if ours else '-slp-vectorizer'
    command = ''
    command += "rm -rf *.bc *.ll *.o *.s exe"+'\n'
    command += "clang ../*.c -Xclang -disable-O0-optnone -fomit-frame-pointer -Xclang -vectorize-loops -Xclang -vectorize-slp -momit-leaf-frame-pointer -S -emit-llvm"+'\n'
    command += ("#optimize all ll files" + '\n' + \
                "for filename in $(ls | grep .ll)" + '\n' + \
                "do" + '\n' + \
                "   opt ${filename::-3}.ll %s -o ${filename::-3}.bc" + '\n' + \
                "   llc ${filename::-3}.bc -O3 -o ${filename::-3}.s" + '\n' + \
                "   clang -c ${filename::-3}.s" + '\n' + \
                "done" + '\n' + \
                "clang *.o -lm -o exe -mno-relax-all")%myPasses
    with open(dir+'/build/compile.sh', 'w') as f:
        f.write(command)
    os.system('. %s; cd %s/build; chmod +x compile.sh; ./compile.sh;'%('/home/cs526/cs526_mp2/env.sh', dir))
    output = subprocess.check_output('. %s; cd %s/build; chmod +x run.sh; ./run.sh'%('/home/cs526/cs526_mp2/env.sh', dir), universal_newlines=True, shell=True)
    print(output)
    return output

#for dir in ['himeno', 'scimark2_files', 'smallpt-1', 'c-ray-1.1']:
for dir in ['himeno', ]:#, 'scimark2_files', 'smallpt-1', 'c-ray-1.1']:
    output_ours = compiler_and_run_dir(dir, ours=True)
    output_original = compiler_and_run_dir(dir, ours=False)
