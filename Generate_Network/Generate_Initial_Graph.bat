@echo off
Generate_DSGL2.py 5000 ..\Data\Source\Acta_Applications.csv ..\Data\Source\Acta_Entity.csv > ..\Data\Input\Acta_DSGL2_Initial_TMP.csv

cat ..\Data\Source\header.dat > ..\Data\Input\Acta_DSGL2_Initial.csv
cat ..\Data\Input\Acta_DSGL2_Initial_TMP.csv | sort | uniq >> ..\data\input\Acta_DSGL2_Initial.csv

erase ..\Data\Input\Acta_DSGL2_Initial_TMP.csv


