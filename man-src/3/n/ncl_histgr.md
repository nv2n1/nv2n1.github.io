---
title: "ncl_histgr(3)"
name: "ncl_histgr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_histgr/"
---

HISTGR - Plots a histogram with various options including specification of class values, spacing between histogram bars, shading of bars, windowing (i.e. scaling), specification of color, labels, titles, etc. Data values are partitioned into classes; histogram bars represent either number of occurrences within each class, or a Y-value associated with that class (user choice). Options are set by calls to subroutines HSTOPL, HSTOPR, HSTOPC, and HSTOPI before the call to HISTGR. 

<h2>Utility</h2>This routine is part of the Histogram utility in NCAR Graphics. To see the overview man page for this utility, type &quot;man histogram&quot;.
<h2>Synopsis</h2>CALL HISTGR (DAT1,NDIM,NPTS,IFLAG,CLASS,NCLASS,WRK,NWRK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_histgr (float *dat1, int ndim, int npts, 
 int iflag, float *class, int nclass, float *wrk, int nwrk)
<h2>Description</h2><dl COMPACT><dt>DAT1
<dd>Two dimensional real array containing data of one of two types, either values to be collected into class intervals before plotting, or values which have already been assigned to class intervals and only need to be displayed. See argument IFLAG for a more complete description of HISTGR input data options. DAT1 is dimensioned: DAT1(NDIM,2).
<dt>NDIM
<dd>The size of the first dimension of DAT1 as set in the dimension statement of the calling program.
<dt>NPTS
<dd>Number of values actually stored into DAT1 on this call. NPTS must always be less than or equal to NDIM.
<dt>IFLAG
<dd>An integer flag which selects one of four options provided by the HISTGR utility. The options are: 

 0 A single array of length NPTS is loaded 
&nbsp;<wbr>&nbsp;<wbr>into the DAT1 array. HISTGR computes NCLASS 
&nbsp;<wbr>&nbsp;<wbr>equally sized class intervals that vary 
&nbsp;<wbr>&nbsp;<wbr>from the minimum value in DAT1 to the 
&nbsp;<wbr>&nbsp;<wbr>maximum value in steps of&nbsp;<wbr>(MAX-MIN)/NCLASS. 

 
&nbsp;<wbr>&nbsp;<wbr>All values of DAT1 that fall in each 
&nbsp;<wbr>&nbsp;<wbr>class interval are separately accumulated 
&nbsp;<wbr>&nbsp;<wbr>for that interval. The final tabulations 
&nbsp;<wbr>&nbsp;<wbr>are plotted as a histogram of NCLASS bars. 
&nbsp;<wbr>&nbsp;<wbr>The bar height can be labeled with the 
&nbsp;<wbr>&nbsp;<wbr>number of points that fall within this 
&nbsp;<wbr>&nbsp;<wbr>particular class interval&nbsp;<wbr>(bin size), or 
&nbsp;<wbr>&nbsp;<wbr>it can be given as a percentage of the 
&nbsp;<wbr>&nbsp;<wbr>number of values input, NPTS. 

 
&nbsp;<wbr>&nbsp;<wbr>Note that under this option the user 
&nbsp;<wbr>&nbsp;<wbr>has no control over the range of the 
&nbsp;<wbr>&nbsp;<wbr>class intervals.&nbsp;<wbr>&nbsp;<wbr>They are internally 
&nbsp;<wbr>&nbsp;<wbr>determined from the range of the data. 

 1 This option is similar to the IFLAG = 0 
&nbsp;<wbr>&nbsp;<wbr>option except that the user can select 
&nbsp;<wbr>&nbsp;<wbr>the range of the class intervals into 
&nbsp;<wbr>&nbsp;<wbr>which the data are collected. For example, 
&nbsp;<wbr>&nbsp;<wbr>say the user wants to collect the number 
&nbsp;<wbr>&nbsp;<wbr>of occurrences of the DAT1 values that 
&nbsp;<wbr>&nbsp;<wbr>fall within 5 equally spaced intervals 
&nbsp;<wbr>&nbsp;<wbr>in the value range from 0. to 10. The 
&nbsp;<wbr>&nbsp;<wbr>user would then input NCLASS+1 class 
&nbsp;<wbr>&nbsp;<wbr>interval end points into array CLASS, 
&nbsp;<wbr>&nbsp;<wbr>namely 0., 2., 4., 6., 8., and 10. 
&nbsp;<wbr>&nbsp;<wbr>These values need not be entered in 
&nbsp;<wbr>&nbsp;<wbr>monotonically increasing order and 
&nbsp;<wbr>&nbsp;<wbr>need not be equally spaced. 

 2 This option allows the user to enter 
&nbsp;<wbr>&nbsp;<wbr>and display data which has already 
&nbsp;<wbr>&nbsp;<wbr>been accumulated into class intervals, 
&nbsp;<wbr>&nbsp;<wbr>i.e., already available histograms. 
&nbsp;<wbr>&nbsp;<wbr>The data input to DAT1 thus have 
&nbsp;<wbr>&nbsp;<wbr>percentage of total, or number of 
&nbsp;<wbr>&nbsp;<wbr>occurrences values. In this case the 
&nbsp;<wbr>&nbsp;<wbr>number of points in DAT1, NPTS, is 
&nbsp;<wbr>&nbsp;<wbr>equal to the number of class intervals 
&nbsp;<wbr>&nbsp;<wbr>(histogram bars), NCLASS. The NCLASS 
&nbsp;<wbr>&nbsp;<wbr>class interval midpoints are loaded 
&nbsp;<wbr>&nbsp;<wbr>into array CLASS. They do not have 
&nbsp;<wbr>&nbsp;<wbr>to be of equal width. 

 3 This option is the same as option 
&nbsp;<wbr>&nbsp;<wbr>IFLAG&nbsp;<wbr>=&nbsp;<wbr>2 except that two histograms 
&nbsp;<wbr>&nbsp;<wbr>can be displayed for comparison 
&nbsp;<wbr>&nbsp;<wbr>purposes. The first histogram is 
&nbsp;<wbr>&nbsp;<wbr>loaded into DAT1(NPTS,1). The second 
&nbsp;<wbr>&nbsp;<wbr>histogram is loaded into DAT1(NPTS,2). 
&nbsp;<wbr>&nbsp;<wbr>The first histogram can partially 
&nbsp;<wbr>&nbsp;<wbr>shade or obscure the second histogram 
&nbsp;<wbr>&nbsp;<wbr>by the appropriate selection of the 
&nbsp;<wbr>&nbsp;<wbr>SPAC and OVERLP options.&nbsp;<wbr>&nbsp;<wbr>Note that 
&nbsp;<wbr>&nbsp;<wbr>NPTS&nbsp;<wbr>=&nbsp;<wbr>NCLASS when IFLAG&nbsp;<wbr>=&nbsp;<wbr>2 or 3.
<dt>CLASS
<dd>Real array containing class values, dimensioned (NCLASS+1). This array has the following IFLAG dependencies: 

 IFLAG = 0 CLASS is not used. 

 IFLAG = 1 NCLASS+1 class interval end points 
&nbsp;<wbr>&nbsp;<wbr>are loaded into array CLASS in a 
&nbsp;<wbr>&nbsp;<wbr>monotonically increasing order.&nbsp;<wbr>&nbsp;<wbr>The 
&nbsp;<wbr>&nbsp;<wbr>intervals need not be of equal width. 

 IFLAG = 2 NCLASS midpoint intervals are loaded 
&nbsp;<wbr>&nbsp;<wbr>into array CLASS. They must be in 
&nbsp;<wbr>&nbsp;<wbr>monotonically increasing order, but 
&nbsp;<wbr>&nbsp;<wbr>need not be of equal widths. The 
&nbsp;<wbr>&nbsp;<wbr>histogram bars will however be 
&nbsp;<wbr>&nbsp;<wbr>displayed with equal widths. 

 IFLAG = 3 Same as for IFLAG = 2.
<dt>NCLASS
<dd>Number of class intervals (histogram bars) specified. NCLASS must be .GE. 1.
<dt>WRK
<dd>Real scratch array, dimensioned by NWRK in the dimension statement of the calling program.
<dt>NWRK
<dd>The dimension size of array WRK determined from: NDIM + 3 * (NCLASS + 1)</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exceptions: 

<dl COMPACT><dt>dat1
<dd>Two dimensional real array dimensioned: dat1(2,ndim).
<dt>ndim
<dd>The size of the second dimension of dat1 as set in the dimension statement of the calling program.</dl><h2>Usage</h2>Many parameters which affect the output histogram can be set before this routine is called. See the histogram_params man page for a short functional description of all available parameters. For more detail on a specific option, see the man pages of the parameter setting routines (HSTOPC, HSTOPI, HSTOPL, or HSTOPR) used to set the parameters defining that option.
<h2>Examples</h2>Use the command &quot;ncargex thstgr&quot; to generate a three frame example of various types of histograms. &quot;ncargex thstmv&quot; will show three examples of histograms with missing values in the input data.
<h2>Access</h2>To use HISTGR or c_histgr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the histogram man page for a description of all Histogram error messages and/or informational messages.
<h2>See Also</h2>Online: histogram, histogram_params, hstopc, hstopi, hstopl, hstopr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
