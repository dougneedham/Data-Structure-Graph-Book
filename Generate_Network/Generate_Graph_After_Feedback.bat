@echo off
Generate_DSGL2.py 3500 ..\Data\Source\Acta_Prime.csv ..\Data\Source\Acta_Entity.csv 		 	> ..\Data\Input\Acta_DSGL2_feedback_tmp.csv
Generate_DSGL2.py 500 ..\Data\Source\EBJ_Prime.csv ..\Data\Source\EBJ_Entity.csv 		 	>> ..\Data\Input\Acta_DSGL2_feedback_tmp.csv
Generate_DSGL2.py 200 ..\Data\Source\FRWN_Prime.csv ..\Data\Source\FRWN_Entity.csv 		 	>> ..\Data\Input\Acta_DSGL2_feedback_tmp.csv
Generate_DSGL2.py 100 ..\Data\Source\WDY_Prime.csv ..\Data\Source\WDY_Entity.csv 		 	>> ..\Data\Input\Acta_DSGL2_feedback_tmp.csv
Generate_DSGL2.py 150 ..\Data\Source\Connected_Applications.csv ..\Data\Source\Connected_Entity.csv	>> ..\Data\Input\Acta_DSGL2_feedback_tmp.csv

cat ..\Data\Source\header.dat > ..\Data\Input\Acta_DSGL2_feedback.csv
cat ..\Data\Input\Acta_DSGL2_Feedback_TMP.csv | sort | uniq >> ..\data\input\Acta_DSGL2_Feedback.csv

erase ..\Data\Input\Acta_DSGL2_Feedback_TMP.csv


