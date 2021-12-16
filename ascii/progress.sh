#!/bin/bash
#shell script to process mp4 into text files

progressbar() {
    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done

    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")

	printf "\rProgress : |${_fill// /\█}${_empty// /-}| ${_progress}%%"
}

#clean-up of old directories

printf "Converting "
so_far=0
total=$(cat milo.txt)
echo "$total frames..."

total=$(($total * 2 + 2))

sleep 2

while [ $so_far -lt  $total ]
do
	x1=$(ls -l $2 | wc -l)
	x2=$(ls -l $3 | wc -l)
	so_far=$(($x1 + $x2)) 
	progressbar $so_far $total
	sleep 0.05

done
