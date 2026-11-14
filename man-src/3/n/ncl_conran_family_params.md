---
title: "ncl_conran_family_params(3)"
name: "ncl_conran_family_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_conran_family_params/"
---

Conran_family_params - Includes a brief description of all Conran_family internal parameters. 

<h2>Description</h2>There are three Conran entries, CONRAN, CONRAQ, and CONRAS. CONRAN can be invoked in two ways. One generates smoothed contours, the other does not. CONRAQ is a quick version of the package which has a more limited set of options than the other entries. CONRAS is the super version of the package. 

 Parameters are set using the CONOP1, CONOP2, CONOP3, and CONOP4 entries. CONOP1 sets option switches, CONOP2 sets option switches and option related integer arguments, CONOP3 sets option switches and option related real arguments, and CONOP4 sets option switches and option related character arguments. This man page provides a functional overview of the parameters. See the man pages for the CONOPx entries for precise information on how to make the option setting calls. 

 All of the following parameters apply to normal, smooth, or super versions of the package. The inclusive set of Conran parameters and their switch defaults: 

 CONOP1 parameters (Switches) [16] 

 
DEF&nbsp;<wbr>(all options begin with defaults) 
EXT=OFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MES=ON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REP=OFF 
GRI=OFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PDV=OFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SCA=ON 
ITP=C1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PER=ON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TFR=ON 
LAB=ON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PMM=OFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TOP=OFF 
LOT=OFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PSL=OFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRI=OFF 

 CONOP2 parameters (Switches &amp; Integer args) [7] 

 
INT=OFF LSZ=OFF NCP=OFF SML=OFF 
SPD=OFF SSZ=OFF STL=OFF 

 CONOP3 parameters (Switches &amp; Real args) [7] 

 
CHL=OFF CIL=OFF CON=OFF DBP=OFF 
SDC=OFF SLD=OFF TEN=OFF 

 CONOP4 parameters (Switches &amp; Character args) [3] 

 
DAS=OFF FMT=OFF TLE=OFF 

 Parameters which are not available in CONRAQ, the quick version of the Conran_family: 

 DAS, DBP, LAB, LSZ, PMM, PSL, SDC, SLD, SML, TEN
<h2>Parameters which set option switches in calls to entry CONOP1:</h2><dl COMPACT><dt>DEF
<dd>This parameter provides a quick way to reset all parameters to their default values.
<dt>EXT
<dd>A parameter to set contour extrapolations. The default is to only plot within the boundaries of the convex hull defined by the user's data. To have the contours fill the rectangular area of the frame, set the EXT switch ON.
<dt>GRI
<dd>The parameter to display the grid. GRI is OFF by default. Note: If GRI=ON, the virtual grid will be superimposed over the contour plot. The X and Y tick intervals will be displayed under the map only if PER=ON. (See parameter PER)
<dt>ITP
<dd>Set the interpolation scheme. There are two schemes -- C1 surfaces and linear. The C1 method (ITP=C1) takes longer but will give the best results when the data is sparse (less than 100 points). The linear method (ITP=LIN) will produce a better plot when there is a dense data set. The default is a C1 surface.
<dt>LAB
<dd>This parameter determines whether to label the contours (LAB=ON) or not (LAB=OFF). The default value is to label the contours. (Does not apply to entry CONRAQ.)
<dt>LOT
<dd>The parameter to list options on the printer. The default value is to not display the options.
<dt>MES
<dd>The parameter to plot a message. The default is that a message is printed below the plot giving contour intervals and execution time in seconds. If PER or GRI is ON, the message also contains the X and Y tick intervals.
<dt>PDV
<dd>The parameter to plot the input data values. The default value is to not plot the input data.
<dt>PER
<dd>The parameter to draw a perimeter. The default is to draw a perimeter around the contour plot.
<dt>PMM
<dd>The parameter to plot relative minima and maxima. The default is to not plot them. (Does not apply to entry CONRAQ.)
<dt>PSL
<dd>The parameter which determines whether the outline of the data shield will be drawn on the same frame as the contour plot. The default is to not draw the shield. (Does not apply to entry CONRAQ.)
<dt>REP
<dd>The parameter indicating the use of the same data in a new execution. The default value is to assume a new input dataset.
<dt>SCA
<dd>The parameter for scaling of the plot on a frame. This parameter is ON by default.
<dt>TFR
<dd>The parameter to advance the frame before triangulation. The default value is TFR=ON, which means that the contours and the triangles will be plotted on separate frames.
<dt>TOP
<dd>The parameter to plot only the triangles. The default is to plot contours, then triangles.
<dt>TRI
<dd>The parameter to plot the triangulation. The default is OFF and therefore the triangles are not drawn.</dl><h2>Parameters of type INTEGER set in calls to entry CONOP2:</h2><dl COMPACT><dt>INT
<dd>The parameter to determine line intensities for various parts of the plot. Intensities vary from a high of 255 to a low of 0. The default is high for all parts of the plot except minor contour lines which are set to low.
<dt>LSZ
<dd>This parameter determines the character size of contour labels. The default value is 9, which results in label characters of a size of 9./1023. NDC units. (Does not apply to entry CONRAQ.)
<dt>NCP
<dd>The parameter NCP controls the number of data points to be used in the interpolation. Increasing NCP causes more of the surrounding data to influence the point of interpolation. In the case of linear interpolation NCP is always 4. In the case of C1 interpolation, NCP can vary from 2 to 25 with 4 as the default. 

 The interpolation option is selected using internal parameter ITP.
<dt>SML
<dd>This parameter specifies the character size of minimum and maximum contour labels. The default value is 15, which results in label character sizes of 15./1023. NDC units. (Does not apply to entry CONRAQ.)
<dt>SPD
<dd>The parameter for the size of the plotted input data values. The default value is 8, which results in a data value character size of 8./1023. NDC units.
<dt>SSZ
<dd>The parameter to determine the resolution (number of steps in each direction). The default is 40.
<dt>STL
<dd>The parameter to determine the size of the main title characters. The default value is 16, which results in title character sizes of 16./1023. NDC units.</dl><h2>Parameters of type REAL set in calls to entry CONOP3:</h2><dl COMPACT><dt>CHL
<dd>This parameter determines how the high and low contour values are set. The default is to compute the high and low values from the input data.
<dt>CIL
<dd>This parameter determines how the contour increment is set. The default is to calculate the increment based on the range of the input data.
<dt>CON
<dd>This parameter determines how the contour levels are set. The default is to have the program compute the contour values and the number of contour levels.
<dt>DBP
<dd>This parameter determines how the dash pattern break point (BP) is set. The default is BP=0. (Does not apply to entry CONRAQ.)
<dt>SDC
<dd>The parameter to determine how to scale the data on the contours. The default scaling is 1. (Does not apply to entry CONRAQ.)
<dt>SLD
<dd>This parameter allows for the entry of a bounding polygon (shield). Only contours within the shield are drawn. The default is no shield. (Does not apply to entry CONRAQ.)
<dt>TEN
<dd>The parameter to determine the tension factor applied when smoothing contour lines. The default value is 2.5. (Does not apply to entry CONRAQ.)</dl><h2>Parameters of type CHARACTER set in calls to entry CONOP4:</h2><dl COMPACT><dt>DAS
<dd>This parameter determines which contours are represented by dashed lines. The default is to draw all contours as solid lines. (Does not apply to entry CONRAQ.)
<dt>FMT
<dd>A parameter which specifies a format for output of the data values. If FMT=OFF, the default values of the format, the number of characters in the format, and the length of the output field described in the format, are (G10.3), 7, and 10, respectively.
<dt>TLE
<dd>The parameter to place a title at the top of the plot. The default value is no title.</dl><h2>See Also</h2>Online: conran_family, conran, conraq, conras, conop1, conop2, conop3, conop4, conpack, conpack_params 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
