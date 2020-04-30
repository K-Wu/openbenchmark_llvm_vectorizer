RT_THREADS=16
time ./exe -t 16 -s 3840x2160 -r 16 -i sphfract -o output.ppm
RT_THREADS=16
time ./exe2 -t 16 -s 3840x2160 -r 16 -i sphfract -o output2.ppm