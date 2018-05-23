import os
import subprocess
import sys



timestep=0.1



for k in range(0,215):
    
    if k<10: 
        path_file_xz  = '/scratch/05518/oasselin/sim1-02-05-2018/output/slicev1  '+str(k)+'.dat'
    if (k<100 and k>9):
        path_file_xz  = '/scratch/05518/oasselin/sim1-02-05-2018/output/slicev1 '+str(k)+'.dat'
    if k>=100:
        path_file_xz  = '/scratch/05518/oasselin/sim1-02-05-2018/output/slicev1'+str(k)+'.dat'


    if os.path.isfile(path_file_xz): 

        if k<10:
            output_file = 'sim1-02-05-2018_gif_slices_xz/slice00'+str(k)+'.png'
        if (k<100 and k>9):
            output_file = 'sim1-02-05-2018_gif_slices_xz/slice0'+str(k)+'.png'
        if k>=100:
            output_file = 'sim1-02-05-2018_gif_slices_xz/slice'+str(k)+'.png'
        
        time = "{0:.2f}".format(timestep*k)

        xlabel = 't='+str(time)

        tt = 'sim1-02-05-2018, WKE, xz'

        gnuplot_command = "gnuplot -e \"set output '"+output_file+"'; set title '"+tt+"'; set xlabel '"+xlabel+"'; filename = '"+path_file_xz+"'\" sim1-02-05-2018_gif_xz.gnu"

        p = subprocess.Popen(gnuplot_command, shell = True)
        os.waitpid(p.pid, 0)
