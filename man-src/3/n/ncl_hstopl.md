---
title: "ncl_hstopl(3)"
name: "ncl_hstopl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_hstopl/"
---

HSTOPL - Turns options off and on for the Histogram utility. 

<h2>Synopsis</h2>CALL HSTOPL (STRING)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_hstopl (char *string)
<h2>Description</h2><dl COMPACT><dt>STRING
<dd>Character, input -- Selects an internal parameter. The possibilities are: 

 
'HOR=ON'&nbsp;<wbr>or&nbsp;<wbr>'HOR=OFF' 
 
'PER=ON'&nbsp;<wbr>or&nbsp;<wbr>'PER=OFF' 
 
'MID=ON'&nbsp;<wbr>or&nbsp;<wbr>'MID=OFF' 
 
'SHA=ON'&nbsp;<wbr>or&nbsp;<wbr>'SHA=OFF' 
 
'DRL=ON'&nbsp;<wbr>or&nbsp;<wbr>'DRL=OFF' 
 
'MED=ON'&nbsp;<wbr>or&nbsp;<wbr>'MED=OFF' 
 
'NMV=ON'&nbsp;<wbr>or&nbsp;<wbr>'NMV=OFF' 
 
'PMV=ON'&nbsp;<wbr>or&nbsp;<wbr>'PMV=OFF' 
 
'PRM=ON'&nbsp;<wbr>or&nbsp;<wbr>'PRM=OFF' 
 
'FRA=ON'&nbsp;<wbr>or&nbsp;<wbr>'FRA=OFF' 
 
'LIS=ON'&nbsp;<wbr>or&nbsp;<wbr>'LIS=OFF' 
 
'DEF=ON'&nbsp;<wbr>or&nbsp;<wbr>'DEF=OFF' 

 The following options are defined by this subroutine:
<dl COMPACT><dd><dl COMPACT><dt>HOR
<dd>The histogram bars are drawn horizontally if 'HOR=ON', vertically if 'HOR=OFF'. The default is 'HOR=OFF'.
<dt>PER
<dd>If 'PER=ON', a labeled percent axis is drawn on the right side of the histogram (top if 'HOR=ON'.) If 'PER=OFF', no percent axis is drawn. The default is 'PER=ON'. 

 This places a second axis on the opposite side of the frame from the normal frequency axis.
<dt>MID
<dd>If 'MID=ON', class labels are placed at the midpoint of each class interval. If 'MID=OFF', the class interval end points are labeled. (MID defaults to ON if IFLAG = 2 or 3.) The default is 'MID=ON'.
<dt>SHA
<dd>If 'SHA=ON', the histogram bars are shaded. If 'SHA=OFF', the bars are not shaded. The default is 'SHA=ON'. 

 Devices will vary as to how they interpret shading.
<dt>DRL
<dd>If 'DRL=ON', lines are drawn through the histogram bars where Y-axis tick marks would occur. When comparing two datasets (IFLAG=3), lines are only drawn through the bars associated with the first dataset. If 'DRL=OFF', no lines are drawn. The default is 'DRL=OFF'.
<dt>MED
<dd>If 'MED=ON', a line is drawn through the median value of all points. If 'MED=OFF', this line is not drawn. MED does not apply when assigning Y-values to X-values; it is valid only for IFLAG = 1 or 2. The default is 'MED=OFF'.
<dt>NMV
<dd>If 'NMV=ON', histogram bar percentages will be calculated with respect to the number of input data values (NPTS) minus the number of detected missing values (MISS), or NMVA = NPTS - MISS. If 'NMV=OFF', histogram bar percentages will be normalized to NPTS.
<dt>PMV
<dd>If 'PMV=ON', missing value counts will be written on the plot. If 'NMV=OFF', they will not.
<dt>PRM
<dd>If 'PRM=ON', a perimeter is drawn around the histogram. If 'PRM=OFF', no perimeter is drawn. The default is 'PRM=OFF'.
<dt>FRA
<dd>If 'FRA=ON', the frame is advanced automatically after the histogram is drawn. If 'FRA=OFF', the frame is not advanced, and the user must call FRAME. The default is 'FRA=ON'.
<dt>LIS
<dd>If 'LIS=ON', all the options along with their values are printed on the standard output. If 'LIS=OFF', nothing is printed on the standard output. The default is 'LIS=OFF'.
<dt>DEF
<dd>If 'DEF=ON', ALL the options are reset to their default values. 'DEF=OFF' has no effect. All parameters begin at their default values.</dl></dl>
</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>HSTOPL is called to toggle histogram options before entry HISTGR is called to generate the histogram.
<h2>Examples</h2>Use the command &quot;ncargex thstgr&quot; to generate a three frame example of various types of histograms. &quot;ncargex thstmv&quot; will show three examples of histograms with missing values in the input data.
<h2>Access</h2>To use HSTOPL or c_hstopl, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the histogram man page for a description of all Histogram error messages and/or informational messages.
<h2>See Also</h2>Online: histogram, histogram_params, histgr, hstopc, hstopi, hstopr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
