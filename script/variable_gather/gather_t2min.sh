#!/bin/bash

FROM=/work/mh1007/MPI-GE/onepct/
TO=/work/mh0033/m300883/3rdPanel/data/influence/t2min/

for ens in {0001..0100}
do
    echo "***************************"
    echo "ens:" ${ens}
	Prex=${FROM}onepct${ens}/outdata/echam6/

	Files=${Prex}onepct${ens}_echam6_ATM_mm_1*.grb

	cdo -P  48 -f nc -yearmean -selmonth,1,2,3,4 -selyear,1851/1999 -shifttime,1mo -mergetime -apply,"-selname,var201,var202" [ ${Files} ] ${TO}onepct${ens}_echam6_echam.nc

done