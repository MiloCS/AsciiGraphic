#concurrently running progress bar and image processing

python process_frames.py $1 $2 $3 & 
P1=$! &
./progress.sh $1 $2 $3 &
P2=$!

wait $P1 $P2

printf "\nFinished processing"