import eigendisp

dbase=eigendisp.eigendispASDF('/lustre/janus_scratch/life9360/cps_working_dir/eigendisp_ringbasin.h5')
dbase.sw4Vprofile('/lustre/janus_scratch/life9360/cps_working_dir/cpsin.txt')
dbase.getdisp(workingdir='/lustre/janus_scratch/life9360/cps_working_dir')