---
title: "ng4ex(1)"
name: "ng4ex"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ng4ex/"
description: "ng4ex – NCAR Graphics High Level Utilities Example Programs"
---

<h2>NAME</h2>
<p> ng4ex &#8211; NCAR Graphics High Level Utilities Example Programs</p>
<h2>SYNOPSIS</h2>
<p> <code>ng4ex</code> [<i>-A</i>] [<i>-C</i>] [<i>-Fortran</i>] [<i>-NCL</i>] [<i>-cdf</i>] [<i>-csagrid</i>] [<i>-cssgrid</i>] [<i>-gui</i>] [<i>-anno</i>] [<i>-gsun</i>] [<code>-W workstation_type</code>] [<i>-app</i>] [<i>-basic</i>] [<i>-contourplot</i>] [<i>-fitgrid</i>] [<i>-labelbar</i>] [<i>-legend</i>] [<i>-primitives</i>] [<i>-mapplot</i>] [<i>-natgrid</i>] [<i>-ngmath</i>] [<i>-streamplot</i>] [<i>-shgrid</i>] [<i>-textitem</i>] [<i>-tickmark</i>] [<i>-title</i>] [<i>-vectorplot</i>] [<i>-xyplot</i>] [<i>-list</i>] [<i>-clean</i>] [<i>-n</i>] <i>name &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>ng4ex</i> provides the user with access to several C, Fortran, and NCL examples illustrating the use of the NCAR Graphics HLUs (High Level Utilities) and NCL. Please note that NCL is not available for Cray systems. </p>
<p> <i>ng4ex</i> copies the source code for the specified example(s) into the current directory and then compiles, links, and executes the example (if it&#8217;s a Fortran or C program) or runs NCL on it (if it&#8217;s an NCL script file). Depending on the example, the output may be sent to an NCGM (NCAR Graphics Metafile) file and/or displayed to an X window on your screen. You must be running X and have your DISPLAY environment set correctly in order for the X window examples to execute properly. </p>
<p> If the requested example creates an NCGM file, it will have the same name as the example, suffixed with &quot;.ncgm&quot;. An option allows you to request that only the source code be copied to your directory, without compiling or running the example. Another option allows you to request that only the NCGM file be left in your directory and that all other files created by <code>ng4ex</code> be deleted. The argument <i>name</i> may be selected from the lists that appear below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-A</i></dt>
<dd> Generate all available examples. </dd>
<dt><i>-C</i></dt>
<dd> Generate all C examples. </dd>
<dt><i>-Fortran</i></dt>
<dd> Generate all Fortran examples. </dd>
<dt><i>-NCL</i></dt>
<dd> Generate all NCL examples. </dd>
<dt><i>-cdf</i></dt>
<dd> Generate all the examples that use netCDF files. For the C and Fortran examples, this option requires that you have the netCDF library installed on your system. </dd>
<dt><i>-gui</i></dt>
<dd> Generate all GUI examples. This option requires that you have the Motif libraries on your system. </dd>
<dt><i>-anno</i></dt>
<dd> Generate all annotation examples. </dd>
<dt><i>-W</dt>
<dd> Specify the workstation type. This argument can only be specified as a string. Some examples are meant to display to the X workstation, to an NCGM file, or to a PostScript file only, in which case this option may be ignored. You cannot specify more than one workstation type. If you don&#8217;t specify one, then a default one will be used. The following workstation_type strings are valid:</dd>
<dt> ncgm</dt>
<dd> &#8211; NCGM file</dd>
<dt> x11</dt>
<dd> &#8211; X11 window</dd>
<dt> ps</dt>
<dd> &#8211; PostScript file</dd>
<dt> pdf</dt>
<dd> &#8211; PDF file </dd>
<dt>-app</i></dt>
<dd> Generate all the app Fortran, C, and NCL examples that show how to do specific things with resources. </dd>
<dt><i>-basic</i></dt>
<dd> Generate all the basic Fortran, C, and NCL examples that relate to the basic examples discussed in the Quick Start Guide. </dd>
<dt><i>-contourplot</i></dt>
<dd> Generate all Fortran, C, and NCL ContourPlot examples. </dd>
<dt><i>-csagrid</i></dt>
<dd> Generate all NCL Csagrid examples. </dd>
<dt><i>-cssgrid</i></dt>
<dd> Generate all NCL Cssgrid examples. </dd>
<dt><i>-dsgrid</i></dt>
<dd> Generate all Fortran, C, and NCL Dsgrid examples. </dd>
<dt><i>-fitgrid</i></dt>
<dd> Generate all NCL Natgrid examples. </dd>
<dt><i>-labelbar</i></dt>
<dd> Generate all Fortran, C, and NCL Labelbar examples. </dd>
<dt><i>-legend</i></dt>
<dd> Generate all Fortran, C, and NCL Legend examples. </dd>
<dt><i>-natgrid</i></dt>
<dd> Generate all Fortran, C, and NCL Natgrid examples. </dd>
<dt><i>-primitives</i></dt>
<dd> Generate all Fortran, C, and NCL GraphicStyle examples. </dd>
<dt><i>-mapplot</i></dt>
<dd> Generate all Fortran, C, and NCL MapPlot examples. </dd>
<dt><i>-ngmath</i></dt>
<dd> Generate all Fortran, C, and NCL Ngmath examples. </dd>
<dt><i>-shgrid</i></dt>
<dd> Generate all NCL Shgrid examples. </dd>
<dt><i>-streamlineplot</i></dt>
<dd> Generate all Fortran, C, and NCL StreamlinePlot examples. </dd>
<dt><i>-textitem</i></dt>
<dd> Generate all Fortran, C, and NCL TextItem examples. </dd>
<dt><i>-tickmark</i></dt>
<dd> Generate all Fortran, C, and NCL TickMark examples. </dd>
<dt><i>-title</i></dt>
<dd> Generate all Fortran, C, and NCL Title examples. </dd>
<dt><i>-vectorplot</i></dt>
<dd> Generate all Fortran, C, and NCL VectorPlot examples. </dd>
<dt><i>-xyplot</i></dt>
<dd> Generate all Fortran, C, and NCL xyPlot examples. </dd>
<dt><i>-gsun</i></dt>
<dd> Generate all the GSUN examples (NCL scripts only). </dd>
<dt><i>-list</i></dt>
<dd> Specifies that the names of the selected examples should be echoed to the screen instead of being copied or generated. This option must be used with one of the other options that selects a particular subset of examples. For example, if you want to see a list of all the available examples, then use <i>-list</i> in conjunction with the <i>-A</i> option. If you want to see a list of all the ContourPlot examples, then use <i>-list</i> with the <i>-contourplot</i> option (and so on). </dd>
<dt><i>-clean</i></dt>
<dd> Remove everything but the &quot;.ncgm&quot; file. </dd>
<dt><i>-n</i></dt>
<dd> Specifies that the example should just be copied, and not linked or executed. </dd>
<dt><i>name(s)</i></dt>
<dd> Name(s) of example programs to generate.</dd></dl>
<h2>EXAMPLES AVAILABLE</h2>
<p> Please notice that the C examples end with the letter &#8216;c&#8217;, the Fortran examples end with the letter &#8216;f&#8217;, and NCL examples with the letter &#8216;n&#8217;.</p>
<dl>
<dt>ap01c,ap01f,ap01n</dt>
<dd> Demonstrates various ways to use resource files.</dd>
<dt>basic01c,basic01f,basic01n</dt>
<dd> Demonstrates how to draw a contour plot using mostly defaults. No data is used in this example.</dd>
<dt>basic02c,basic02f,basic02n</dt>
<dd> Demonstrates how to set the view port and how to produce multiple plots on a single frame.</dd>
<dt>basic03c,basic03f,basic03n</dt>
<dd> Demonstrates how to create a scalar data object, set resources using a resource file, set resources during object creation, and set resources after object creation.</dd>
<dt>basic04c,basic04f,basic04n</dt>
<dd> Demonstrates how to select and change the workstation device for drawing your output to an NCGM file or an X workstation window.</dd>
<dt>basic05c,basic05f,basic05n</dt>
<dd> Demonstrates how to read and manipulate colormaps.</dd>
<dt>basic06c,basic06f,basic06n</dt>
<dd> Demonstrates how to position objects on an output device and how to change their sizes.</dd>
<dt>basic07c,basic07f,basic07n</dt>
<dd> Demonstrates creating three simultaneous workstations.</dd>
<dt>basic08c,basic08f,basic08n</dt>
<dd> Demonstrates use of a procedure that limits a plot, including annotations that extend outside the plot viewport, to a pre-defined bounding box within NDC space.</dd>
<dt>basic09c,basic09f,basic09n</dt>
<dd> Lists all the fonts with their number, name, and what the font looks like.</dd>
<dt>cn01c,cn01f,cn01n</dt>
<dd> Shows all the default settings for the ContourPlot resources using a simple data set.</dd>
<dt>cn02c,cn02f,cn02n</dt>
<dd> Demonstrates basic features of the ContourPlot object.</dd>
<dt>cn03c,cn03f,cn03n</dt>
<dd> Demonstrates basic features of the ContourPlot object. The first frame emulates the contour plot drawn in cn01.</dd>
<dt>cn04c,cn04f,cn04n</dt>
<dd> Emulates the output of the ncargex example &quot;cpex02&quot;.</dd>
<dt>cn05c,cn05f,cn05n</dt>
<dd> Demonstrates how to create a map plot animation with a contour overlay and labelbar annotation.</dd>
<dt>cn06c,cn06f,cn06n</dt>
<dd> Shows how to read a netCDF file and produce a series of temperature contour plots.</dd>
<dt>cn07c,cn07f,cn07n</dt>
<dd> Shows how to read a netCDF file and produce a series of contour plots.</dd>
<dt>cn08c,cn08f,cn08n</dt>
<dd> Shows how to read a netCDF file and draw a vertical profiles of temperature for longitude separated by 5 degrees.</dd>
<dt>cn09c,cn09f,cn09n</dt>
<dd> Shows how to read a netCDF file and produce a series of surface pressure contour plots.</dd>
<dt>cn10f,cn10c,cn10n</dt>
<dd> Demonstrates how to read a netCDF file and produce three contour plots, an xyplot, and a map plot.</dd>
<dt>cn11c,cn11f</dt>
<dd> Demonstrates how to combine LLU and HLU calls.</dd>
<dt>cn12c,cn12f,cn12n</dt>
<dd> Emulates example &quot;cpex08&quot; and draws a filled contour plot over a map of Africa with a labelbar.</dd>
<dt>cn13c,cn13f,cn13n</dt>
<dd> Emulates example &quot;mpex10&quot; and draws a raster contour plot over a map using inverse map transformations.</dd>
<dt>cn14c,cn14f,cn14n</dt>
<dd> Shows how to do a contour/map overlay with tick marks showing the lat/lon locations.</dd>
<dt>cn15c,cn15f,cn15n</dt>
<dd> Shows how to combine contour plot and xy plot on a single frame. Also shows how to do multiple workstation outputs, and how to position your PostScript output on the page.</dd>
<dt>cn16c,cn16f,cn16n</dt>
<dd> Shows how to combine a vector fill contour plot, a raster contour plot, and a map plot on a single frame.</dd>
<dt>cn17c,cn17f,cn17n</dt>
<dd> Shows how to restrict a contour plot to a certain area over a satellite projection, how to label the US states with AnnoManager, how to use NhlDataPoly{line,marker} to draw lines/markers on a map projection, and how to mix LLUs/HLUs to draw text in the map projection. The NCL version doesn&#8217;t have the LLU/HLU part.</dd>
<dt>lb01c,lb01f,lb01n</dt>
<dd> Shows all the default settings for the LabelBar resources.</dd>
<dt>lb02c,lb02f,lb02n</dt>
<dd> Shows how to modify some of the default resources to create a solid filled set of boxes.</dd>
<dt>lg01c,lg01f,lg01n</dt>
<dd> Shows all the default settings for the Legend resources.</dd>
<dt>lg02c,lg02f,lg02n</dt>
<dd> Shows how to modify some of the default resources to create a legend of five markers.</dd>
<dt>lg03c,lg03f,lg03n</dt>
<dd> Shows how to create a legend of five lines.</dd>
<dt>pr01c,pr01f,pr01n</dt>
<dd> Demonstrates basic GraphicStyle capabilities.</dd>
<dt>pr02c,pr02f,pr02n</dt>
<dd> Demonstrates GraphicStyle capabilities and how to some GS resources.</dd>
<dt>pr03c,pr03f,pr03n</dt>
<dd> Demonstrates graphics primitives drawn in NDC space and how clipping works.</dd>
<dt>pr04c,pr04f,pr04n</dt>
<dd> Demonstrates graphics primitives drawn into an IrregularPlot object.</dd>
<dt>pr05c,pr05f,pr05n</dt>
<dd> Demonstrates overlaying graphics primitives on a MapPlot.</dd>
<dt>mp01c,mp01f,mp01n</dt>
<dd> Demonstrates basic MapPlot capabilities.</dd>
<dt>mp02c,mp02f,mp02n</dt>
<dd> Demonstrates individual control of MapPlot areas.</dd>
<dt>mp03c,mp03f,mp03n</dt>
<dd> Demonstrates MapPlot masking; loosely emulates the ncargex example &quot;colcon&quot;.</dd>
<dt>mp04c,mp04f,mp04n</dt>
<dd> Illustrates the use of AnnoManager objects with MapPlot objects.</dd>
<dt>mp05c,mp05f,mp05n</dt>
<dd> Shows how to create the ten different map projections.</dd>
<dt>mp06c,mp06f,mp06n</dt>
<dd> Shows how to draw county lines in the United States.</dd>
<dt>mp07c,mp07f,mp07n</dt>
<dd> Shows how to use high resolution RANGS/GSHHS map database.</dd>
<dt>nm01c,nm01f,nm01n</dt>
<dd> Simple example of natural neighbor linear interpolation.</dd>
<dt>nm02c,nm02f,nm02n</dt>
<dd> Simple example of natural neighbor linear regridding.</dd>
<dt>nm03c,nm03f,nm03n</dt>
<dd> Shows how to retrieve aspects and slopes of an interpolation.</dd>
<dt>nm04c,nm04f,nm04n</dt>
<dd> Shows a simple 3D interpolation.</dd>
<dt>nm05c,nm05f,nm05n</dt>
<dd> Shows how to vary the exponent of the distances in a simple 2D interpolation..</dd>
<dt>nm06c,nm06f,nm06n</dt>
<dd> Smoothing in a simple 2D interpolation.</dd>
<dt>nm07n</dt>
<dd> Illustrates use of ftcurv, ftcurv, and ftcurvi.</dd>
<dt>nm08n</dt>
<dd> Illustrates use of ftcurvp and ftcurvpi.</dd>
<dt>nm09n</dt>
<dd> Illustrates use of ftcurvs and ftcurvps.</dd>
<dt>nm10n</dt>
<dd> Illustrates use of ftkurv and ftkurvd.</dd>
<dt>nm11n</dt>
<dd> Illustrates use of ftkurvp and ftkurvpd.</dd>
<dt>nm12n</dt>
<dd> Illustrates use of ftsurf.</dd>
<dt>nm13n</dt>
<dd> Illustrates the use of csa1s.</dd>
<dt>nm14n</dt>
<dd> Illustrates the effect of weighting the input points using csa1xs.</dd>
<dt>nm15n</dt>
<dd> Illustrates extrapolation into data sparse regions using csa1xs.</dd>
<dt>nm16n</dt>
<dd> Illustrates two-dimensional approximation and second-order mixed partial using csa2s and csa2xs.</dd>
<dt>nm17n,nm18n</dt>
<dd> Illustrates the use of csa3s.</dd>
<dt>nm19n</dt>
<dd> Illustrates the use of csa2ls.</dd>
<dt>nm20n</dt>
<dd> Illustrates the use of triangulation and Voronoi diagram capabilities of the cssgrid package.</dd>
<dt>nm21n</dt>
<dd> Illustrates the use of the interpolation capabilities of the cssgrid package.</dd>
<dt>nm22n</dt>
<dd> Illustrates the use of shgrid. cssgrid package.</dd>
<dt>st01c,st01f,st01n</dt>
<dd> Demonstrates basic StreamlinePlot example.</dd>
<dt>st02c,st02f,st02n</dt>
<dd> Demonstrates line-drawn streamline arrows and some basic resources.</dd>
<dt>st03c,st03f,st03n</dt>
<dd> Shows how to overlay a StreamlinePlot on a map projection.</dd>
<dt>st04c,st04f,st04n</dt>
<dd> Shows a StreamlinePlot of wind vector data over a MapPlot.</dd>
<dt>ti01c,ti01f,ti01n</dt>
<dd> Shows all the default settings for the Title resources which results in a blank plot.</dd>
<dt>ti02c,ti01f,ti01n</dt>
<dd> Turns on the main, x-axis, and y-axis strings to produce a plot with three titles.</dd>
<dt>ti03c,ti03f,ti03n</dt>
<dd> Shows how to change resources to get high quality filled and colored titles.</dd>
<dt>tm01c,tm01f,tm01n</dt>
<dd> Shows all the default settings for the TickMark resources.</dd>
<dt>tm02c,tm02f,tm02n</dt>
<dd> Shows how to modify the resources to create tick marks on the axes.</dd>
<dt>tm03c,tm03f,tm03n</dt>
<dd> Shows how to modify the resources to change the scaling and the tick mark labels.</dd>
<dt>tx01c,tx01f,tx01n</dt>
<dd> Shows all the default settings for the TextItem resources.</dd>
<dt>tx02c,tx02f,tx02n</dt>
<dd> Shows how to modify default resources to produce a text string.</dd>
<dt>tx03c,tx03f,tx03n</dt>
<dd> Uses the same resources as example &quot;tx02c&quot;, except 114 frames are produced with varying background colors.</dd>
<dt>tx04c,tx04f,tx04n</dt>
<dd> Shows how to use the TextItem object of the HLU library.</dd>
<dt>tx05c,tx05f,tx05n</dt>
<dd> Demonstrates the TextItem object with text having various heights and various angles.</dd>
<dt>tx06c,tx06f,tx06n</dt>
<dd> Demonstrates TextItem text justifications.</dd>
<dt>tx07c,tx07f,tx07n</dt>
<dd> Demonstrates TextItem text spacings and aspect ratios.</dd>
<dt>tx08c,tx08f,tx08n</dt>
<dd> Simple Annotation example.</dd>
<dt>vc01c,vc01f,vc01n</dt>
<dd> Basic VectorPlot example.</dd>
<dt>vc02c,vc02f,vc02n</dt>
<dd> Demonstrates line-drawn vector arrows and the use of some basic VectorPlot resources.</dd>
<dt>vc03c,vc03f,vc03n</dt>
<dd> Manipulates the FillArrow resources to demonstrate some of the possible stylistic variations on the appearance of filled vector arrows.</dd>
<dt>vc04c,vc04f,vc04n</dt>
<dd> Demonstrates how to rotate a VectorPlot 90 degrees while preserving the original relationship of the data elements.</dd>
<dt>vc05c,vc05f,vc05n</dt>
<dd> Demonstrates how to overlay a VectorPlot on a MapPlot.</dd>
<dt>vc06c,vc06f,vc06n</dt>
<dd> Demonstrates how to use a scalarfield to determine the color of the vector arrow fill.</dd>
<dt>vc07c,vc07f,vc07n</dt>
<dd> Emulates the LLU example &quot;fcover&quot;; shows how to overlay contours and vectors on a MapPlot.</dd>
<dt>vc08c,vc08f,vc08n</dt>
<dd> Plots wind vectors at a grid stride of 3. Vectors are colored by wind speed.</dd>
<dt>vc09c,vc09f,vc09n</dt>
<dd> Plots an animation of the January 1996 snow storm using wind vectors colored by temperature over a pressure field contour plot.</dd>
<dt>xy01c,xy01f,xy01n</dt>
<dd> Shows all the default resources for an xyPlot object.</dd>
<dt>xy02c,xy02f,xy02n</dt>
<dd> The same as example xy01c, only with some of the X and Y axis resources tweaked.</dd>
<dt>xy03c,xy03f,xy03n</dt>
<dd> The same as example xy01c, but with the data modified a little, and the line resources tweaked.</dd>
<dt>xy04c,xy04f,xy04n</dt>
<dd> Demonstrates how to create an xyPlot with multiple lines. Some of the line resources are tweaked.</dd>
<dt>xy05c,xy05f,xy05n</dt>
<dd> Demonstrates how to create an XyPlot with multiple lines, using multiple data items (except for xy05c, which uses the CoordArrTable object).</dd>
<dt>xy06c,xy06f,xy06n</dt>
<dd> Demonstrates how to read in netCDF files to generate various xy plots.</dd>
<dt>xy07c,xy07f,xy07n</dt>
<dd> Demonstrates how to draw a &quot;scattergram&quot;.</dd>
<dt>xy08c,xy08f,xy08n</dt>
<dd> Shows how to use irregular points to change the transformation of your plot.</dd>
<dt>xy09c,xy09f,xy09n</dt>
<dd> Shows how to create different kinds of axes.</dd>
<dt>xy10c,xy10f,xy10n</dt>
<dd> Shows how to overlay an XyPlot on a MapPlot.</dd>
<dt>xy11c,xy11f,xy11n</dt>
<dd> Demonstrates how to display an xyPlot to an X Window, and then copy it to a meta file.</dd>
<dt>xy12c</dt>
<dd> Demonstrates how to incorporate the HLU library with a GUI. It uses an X/Motif interface, and also allows the user to copy frames from the X Window to a meta file.</dd>
<dt>xy13c</dt>
<dd> Shows how to interactively retrieve data values from a plot by pointing and clicking on the plot.</dd>
<dt>xy14c,xy14f,xy14n</dt>
<dd> Demonstrates the data manipulation capabilities of NCL.</dd>
<dt>xy15c,xy15f,xy15n</dt>
<dd> Demonstrates the creation of a set of four stacked XyPlots.</dd>
<dt>xy16c,xy16f,xy16n</dt>
<dd> Demonstrates how to draw three different xy lines on the same plot, but with different axis scales.</dd>
<dt>xy17c,xy17f,xy17n</dt>
<dd> Demonstrates how to stack three xy plots.</dd></dl>
<h2>SEE ALSO</h2>
<p> ncargex(1NCARG)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2000<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
