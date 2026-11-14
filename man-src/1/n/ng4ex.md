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
<dt><i>-A</i></p>
<dd> Generate all available examples. </p>
<dt><i>-C</i></p>
<dd> Generate all C examples. </p>
<dt><i>-Fortran</i></p>
<dd> Generate all Fortran examples. </p>
<dt><i>-NCL</i></p>
<dd> Generate all NCL examples. </p>
<dt><i>-cdf</i></p>
<dd> Generate all the examples that use netCDF files. For the C and Fortran examples, this option requires that you have the netCDF library installed on your system. </p>
<dt><i>-gui</i></p>
<dd> Generate all GUI examples. This option requires that you have the Motif libraries on your system. </p>
<dt><i>-anno</i></p>
<dd> Generate all annotation examples. </p>
<dt><i>-W</p>
<dd> Specify the workstation type. This argument can only be specified as a string. Some examples are meant to display to the X workstation, to an NCGM file, or to a PostScript file only, in which case this option may be ignored. You cannot specify more than one workstation type. If you don&#8217;t specify one, then a default one will be used. The following workstation_type strings are valid:</p>
<dt> ncgm</p>
<dd> &#8211; NCGM file</p>
<dt> x11</p>
<dd> &#8211; X11 window</p>
<dt> ps</p>
<dd> &#8211; PostScript file</p>
<dt> pdf</p>
<dd> &#8211; PDF file </p>
<dt>-app</i></p>
<dd> Generate all the app Fortran, C, and NCL examples that show how to do specific things with resources. </p>
<dt><i>-basic</i></p>
<dd> Generate all the basic Fortran, C, and NCL examples that relate to the basic examples discussed in the Quick Start Guide. </p>
<dt><i>-contourplot</i></p>
<dd> Generate all Fortran, C, and NCL ContourPlot examples. </p>
<dt><i>-csagrid</i></p>
<dd> Generate all NCL Csagrid examples. </p>
<dt><i>-cssgrid</i></p>
<dd> Generate all NCL Cssgrid examples. </p>
<dt><i>-dsgrid</i></p>
<dd> Generate all Fortran, C, and NCL Dsgrid examples. </p>
<dt><i>-fitgrid</i></p>
<dd> Generate all NCL Natgrid examples. </p>
<dt><i>-labelbar</i></p>
<dd> Generate all Fortran, C, and NCL Labelbar examples. </p>
<dt><i>-legend</i></p>
<dd> Generate all Fortran, C, and NCL Legend examples. </p>
<dt><i>-natgrid</i></p>
<dd> Generate all Fortran, C, and NCL Natgrid examples. </p>
<dt><i>-primitives</i></p>
<dd> Generate all Fortran, C, and NCL GraphicStyle examples. </p>
<dt><i>-mapplot</i></p>
<dd> Generate all Fortran, C, and NCL MapPlot examples. </p>
<dt><i>-ngmath</i></p>
<dd> Generate all Fortran, C, and NCL Ngmath examples. </p>
<dt><i>-shgrid</i></p>
<dd> Generate all NCL Shgrid examples. </p>
<dt><i>-streamlineplot</i></p>
<dd> Generate all Fortran, C, and NCL StreamlinePlot examples. </p>
<dt><i>-textitem</i></p>
<dd> Generate all Fortran, C, and NCL TextItem examples. </p>
<dt><i>-tickmark</i></p>
<dd> Generate all Fortran, C, and NCL TickMark examples. </p>
<dt><i>-title</i></p>
<dd> Generate all Fortran, C, and NCL Title examples. </p>
<dt><i>-vectorplot</i></p>
<dd> Generate all Fortran, C, and NCL VectorPlot examples. </p>
<dt><i>-xyplot</i></p>
<dd> Generate all Fortran, C, and NCL xyPlot examples. </p>
<dt><i>-gsun</i></p>
<dd> Generate all the GSUN examples (NCL scripts only). </p>
<dt><i>-list</i></p>
<dd> Specifies that the names of the selected examples should be echoed to the screen instead of being copied or generated. This option must be used with one of the other options that selects a particular subset of examples. For example, if you want to see a list of all the available examples, then use <i>-list</i> in conjunction with the <i>-A</i> option. If you want to see a list of all the ContourPlot examples, then use <i>-list</i> with the <i>-contourplot</i> option (and so on). </p>
<dt><i>-clean</i></p>
<dd> Remove everything but the &quot;.ncgm&quot; file. </p>
<dt><i>-n</i></p>
<dd> Specifies that the example should just be copied, and not linked or executed. </p>
<dt><i>name(s)</i></p>
<dd> Name(s) of example programs to generate.</dl>
<h2>EXAMPLES AVAILABLE</h2>
<p> Please notice that the C examples end with the letter &#8216;c&#8217;, the Fortran examples end with the letter &#8216;f&#8217;, and NCL examples with the letter &#8216;n&#8217;.</p>
<dl>
<dt>ap01c,ap01f,ap01n</p>
<dd> Demonstrates various ways to use resource files.</p>
<dt>basic01c,basic01f,basic01n</p>
<dd> Demonstrates how to draw a contour plot using mostly defaults. No data is used in this example.</p>
<dt>basic02c,basic02f,basic02n</p>
<dd> Demonstrates how to set the view port and how to produce multiple plots on a single frame.</p>
<dt>basic03c,basic03f,basic03n</p>
<dd> Demonstrates how to create a scalar data object, set resources using a resource file, set resources during object creation, and set resources after object creation.</p>
<dt>basic04c,basic04f,basic04n</p>
<dd> Demonstrates how to select and change the workstation device for drawing your output to an NCGM file or an X workstation window.</p>
<dt>basic05c,basic05f,basic05n</p>
<dd> Demonstrates how to read and manipulate colormaps.</p>
<dt>basic06c,basic06f,basic06n</p>
<dd> Demonstrates how to position objects on an output device and how to change their sizes.</p>
<dt>basic07c,basic07f,basic07n</p>
<dd> Demonstrates creating three simultaneous workstations.</p>
<dt>basic08c,basic08f,basic08n</p>
<dd> Demonstrates use of a procedure that limits a plot, including annotations that extend outside the plot viewport, to a pre-defined bounding box within NDC space.</p>
<dt>basic09c,basic09f,basic09n</p>
<dd> Lists all the fonts with their number, name, and what the font looks like.</p>
<dt>cn01c,cn01f,cn01n</p>
<dd> Shows all the default settings for the ContourPlot resources using a simple data set.</p>
<dt>cn02c,cn02f,cn02n</p>
<dd> Demonstrates basic features of the ContourPlot object.</p>
<dt>cn03c,cn03f,cn03n</p>
<dd> Demonstrates basic features of the ContourPlot object. The first frame emulates the contour plot drawn in cn01.</p>
<dt>cn04c,cn04f,cn04n</p>
<dd> Emulates the output of the ncargex example &quot;cpex02&quot;.</p>
<dt>cn05c,cn05f,cn05n</p>
<dd> Demonstrates how to create a map plot animation with a contour overlay and labelbar annotation.</p>
<dt>cn06c,cn06f,cn06n</p>
<dd> Shows how to read a netCDF file and produce a series of temperature contour plots.</p>
<dt>cn07c,cn07f,cn07n</p>
<dd> Shows how to read a netCDF file and produce a series of contour plots.</p>
<dt>cn08c,cn08f,cn08n</p>
<dd> Shows how to read a netCDF file and draw a vertical profiles of temperature for longitude separated by 5 degrees.</p>
<dt>cn09c,cn09f,cn09n</p>
<dd> Shows how to read a netCDF file and produce a series of surface pressure contour plots.</p>
<dt>cn10f,cn10c,cn10n</p>
<dd> Demonstrates how to read a netCDF file and produce three contour plots, an xyplot, and a map plot.</p>
<dt>cn11c,cn11f</p>
<dd> Demonstrates how to combine LLU and HLU calls.</p>
<dt>cn12c,cn12f,cn12n</p>
<dd> Emulates example &quot;cpex08&quot; and draws a filled contour plot over a map of Africa with a labelbar.</p>
<dt>cn13c,cn13f,cn13n</p>
<dd> Emulates example &quot;mpex10&quot; and draws a raster contour plot over a map using inverse map transformations.</p>
<dt>cn14c,cn14f,cn14n</p>
<dd> Shows how to do a contour/map overlay with tick marks showing the lat/lon locations.</p>
<dt>cn15c,cn15f,cn15n</p>
<dd> Shows how to combine contour plot and xy plot on a single frame. Also shows how to do multiple workstation outputs, and how to position your PostScript output on the page.</p>
<dt>cn16c,cn16f,cn16n</p>
<dd> Shows how to combine a vector fill contour plot, a raster contour plot, and a map plot on a single frame.</p>
<dt>cn17c,cn17f,cn17n</p>
<dd> Shows how to restrict a contour plot to a certain area over a satellite projection, how to label the US states with AnnoManager, how to use NhlDataPoly{line,marker} to draw lines/markers on a map projection, and how to mix LLUs/HLUs to draw text in the map projection. The NCL version doesn&#8217;t have the LLU/HLU part.</p>
<dt>lb01c,lb01f,lb01n</p>
<dd> Shows all the default settings for the LabelBar resources.</p>
<dt>lb02c,lb02f,lb02n</p>
<dd> Shows how to modify some of the default resources to create a solid filled set of boxes.</p>
<dt>lg01c,lg01f,lg01n</p>
<dd> Shows all the default settings for the Legend resources.</p>
<dt>lg02c,lg02f,lg02n</p>
<dd> Shows how to modify some of the default resources to create a legend of five markers.</p>
<dt>lg03c,lg03f,lg03n</p>
<dd> Shows how to create a legend of five lines.</p>
<dt>pr01c,pr01f,pr01n</p>
<dd> Demonstrates basic GraphicStyle capabilities.</p>
<dt>pr02c,pr02f,pr02n</p>
<dd> Demonstrates GraphicStyle capabilities and how to some GS resources.</p>
<dt>pr03c,pr03f,pr03n</p>
<dd> Demonstrates graphics primitives drawn in NDC space and how clipping works.</p>
<dt>pr04c,pr04f,pr04n</p>
<dd> Demonstrates graphics primitives drawn into an IrregularPlot object.</p>
<dt>pr05c,pr05f,pr05n</p>
<dd> Demonstrates overlaying graphics primitives on a MapPlot.</p>
<dt>mp01c,mp01f,mp01n</p>
<dd> Demonstrates basic MapPlot capabilities.</p>
<dt>mp02c,mp02f,mp02n</p>
<dd> Demonstrates individual control of MapPlot areas.</p>
<dt>mp03c,mp03f,mp03n</p>
<dd> Demonstrates MapPlot masking; loosely emulates the ncargex example &quot;colcon&quot;.</p>
<dt>mp04c,mp04f,mp04n</p>
<dd> Illustrates the use of AnnoManager objects with MapPlot objects.</p>
<dt>mp05c,mp05f,mp05n</p>
<dd> Shows how to create the ten different map projections.</p>
<dt>mp06c,mp06f,mp06n</p>
<dd> Shows how to draw county lines in the United States.</p>
<dt>mp07c,mp07f,mp07n</p>
<dd> Shows how to use high resolution RANGS/GSHHS map database.</p>
<dt>nm01c,nm01f,nm01n</p>
<dd> Simple example of natural neighbor linear interpolation.</p>
<dt>nm02c,nm02f,nm02n</p>
<dd> Simple example of natural neighbor linear regridding.</p>
<dt>nm03c,nm03f,nm03n</p>
<dd> Shows how to retrieve aspects and slopes of an interpolation.</p>
<dt>nm04c,nm04f,nm04n</p>
<dd> Shows a simple 3D interpolation.</p>
<dt>nm05c,nm05f,nm05n</p>
<dd> Shows how to vary the exponent of the distances in a simple 2D interpolation..</p>
<dt>nm06c,nm06f,nm06n</p>
<dd> Smoothing in a simple 2D interpolation.</p>
<dt>nm07n</p>
<dd> Illustrates use of ftcurv, ftcurv, and ftcurvi.</p>
<dt>nm08n</p>
<dd> Illustrates use of ftcurvp and ftcurvpi.</p>
<dt>nm09n</p>
<dd> Illustrates use of ftcurvs and ftcurvps.</p>
<dt>nm10n</p>
<dd> Illustrates use of ftkurv and ftkurvd.</p>
<dt>nm11n</p>
<dd> Illustrates use of ftkurvp and ftkurvpd.</p>
<dt>nm12n</p>
<dd> Illustrates use of ftsurf.</p>
<dt>nm13n</p>
<dd> Illustrates the use of csa1s.</p>
<dt>nm14n</p>
<dd> Illustrates the effect of weighting the input points using csa1xs.</p>
<dt>nm15n</p>
<dd> Illustrates extrapolation into data sparse regions using csa1xs.</p>
<dt>nm16n</p>
<dd> Illustrates two-dimensional approximation and second-order mixed partial using csa2s and csa2xs.</p>
<dt>nm17n,nm18n</p>
<dd> Illustrates the use of csa3s.</p>
<dt>nm19n</p>
<dd> Illustrates the use of csa2ls.</p>
<dt>nm20n</p>
<dd> Illustrates the use of triangulation and Voronoi diagram capabilities of the cssgrid package.</p>
<dt>nm21n</p>
<dd> Illustrates the use of the interpolation capabilities of the cssgrid package.</p>
<dt>nm22n</p>
<dd> Illustrates the use of shgrid. cssgrid package.</p>
<dt>st01c,st01f,st01n</p>
<dd> Demonstrates basic StreamlinePlot example.</p>
<dt>st02c,st02f,st02n</p>
<dd> Demonstrates line-drawn streamline arrows and some basic resources.</p>
<dt>st03c,st03f,st03n</p>
<dd> Shows how to overlay a StreamlinePlot on a map projection.</p>
<dt>st04c,st04f,st04n</p>
<dd> Shows a StreamlinePlot of wind vector data over a MapPlot.</p>
<dt>ti01c,ti01f,ti01n</p>
<dd> Shows all the default settings for the Title resources which results in a blank plot.</p>
<dt>ti02c,ti01f,ti01n</p>
<dd> Turns on the main, x-axis, and y-axis strings to produce a plot with three titles.</p>
<dt>ti03c,ti03f,ti03n</p>
<dd> Shows how to change resources to get high quality filled and colored titles.</p>
<dt>tm01c,tm01f,tm01n</p>
<dd> Shows all the default settings for the TickMark resources.</p>
<dt>tm02c,tm02f,tm02n</p>
<dd> Shows how to modify the resources to create tick marks on the axes.</p>
<dt>tm03c,tm03f,tm03n</p>
<dd> Shows how to modify the resources to change the scaling and the tick mark labels.</p>
<dt>tx01c,tx01f,tx01n</p>
<dd> Shows all the default settings for the TextItem resources.</p>
<dt>tx02c,tx02f,tx02n</p>
<dd> Shows how to modify default resources to produce a text string.</p>
<dt>tx03c,tx03f,tx03n</p>
<dd> Uses the same resources as example &quot;tx02c&quot;, except 114 frames are produced with varying background colors.</p>
<dt>tx04c,tx04f,tx04n</p>
<dd> Shows how to use the TextItem object of the HLU library.</p>
<dt>tx05c,tx05f,tx05n</p>
<dd> Demonstrates the TextItem object with text having various heights and various angles.</p>
<dt>tx06c,tx06f,tx06n</p>
<dd> Demonstrates TextItem text justifications.</p>
<dt>tx07c,tx07f,tx07n</p>
<dd> Demonstrates TextItem text spacings and aspect ratios.</p>
<dt>tx08c,tx08f,tx08n</p>
<dd> Simple Annotation example.</p>
<dt>vc01c,vc01f,vc01n</p>
<dd> Basic VectorPlot example.</p>
<dt>vc02c,vc02f,vc02n</p>
<dd> Demonstrates line-drawn vector arrows and the use of some basic VectorPlot resources.</p>
<dt>vc03c,vc03f,vc03n</p>
<dd> Manipulates the FillArrow resources to demonstrate some of the possible stylistic variations on the appearance of filled vector arrows.</p>
<dt>vc04c,vc04f,vc04n</p>
<dd> Demonstrates how to rotate a VectorPlot 90 degrees while preserving the original relationship of the data elements.</p>
<dt>vc05c,vc05f,vc05n</p>
<dd> Demonstrates how to overlay a VectorPlot on a MapPlot.</p>
<dt>vc06c,vc06f,vc06n</p>
<dd> Demonstrates how to use a scalarfield to determine the color of the vector arrow fill.</p>
<dt>vc07c,vc07f,vc07n</p>
<dd> Emulates the LLU example &quot;fcover&quot;; shows how to overlay contours and vectors on a MapPlot.</p>
<dt>vc08c,vc08f,vc08n</p>
<dd> Plots wind vectors at a grid stride of 3. Vectors are colored by wind speed.</p>
<dt>vc09c,vc09f,vc09n</p>
<dd> Plots an animation of the January 1996 snow storm using wind vectors colored by temperature over a pressure field contour plot.</p>
<dt>xy01c,xy01f,xy01n</p>
<dd> Shows all the default resources for an xyPlot object.</p>
<dt>xy02c,xy02f,xy02n</p>
<dd> The same as example xy01c, only with some of the X and Y axis resources tweaked.</p>
<dt>xy03c,xy03f,xy03n</p>
<dd> The same as example xy01c, but with the data modified a little, and the line resources tweaked.</p>
<dt>xy04c,xy04f,xy04n</p>
<dd> Demonstrates how to create an xyPlot with multiple lines. Some of the line resources are tweaked.</p>
<dt>xy05c,xy05f,xy05n</p>
<dd> Demonstrates how to create an XyPlot with multiple lines, using multiple data items (except for xy05c, which uses the CoordArrTable object).</p>
<dt>xy06c,xy06f,xy06n</p>
<dd> Demonstrates how to read in netCDF files to generate various xy plots.</p>
<dt>xy07c,xy07f,xy07n</p>
<dd> Demonstrates how to draw a &quot;scattergram&quot;.</p>
<dt>xy08c,xy08f,xy08n</p>
<dd> Shows how to use irregular points to change the transformation of your plot.</p>
<dt>xy09c,xy09f,xy09n</p>
<dd> Shows how to create different kinds of axes.</p>
<dt>xy10c,xy10f,xy10n</p>
<dd> Shows how to overlay an XyPlot on a MapPlot.</p>
<dt>xy11c,xy11f,xy11n</p>
<dd> Demonstrates how to display an xyPlot to an X Window, and then copy it to a meta file.</p>
<dt>xy12c</p>
<dd> Demonstrates how to incorporate the HLU library with a GUI. It uses an X/Motif interface, and also allows the user to copy frames from the X Window to a meta file.</p>
<dt>xy13c</p>
<dd> Shows how to interactively retrieve data values from a plot by pointing and clicking on the plot.</p>
<dt>xy14c,xy14f,xy14n</p>
<dd> Demonstrates the data manipulation capabilities of NCL.</p>
<dt>xy15c,xy15f,xy15n</p>
<dd> Demonstrates the creation of a set of four stacked XyPlots.</p>
<dt>xy16c,xy16f,xy16n</p>
<dd> Demonstrates how to draw three different xy lines on the same plot, but with different axis scales.</p>
<dt>xy17c,xy17f,xy17n</p>
<dd> Demonstrates how to stack three xy plots.</dl>
<h2>SEE ALSO</h2>
<p> ncargex(1NCARG)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2000<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
