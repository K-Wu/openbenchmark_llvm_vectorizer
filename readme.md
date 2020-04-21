# OpenBenchmark Tests for LLVM Custom Vectorization Pass

This repo contains several tests from openbenchmark [1] for the purpose of benchmarking custom vectorization pass.

## Usage
Modify the `myPasses` in the compile.sh script in each benchmark build folder. Compile and run.

The appropriate myPasses variable can be gained in the following way:

1. Obtain the original O3 optimization pipeline.
2. Replace or add your pass to the appropriate position in this optimization pipeline. (Usually beginning or after the vectorization passes, i.e., before -loop-vectorize or after -slp-vectorizer.)

The following code shows how to obtain pass sequence in the original O3 optimization pipeline:

```
[#####@######## ###########]$ llvm-as </dev/null | opt -O3 -disable-output -debug-pass=Arguments
Pass Arguments:  -tti -tbaa -scoped-noalias -assumption-cache-tracker -targetlibinfo -verify -ee-instrument -simplifycfg -domtree -sroa -early-cse -lower-expect
Pass Arguments:  -targetlibinfo -tti -tbaa -scoped-noalias -assumption-cache-tracker -profile-summary-info -forceattrs -inferattrs -domtree -callsite-splitting -ipsccp -called-value-propagation -globalopt -domtree -mem2reg -deadargelim -domtree -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -simplifycfg -basiccg -globals-aa -prune-eh -inline -functionattrs -argpromotion -domtree -sroa -basicaa -aa -memoryssa -early-cse-memssa -speculative-execution -basicaa -aa -lazy-value-info -jump-threading -correlated-propagation -simplifycfg -domtree -aggressive-instcombine -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -libcalls-shrinkwrap -loops -branch-prob -block-freq -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -pgo-memop-opt -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -tailcallelim -simplifycfg -reassociate -domtree -loops -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -loop-rotate -licm -loop-unswitch -simplifycfg -domtree -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -loop-simplify -lcssa-verification -lcssa -scalar-evolution -indvars -loop-idiom -loop-deletion -loop-unroll -mldst-motion -phi-values -basicaa -aa -memdep -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -gvn -phi-values -basicaa -aa -memdep -memcpyopt -sccp -demanded-bits -bdce -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -lazy-value-info -jump-threading -correlated-propagation -basicaa -aa -phi-values -memdep -dse -loops -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -licm -postdomtree -adce -simplifycfg -domtree -basicaa -aa -loops -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -barrier -elim-avail-extern -basiccg -rpo-functionattrs -globalopt -globaldce -basiccg -globals-aa -float2int -domtree -loops -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -loop-rotate -loop-accesses -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -loop-distribute -branch-prob -block-freq -scalar-evolution -basicaa -aa -loop-accesses -demanded-bits -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -loop-vectorize -loop-simplify -scalar-evolution -aa -loop-accesses -loop-load-elim -basicaa -aa -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -simplifycfg -domtree -loops -scalar-evolution -basicaa -aa -demanded-bits -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -slp-vectorizer -opt-remark-emitter -instcombine -loop-simplify -lcssa-verification -lcssa -scalar-evolution -loop-unroll -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instcombine -loop-simplify -lcssa-verification -lcssa -scalar-evolution -licm -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -transform-warning -alignment-from-assumptions -strip-dead-prototypes -globaldce -constmerge -domtree -loops -branch-prob -block-freq -loop-simplify -lcssa-verification -lcssa -basicaa -aa -scalar-evolution -branch-prob -block-freq -loop-sink -lazy-branch-prob -lazy-block-freq -opt-remark-emitter -instsimplify -div-rem-pairs -simplifycfg -verify
Pass Arguments:  -domtree
Pass Arguments:  -targetlibinfo -domtree -loops -branch-prob -block-freq
Pass Arguments:  -targetlibinfo -domtree -loops -branch-prob -block-freq
```

## Included Tests
1. SciMark 1.3.2 https://openbenchmarking.org/innhold/ae5c89d0c2f3f26542cf0be61c4e8b1afcfcfa97
    * >This test runs the ANSI C version of SciMark 2.0, which is a benchmark for scientific and numerical computing developed by programmers at the National Institute of Standards and Technology. This test is made up of Fast Foruier Transform, Jacobi Successive Over-relaxation, Monte Carlo, Sparse Matrix Multiply, and dense LU matrix factorization benchmarks.
2. N-Queens 1.2.1 https://openbenchmarking.org/innhold/650d63a3751db0e4dce260d01d0584d67283591f
    * >This is a test of the OpenMP version of a test that solves the N-queens problem. The board problem size is 18.
3. Smallpt 1.2.1 https://openbenchmarking.org/innhold/49d405a16a7cabc437e6afefcaca140242b1f99b
    * >Smallpt is a C++ global illumination renderer written in less than 100 lines of code. Global illumination is done via unbiased Monte Carlo path tracing and there is multi-threading support via the OpenMP library.
4. Himeno Benchmark 1.3.0 https://openbenchmarking.org/innhold/f8bb3ce687f2b9a04ed8e6116d869875ea79356d
    * >The Himeno benchmark is a linear solver of pressure Poisson using a point-Jacobi method.
5. C-Ray 1.2.0 https://openbenchmarking.org/innhold/91db3ffff901d12dabd732bc568a44d02e5c6387
    * >This is a test of C-Ray, a simple raytracer designed to test the floating-point CPU performance. This test is multi-threaded (16 threads per core), will shoot 8 rays per pixel for anti-aliasing, and will generate a 1600 x 1200 image.

## Unsupported Tests
x Timed HMMer Search 1.1.2 https://openbenchmarking.org/innhold/0f6769daa1e05a4b6541d74551c7f973521233f0

x Timed MAFFT Alignment 1.5.0 https://openbenchmarking.org/innhold/708f4fe22127dc1499397d049f96d0331163d2b0

x GraphicsMagick 2.0.1 https://openbenchmarking.org/innhold/c17e05abdf23597dfaf912058d1ec8c45191f5ba

x Timed ImageMagick Compilation 1.7.2 https://openbenchmarking.org/innhold/d18befcc4fb18537d42b71fdab18c2aeeb261fed

x x264 2.6.1 https://openbenchmarking.org/innhold/3882bb39dde86872bb7ebcb071ebfcc5481e77af

x Timed PHP Compilation 1.5.1 https://openbenchmarking.org/innhold/311b9e5f597e5f35c82cb654e78afdd0421719e1

x Primesieve 1.7.0 https://openbenchmarking.org/innhold/d0da40472d821530a1e2ba99163369b4f13b14ae

x Apache Benchmark 1.7.2 https://openbenchmarking.org/innhold/cc3d6b734f26fde4fa8b0d0d09e7e9078d96afb7

x LAME MP3 Encoding 1.7.4 https://openbenchmarking.org/innhold/7d6b10be9f9f98224f6a2aa94ed3287381798706

x FLAC Audio Encoding 1.6.0 https://openbenchmarking.org/innhold/e1c20b2e195536f5bc128d11968e43dcc22e6a43

## Reference
1. OpenBenchmark Test on SLPVectorizer in LLVM 3.4 <https://openbenchmarking.org/result/1307291-SO-FSLPVECTO83>