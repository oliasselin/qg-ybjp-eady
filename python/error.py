#!/usr/bin/env python                                                                                                                                                               
import os
import numpy as np

scratch_location = '/oasis/scratch/comet/oasselin/temp_project/'
folder = 'steady_wave/'
run = 'm5_U0.25'


tmax = 500
error = np.zeros((tmax,2))
timestep = 0.1

for ts in range(tmax):

    spaces_ts = (3-len(str(ts)))*' '
    path_bo = scratch_location+folder+'BO/'+run+'/output/slicehtop1'+spaces_ts+str(ts)+'.dat'
    path_ybj = scratch_location+folder+'YBJ/'+run+'/output/slicehtop1'+spaces_ts+str(ts)+'.dat'
 
    if os.path.isfile(path_bo) and os.path.isfile(path_ybj):
        print 'Calculating error for the slice no ',ts
        wke_bo = np.loadtxt(path_bo) 
        wke_ybj= np.loadtxt(path_ybj) 

        error[ts,1]  = np.mean(np.square(wke_ybj-wke_bo)) / np.mean(np.square(wke_bo))    #Same as (3.22) in TBS but with A -> wke
        error[ts,0]  = ts*timestep

    else:
        error = error[:ts-1,:]
        break


np.savetxt('data/error_'+run+'.dat',error)