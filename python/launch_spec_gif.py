from compute_spec_A import specA
from compute_spec_A import make_png
from compute_spec_A import make_gif


run='storm/test5'
recompute=False
timestep=0.001
tt_max=550

specA(run,recompute=recompute,tt_max=tt_max)
make_png(run,timestep=timestep,recompute=recompute,tt_max=tt_max)
make_gif(run)
