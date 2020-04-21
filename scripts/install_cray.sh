#!/bin/sh
wget http://www.phoronix-test-suite.com/benchmark-files/c-ray-1.1.tar.gz
wget https://raw.githubusercontent.com/jar/c-ray-1.1-coprthr2/master/sphfract
tar -zxvf c-ray-1.1.tar.gz

cd c-ray-1.1/
cc -o c-ray-mt c-ray-mt.c -lm -lpthread -O3 $CFLAGS
echo $? > ~/install-exit-status
cd ..

echo "#!/bin/sh
cd c-ray-1.1/
RT_THREADS=\$((\$NUM_CPU_CORES * 16))
./c-ray-mt -t \$RT_THREADS -s 3840x2160 -r 16 -i sphfract -o output.ppm > \$LOG_FILE 2>&1
echo \$? > ~/test-exit-status" > c-ray
chmod +x c-ray