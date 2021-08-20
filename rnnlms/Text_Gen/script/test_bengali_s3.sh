#!/bin/bash

rnnpath=/home/snlp-project-21/rnnlm/
trainfile=../data/bengali/s3.txt
testfile=../data/bengali/s3_test.txt
rnnmodel=../models/bengali/model_s3
temp=../temp

if [ ! -e $rnnmodel ]; then
    echo "model file not found... run first train.sh"
    exit
fi

echo "Generating data..."

$rnnpath/rnnlm -rnnlm $rnnmodel -gen 10 -debug 0 > $temp/generated_s3_10.txt

$rnnpath/rnnlm -rnnlm $rnnmodel -gen 100 -debug 0 > $temp/generated_s3_100.txt

$rnnpath/rnnlm -rnnlm $rnnmodel -gen 1000 -debug 0 > $temp/generated_s3_1000.txt

$rnnpath/rnnlm -rnnlm $rnnmodel -gen 10000 -debug 0 > $temp/generated_s3_10000.txt

$rnnpath/rnnlm -rnnlm $rnnmodel -gen 100000 -debug 0 > $temp/generated_s3_100000.txt

$rnnpath/rnnlm -rnnlm $rnnmodel -gen 1000000 -debug 0 > $temp/generated_s3_1000000.txt

$rnnpath/rnnlm -rnnlm $rnnmodel -gen 10000000 -debug 0 > $temp/generated_s3_10000000.txt

echo "Data Generation done"
