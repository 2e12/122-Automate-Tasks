#!/bin/bash

number1=$1
number2=$2

if [ $number1 == 0 ] 
then
    echo $number2
    exit
fi

while [ $number2 != 0 ]
do
    if [ $number1 -gt $number2 ] 
    then
        number1=$(( $number1 - $number2 ))
    else
        number2=$(( $number2 - $number1 ))
    fi
done

echo $number1
