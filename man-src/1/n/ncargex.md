---
title: "ncargex(1)"
name: "ncargex"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncargex/"
description: "ncargex – NCAR Graphics Fortran and C Low-Level Utility Examples"
---

<h2>NAME</h2>
<p> ncargex &#8211; NCAR Graphics Fortran and C Low-Level Utility Examples</p>
<h2>SYNOPSIS</h2>
<pre><code>
ncargex[-A][-E][-F][-P][-T]
       [-U][-C][-Fortran][-class][-ps]
       [-x11][-W workstation_type][-areas]
       [-autograph][-bivar][-colconv][-conpack]
       [-conpackt][-conran_family][-conrec_family]
       [-csagrid][-cssgrid][-dashline][-dashpack]
       [-dsgrid][-ezmap][-field_flow][-fitgrid]
       [-gflash][-gks][-gridall][-halftone]
       [-histogram][-isosrfhr][-isosurface][-labelbar]
       [-natgrid][-ngmath][-ngmisc][-plotchar]
       [-polypack][-pwrite_family][-scrolled_title]
       [-seter][-shgrid][-softfill][-spps]
       [-streamlines][-surface][-tdpack][-threed]
       [-vaspackt][-vectors][-wmap][-misc]
       [-clean][-n][-ncarbd][-noX11][-onebyone] example_name...
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>ncargex</i> provides the user with access to over 300 complete example NCAR Graphics Fortran and C source codes, including the examples in the NCAR Graphics Tutorial. <i>ncargex</i> copies the source code for the specified example(s) into the current directory and then compiles, links, and executes the example. Depending on the type of workstation specified on the command line, the output may either be an NCGM (NCAR Graphics Metafile) file, one of many types of PostScript files, or a text dump. It is also possible for no output to be produced if you select the &quot;x11&quot; workstation, in which case each frame is displayed directly to a separate X window after it is generated. If no workstation is specified on the command line, then it defaults to an &quot;NCGM&quot;, unless the example is a special one which is discussed below. </p>
<p> If you select one of the workstation types that produces an output file, then the file name will have the same name as the example and ending with an appropriate suffix: &quot;.ncgm&quot;, &quot;.txt&quot;, &quot;.ps&quot;, etc. </p>
<p> Certain examples were created to demonstrate a particular function, like how to rename your metafile from within the program, how to use the full page when going to PostScript output, how to use the X11 driver and produce a graphic file at the same time, etc. If the example that you ask for is one of these, a message will be printed to this effect to alert you. </p>
<p> In order to run <i>ncargex</i>, you must have your NCARG_ROOT environment variable set to the parent directory where the NCAR Graphics libraries, binaries, and include files were installed. If this environment variable is not set, <i>ncargex</i> will attempt to set it for you. If the NCAR Graphics libraries, binaries, and include files were not installed under one parent directory, then you will need to set the environment variables NCARG_LIB, NCARG_BIN, and NCARG_INCLUDE instead. Please see &quot;man ncargintro&quot; for more information. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-W</p>
<dd> Specify the workstation type. This argument can be specified as a number or as a string, where the number has the same value you would use in a call to GOPWK. The following numbers are valid:</p>
<dt> 1</p>
<dd> &#8211; NCGM</p>
<dt> 8</p>
<dd> &#8211; X11 window.</p>
<dt> 10</p>
<dd> &#8211; text dump of graphics output.</p>
<dt> 20</p>
<dd> &#8211; color PostScript in portrait mode.</p>
<dt> 21</p>
<dd> &#8211; color Encapsulated PostScript (EPS) in portrait mode.</p>
<dt> 22</p>
<dd> &#8211; color Encapsulated PostScript Interchange format (EPSI) in portrait mode.</p>
<dt> 23</p>
<dd> &#8211; monochrome PostScript in portrait mode.</p>
<dt> 24</p>
<dd> &#8211; monochrome Encapsulated PostScript (EPS) in portrait mode.</p>
<dt> 25</p>
<dd> &#8211; monochrome Encapsulated PostScript Interchange format (EPSI) in portrait mode.</p>
<dt> 26</p>
<dd> &#8211; color PostScript in landscape mode.</p>
<dt> 27</p>
<dd> &#8211; color Encapsulated PostScript (EPS) in landscape mode.</p>
<dt> 28</p>
<dd> &#8211; color Encapsulated PostScript Interchange format (EPSI) in landscape mode.</p>
<dt> 29</p>
<dd> &#8211; monochrome PostScript in landscape mode.</p>
<dt> 30</p>
<dd> &#8211; monochrome Encapsulated PostScript (EPS) in landscape mode.</p>
<dt> 31</p>
<dd> &#8211; monochrome Encapsulated PostScript Interchange format (EPSI) in landscape mode. </p>
<dt>
<dd> If you want to specify the workstation as a string, then there are a few ways this can be done. For example, the following workstation types are valid:</p>
<dt> ncgm</p>
<dd> &#8211; NCGM</p>
<dt> x11</p>
<dd> &#8211; X11 window</p>
<dt> text</p>
<dd> &#8211; text dump of graphics output </p>
<dt>
<dd> For PostScript output, there are more attributes: the type of PostScript you file want (&quot;ps&quot;, &quot;eps&quot;, or &quot;epsi&quot;), whether you want color or monochrome (&quot;color&quot; or &quot;mono&quot;), and whether you want portrait or landscape mode (&quot;port&quot; or &quot;land&quot;). The orientation and the color preference can be omitted (as they will will default to &quot;port&quot; and &quot;color&quot; respectively), but you must specify the PostScript file type. Each attribute can be entered in any order, separated by periods. The following are examples of valid PostScript workstation types:</p>
<dt>ps.color</p>
<dd> &#8211; color PostScript in portrait mode.</p>
<dt>land.eps.mono</p>
<dd> &#8211; monochrome Encapsulated PostScript format (EPS) in landscape mode.</p>
<dt>epsi</p>
<dd> &#8211; color Encapsulated PostScript Interchange format (EPSI) in portrait mode.</p>
<dt>port.mono.ps</p>
<dd> &#8211; monochrome PostScript in portrait mode. </p>
<p> Any combination of these three types of attributes can be used, as long as one of them is the PostScript file type. </p>
<dt>-A</p>
<dd> Generate all available C/Fortran examples, tests, programmer doc, fundamental and tutorial examples. </p>
<dt>-E</p>
<dd> Generate all available C/Fortran examples. </p>
<dt>-F</p>
<dd> Generate all available fundamental C/Fortran examples. </p>
<dt>-P</p>
<dd> Generate all available programmer doc C/Fortran examples. </p>
<dt>-T</p>
<dd> Generate all available tests. </p>
<dt>-U</p>
<dd> Generate all available tutorial C/Fortran examples. </p>
<dt>-C</p>
<dd> Generate all available C examples. </p>
<dt>-Fortran</p>
<dd> Generate all available Fortran examples. </p>
<dt>-class</p>
<dd> Generate all available class C/Fortran examples. </p>
<dt>-ps</p>
<dd> Generate all C/Fortran examples that use the PostScript driver. </p>
<dt>-x11</p>
<dd> Generate all C/Fortran examples that use the X11 driver. </p>
<dt>-areas</p>
<dd> Generate all Areas C/Fortran examples. </p>
<dt>-autograph</p>
<dd> Generate all Autograph C/Fortran examples. </p>
<dt>-bivar</p>
<dd> Generate all bivar C/Fortran examples. </p>
<dt>-colconv</p>
<dd> Generate all Colconv C/Fortran examples. </p>
<dt>-conpack</p>
<dd> Generate all Conpack C/Fortran examples. </p>
<dt>-conpackt</p>
<dd> Generate all Conpackt C/Fortran examples. </p>
<dt>-conran_family</p>
<dd> Generate all Conran Fortran examples. </p>
<dt>-conrec_family</p>
<dd> Generate all Conrec Fortran examples. </p>
<dt>-csagrid</p>
<dd> Generate all Ngmath Csagrid C/Fortran examples. </p>
<dt>-cssgrid</p>
<dd> Generate all Ngmath Cssgrid C/Fortran examples. </p>
<dt>-dashline</p>
<dd> Generate all Dashline C/Fortran examples. </p>
<dt>-dashpack</p>
<dd> Generate all Dashpack C/Fortran examples. </p>
<dt>-dsgrid</p>
<dd> Generate all Ngmath Dsgrid C/Fortran examples. </p>
<dt>-ezmap</p>
<dd> Generate all Ezmap C/Fortran examples. </p>
<dt>-field_flow</p>
<dd> Generate all Field_flow C/Fortran examples. Includes streamlines and vectors examples. </p>
<dt>-fitgrid</p>
<dd> Generate all Ngmath Fitgrid C/Fortran examples. </p>
<dt>-gflash</p>
<dd> Generate all Gflash C/Fortran examples. </p>
<dt>-gks</p>
<dd> Generate all GKS C/Fortran examples. </p>
<dt>-gridall</p>
<dd> Generate all Gridall C/Fortran examples. </p>
<dt>-halftone</p>
<dd> Generate all Halftone Fortran examples. </p>
<dt>-histogram</p>
<dd> Generate all Histogram C/Fortran examples. </p>
<dt>-isosrfhr</p>
<dd> Generate all Isosrfhr Fortran examples. </p>
<dt>-isosurface</p>
<dd> Generate all Isosurface C/Fortran examples. </p>
<dt>-labelbar</p>
<dd> Generate all Labelbar C/Fortran examples. </p>
<dt>-natgrid</p>
<dd> Generate all Ngmath Natgrid C/Fortran examples. </p>
<dt>-ngmath</p>
<dd> Generate all Ngmath C/Fortran examples. </p>
<dt>-ngmisc</p>
<dd> Generate all Ngmisc C/Fortran examples. </p>
<dt>-plotchar</p>
<dd> Generate all Plotchar C/Fortran examples. </p>
<dt>-polypack</p>
<dd> Generate all Polypack C/Fortran examples. </p>
<dt>-pwritx_family</p>
<dd> Generate all Pwrite Fortran examples. </p>
<dt>-scrolled_title</p>
<dd> Generate all Scrolled title C/Fortran examples. </p>
<dt>-seter</p>
<dd> Generate all Seter C/Fortran examples. </p>
<dt>-shgrid</p>
<dd> Generate all Ngmath Shgrid C/Fortran examples. </p>
<dt>-softfill</p>
<dd> Generate all Softfill C/Fortran examples. </p>
<dt>-spps</p>
<dd> Generate all SPPS C/Fortran examples. </p>
<dt>-streamlines</p>
<dd> Generate all Streamlines C/Fortran examples. </p>
<dt>-surface</p>
<dd> Generate all Surface C/Fortran examples. </p>
<dt>-tdpack</p>
<dd> Generate all Tdpack C/Fortran examples. </p>
<dt>-threed</p>
<dd> Generate all Threed C/Fortran examples. </p>
<dt>-vaspackt</p>
<dd> Generate all Vaspackt C/Fortran examples. </p>
<dt>-vectors</p>
<dd> Generate all Vectors C/Fortran examples. </p>
<dt>-wmap</p>
<dd> Generate all Weather map C/Fortran examples. </p>
<dt>-misc</p>
<dd> Generate all miscellaneous C/Fortran examples. </p>
<dt>-clean</p>
<dd> Remove everything but the &quot;.ncgm&quot; file. </p>
<dt>-n</p>
<dd> Specifies that the example should not be compiled, linked, or run, but just copied into your local directory. </p>
<dt>-ncarbd</p>
<dd> Use this option for compilers that appear to be having trouble initializing blockdata variables. It will cause one or two small subroutines to be linked in that helps force the loading of blockdata initialization routines. </p>
<dt>-ngmathbd</p>
<dd> Use this option for compilers that appear to be having trouble initializing blockdata variables. It will cause a small subroutine to be linked in that helps force the loading of blockdata initialization routines. </p>
<p> Note: this option doesn&#8217;t need to be specified separately if you are already including the <code>-ncarbd</code> and <code>-ngmath</code> options. </p>
<dt>-noX11</p>
<dd> Do not link in the X library when linking the selected examples and/or tests. A stub will be linked instead. </p>
<dt>-onebyone</p>
<dd> Specifies that the selected examples and/or tests should be generated one at a time and viewed as they are generated. This is intended for use during testing of new releases at NCAR. </p>
<p> Below is a list of all the available <i>ncargex</i> examples. They are listed according to which utility they belong with. </p>
</dl>
<h2>EXAMPLES AVAILABLE</h2>
<p> <i>AREAS Examples:</i> </p>
<p> arex01 arex02 arex03 cardb1 cardb2 caredg carfill carline carmap tareas c_tareas </p>
<p> <i>AUTOGRAPH Examples:</i> </p>
<p> agdp01 agex01 agex02 agex03 agex04 agex05 agex06 agex07 agex08 agex09 agex10 agex11 agex12 agex13 fagaxclr fagaxlbl fagaxmax fagcuclr fagcudsh fagezmxy fagezmy fagezxy fagezy fagilclr fagovrvw tagupw tautog c_agex07 </p>
<p> <i>BIVAR Examples:</i> </p>
<p> cbex01 cidsfft c_cbex01 </p>
<p> <i>COLCONV Examples:</i> </p>
<p> coex01 coex02 coex03 fcce01 fcce02 tcolcv c_coex02 </p>
<p> <i>CONPACK Examples:</i> </p>
<p> cbex01 ccpback ccpcff ccpcfx ccpcica ccpcir ccpcis ccpcit ccpclc ccpcld ccpcldm ccpcldr ccpcll ccpclu ccpcnrc ccpdflt ccpezct ccpfil ccpga ccphand ccphcf ccphl ccphlt ccpila ccpils ccpilt ccpklb ccplbam ccplbdr ccpline ccpllb ccpllc ccplll ccpllo ccpllp ccpllt ccpllw ccpmap ccpmovi ccpmpxy ccpncls ccpnet ccpnof ccpnsd ccppc ccppc1 ccppc2 ccppc3 ccppc4 ccppkcl ccppole ccprc ccprect ccprwc ccprwu ccpscam ccpset ccpsps1 ccpsps2 ccpspv ccpt2d ccptitle ccpvp ccpvs cidsfft colcon cpex01 cpex02 cpex03 cpex04 cpex05 cpex06 cpex07 cpex08 cpex09 cpex10 cpex11 cpex12 cpex13 cpex14 cpex15 cpex16 tconpa c_cbex01 c_colcon </p>
<p> <i>CONPACKT Examples:</i> </p>
<p> ctcbay ctex01 ctex02 ctfite ctgaus ctgc23 ctgeo1 ctgeo2 ctgeo3 ctiscp ctisc2 ctllg1 ctllg2 ctllg3 ctnccl ctorca ctpopg ctswth ctterr ctwng1 ctwng2 cttd01 cttd02 c_ctllg3 </p>
<p> <i>CONRAN FAMILY Examples:</i> </p>
<p> tconan tconaq tconas </p>
<p> <i>CONREC FAMILY Examples:</i> </p>
<p> tcnqck tcnsmt tcnsup tconre </p>
<p> <i>CSAGRID Examples:</i> </p>
<p> csex01 csex02 csex03 csex04 csex05 csex06 csex07 c_csex01 c_csex02 c_csex03 c_csex04 c_csex05 c_csex06 c_csex07 </p>
<p> <i>CSSGRID Examples:</i> </p>
<p> cssex01 cssex02 cssex03 c_cssex01 c_cssex02 c_cssex03 </p>
<p> <i>DASHLINE Examples:</i> </p>
<p> fdlcurvd fdldashc fdldashd fdlsmth tdashc tdashl tdashp tdashs c_fdldashc </p>
<p> <i>DASHPACK Examples:</i> </p>
<p> tdshpk c_tdshpk </p>
<p> <i>DSGRID Examples:</i> </p>
<p> dsex01 dsex01d dsex02 dsex03 dsex04 dsex05 dsex06 c_dsex01 c_dsex01d c_dsex02 c_dsex03 c_dsex04 c_dsex05 c_dsex06 </p>
<p> <i>EZMAP Examples:</i> </p>
<p> cezmap1 cezmap2 cezmap3 cmpclr cmpdd cmpdrw cmpel cmpfil cmpgci cmpgrd cmpgrp cmpita cmpitm cmplab cmplbl cmplot cmpmsk cmpou cmppos cmpsat cmpsup cmptit cmptra cmpusr eezmpa mpex01 mpex02 mpex03 mpex04 mpex05 mpex06 mpex07 mpex08 mpex09 mpex10 mpex11 mpex12 mpex13 mpex14 mpex15 mpexfi tezmap tezmpa tezmpb c_mpex05 c_eezmpa c_eezmpb </p>
<p> <i>FIELD FLOW Examples:</i> </p>
<p> ffex00 ffex01 ffex02 ffex03 ffex04 ffex05 fcover fstream stex01 stex02 stex03 vvex01 vvex02 vvex03 c_ffex03 c_vvex03 </p>
<p> <i>FITGRID Examples:</i> </p>
<p> ftex01 ftex02 ftex03 ftex04 ftex05 ftex06 c_ftex01 c_ftex02 c_ftex03 c_ftex04 c_ftex05 c_ftex06 </p>
<p> <i>GFLASH Example:</i> </p>
<p> tgflas c_tgflas </p>
<p> <i>GKS Examples:</i> </p>
<p> fcell fcell0 fgke01 fgke02 fgke03 fgke04 fgkgpl fgkgpm fgkgtx fgklnclr fgklnwth fcirc fgpm01 pgkex01 pgkex02 pgkex03 pgkex04 pgkex05 pgkex06 pgkex07 pgkex08 pgkex09 pgkex10 pgkex11 pgkex12 pgkex13 pgkex14 pgkex15 pgkex16 pgkex17 pgkex18 pgkex19 pgkex20 pgkex21 pgkex22 pgkex23 pgkex24 pgkex25 pgkex26 pgkex27 c_gtxpac c_pgkex21 </p>
<p> <i>GRIDALL Example:</i> </p>
<p> ccpga tgrida c_tgrida </p>
<p> <i>HALFTONE Example:</i> </p>
<p> thafto </p>
<p> <i>HISTOGRAM Examples:</i> </p>
<p> thstgr thstmv c_thstmv </p>
<p> <i>ISOSRFHR Example:</i> </p>
<p> tisohr </p>
<p> <i>ISOSURFACE Examples:</i> </p>
<p> fisissrf fispwrzi tisosr tpwrzi c_tisosr </p>
<p> <i>LABELBAR Examples:</i> </p>
<p> elblba tlblba clbfil clbbar clblbr c_elblba </p>
<p> <i>NATGRID Examples:</i> </p>
<p> nnex01 nnex01d nnex02 nnex03 nnex04 nnex05 nnex06 nnex07 nnex08 nnex09 c_nnex01 c_nnex01d c_nnex02 c_nnex03 c_nnex06 </p>
<p> <i>NGMATH Examples:</i> </p>
<p> csex01 csex02 csex03 csex04 csex05 csex06 csex07 cssex01 cssex02 cssex03 dsex01 dsex01d dsex02 dsex03 dsex04 dsex05 dsex06 ftex01 ftex02 ftex03 ftex04 ftex05 ftex06 nnex01 nnex01d nnex02 nnex03 nnex04 nnex05 nnex06 nnex07 nnex08 nnex09 shex01 shex02 shex03 c_csex01 c_csex02 c_csex03 c_csex04 c_csex05 c_csex06 c_csex07 c_cssex01 c_cssex02 c_cssex03 c_dsex01 c_dsex01d c_dsex02 c_dsex03 c_dsex04 c_dsex05 c_dsex06 c_ftex01 c_ftex02 c_ftex03 c_ftex04 c_ftex05 c_ftex06 c_nnex01 c_nnex01d c_nnex02 c_nnex03 c_nnex06 c_shex01 c_shex02 c_shex03 </p>
<p> <i>NGMISC Examples:</i> </p>
<p> fngngdts fngwsym c_fngwsym </p>
<p> <i>PLOTCHAR Examples:</i> </p>
<p> epltch fpchiqu fpcloqu fpcfonts tpltch c_epltch </p>
<p> <i>POLYPACK Examples:</i> </p>
<p> ppex01 tppack c_ppex01 </p>
<p> <i>PWRITE FAMILY Examples:</i> </p>
<p> tpwrtx tpwry </p>
<p> <i>SCROLLED TITLE Examples:</i> </p>
<p> fslfont slex01 slex02 tstitl c_slex01 </p>
<p> <i>SETER Examples:</i> </p>
<p> tseter </p>
<p> <i>SHGRID Examples:</i> </p>
<p> shex01 shex02 shex03 c_shex01 c_shex02 c_shex03 </p>
<p> <i>SOFTFILL Examples:</i> </p>
<p> fsfsgfa fsfwrld sfex01 sfex02 tsoftf c_sfex02 </p>
<p> <i>SPPS Examples:</i> </p>
<p> fcoord fcoord1 fcoord2 fspcurve fspline fsppoint fspponts splogy sprevx c_fcoord2 </p>
<p> <i>STREAMLINES Examples:</i> </p>
<p> fstream ffex00 ffex01 ffex03 ffex04 stex01 stex02 stex03 tstrml c_ffex03 </p>
<p> <i>SURFACE Examples:</i> </p>
<p> fsrezsrf fsrpwrzs fsrsrfac srex01 tsrfac tpwrzs c_srex01 </p>
<p> <i>TDPACK Examples:</i> </p>
<p> tdex01 tdex02 tdex03 tdex04 tdex05 tdex06 tdex07 tdex08 c_tdex01 c_tdex03 </p>
<p> <i>THREED Examples:</i> </p>
<p> fthex01 fthex02 fthex03 fthex04 fthex05 tthree tpwrzt c_fthex01 </p>
<p> <i>VECTORS Examples:</i> </p>
<p> ffex00 ffex01 ffex02 ffex05 fcover tvelvc vvex01 vvex02 vvex03 c_vvex03 </p>
<p> <i>WEATHER MAP Examples:</i> </p>
<p> wmex01 wmex02 wmex03 wmex04 wmex05 wmex06 wmex07 wmex08 wmex09 wmex10 wmex11 wmex12 wmex13 wmex14 wmex15 c_wmex09 </p>
<p> <i>Miscellaneous Examples:</i> </p>
<p> bnchmk example ncargworld </p>
<p> <i>X11 Examples:</i> </p>
<p> fgke01 fgke04 c_xwndws </p>
<h2>SEE ALSO</h2>
<p> Online: <code>ncargf77(1NCARG),</code> <code>ncargcc(1NCARG),</code> <code>ncargfile(1NCARG),</code> <code>ng4ex(1NCARG),</code> <code>ncarg_cbind(5NCARG),</code> <code>ncargintro(5NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
