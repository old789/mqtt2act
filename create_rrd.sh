#!/usr/bin/env bash

if [ -z "$2" -a -z "$1" ]; then
    echo "Usage: $0 <RRD's name> <obj name>"
    exit
fi

NAME=$1
OBJ=$2
RRDDIR="/var/db/rrd/"

STEP=60
HEARTBEAT=$((2*$STEP))
START=$(date +%s)

if [ ! -d "$RRDDIR" ]; then
    mkdir -p "$RRDDIR" || exit
fi

RRDf="$RRDDIR$NAME.rrd"

if [ -f "$RRDf" ]; then
    echo "$RRDf" exists!
    exit
fi

rrdtool create "$RRDf" \
            --start $START  --step $STEP \
            DS:$OBJ:GAUGE:$HEARTBEAT:U:U   \
            RRA:AVERAGE:0.5:1:1440  \
            RRA:AVERAGE:0.5:7:1440  \
            RRA:AVERAGE:0.5:30:17280

if [ -f "$RRDf" -a -s "$RRDf" ]; then
    echo "$RRDf" created
fi

