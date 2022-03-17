#!/usr/bin/python
"""
Driver for generic plotting functions following the ARNA campaign
"""
import arna as ar


def main():
    """
    Main driver function
    """
#    from arna import get_FAAM_core4flightnum, get_filters_data4flight, get_GEOSCF4flightnum, add_derived_FAAM_flags2df4flight, get_GEOSChem4flightnum, plt_flightpath_spatially_over_CVAO, get_CIMS_data4flight

    # Seaborn context for plots?
#    context = 'talk'
    context = 'paper'

    # - Plot up all comparisons by altitude together
#     ar.plt_comp_by_alt_4ARNA_together(context=context,
#                                       res='0.25x0.3125',
#                                       just_SLR=True,)
#     ar.plt_comp_by_alt_4ARNA_together(context=context,
#                                       res='0.25x0.3125',
#                                       just_SLR=False)
#     ar.plt_comp_by_alt_4ARNA_together(context=context,
#                                       res='4x5', RunSet=None,
#                                       just_SLR=False,)
    # temp for testing
#    flight_nums = []
#    RunSet = None
#    res = '4x5'
#    NOxAsLog = True
#    CoreRunsOnly = False
#    CoreRunsOnly = True
#    savetitle = 'ARNA_altitude_binned_combined_file_{}'.format(res)
#     ar.plt_comp_by_alt_4ARNA_together(context=context,
#                                       res=res, RunSet=RunSet,
#                                       flight_nums=flight_nums,
#                                       savetitle=savetitle,
#                                       just_SLR=False,
#                                       NOxAsLog=NOxAsLog,
#                                       CoreRunsOnly=CoreRunsOnly,
#                                       debug=True)
    # Output the same bulk plots for the ACID runs
    flight_nums = []
    RunSet = 'ACID'
    res = '4x5'
    NOxAsLog = True
    CoreRunsOnly = True
    savetitle = 'ARNA_altitude_binned_combined_file_{}_{}'
    savetitle = savetitle.format(res, RunSet)
    ar.plt_comp_by_alt_4ARNA_together(context=context,
                                      res=res, RunSet=RunSet,
                                      flight_nums=flight_nums,
                                      savetitle=savetitle,
                                      just_SLR=False,
                                      NOxAsLog=NOxAsLog,
                                      CoreRunsOnly=CoreRunsOnly,
                                      debug=True)

    # The same plots as above, but split by their own PDF file..
    # NOTE: below function fails with a ValueError
#     ar.plt_comp_by_alt_4ARNA_all(just_SLR=True, context=context,
#                                  RunSet='FP-Nest', inc_GEOSChem=True,
#                                  just_plot_GEOS_Chem=True,
#                                  res='0.25x0.3125', close_pdf=True)

    # Plot up data for SLRs with and without dust
#    ar.plt_comp_by_alt_4ARNA_all(just_SLR=False, context=context)
#    ar.plt_comp_by_alt_4ARNA_all(just_SLR=True, context=context)
#     ar.plt_comp_by_alt_4ARNA_all(just_SLR=False, context=context,
#                                  RunSet='FP-Nest', inc_GEOSChem=True,
#                                  just_plot_GEOS_Chem=True,
#                                  res='0.25x0.3125', close_pdf=True)
#
#     ar.plt_comp_by_alt_4ARNA_flights_CIMS(context=context,
#                                           RunSet='FP-Nest',
#                                           res='0.25x0.3125',
#                                           inc_GEOSChem=True,
#                                           just_SLR=True)
#
#     ar.plt_comp_by_alt_4ARNA_all_DUST(plt_model=False, context=context)
#     ar.plt_comp_by_alt_4ARNA_all_DUST(plt_model=True, context=context)
#     ar.plt_comp_by_alt_4ARNA_CIMS_all_DUST(context=context)

    # - Plot up core comparisons by flight as
    # As timeseries ...
#     ar.plt_ts_comp4ARNA_flights(inc_GEOSChem=False, context=context)
#     ar.plt_ts_comp4ARNA_flights(inc_GEOSChem=True, context=context,
#                                 just_plot_GEOS_Chem=True,
#                                 RunSet='FP-Nest', res='0.25x0.3125')
    # By altitude (and by flight)
#     ar.plt_comp_by_alt_4ARNA_flights(context=context)
#     ar.plt_comp_by_alt_4ARNA_flights(inc_GEOSChem=True, context=context,
#                                      just_plot_GEOS_Chem=True,
#                                      RunSet='FP-Nest', res='0.25x0.3125')

    # - Plot up ToF-CIMS data by flight as
    # As timeseries ...
#     ar.plt_ts_comp4ARNA_flights_CIMS(context=context)
#     ar.plt_ts_comp4ARNA_flights_CIMS(context=context,
#                                      RunSet='FP-Nest',
#                                      res='0.25x0.3125',
#                                      inc_GEOSChem=True,
#                                      flight_nums=flight_nums,
#                                      LatVar='LAT',
#                                      LonVar='LON',)
    # By altitude (and by flight)
#     ar.plt_comp_by_alt_4ARNA_flights_CIMS(context=context)
#     ar.plt_comp_by_alt_4ARNA_flights_CIMS(context=context,
#                                           RunSet='FP-Nest',
#                                           res='0.25x0.3125',
#                                           inc_GEOSChem=True,
#                                           )

    # - Plot up nitrate aerosol data by flight as
    # As timeseries ...
#     ar.plt_ts_comp4ARNA_flights_filters(context=context)
#     ar.plt_ts_comp4ARNA_flights_filters(context=context,
#                                         RunSet='FP-Nest',
#                                         res='0.25x0.3125',
#                                         inc_GEOSChem=True,
#                                         LatVar='LAT',
#                                         LonVar='LON',)
#     ar.plt_ts_comp4ARNA_flights_filters(context=context,
#                                         res='4x5',
#                                         inc_GEOSChem=True,
#                                         LatVar='LAT',
#                                         LonVar='LON',
#                                         )

    # Plot up nitrate, JNIT, and their project
#    AC.mk_tri_NO3_JNIT_combination_plt()

    # - Plot up SWAS data by flight
    # Plot up SWAS data
#     ar.plt_ts_comp4ARNA_flights_SWAS(context=context)

    # - Plot up PCASP/CDP data by flight as
    # NOTE: CAS data being ignored currently due to issue with mirror window
    # As timeseries ...
#    ar.plt_ts_comp4ARNA_flights_PCASP()

    # - Plot up velocity and Roll, amongst other core physical vars by flight
    # As timeseries ...
#     ar.plt_ts_comp4ARNA_flights_PHYSICAL_VARS(context=context)
    ar.plt_ts_comp4ARNA_flights_PHYSICAL_VARS(context=context,
                                              just_plot_GEOS_Chem=True,
                                              inc_GEOSChem=True,
                                              res='0..25x0.3125',
                                              RunSet='FP-Nest')
    # Plot up the temperature data from Hannah Price
    # N/A? this is only for 2019. Data to be worked up for 2020.

    # - Plot up SWAS data by flight
    # Plot a comparison of NOy
#     ar.plt_ts_comp4ARNA_flights_NOy_ALL(context=context)
#     ar.plt_ts_comp4ARNA_flights_NOy_ALL(context=context,
#                                         RunSet='FP-Nest',
#                                         res='0.25x0.3125',
#                                         inc_GEOSChem=True,
#                                         LatVar='LAT',
#                                         LonVar='LON',)

    # - Other misc. plotting tasks
#    explore_high_ozone_near_CVAO()
#    extract_GEOS54all_ARNA_flights()

    # Evaluate the high resolution modelling region
#     ar.evaluate_regional_grid4GEOSChem()

    # Also plot up for related biomass-burning flights in MOYA campaign
#     ar.plt_ts_comp4MOYA_flights()
#     ar.plt_ts_comp4MOYA_flights_PHYSICAL_VARS()

    # Plot seasonal and vertical comparisons of nitrate (CVAO)
    plt_seasonal_comparoisons_of_nitrate()
    mk_vertical_comparisons_with_nirate()


def explore_high_ozone_near_CVAO():
    """
    High ozone seen in some locations just in nested GEOS output
    """
    import seaborn as sns
    import gc
    # - plot up locations of high ozone by flight.
    # Use the high res model
    RunSet = 'FP-Nest'
    res = '0.25x0.3125'
    # Which flights to plot? - Just use non-transit ARNA flights
    flights_nums = [218, 219, 220, 221, 222, 223, 224, 225, ]
    flight_IDs = ['C{}'.format(i) for i in flights_nums]
    # Get model data
    dfs_mod_GC = {}
    for flight_ID in flight_IDs:
        dfs_mod_GC[flight_ID] = ar.get_GEOSChem4flightnum(flight_ID=flight_ID,
                                                          res=res,
                                                          RunSet=RunSet,)
    # Observations
    dfs_obs = {}
    for flight_ID in flight_IDs:
        dfs_obs[flight_ID] = ar.get_FAAM_core4flightnum(flight_ID=flight_ID)

    # Now plot high ozone locations by flight
    # Setup PDF to save PDF plots to
    savetitle = 'ARNA_flighttrack_high_ozone'
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)
    for flight_ID in flight_IDs:
        #    for flight_ID in flight_IDs[-1:]:
        # Get dataframes for flight
        df_obs = dfs_obs[flight_ID]
        df_mod = dfs_mod_GC[flight_ID]
        # subselect locations where ozone > 70 ppbv
        df2plot = df_mod['FP-Nest']
        LatVar = 'LAT'
        LonVar = 'LON'
        cut_off = 70
        df2plot = df2plot.loc[df2plot['O3'] > cut_off*1E-09, :]
        title_str = 'Locations with modelled ozone >{} ppbv during {}'
        if (df2plot.shape[0] != 0):
            prt_str = 'Plotting {} for values >{} ppbv'
            print(prt_str.format(flight_ID, cut_off))

            title = title_str.format(cut_off, flight_ID)
            ar.plt_flightpath_spatially_over_CVAO(df=df2plot,
                                                  flight_ID=flight_ID,
                                                  title=title,
                                                  LatVar=LatVar, LonVar=LonVar)

            # Save to PDF
            AC.plot2pdfmulti(pdff, savetitle, dpi=dpi, tight=True)
            plt.close()
        else:
            prt_str = 'WARNING: Not plotting for {} as no O3 ppbv values >{}'
            print(prt_str.format(flight_ID, cut_off))
    # - Save entire pdf
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')

    # - Check the average modelled ozone vertical profile at Cape verde

    #
    RunSet = 'FP-Nest'
    res = '0.25x0.3125'
    RunDict = ar.get_dict_of_GEOSChem_model_output(res=res, RunSet=RunSet)
    Folder = '{}/OutputDir/'.format(RunDict[RunSet])

    #
    ds = AC.get_GEOSChem_files_as_ds(wd=Folder)
#    StateMet = AC.get_StateMet_ds(wd=Folder)
    ModelAlt = AC.gchemgrid('c_km_geos5')
    prefix = 'SpeciesConc_'
    specs2plot = [i for i in ds.data_vars if prefix in i]
    specs2plot = [i.split(prefix)[-1] for i in specs2plot][::-1]
#    specs2plot = ['O3', 'CO', 'NO2'][::-1]

    # Setup PDF to save PDF plots to
    import seaborn as sns
    sns.set(color_codes=True)
    sns.color_palette('colorblind')
    sns.set_context(context)
    savetitle = 'ARNA_vertical_above_CVAO_GEOSChem_campaign_01'
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)
    save2png = False
    show_plot = False
    font_scale = 1

    from funcs4obs import gaw_2_loc
    for spec in specs2plot[:100]:
        #    for spec in specs2plot[-100:]:
        #    for spec in specs2plot[-100:-90]:
        site = 'CVO'
        lat, lon, alt, TZ = gaw_2_loc(site)
        ds_tmp = ds[prefix+spec].sel(lat=lat, lon=lon, method='nearest')
        ds_tmp = ds_tmp.mean(dim='time')
        ds_tmp['lev'] = ModelAlt
        units, scalby = AC.tra_unit(spec, scale=True)
        ds_tmp *= scalby
        #  plot up...
        ds_tmp.plot(y='lev')
        plt.ylabel('{} ({})'.format('Altitude', 'km'))
        plt.xlabel('{} ({})'.format(spec, units))
        plt.title('Vertical Profile at CVAO during ARNA-2')
        plt.ylim(0, 15)
        if spec == 'O3':
            plt.xlim(-20, 200)
        elif spec == 'NO2':
            plt.xlim(-0.05, 0.2)
        elif spec == 'CO':
            plt.xlim(40, 160)
        if save2png:
            save_str = 'ARNA_vertical_above_CVAO_GEOSChem_{}'
            AC.save_plot(save_str.format(spec))
            AC.close_plot()
        else:
            # Save to PDF
            AC.plot2pdfmulti(pdff, savetitle, dpi=dpi, tight=True)
            if show_plot:
                plt.show()
            plt.close()
        # Do some memory management...
        gc.collect()

    # - Save entire pdf
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')

    # - Explore high ozone in vertical column in coarse output
    site = 'CVO'
    from funcs4obs import gaw_2_loc
    lat, lon, alt, TZ = gaw_2_loc(site)
    NIU, NIU, ModelAlt = AC.get_latlonalt4res('4x5', full_vert_grid=True)
    ModelhPa = AC.hPa_to_Km(ModelAlt, reverse=True)

    def hPa_to_Km_reverse(value, reverse=True):
        return AC.hPa_to_Km(value, reverse=reverse)

    def hPa_to_Km_local(value, reverse=False):
        return AC.hPa_to_Km(value, reverse=reverse)

    # dates2use
    dates2use = [datetime.datetime(2020, 1, 1+i) for i in range(31)]
    dates2use += [datetime.datetime(2020, 2, 1+i) for i in range(29)]

    # Model runs to use?
    res = '4x5'
    RunSet = 'ACID'
    CoreRunsOnly = True
    folder4netCDF = True
    RunDict = ar.get_dict_of_GEOSChem_model_output(res=res, RunSet=RunSet,
                                                   CoreRunsOnly=CoreRunsOnly,
                                                   folder4netCDF=folder4netCDF)
    # Add other runs?
    # merra
    RunRoot = ar.get_local_folder('RunRoot')
    RunStr = '/merra2_4x5_standard.v12.9.0.BASE.2019.2020.diags/OutputDir/'
    RunDict['MERRA.4x5'] = RunRoot + RunStr

    # no biomass burning
    RunStr = '/geosfp_4x5_aciduptake.v12.9.0.BASE.2019.2020.ARNA.DustUptake'
    RunStr += '.JNIT.Isotherm.BCs.repeat.ON.II.diags.J50.BBx0/OutputDir/'
    RunDict['Acid-4x5-J50-NoBB'] = RunRoot + RunStr

    # limit plotted values to within the month before the campaign end
    sdate = datetime.datetime(2020, 1, 15)
    edate = datetime.datetime(2020, 2, 15)
    limit_time2campaign = True

    # Get data
    prefix = 'SpeciesConc_'
    dsD = {}
    for key in RunDict.keys():
        ds = AC.GetSpeciesConcDataset(wd=RunDict[key],
                                      dates2use=dates2use)
        ds = AC.AddChemicalFamily2Dataset(ds, fam='NOx', prefix=prefix)
        if limit_time2campaign:
            bool1 = AC.dt64_2_dt(ds.time) >= sdate
            bool2 = AC.dt64_2_dt(ds.time) <= edate
            ds = ds.isel(time=bool1)
            ds = ds.isel(time=bool2)
        dsD[key] = ds

    # Get GEOS-CF data and...
#    dates2use = [datetime.datetime(2020, 2, 1+i) for i in range(29)]
    dsCF = ar.get_GEOS_assim_expanded_dataset4ARNA(dts=dates2use)
#    dsCF['NOx'] = dsCF['NO'] + dsCF['NO2']
#    dsCF = ar.add_extra_derived_species(dsCF)
    dsCF = AC.AddChemicalFamily2Dataset(dsCF, fam='NOx', prefix='')
    # Update altitude
#    HPa_l = AC.get_GEOSCF_vertical_levels(native_levels=True)
#    hPa_as_km = [i for i in AC.hPa_to_Km(HPa_l)]

    # ... save via disk
    VarNames = ['O3', 'CO', 'NOx']
    ds2plotCF = dsCF[VarNames].sel(lat=lat, lon=lon, method='nearest')
    if limit_time2campaign:
        bool1 = AC.dt64_2_dt(ds2plotCF.time) >= sdate
        bool2 = AC.dt64_2_dt(ds2plotCF.time) <= edate
        ds2plotCF = ds2plotCF.isel(time=bool1)
        ds2plotCF = ds2plotCF.isel(time=bool2)
    ds2plotCF = ds2plotCF.mean(dim='time')
    savename = 'TEMP_NetCDF_GEOSCF_VI.nc'
    ds2plotCF = AC.save_ds2disk_then_reload(ds2plotCF, savename=savename)

    # plot up
    savetitle = 'ARNA_vertical_above_CVAO_GEOSChem_campaign_period2020'
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)

    # plot up GEOS-Chem runs
    prefix = 'SpeciesConc_'
    for VarName in VarNames:
        for key in RunDict.keys():
            ds = dsD[key][[prefix+VarName]]
            ds = ds.sel(lat=lat, lon=lon, method='nearest')
            X = ds[prefix+VarName].values[0] * 1E9
            Y = np.array(ModelhPa[:len(X)])
#            Y = ds.lev.values
            plt.plot(X, Y, label=key)

        # Plot up GEOS-CG
        X = ds2plotCF[VarName].values * 1E9
        Y = ds2plotCF.lev.values
        plt.plot(X, Y, label='GEOS-CF')

        # Beautify and save
        ax = plt.gca()
        if VarName == 'O3':
            plt.xlim(0, 100)
        elif VarName == 'NOx':
            plt.xlim(0, 1)
            ax.set_xscale('log')

#        ax.invert_yaxis()
        # Add a twin y axis
#         secax = ax.secondary_yaxis('right',
#                                    functions=(hPa_to_Km_local,
#                                    hPa_to_Km_reverse)
#                                    )
        plt.ylim()
        ax.invert_yaxis()
#        ax.set_yscale('log')

        ax.set_ylabel('Pressure altitude (hPa)')
        print(ax.get_ylim())
        ax.set_ylim(1000, 100)

        secax = ax.secondary_yaxis('right', functions=(AC.hPa2Km, AC.km2hPa))
        secax.set_ylabel('Altitude (km)')
#        secax.set_yscale('linear')
        print(secax.get_ylim())
        secax.set_ylim(0, 20)

        plt.title(VarName)
        plt.legend()
        AC.plot2pdfmulti(pdff, savetitle, dpi=dpi)  # , tight=True)
        plt.close()

    # - Save entire pdf
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')


def extract_GC_data4CVAO():
    """
    Extract model data for CVAO
    """
    # - Get photolysis surface data for Simone
    RunRoot = ar.get_local_folder('RunRoot')
    folder = 'geosfp_4x5_standard.v12.9.0.BASE.2019.2020.ARNA.BCs.'
    folder += 'TEST.PF_Jrates.JVALS.GLOBAL/OutputDir/'
    folder = RunRoot + folder
    # Open the dataset
    ds = AC.GetJValuesDataset(wd=folder)
    # Extract for CVAO
    site = 'CVO'
    lat, lon, alt, TZ = gaw_2_loc(site)
    ds_tmp = ds.sel(lat=lat, lon=lon, method='nearest')
    ds_tmp = ds_tmp.sel(lev=ds_tmp.lev.values[0])
    # save out to csv.
    vars2use = [i for i in ds.data_vars if 'UV' in i]
    vars2use += [i for i in ds.data_vars if 'Jval_' in i]
    vars2use = list(set(vars2use))
    # Reduce to the variables of intereest and then save to disk
    ds_tmp = ds_tmp[vars2use].squeeze()
    del ds_tmp['lat']
    del ds_tmp['lon']
    del ds_tmp['lev']
    ds_tmp = AC.save_ds2disk_then_reload(ds_tmp)
    df = ds_tmp.to_dataframe()
    df.to_csv('GC_JValues_Collection_4x5_FP-GLOBAL_CVAO.csv')


def test_new_planeflight_Jrate_output():
    """
    Test online rxn. output via plane-flight diagnostic from GEOS-Chem
    """
    from funcs4obs import gaw_2_loc
    # - Setup sites to use
    df = pd.DataFrame()
    GAW_sites = [
        'ASK', 'BRW', 'CGO', 'CMN', 'CPT', 'CVO', 'JFJ', 'LAU', 'MHD', 'MLO',
        'MNM', 'NMY', 'SMO', 'SPO', 'THD'
    ]

    # - Get plane flight output
    RunRoot = ar.get_local_folder('RunRoot')
    folder = RunRoot +'/geosfp_4x5_standard.v12.9.0.BASE.2019.2020.ARNA.BCs
    folder += '.TEST.PF_Jrates.REA.VI/'
    files2use = list(sorted(glob.glob(folder + '/TEST_1day/*plane*')))
    file2use = files2use[0]
    # Get Header infomation from first file
    vars, sites = AC.get_pf_headers(file2use, debug=debug)
    # Extract all points from file
    dfs = []
    for file2use in files2use:
        print(file2use)
        df, NIU = AC.pf_csv2pandas(file=file2use, vars=vars, epoch=True,
                                   r_vars=True)
        dfs += [df]
    # Append the dataframes together
    df = dfs[0].append(dfs[1:])
    df = AC.DF_YYYYMMDD_HHMM_2_dt(df, rmvars=None, epoch=False)
    df.index.name = None

    # Process and save csv files by date
    filename = 'GC_planeflight_data_FP-GLOBAL_JVALS_ARNA1_{}.csv'
    for file2use in files2use:
        date = file2use.split('plane.log.')[-1]
        print(file2use)
        vars, sites = AC.get_pf_headers(file2use, debug=debug)
        df, NIU = AC.pf_csv2pandas(file=file2use, vars=vars, epoch=True,
                                   r_vars=True)
        # Update the datetime index
        df = AC.DF_YYYYMMDD_HHMM_2_dt(df, rmvars=None, epoch=False)
        df.index.name = None
        df.to_csv(filename.format(date))

    # - Get output from NetCDF diagnostics
    # Get Get J-values
    folder = RunRoot+'/geosfp_4x5_standard.v12.9.0.BASE.2019.2020.ARNA.BCs.TEST.PF_Jrates.REA.III/OutputDir/'
    ds = AC.GetJValuesDataset(wd=folder)
    # And get StateMet
    FileStr = 'GEOSChem.StateMet.*'
    ds2 = xr.open_mfdataset(folder+FileStr)
    ds2 = ds2['Met_PMID']
    ds = xr.merge([ds2, ds])

    s_d = {}
    for site in GAW_sites:
        # Get: lat, lon, alt (press), timezone (UTC)
        lat, lon, alt, TZ = gaw_2_loc(site)
        # Use nearest grid box
#                lev2use = AC.find_nearest_value(HPa_r, alt)

        # Get the closest location
        ds_tmp = ds.sel(lat=lat, lon=lon, method='nearest')
        # then select height
#                lev=ds.lev.values[lev2use]
        lev2use = ds_tmp['Met_PMID'].mean(dim='time')
        first_level = int(lev2use.values[0])
        lev2use = AC.find_nearest(lev2use.values, alt)
#                int(lev2use.sel(lev=alt, method='nearest').values)
        ds_tmp = ds_tmp.isel(lev=lev2use)
        print(site, alt, lev2use, lev2use == 0)
        # extract data
        prefix = 'Jval_'
        vars2use = [i for i in ds_tmp.data_vars if prefix in i]
        ds_tmp = ds_tmp[vars2use]
        name_dict = zip(vars2use, [i.split(prefix)[-1] for i in vars2use])
        name_dict = dict(name_dict)
        ds_tmp = ds_tmp.rename(name_dict=name_dict)
        #
        for coord in [i for i in ds_tmp.coords if i != 'time']:
            del ds_tmp[coord]
        S = ds_tmp.to_dataframe()
        s_d[site] = S

    # - plot up
    specs2plot = ['NO2', 'HNO3', 'HNO2', 'BrO', 'IO', 'CH2I2', 'O3', 'PAN']
    # Setup PDF to save PDF plots to
    savetitle = 'ARNA_test_Jvals'
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)
    for site in GAW_sites:
        print(site)
        #
        nc_data = s_d[site]
        pf_data = df.loc[df['TYPE'] == site, :]
        for spec in specs2plot:
            print(spec)

            # Plot up PF
            pf_spec = None
            if spec == 'BrO':
                pf_spec = 'JVL_028'
            elif spec == 'O3':
                pf_spec = 'JVL_002'
            elif spec == 'NO2':
                pf_spec = 'JVL_011'
            elif spec == 'IO':
                pf_spec = 'JVL_116'
            elif spec == 'CH2I2':
                pf_spec = 'JVL_123'
            elif spec == 'PAN':
                pf_spec = 'JVL_059'
            elif spec == 'HNO3':
                pf_spec = 'JVL_016'
            elif spec == 'HNO2':
                pf_spec = 'JVL_015'
            elif spec == 'O1D':
                pf_spec = 'JVL_002'  # Also ???
            else:
                print('case not setup for species: {}'.format(spec))
            if isinstance(pf_spec, str):
                print(spec, pf_spec)
                data = pf_data[pf_spec]
                plt.plot(data.index, data.values, label='PF')
            # Plot up NC
            data = nc_data[spec]
            plt.plot(data.index, data.values, label='NetCDF')
            plt.legend()
            plt.title('{} @ {}'.format(spec, site))
            # save
            AC.plot2pdfmulti(pdff, savetitle, dpi=dpi, tight=True)
            plt.close()

    # - Save entire pdf
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')

    # - Plot up differences between J rates in nested and global run
    savetitle = 'ARNA_Jvals_Global_vs_nest_model'
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)
    RunRoot = ar.get_local_folder('RunRoot')
    RunStr = 'geosfp_4x5_standard.v12.9.0.BASE.2019.2020.'
    folderNest = RunRoot + RunStr + 'ARNA.Nest.repeat.JVALS/'
    folderGlobal = RunRoot + RunStr + 'ARNA.BCs.TEST.PF_Jrates.JVALS.GLOBAL/'
    files2useNest = list(sorted(glob.glob(folderNest + '/*plane*log*')))
    files2useGlobal = list(sorted(glob.glob(folderGlobal + '/*plane*log*')))
    for nfile2use, file2useNest in enumerate(files2useNest):
        date = file2use.split('plane.log.')[-1]
        print(file2use)
        file2useGlobal = files2useGlobal[nfile2use]
        file2use_dict = {'Nest': file2useNest, 'Global': file2useGlobal}
        dfs = {}
        for key in file2use_dict.keys():
            file2use = file2use_dict[key]
            vars, sites = AC.get_pf_headers(file2use, debug=debug)
            df, NIU = AC.pf_csv2pandas(file=file2use, vars=vars, epoch=True,
                                       r_vars=True)
            # Update the datetime index
            df = AC.DF_YYYYMMDD_HHMM_2_dt(df, rmvars=None, epoch=False)
            df.index.name = None
            dfs[key] = df
        # Now plot
        for nkey, key in enumerate(list(dfs.keys())):
            dfs[key]['JVL_134'].plot(label=key, color=['blue', 'red'][nkey])
            plt.title('JHNO3 for flighttrack on {}'.format(date))
        # save
        plt.ylabel('J-rate (s$^{-1}$)')
        plt.legend()
        AC.plot2pdfmulti(pdff, savetitle, dpi=dpi, tight=True)
        plt.close()
    # - Save entire pdf
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')


def evaluate_regional_grid4GEOSChem(show_plot=False, dpi=320):
    """
    Evaluate the regional variable high(er) resolution (flex)grid for GEOS-chem
    """
    # - Load FAAM flighttrack data
    # Import all of the flights by campaign and plot on grid
    # All FAAM campaigns - included in James and Freya's analysis
    # NOTE: this will only use the downloaded files for now.
    campaign = 'ARNA-2'
    dfARNA = get_flighttracks4campaign(campaign)
    campaigns = [
        'ARNA-2', 'ACISIS-5', 'ACRUISE', 'ACISIS-4', 'MOYA-2', 'ACISIS-3',
        'ACISIS-2',
        #    'Clarify', # FAAM files not downloaded
        'MOYA-1',
        #    'ACISIS-1' # FAAM files not downloaded
    ]
    dfs = [get_flighttracks4campaign(i) for i in campaigns]

    # - Plot up high resolution modelling region around ARNA-2 flights
    savetitle = 'ARNA_high_resolution_model_grid'
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)
    # Plot up a blank global background
    fig, ax = plt_highres_modelling_region(plot_blank_data=True)
    # Add the campaign flights to this
    campaign = 'ARNA-2'
    df = dfARNA
    LatVar = 'LAT_GIN'
    LonVar = 'LON_GIN'
    lats = df[LatVar].values
    lons = df[LonVar].values
    color_list = AC.get_CB_color_cycle()
    projection = ccrs.PlateCarree
    # Now scatter points on plot
    ax = add_scatter_points2cartopy_ax(ax=ax, lons=lons, lats=lats,
                                       color=color_list[0],
                                       label=campaign)

    fig.legend(loc=7)
    fig.suptitle('Flight-tracks during ARNA-2 campaign')
    # Save to PDF
    AC.plot2pdfmulti(pdff, savetitle, dpi=dpi)
    if show_plot:
        plt.show()
    plt.close()

    # - Plot up high resolution modelling region around BB FAAM flights
    fig, ax = plt_highres_modelling_region(plot_blank_data=True)
    for n_campaign, campaign in enumerate(campaigns):
        df = dfs[campaigns.index(campaign)]
        print(campaign)
        lats = df[LatVar].values
        lons = df[LonVar].values
        ax = add_scatter_points2cartopy_ax(ax=ax, lons=lons, lats=lats,
                                           color=color_list[n_campaign],
                                           label=campaign)
    title = "Flight-tracks during FAAM campaigns in biomass burning analysis"
    fig.suptitle(title)
    fig.legend(loc=7)
    # Save to PDF
    AC.plot2pdfmulti(pdff, savetitle, dpi=dpi)
    if show_plot:
        plt.show()
    plt.close()

    # - Now evaluate biomass burning emissions for grid
    earth0_folder = '/mnt/lustre/groups/chem-acm-2018/earth0_data/'
    HEMCO_folder = earth0_folder + 'GEOS//ExtData/HEMCO/'
    # Get GFAS emissions for the year

    # Plot by seasons - TODO

    # Plot for feb 2020
    folder = HEMCO_folder+'/GFAS/v2018-09/2020/'
    filename = 'GFAS_202002.nc'
    ds = xr.open_dataset(folder+filename)
    # Update lon to be in degrees West -
    var2use = 'cofire'
    ds = ds[[var2use]]
    ds = ds.assign_coords({'lon': ds.lon.values - 180})
    # Update name and scaling
    Uvar2use = '{} (1E-9 {})'.format(ds[var2use].long_name, ds[var2use].units)
    ds = ds.rename({var2use: Uvar2use})
    var2use = Uvar2use
    ds = ds[[var2use]].mean(dim='time') * 1E9
    # Remove zero data
    arr = ds[var2use].values
    arr[arr <= 0] = np.NaN
    ds[var2use].values = arr
    # And Roll the variables too
#    ds = ds.roll(lon=-int(len(ds.lon)/2))
    arr = ds[var2use].values
    arr = np.roll(arr, -int(len(ds.lon)/2), axis=1)
    ds[var2use].values = arr
    # Plot up the data
    fig, ax = plt_highres_modelling_region(ds=ds, var2use=var2use,
                                           plot_blank_data=False,
                                           rm_colourbar=False)

    fig.suptitle('Biomass burning emissions (GFAS) - Feb 2020 (ARNA-2)')
    del ds
    # Save to PDF
    AC.plot2pdfmulti(pdff, savetitle, dpi=dpi)
    if show_plot:
        plt.show()
    plt.close()

    # - Now evaluate dust emission for grid
    # Plot by seasons - TODO

    # Plot for February
    folder = HEMCO_folder+'/OFFLINE_DUST/v2019-01/0.5x0.625/2019/02/'
    files2use = glob.glob(folder+'*nc')
    ds = xr.open_mfdataset(files2use)
    # Combine all dust emissions
    var2use = 'Total dust emission (kg/m2/s)'
    ds[var2use] = ds['EMIS_DST1'].copy()
    ds[var2use] = ds[var2use].values + ds['EMIS_DST2']
    ds[var2use] = ds[var2use].values + ds['EMIS_DST3']
    ds[var2use] = ds[var2use].values + ds['EMIS_DST4']
    ds = ds[[var2use]].mean(dim='time')
    # Remove zero data
    arr = ds[var2use].values
    arr[arr <= 0] = np.NaN
    ds[var2use].values = arr
    # Plot up the data
    fig, ax = plt_highres_modelling_region(ds=ds, var2use=var2use,
                                           plot_blank_data=False,
                                           rm_colourbar=False)

    fig.suptitle('Dust emissions (online) - Feb *2019* (ARNA-2)')
    # Save to PDF
    AC.plot2pdfmulti(pdff, savetitle, dpi=dpi)
    if show_plot:
        plt.show()
    plt.close()

    # - Now evaluate NOx emission for grid?

    # - Others variables to plot / consider?
    # Night lights?

    # Save entire pdf
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')


def mk_comparisons_of_humidty():
    """
    Make comparisons between observed and modelled humidity
    """
    # --- GEOS-Chem
    # Get model data
    dfs_mod_GC
    run2use = 'Acid-4x5-J00'
    dfs = [dfs_mod_GC[i][run2use] for i in flight_IDs]
    df = pd.concat(dfs)

    # Add satuation pressure to df
    # 𝑒𝑠0 saturation vapor pressure at 𝑇0 (Pa)
    T0 = 273.16
    T = df['GMAO_TEMP'].values  # model temp (already in kelvin)
    CC_partial_solution = np.exp((17.67 * (T - T0)) / (T - 29.65))
    df['Es'] = 611.0 * CC_partial_solution

    # NOTE: the model expoerts absolute humidty, not specific humidity
    # 𝑞  specific humidity or the mass mixing ratio of water vapor to total air (dimensionless)
    q = df['GMAO_ABSH']  # unitless (which is ≈ 𝑤 )
    p = df['GMAO_PRES']  # HPa

    # And then calculate Ws ...
    # where "𝑝 pressure (Pa)"
    df['Ws'] = 0.622 * df['Es'] / p

    # Complete calculation
    df['RH'] = 0.263 * p * q * (CC_partial_solution**-1)

    # --- GEOS-CF
    df = pd.concat([dfs_mod_CF[i] for i in flight_IDs])
    df['Alt'] = AC.hPa_to_Km(df['model-lev'].values)

    # plot
    import seaborn as sns
    sns.set(color_codes=True)
    fig, ax = plt.subplots()

    plt.title('Modelled Relative Humidity for ARNA-2 flights')
    # Plot up model data
    plt.scatter(df['RH'].values, df['Alt'].values,
                label='Relative Humidity')
#    plt.hlines( 0.753 )
#    plt.vlines(x=0.753, ymin=1000, ymax=150 )
#    ax.invert_yaxis()

    # Add a second axis
    plt.legend()
    AC.save_plot(dpi=720)
    plt.close('all')


def mk_vertical_comparisons_with_nirate():
    """
    """

    # folder

    # Now plot by location

    #

    pass


def plt_seasonal_species_at_sites():
    """
    Plot up seasonal comparisons at campaign sites (Bermuda and CVAO)
    """
    # Get data
    RunRoot = ar.get_local_folder('RunRoot')
    FolderStr = 'geosfp_4x5_aciduptake.v12.9.0.BASE.2019.2020.ARNA.DustUptake.'
    FolderStr += 'JNIT.Isotherm.BCs.repeat.ON.II.diags.v2.J00.HourlyOutput/'
    FolderStr = RunRoot + FolderStr + 'OutputDir/'
    RunDict = {'J00': FolderStr}
    # Dates to use?
    sdate = datetime.datetime(2019, 1, 1)
    edate = datetime.datetime(2019, 12, 31)
    dates2use = pd.date_range(sdate, edate, freq='1H')

    # Put data into a dictionary
    dsD = {}
    file_str = 'GEOSChem.SpeciesConcSubset.*.nc4'
    for key in RunDict.keys():
        ds = AC.get_GEOSChem_files_as_ds(wd=RunDict[key],
                                         file_str=file_str,
                                         dates2use=dates2use)
        # Select year and surface data
        bool1 = AC.dt64_2_dt(ds.time) >= sdate
        bool2 = AC.dt64_2_dt(ds.time) <= edate
        ds = ds.isel(time=bool1)
        ds = ds.isel(time=bool2)
        ds = ds.sel(lev=ds.lev.values[0])
        # Drop excess variables and rename speices
        drop_vars = ['hyam', 'hybm', 'hyai', 'hybi', 'P0', 'AREA']
        for var in drop_vars:
            try:
                del ds[var]
            except KeyError:
                print('Not deleting: {}'.format(var))
        prefix = 'SpeciesConc_'
        VarNames = [i.split(prefix)[-1] for i in ds.data_vars]
        name_dict = dict(zip(ds.data_vars, VarNames))
        ds = ds.rename(name_dict=name_dict)
        # Save to dict
        dsD[key] = ds

    # Other runs to plot

    # Sites to plot
    # Bermuda, CVAO
    sites = ['CVO', 'BMW']
    for site in sites:

        # Sub-select data for site
        lon, lat, alt = AC.get_loc(site)

        # Plot up
        dfs = {}
        for key in RunDict.keys():

            # Subselect data
            ds2plot = ds.sel(lat=lat, lon=lon, method='nearest')
            del ds2plot['lev']
            del ds2plot['ilev']
            del ds2plot['lat']
            del ds2plot['lon']

            # Save output to csv file
            savename = 'TEMP_NetCDF_{}.nc'.format(site)
            AC.save_ds2disk_then_reload(ds2plot, savename=savename)
#            df = ds2plot.to_dataframe()
#            df.to_csv('ARNA_GEOSChem_v12_9_0_{}_{}'.format(site, key))
#            dfs[key] = df
        # Now loop to plot the species

    # Now plot
    specs2plot = ['O3', 'CO', 'HCl', 'ClNO2', 'IO', 'BrO', ]

    # plot up as diurnal
    savetitle = 'GEOSChem_v12_9_0_seasonal_diel_at_{}'.format(site)
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)

    for spec in specs2plot:

        units, scaleby = AC.tra_unit(spec, scale=True)

        AC.plot_up_diel_by_season(dfs={'model': df.copy()*scaleby}, spec=spec,
                                  sub_str=site,
                                  units=units)

        # Save to PDF
        AC.plot2pdfmulti(pdff, savetitle, dpi=dpi, tight=True)
        plt.close()

    # - Save entire pdf
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')


def plt_bermuda_obs(debug=False):
    """
    Plot up Bermuda observations
    """
    # Switches
    ReadFromCSV = True
    UseV13output = True

    # Get observational data
    ExcelFileName = 'Bermuda_data_hourly.xlsx'
    Folder = '/users/ts551/scratch/data/ARNA/Bermunda/'
    format = '%Y-%m-%d %H:%M:%S'
    # Spring Data
    if ReadFromCSV:
        CSVFileName = 'Bermuda_data_hourly_spring.csv'
        dfSpring = pd.read_csv(Folder+CSVFileName)
        UnitsSpring = dfSpring.loc[0, :].to_dict()
        dfSpring = dfSpring.drop(0)
        TimeVar = 'Time (utc-3)'
        dfSpring.index = pd.to_datetime(dfSpring[TimeVar].values)
    else:
        SheetName = 'Bermuda_Spring_data_hourly'
        dfSpring = pd.read_excel(Folder+FileName, SheetName=SheetName,
                                 date_parser=format)
        # Save the units as attributes
        UnitsSpring = dfSpring.loc[0, :].to_dict()
        dfSpring = dfSpring.drop([0])  # Drop the unit row
        dfSpring.index = dfSpring['Time (utc-3)']

    # Summer Data
    if ReadFromCSV:
        CSVFileName = 'Bermuda_data_hourly_summer.csv'
        dfSummer = pd.read_csv(Folder+CSVFileName)
        UnitsSummer = dfSummer.loc[0, :].to_dict()
        dfSummer = dfSummer.drop(0)
        TimeVar = 'Time'
        dfSummer.index = pd.to_datetime(dfSummer[TimeVar].values)
    else:
        SheetName = 'Bermuda_Summer_data_hourly'
        dfSummer = pd.read_excel(Folder + FileName, SheetName=SheetName,
                                 date_parser=format)
        # Save the units as attributes
        UnitsSummer = dfSummer.loc[0, :].to_dict()
        dfSummer = dfSummer.drop([0])  # Drop the unit row
        dfSummer.index = dfSummer['Time (utc-3)']

    # Store the start and end dates of the observational period
    # With a one dat buffer to improve mundging with model
    seasons = ('Spring', 'Summer', )
    dPeriods = {
        'Summer': (datetime.datetime(2019, 8, 10),
                   datetime.datetime(2019, 9, 12)
                   ),
        'Spring': (datetime.datetime(2019, 4, 16),
                   datetime.datetime(2019, 5, 14)
                   ),
    }
    # Ensure the units are the same in obs. between spring and summer
    for key in UnitsSummer.keys():
        if debug:
            print(key)
        NewUnits = UnitsSummer[key]
        if (key in list(UnitsSpring.keys())):
            CurrentUnits = UnitsSpring[key]
            SameUnits = CurrentUnits == NewUnits
            if not (SameUnits):
                PrtStr = "'Units in list for: '{}', as: '{}', ({}, same?:{})"
                print(PrtStr.format(key, NewUnits, CurrentUnits, SameUnits))
                print('Why the units different?')

    # Combine data into a single dataframe
    dfObs = pd.concat([dfSpring, dfSummer], axis=0)
    # convert times to UTC
    index = AC.dt64_2_dt(dfObs.index.values)
    dfObs.index = AC.add_hrs(index, 3)

    # Combine columns for HONO (due to inconsistent naming)
    Var1 = '[HONO]'
    Var2 = '[HONO] '
    VarHONO_Obs = 'HONO_processed'
    dfHONO = pd.concat([dfObs[Var1].dropna(), dfObs[Var2].dropna()])
    dfObs[VarHONO_Obs] = dfHONO

    # Clean up other columns and
    vars2del = Var1, Var2, 'Time (utc-3)', 'Time', 'Time.1',
    for var in vars2del:
        try:
            del dfObs[var]
        except:
            print("Error: failed to delete var: '{}'".format(var))
    # force columns to be numeric
    for col in dfObs.columns:
        dfObs[col] = pd.to_numeric(dfObs[col], errors='coerce')

    # Also add model to the comparisons
    # Use the generic year of Bermuda obs run for Pete/
    if UseV13output:
        FileName = 'v13-4-0_bermua.csv'
        dfMod = pd.read_csv(Folder + FileName)
        dfMod.index = pd.to_datetime(dfMod['datetime'].values)
        # Just use 2018 data for now.
        dfMod = dfMod.loc[dfMod.index.year == 2018, :]
        # But kludge the year to be 2019
        index = AC.dt64_2_dt(dfMod.index.values)
        dfMod.index = [AC.update_year(i, year=2019) for i in index]

    else:
        FileName = 'NSFB_ARNA_GEOSChem_v12_9_0_BMW_J00.csv'
        dfMod = pd.read_csv(Folder + FileName)
        dfMod.index = pd.to_datetime(dfMod['time'].values)

    # Add NOx to obs and model
    var1 = '[NO] (NOx system)'
    var2 = '[NO2] (NOx system)'
    dfObs['NOx'] = dfObs[var1] + dfObs[var1]
    dfMod['NOx'] = dfMod['NO'] + dfMod['NO2']
    NIT_all = ['NITD4', 'NITD3', 'NITD2', 'NITD1', 'NITs', 'NIT', ]
    dfMod['NITs-all'] = dfMod[NIT_all].sum(axis=1)

    # Map obs. species names to model ones
    dObs2Mod = {
        'Time (utc-3)': np.NaN,
        'Time': np.NaN,
        '[HNO3]': 'HNO3',
        '[pNO3] corrected': 'NITs-all',
        '[NO] (NOx system)': 'NO',
        '[NO2] (NOx system)': 'NO2',
        '[O3]': 'O3',
        'WS': 'NOT IN CURRENT DATASET',
        'WD': 'NOT IN CURRENT DATASET',
        'AirTempC_Avg': 'GMAO_TEMP',
        'RH_Avg': 'NOT IN CURRENT DATASET',
        'BP_mmHg_Avg': 'NOT IN CURRENT DATASET',
        'TSP': 'NOT IN CURRENT DATASET',
        'J(HONO)': 'NOT IN CURRENT DATASET',
        #    '[HONO] ': 'HNO2',
        # add derived variables
        'NOx': 'NOx',
        VarHONO_Obs: 'HNO2',
    }
    dObs2Mod_r = {v: k for k, v in list(dObs2Mod.items())}

    # Which vars to plot
    # TODO
    vars2plot = [
        'O3', 'NO', 'NO2', 'NOx', 'HNO3', 'NITs-all', 'HNO2',
        # Add J-rates and GMAO values
        #    'GMAO_TEMP',
    ]

    # - Plot up whole data as a generic time series
    context = 'paper'
    import seaborn as sns
    sns.set(color_codes=True)
    sns.set_context(context)
    savetitle = 'ARNA_Bermunda_comp_v13'
    pdff = AC.plot2pdfmulti(title=savetitle, open=True, dpi=dpi)
    for season in seasons:
        # Sub-select dates for season
        sdate, edate = dPeriods[season]

        for var in vars2plot:
            print(season, var)
            units, scaleby = AC.tra_unit(var, scale=True)
            # Force units to be the same as observations in pptv
            pptv_units = 'HNO3', 'HNO2', 'NO', 'NO2', 'NOx'
            if (var in pptv_units):
                units, scaleby = 'pptv', 1E12
            # V13 alreaedy scaled
            if UseV13output:
                scaleby = 1
            # Plot obs
            bool1 = dfObs.index >= sdate
            bool2 = dfObs.index <= edate
            df2plot = dfObs.loc[(bool1 & bool2), :]
            plt.plot(df2plot[dObs2Mod_r[var]].index,
                     df2plot[dObs2Mod_r[var]].values,
                     label='Obs.',
                     color='Black',
                     )

            # Try to plot model
            bool1 = dfMod.index >= sdate
            bool2 = dfMod.index <= edate
            df2plot = dfMod.loc[(bool1 & bool2), :]
            plt.plot(df2plot[var].index,
                     df2plot[var].values * scaleby,
                     label='Model',
                     color='Red',
                     )

            plt.legend()

            # Add a title
            PrtStr = "Timeseries {} @ Bermuda during *{}* campaign ({})"
            plt.title(PrtStr.format(var, season.lower(), units))

            # Update x axis label rotation
            plt.xticks(rotation=45)

            # Save to PDF
            AC.plot2pdfmulti(pdff, savetitle, dpi=dpi, tight=True)
            plt.close()

        # Plot up daily cycles
        for var in vars2plot:
            fig, ax = plt.subplots()
            print(season, var)
            units, scaleby = AC.tra_unit(var, scale=True)
            # Force units to be the same as
            pptv_units = 'HNO3', 'HNO2', 'NO', 'NO2', 'NOx'
            if (var in pptv_units):
                units, scaleby = 'pptv', 1E12

            # Plot obs
            bool1 = dfObs.index >= sdate
            bool2 = dfObs.index <= edate
            df2plot = dfObs.loc[(bool1 & bool2), :]

            AC.BASIC_diel_plot(dates=df2plot[dObs2Mod_r[var]].index,
                               data=df2plot[dObs2Mod_r[var]].values,
                               label='Obs.',
                               color='Black',
                               spec=var, units=units,
                               fig=fig, ax=ax)

            # Try to plot model
            bool1 = dfMod.index >= sdate
            bool2 = dfMod.index <= edate
            df2plot = dfMod.loc[(bool1 & bool2), :]

            AC.BASIC_diel_plot(dates=df2plot[var].index,
                               data=df2plot[var].values * scaleby,
                               label='Obs.',
                               color='Red',
                               spec=var, units=units,
                               fig=fig, ax=ax)

            # Add a title
            PrtStr = "Diel cycle {} @ Bermuda during {} campaign ({})"
            plt.title(PrtStr.format(var, season.lower(), units))

            # Save to PDF
            AC.plot2pdfmulti(pdff, savetitle, dpi=dpi, tight=True)
            plt.close()

    # Save PDF
    AC.plot2pdfmulti(pdff, savetitle, close=True, dpi=dpi)
    plt.close('all')


def plt_comp_with_NASA_Atom():
    """
    Plot up comparisons with NASA ATom data
    """
    # Get lastest NASA ATom data and plot up

    #

    #

    pass


if __name__ == "__main__":
    main()
