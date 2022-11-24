from __future__ import absolute_import
from getcpus import getcpus

option_list = ( ( 'machine', 'NCPU_DDF', int, getcpus(),
                  'Number of CPUS to use for DDF'),
                ( 'machine', 'NCPU_killms', int, getcpus(),
                  'Number of CPUS to use for KillMS' ),
                ( 'data', 'mslist', str, None,
                  'Initial measurement set list to use -- must be specified' ),
                ( 'data', 'full_mslist', str, None,
                  'Full-bandwidth measurement set to use for final step, if any' ),
                ( 'data', 'colname', str, 'CORRECTED_DATA', 'MS column to use' ),
                ( 'solutions', 'ndir', int, 45, 'Number of directions' ),
                ( 'solutions', 'SolsDir', str, "SOLSDIR", 'Directory for solutions' ),
                ( 'solutions', 'NChanSols', int, 1, 'NChanSols for killMS' ),
                ( 'solutions', 'dt_slow', float, 1., 'Time interval for killMS (minutes)' ),
                ( 'solutions', 'do_very_slow', bool, True, 'Enable very slow amplitude smoothing'),
                ( 'solutions', 'sigma_clip', float, 5.0, 'Sigma clip for amplitude outliers'),
                ( 'solutions', 'dt_very_slow', float, 43.63, 'Time interval for killMS (minutes)' ),
                ( 'solutions', 'dt_di', float, 0.5, 'Time interval for DI killMS (minutes)' ),
                ( 'solutions', 'dt_fast', float, 0.5, 'Time interval for full-bandwidth killMS (minutes)' ),
                ( 'solutions', 'LambdaKF', float, 0.5, 'Kalman filter lambda for killMS' ),
                ( 'solutions', 'NIterKF', list, [1, 1, 1, 1, 6, 1, 6], 'Kalman filter iterations for killMS for the 7 killMS steps' ),
                ( 'solutions', 'normalize', list, ['BLBased', 'BLBased', 'SumBLBased'], 'How to normalize solutions for the three self-cal steps' ),
                ( 'solutions', 'uvmin', float, None, 'Minimum baseline length to use in self-calibration (km)' ),
                ( 'solutions', 'uvmin_very_slow', float, 0.5, 'Minimum baseline length to use in slow smoothing of self-cal solutions (km)' ),
                ( 'solutions', 'wtuv', float, None, 'Factor to apply to fitting weights of data below uvmin. None implies, effectively, zero.'),
                ( 'solutions', 'robust', float, None, 'Briggs robustness to use in killMS. If None, natural weighting is used.'),
                ( 'solutions', 'smoothing', bool, True, 'Smooth the solutions.'),
                ( 'solutions', 'smoothingtype', str, 'TEC,PolyAmp', 'Type of smoothing to do on the solutions.'),
                ( 'solutions', 'apply_sols', list, ['P', 'AP', 'AP', 'AP', 'AP', 'AP', 'AP'], 'Solutions to apply after the 7 killMS steps' ),
                ( 'image', 'do_wide', bool, False, 'do widefield image and subtract sources in annulus' ),
                ( 'image', 'wide_imsize', int, 10000, 'Widefield image size in pixels' ),
                ( 'image', 'wide_cell', float, 10., 'Widefield pixel size in arcsec' ),
                ( 'image', 'wide_robust', float, -0.20, 'Widefield imaging robustness' ),
                ( 'image', 'wide_psf_arcsec', float, 45., 'Widefield restoring beam in arcsec' ),
                ( 'image', 'imsize', int, 20000, 'Image size in pixels' ),
                ( 'image', 'cellsize', float, 1.5, 'Pixel size in arcsec' ),
                ( 'image', 'robust', float, -0.15, 'Imaging robustness' ),
                ( 'image', 'final_robust', float, -0.5, 'Final imaging robustness' ),
                ( 'image', 'psf_arcsec', float, 12.0, 'Force restore with this PSF size in arcsec if set, otherwise use default' ),
                ( 'image', 'final_psf_arcsec', float, 6.0, 'Final image restored with this PSF size in arcsec' ),
                ( 'image', 'final_psf_minor_arcsec', float, None, 'Final image restored with this PSF minor axis in arcsec' ),
                ( 'image', 'final_psf_pa_deg', float, None, 'Final image restored with PSF with this PA in degrees' ),
                ( 'image', 'final_rmsfactor', float, 1.0, 'Final image RMS factor for cleaning' ),
                ( 'image', 'low_psf_arcsec', float, None, 'Low-resolution restoring beam in arcsec. If None, no image will be made.' ),
                ( 'image', 'low_robust', float, -0.20, 'Low-resolution image robustness' ),
                ( 'image', 'low_cell', float, 4.5, 'Low-resolution image pixel size in arcsec' ),
                ( 'image', 'low_imsize', int, None, 'Low-resolution image size in pixels' ),
                ( 'image', 'vlow_psf_arcsec', float, None, 'Very low-resolution QU restoring beam in arcsec. If None, no image will be made.' ),
                ( 'image', 'vlow_robust', float, -0.20, 'Very low-resolution QU image robustness' ),
                ( 'image', 'vlow_cell', float, 50.0, 'Very low-resolution QU image pixel size in arcsec' ),
                ( 'image', 'vlow_imsize', int, 500, 'Very low-resolution QU image size in pixels' ),
                ( 'image', 'do_decorr', bool, True, 'Use DDF\'s decorrelation mode' ),
                ( 'image', 'HMPsize', int, 10, 'Island size to use HMP initialization' ),
                ( 'image', 'uvmin', float, 0.1, 'Minimum baseline length to use in imaging (km)'),
                ( 'image', 'uvmax', float, 1000.0, 'Maximum baseline length to use in imaging (km)'),
                ( 'image', 'apply_weights', list, [False, True, True, True], 'Use IMAGING_WEIGHT column from killms'),
                ( 'image', 'use_weightspectrum', bool, False, 'Use WEIGHT_SPECTRUM column when not using IMAGING_WEIGHT column from killms'),
                ( 'image', 'clusterfile', str, None, 'User-defined cluster file to use'),
                ( 'image', 'centralfreqs', list, [128.0, 143.7, 160.2],'Central frequencies to use for channel images (MHz)'),
                ( 'image', 'use_splitisland', bool, False, 'Use the SSDClean-MaxIslandSize option in DDFacet'),
                ( 'masking', 'thresholds', list, [15,10,10,5],
                  'sigmas to use in (auto)masking for initial clean and 3 self-cals'),
                ( 'masking', 'tgss', str, None, 'Path to TGSS catalogue file' ),
                ( 'masking', 'tgss_radius', float, 8.0, 'TGSS mask radius in pixels' ), 
                ( 'masking', 'tgss_flux', float, 300, 'Use TGSS components with peak flux in catalogue units (mJy) above this value' ),
                ( 'masking', 'tgss_extended', bool, False, 'Make extended regions for non-pointlike TGSS sources' ),
                ( 'masking', 'tgss_pointlike', float, 30, 'TGSS source considered pointlike if below this size in arcsec' ),
                ( 'masking', 'region', str, None, 'ds9 region to merge with mask'),
                ( 'masking', 'external_fits_mask', str, None, 'fits mask to merge with masks produced'),
                ( 'masking', 'extended_size', int, None,
                  'If generating a mask from the bootstrap low-res images, use islands larger than this size in pixels' ),
                ( 'masking', 'extended_rms', float, 3.0,
                  'Threshold value defining an island in the extended mask'),
                ( 'masking', 'rmsfacet', bool, False, 'If True calculate one rms per facet rather than per image when making the extended rms maps' ),  
                ( 'masking','thres_outmaskextended', float, 15, 'Masking threshold for making MaskDiffuse.fits'),
                ( 'control', 'quiet', bool, False, 'If True, do not log to screen' ),
                ( 'control', 'nobar', bool, False, 'If True, do not print progress bars' ),
                ( 'control', 'logging', str, 'logs', 'Name of directory to save logs to, or \'None\' for no logging' ),
                ( 'control', 'dryrun', bool, False, 'If True, don\'t run anything, just print what would be run' ),
                ( 'control', 'restart', bool, True, 'If True, skip steps that would re-generate existing files' ),
                ( 'control', 'cache_dir', str, None, 'Directory for ddf cache files -- default is working directory'),
                ( 'control', 'clearcache', bool, True, 'If True, clear all DDF cache before running' ),
                ( 'control', 'clearcache_end', bool, True, 'If True, clear all DDF cache at successful end of the pipeline' ),
                ( 'control', 'skip_di', bool, False, 'If True, skip the DI calibration steps' ),
                ( 'control', 'bootstrap', bool, False, 'If True, do bootstrap' ),
                ( 'control', 'catch_signal', bool, True, 'If True, catch SIGUSR1 as graceful exit signal -- stops when control returns to the pipeline.'),
                ( 'control', 'exitafter', str, None, 'Step to exit after -- cleanup, dirin, dirin_di, bootstrap, phase, ampphase, fulllow'),
                ( 'control', 'redofrom', str, None, 'Step to redo from after -- start or dirin'),
                ( 'control', 'archive_dir', str, 'old', 'Directory to archive to if redofrom is set'),
                ( 'control', 'msss_mode', bool, False, 'Work in "MSSS mode" where a smooth beam and spectral cube are computed in the ampphase1 step' ),
                ( 'control', 'remove_columns', bool, False, 'Remove all pipeline-generated columns before the run' ),
                ( 'control', 'spectral_restored', bool, False, 'Make multi-frequency images ' ),
                ( 'control', 'polcubes', bool, False, 'Make polarization cubes' ),
                ( 'control', 'split_polcubes', bool, False, 'Split polarization cubes into Q and U' ),	
                ( 'control', 'stokesv', bool, False, 'Make Stokes V image' ),
                ( 'control', 'redo_DI', bool, False, 'Redo DI cal with DP3' ),
		( 'control', 'redo_DI_type',str, 'GSM', 'Sky model for redoing DI -- TGSS or GSM'),
                ( 'control', 'beam_at',str,'facet','Where to compute beam in DDF and kMS. Leave unset for default behaviour which will be "facet" for new DDF versions and "tessel" for old ones. Set to "tessel" to force old behaviour.'), 
                ( 'bootstrap', 'catalogues', list, None, 'File names of catalogues for doing bootstrap' ),
                ( 'bootstrap', 'groups', list, None, 'Group numbers for catalogues. At least one match must be found in each group. Optional -- if not present each catalogue is in a different group.' ), 
                ( 'bootstrap', 'frequencies', list, None, 'Frequencies for catalogues (Hz)' ), 
                ( 'bootstrap', 'names', list, None, 'Short names for catalogues' ), 
                ( 'bootstrap', 'radii', list, None, 'Crossmatch radii for catalogues (arcsec)' ),
                ( 'compression', 'compress_polcubes', bool, False, 'Compress polarization cubes'),
                ( 'compression', 'fpack_q', int, 4, 'fpack compression factor to use'),
                ( 'compression', 'delete_compressed', bool, False, 'Delete original cube files after compression'),
                ( 'compression', 'compress_ms', bool, False, 'Compress measurement sets with dysco'),
                ( 'offsets', 'method', str, None, 'Offset correction method to use. None -- no correction'),
                ( 'offsets', 'fit', str, 'mcmc', 'Histogram fit method' ),
                ( 'offsets', 'mode', str, 'normal', 'Mode of operation: normal or test' ),
                ( 'spectra', 'do_dynspec', bool, False, 'Do dynamic spectra'),
                ( 'spectra', 'bright_threshold', float, 1.0, 'Threshold for auto-selection of bright sources'),
                ( 'inputmodel',  'basedicomodel',str,None,'Input dicomodel for calibration'),
                ( 'inputmodel',  'basemaskname',str,None,'Input mask for calibration'),
                ( 'inputmodel',  'baseimagename',str,None,'Input image for calibration'))
