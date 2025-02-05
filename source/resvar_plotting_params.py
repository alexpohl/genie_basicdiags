# gives for each possible variable of the '.res' output, plotting options
# this script is shared among different plotting tools

# below, the only place where the list is really up-to-date

# LIST OF VARIABLES
# -3  ::  methanogenesis (mol yr-1)
# -2  ::  RCH4ox_kgCH4_yr_k0 (Tg CH4 / yr)
# -1  ::  special case, shelf area (above 1000 m)
#  1  ::  global mean O2 (mol kg-1)
#  2  ::  benthic O2 ($\mu$mol kg-1)
#  3  ::  global POC flux (mol yr-1)
#  4  ::  mean global ventilation age (yr)
#  5  ::  benthic ventilation age (yr)
#  6  ::  surface air temperature (degrees C)
#  7  ::  NC -- mean --  eco2D_Size_Mean -- Geometric Mean of Cell Diameter
#  8  ::  NC -- mean -- eco2D_Size_Frac_Micro_Chl -- Micro chlorophyll biomass
#  9  ::  NC -- mean -- eco2D_Size_Frac_Nano_Chl -- Nano chlorophyll biomass
# 10  ::  NC -- mean -- eco2D_Size_Frac_Pico_Chl -- Pico chlorophyll biomass
# 11  ::  global min overturning (Sv)
# 12  ::  global max overturning (Sv)
# 13  ::  global sea-ice area (Mm2)
# 14  ::  global sea-ice volume (Mm3)
# 15  ::  mean sea-ice thickness (m)
# 16  ::  pCO2 (ppm)
# 17  ::  salinity (o/oo)
# 18  ::  global mean PO4 (umol kg-1) (umol kg-1)
# 19  ::  pO2 (ppm)
# 20  ::  total PO4 (x1E12 mol)
# 35  ::  global ocean area (Mkm2)
# 36  ::  surface ocean temperature (degC)
# 37  ::  benthic ocean temperature (degC)
# 38  ::  global total DIC_13C (mol)
# 39  ::  global DIC_13C o/oo)
# 40  ::  surface DIC_13C (o/oo)
# 41  ::  benthic DIC_13C (o/oo)
# 42  ::  global ocean temperature (degC)
# 54  ::  global ocean volume (m3)
# 55  ::  NC -- mean -- benthic O2 ($\mu$mol kg-1)
# 56  ::  NC -- mean -- shallow benthic O2 ($\mu$mol kg-1), shallow only
# 57  ::  NC -- median -- benthic O2 ($\mu$mol kg-1)
# 58  ::  NC -- median -- shallow benthic O2 ($\mu$mol kg-1), shallow only
# 59  ::  NC -- median -- ocean O2 ($\mu$mol kg-1) at given level
# 60  ::  NC -- median -- deep benthic O2 ($\mu$mol kg-1), deep only
# 61  ::  NC -- mean -- ocean O2 ($\mu$mol kg-1) at given level
# 62  ::  NC -- mean -- ocean H2S ($\mu$mol kg-1) at given level
# 63  ::  NC -- mean -- benthic water age (yr), deep only
# 64  ::  NC -- mean -- benthic O2 ($\mu$mol kg-1), deep only
# 65  ::  NC -- mean -- benthic ocean temperature, deep only
# 66  ::  NC -- mean -- mean low-lat (-10 - 10 deg) SST
# 67  ::  NC -- mean -- mean low-lat (-10 - 10 deg) benthic ocean temperature, deep only
# 68  ::  NC -- mean -- mean South Pole sea-ice fraction
# 69  ::  NC -- mean -- mean high-lat sea-ice fraction
# 70  ::  global total ALK (mol)
# 71  ::  global total DIC 'mol)
# 72  ::  atlantic min overturning (Sv)
# 73  ::  atlantic max overturning (Sv)
# 74  ::  pCH4 (ppm)
# 75  ::  NC -- mean -- mean mid-lat (-40 - 40 deg) SST
# 76  ::  NC -- mean -- mean low-lat (-30 - 30 deg) SST
# 77  ::  NC -- mean -- mean low-lat (-15 - 15 deg) SST
# 78  :: global total SO4 (mol)
# 79  :: global mean SO4 (mol kg-1)
# 80  ::  NC -- mean -- shallow benthic SO4 ($\mu$mol kg-1), shallow only
# 81  ::  NC -- mean -- deep benthic SO4 ($\mu$mol kg-1), deep only
# 82  ::  global total DOM_C (mol)
# 83  ::  global mean SO4 ($\mu$mol kg-1)
# 84  ::  global mean H2S ($\mu$mol kg-1)
# 85  ::  global ocnsed POC flux (Tg yr-1)
# 1001 :: weather_fCaCO3 (Tmol yr-1)
# 1002 :: weather_fCaSiO3 (Tmol yr-1)
# 1003 :: global sedocn PO4 flux (mol yr-1)
# 1004 :: mean CaCO3 composition (wt%)
# 1005 :: mean POP composition (wt%)
# 1006 :: global ocnsed POP flux (mol yr-1)
# 1007 :: global weather PO4 flux (mol yr-1)
# 1008 :: estimated global POC burial flux (mol yr-1)
# 1009 :: mean POC composition (wt%)
# 1010 :: global weather ALK flux (mol yr-1)
# 1011 :: global weather H2S flux (mol yr-1)
# 1012 :: global weather SO4 flux (mol yr-1)


ncvartype = 'std'
ncaggregate = 'mean'
nclatbound = [-90, 90]
shallow_only = 'n'
deep_only = 'n'
put_NaNs_to_zero = False

if varID == -3:
    txtfile = 'biogem_series_diag_reminP_POC_dCH4.res'
    varname = 'Methanogenesis (x10${12}$ mol yr$^{-1}$)'
    factor = 1.E-12
    varname2save = 'methanogenesis_molyr'
    geniesubdir = 'biogem'
elif varID == -2:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'diag_redox_CH4toDIC_dDIC'
    varname = 'Oxidation rate (Tg CH$_4$ yr$^{-1}$)'
    varname2save = 'CH4_surface_oxidation_rate'
    geniesubdir = 'biogem'
elif varID == -1: # -1  ::  special case, shelf area (above 1000 m)
    txtfile = 'fields_biogem_2d.nc'
    ncvar = 'grid_area'
    varname = 'shelf area ($x$10$^6$ km$^{2}$)'
    varname2save = 'shelf_area_Mkm2'
    geniesubdir = 'biogem'
    shallow_only = 'y'
    factor = 1.E-12 # from m2 to Mkm2
    ncaggregate = 'sum'
    put_NaNs_to_zero = True
elif varID == 1:
    txtfile = 'biogem_series_ocn_O2.res'
    col = 2
    factor = 1E6
    varname = 'global mean O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'global_mean_O2_mmol_kg' # for pdf
elif varID == 2:
    txtfile = 'biogem_series_ocn_O2.res'
    col = 4
    factor = 1E6
    varname = 'benthic O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'benthic_O2_mmol_kg' # for pdf
elif varID == 3:
    txtfile = 'biogem_series_fexport_POC.res'
    col = 1
    varname = 'global POC flux ($x$10$^{15}$molC yr$^{-1}$)' # (10E15 mol yr$^{-1}$)'
    factor = 1./1E15
    varname2save = 'global_POC_flux_mol_yr'
elif varID == 4:
    txtfile = 'biogem_series_misc_col_age.res'
    col = 1
    varname = 'mean global ventilation age (yr)'
    varname2save = 'mean_global_ventilation_age_yr'
elif varID == 5:
    txtfile = 'biogem_series_misc_col_age.res'
    col = 3
    varname = 'benthic [> 2000 m] ventilation age (yr)'
    varname2save = 'benthic_ventilation_age_yr'
elif varID == 6:
    txtfile = 'biogem_series_atm_temp.res'
    col = 1
    varname = 'surface air temperature ($^\circ$C)'
    varname2save = 'surface_air_temperature'
elif varID == 7:
    txtfile = 'fields_ecogem_2d.nc'
    ncvar = 'eco2D_Size_Mean'
    varname = 'Geometric Mean of Cell Diameter'
    varname2save = 'Geometric_Mean_of_Cell_Diameter'
    geniesubdir = 'ecogem'
elif varID == 8:
    txtfile = 'fields_ecogem_2d.nc'
    ncvar = 'eco2D_Size_Frac_Micro_Chl'
    varname = 'Micro chlorophyll biomass'
    varname2save = 'Micro_chlorophyll_biomass'
    geniesubdir = 'ecogem'
elif varID == 9:
    txtfile = 'fields_ecogem_2d.nc'
    ncvar = 'eco2D_Size_Frac_Nano_Chl'
    varname = 'Nano chlorophyll biomass'
    varname2save = 'Nano_chlorophyll_biomass'
    geniesubdir = 'ecogem'
elif varID == 10:
    txtfile = 'fields_ecogem_2d.nc'
    ncvar = 'eco2D_Size_Frac_Pico_Chl'
    varname = 'Pico chlorophyll biomass'
    varname2save = 'Pico_chlorophyll_biomass'
    geniesubdir = 'ecogem'
elif varID == 11:
    txtfile = 'biogem_series_misc_opsi.res'
    col = 1
    varname = 'global min overturning (Sv)'
    varname2save = 'global_min_overturning_sv'
    fix_ncols = 7 # file header has a problem prohiting the correct reading of the number of columns
elif varID == 12:
    txtfile = 'biogem_series_misc_opsi.res'
    col = 2
    varname = 'global max overturning (Sv)'
    varname2save = 'global_max_overturning_sv'
    fix_ncols = 7 # file header has a problem prohiting the correct reading of the number of columns
elif varID == 13:
    txtfile = 'biogem_series_misc_seaice.res'
    col = 1
    factor = 1E-12
    varname = 'global sea-ice area (Mkm2)'
    varname2save = 'global_seaice_area_Mkm2'
elif varID == 14:
    txtfile = 'biogem_series_misc_seaice.res'
    col = 3
    factor = 1E-6
    varname = 'global sea-ice volume (Mm3)'
    varname2save = 'globalseaice_volume_Mm3'
elif varID == 15:
    txtfile = 'biogem_series_misc_seaice.res'
    col = 4
    varname = 'mean sea-ice thickness (m)'
    varname2save = 'mean_seaice_thickness_m'
elif varID == 16:
    txtfile = 'biogem_series_atm_pCO2.res'
    col = 2
    factor = 1E6
    varname = 'pCO2 (ppm)'
    varname2save = 'pCO2_ppm'
elif varID == 17:
    txtfile = 'biogem_series_ocn_sal.res'
    col = 1
    varname = 'salinity (o/oo)'
    varname2save = 'global_salinity'
elif varID == 18:
    txtfile = 'biogem_series_ocn_PO4.res'
    col = 2
    factor = 1E6
    varname = 'global mean PO4 ($\mu$mol kg-1)'
    varname2save = 'global_mean_PO4_umolkg'
elif varID == 19:
    txtfile = 'biogem_series_atm_pO2.res'
    col = 2
    varname = 'pO2 (atm)'
    varname2save = 'pO2_atm'
elif varID == 20:
    txtfile = 'biogem_series_ocn_PO4.res'
    col = 1
    varname = 'total PO$_4$ ($x$10$^{12}$ mol)'
    varname2save = 'PO4_Mmol'
elif varID == 35:
    agestr = str(int(time2plot_def-0.5))
    txtfile = 'biogem_year_' + (5-len(agestr))*'0' + agestr+ '_500_diag_GLOBAL_AVERAGE.res'
    line2read = 11
    charmin = 54
    charmax = 67
    factor = 1E-12
    varname = 'global ocean area (Mkm$^2$)'
    varname2save = 'global_ocean_area_Mkm2'
elif varID == 36:
    txtfile = 'biogem_series_ocn_temp.res'
    col = 4
    varname = 'surface ocean temperature ($^\circ$C)'
    varname2save = 'surT'
elif varID == 37:
    txtfile = 'biogem_series_ocn_temp.res'
    col = 3
    varname = 'benthic ocean temperature ($^\circ$C)'
    varname2save = 'benT'
elif varID == 38:
    txtfile = 'biogem_series_ocn_DIC_13C.res'
    col = 1
    varname = 'global total DIC 13C (mol)'
    varname2save = 'global_total_DIC_13C_mol'
elif varID == 39:
    txtfile = 'biogem_series_ocn_DIC_13C.res'
    col = 2
    varname = 'global DIC 13C ($_o$/$^{oo}$)'
    varname2save = 'global_DIC_13C_permil'
elif varID == 40:
    txtfile = 'biogem_series_ocn_DIC_13C.res'
    col = 5
    varname = 'surface DIC 13C ($_o$/$^{oo}$)'
    varname2save = 'surface_DIC_13C_permil'
elif varID == 41:
    txtfile = 'biogem_series_ocn_DIC_13C.res'
    col = 4
    varname = 'benthic DIC 13C ($_o$/$^{oo}$)'
    varname2save = 'benthic_DIC_13C_permil'
elif varID == 42:
    txtfile = 'biogem_series_ocn_temp.res'
    col = 1
    varname = 'global temperature ($^\circ$C)'
    varname2save = 'global_temp'
elif varID == 54:
    agestr = str(int(time2plot_def-0.5))
    txtfile = 'biogem_year_' + (5-len(agestr))*'0' + agestr+ '_500_diag_GLOBAL_AVERAGE.res'
    line2read = 13
    charmin = 54
    charmax = 67
    factor = 1.
    varname = 'global ocean volume (m$^3$)'
    varname2save = 'global_ocean_volume_m3'
elif varID == 55:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'benthic O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'benthic_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    ncaggregate = 'mean'
elif varID == 56:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'shallow benthic O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'shallow_benthic_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    shallow_only = 'y'
elif varID == 57:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'benthic O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'median_benthic_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    ncaggregate = 'median'
elif varID == 58:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'shallow benthic O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'median_shallow_benthic_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    shallow_only = 'y'
    ncaggregate = 'median'
elif varID == 59:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'median_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'level'
    factor = 1E6
    ncaggregate = 'median'
elif varID == 60:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'deep benthic O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'median_deep_benthic_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    ncaggregate = 'median'
    deep_only = 'y'
elif varID == 61:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'O$_2$ ($\mu$mol kg$^{-1}$)        '
    varname2save = 'mean_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'level'
    factor = 1E6
    ncaggregate = 'mean'
elif varID == 62:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_H2S'
    varname = 'H$_2$S ($\mu$mol kg$^{-1}$)        '
    varname2save = 'mean_H2S_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'level'
    factor = 1E6
    ncaggregate = 'mean'
elif varID == 63:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'misc_col_Dage'
    varname = 'mean deep benthic water age (yr)        '
    varname2save = 'mean_deep_misc_col_age_kyrs'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    ncaggregate = 'mean'
    deep_only = 'y'
elif varID == 64:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_O2'
    varname = 'mean deep benthic O$_2$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'mean_deep_benthic_O2_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    ncaggregate = 'mean'
    deep_only = 'y'
elif varID == 65:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_temp'
    varname = 'mean deep benthic temperature ($^\circ$C)'
    varname2save = 'mean_deep_benthic_temperature'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    ncaggregate = 'mean'
    deep_only = 'y'
elif varID == 66:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_temp'
    varname = 'SST ($^\circ$C)        '
    nclatbound = [-10, 10]
    varname2save = 'mean_SST_lowlat10' 
    geniesubdir = 'biogem'
    ncvartype = 'level'
    ncaggregate = 'mean'
elif varID == 67:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_temp'
    varname = 'mean low-lat deep benthic temperature ($^\circ$C)'
    varname2save = 'mean_deep_benthic_temperature_lowlat10'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    nclatbound = [-10, 10]
    ncaggregate = 'mean'
    deep_only = 'y'
elif varID == 68:
    txtfile = 'fields_biogem_2d.nc'
    ncvar = 'phys_seaice'
    varname = 'sea-ice cover South Pole'
    varname2save = 'phys_seaice_SPole'
    geniesubdir = 'biogem'
    nclatbound = [-90, -75]
    ncaggregate = 'mean'
elif varID == 68:
    txtfile = 'fields_biogem_2d.nc'
    ncvar = 'phys_seaice'
    varname = 'sea-ice cover high-lat South'
    varname2save = 'phys_seaice_S_highlat'
    geniesubdir = 'biogem'
    nclatbound = [-65, -75]
    ncaggregate = 'mean'
elif varID == 69:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_temp'
    varname = 'SST ($^\circ$C)        '
    nclatbound = [-2., 2.]
    varname2save = 'mean_SST_lowlat2'
    geniesubdir = 'biogem'
    ncvartype = 'level'
    ncaggregate = 'mean'
elif varID == 70:
    txtfile = 'biogem_series_ocn_ALK.res'
    col = 1
    varname = 'global total ALK (mol)'
    varname2save = 'global_total_ALK_mol'
elif varID == 71:
    txtfile = 'biogem_series_ocn_DIC.res'
    col = 1
    varname = 'global total DIC (mol)'
    varname2save = 'global_total_DIC_mol'
elif varID == 72:
    txtfile = 'biogem_series_misc_opsi.res'
    col = 3
    varname = 'atlantic min overturning (Sv)'
    varname2save = 'atlantic_min_overturning_sv'
elif varID == 73:
    txtfile = 'biogem_series_misc_opsi.res'
    col = 4
    varname = 'atlantic max overturning (Sv)'
    varname2save = 'atlantic_max_overturning_sv'
elif varID == 74:
    txtfile = 'biogem_series_atm_pCH4.res'
    col = 2
    factor = 1E9
    varname = 'pCH$_4$ (ppb)'
    varname2save = 'pCH4_ppb'
elif varID == 75:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_temp'
    varname = 'SST ($^\circ$C)        '
    nclatbound = [-40, 40]
    varname2save = 'mean_SST_lowlat40'
    geniesubdir = 'biogem'
    ncvartype = 'level'
    ncaggregate = 'mean'
elif varID == 76:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_temp'
    varname = 'SST ($^\circ$C)        '
    nclatbound = [-30, 30]
    varname2save = 'mean_SST_lowlat30'
    geniesubdir = 'biogem'
    ncvartype = 'level'
    ncaggregate = 'mean'
elif varID == 77:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_temp'
    varname = 'SST ($^\circ$C)        '
    nclatbound = [-15., 15.]
    varname2save = 'mean_SST_lowlat15'
    geniesubdir = 'biogem'
    ncvartype = 'level'
    ncaggregate = 'mean'
elif varID == 78:
    txtfile = 'biogem_series_ocn_SO4.res'
    col = 1
    varname = 'global total SO$_4$ (mol)'
    varname2save = 'global_total_SO4_mol'
elif varID == 79:
    txtfile = 'biogem_series_ocn_SO4.res'
    col = 2
    varname = 'global mean SO$_4$ (mol kg$^{-1}$)'
    varname2save = 'global_mean_SO4_molkg'
elif varID == 80:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_SO4'
    varname = 'shallow benthic SO$_4$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'shallow_benthic_SO4_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    shallow_only = 'y'
elif varID == 81:
    txtfile = 'fields_biogem_3d.nc'
    ncvar = 'ocn_SO4'
    varname = 'deep benthic SO$_4$ ($\mu$mol kg$^{-1}$)'
    varname2save = 'deep_benthic_SO4_umolkg'
    geniesubdir = 'biogem'
    ncvartype = 'deep'
    factor = 1E6
    ncaggregate = 'mean'
    deep_only = 'y'
elif varID == 82:
    txtfile = 'biogem_series_ocn_DOM_C.res'
    col = 1
    varname = 'global total DOM_C (mol)'
    varname2save = 'global_total_DOM_C_mol'
elif varID == 83:
    txtfile = 'biogem_series_ocn_SO4.res'
    col = 2
    factor = 1E6
    varname = 'global mean SO$_4$ ($\mu$mol kg-1)'
    varname2save = 'global_mean_SO4_umolkg'
elif varID == 84:
    txtfile = 'biogem_series_ocn_H2S.res'
    col = 2
    factor = 1E6
    varname = 'global mean H$_2$S ($\mu$mol kg-1)'
    varname2save = 'global_mean_H2S_umolkg'
elif varID == 85:
    txtfile = 'biogem_series_focnsed_POC.res'
    col = 1
    factor = 12.
    varname = 'global POC flux (Tg yr-1)'
    varname2save = 'global_mean_H2S_umolkg'
elif varID == 1001:
    txtfile = 'rokgem_series_weather_fCaCO3.res'
    col = 1
    varname = 'weather_fCaCO3 (Tmol yr-1)'
    varname2save = 'weather_fCaCO3_Tmol_yr'
    geniesubdir = 'rokgem'
elif varID == 1002:
    txtfile = 'rokgem_series_weather_fCaSiO3.res'
    col = 1
    varname = 'weather_fCaSiO3 (Tmol yr-1)'
    varname2save = 'weather_fCaSiO3_Tmol_yr'
    geniesubdir = 'rokgem'
elif varID == 1003:
    txtfile = 'biogem_series_fsedocn_PO4.res'
    col = 1
    varname = 'global sedocn PO4 flux (mol yr-1)'
    varname2save = 'global_sedocn_PO4_flux_mol_yr'
elif varID == 1004:
    txtfile = 'biogem_series_sed_CaCO3.res'
    col = 1
    varname = 'mean CaCO3 composition (wt%)'
    varname2save = 'CaCO3_mean_composition_wtpercent'
elif varID == 1005:
    txtfile = 'biogem_series_sed_POP.res'
    col = 1
    varname = 'mean POP composition (wt%)'
    varname2save = 'mean_POP_composition_wtpercent'
elif varID == 1006:
    txtfile = 'biogem_series_focnsed_POP.res'
    col = 1
    varname = 'global ocnsed POP flux (mol yr-1)'
    varname2save = 'global_ocnsed_POP_flux_mol_yr'
elif varID == 1007:
    txtfile = 'biogem_series_diag_weather_PO4.res'
    col = 1
    varname = 'global weather PO4 flux (mol yr-1)'
    varname2save = 'global_weather_PO4_mol_yr'
elif varID == 1008:
    txtfile = 'biogem_series_misc_fsed_POC.res'
    col = 1
    varname = 'estimated global POC burial flux (mol yr-1)'
    varname2save = 'estimated_global_POC_burial_flux_mol_yr'
elif varID == 1009:
    txtfile = 'biogem_series_sed_POC.res'
    col = 1
    varname = 'mean POC composition (wt%)'
    varname2save = 'mean_POC_composition_wtpercent'
elif varID == 1010:
    txtfile = 'biogem_series_diag_weather_ALK.res'
    col = 1
    varname = 'global weather ALK flux (mol yr-1)'
    varname2save = 'global_weather_ALK_mol_yr'
elif varID == 1011:
    txtfile = 'biogem_series_fsedocn_H2S.res'
    col = 1
    varname = 'global weather H$_2$S flux (mol yr$^{-1}$)'
    varname2save = 'global_weather_H2S_mol_yr'
elif varID == 1012:
    txtfile = 'biogem_series_fsedocn_SO4.res'
    col = 1
    varname = 'global weather SO$_4$ flux (mol yr$^{-1}$)'
    varname2save = 'global_weather_SO4_mol_yr'
else:
    print('ERROR: unknown variable ID')
    print('ERROR: exiting now')
    sys.exit()

