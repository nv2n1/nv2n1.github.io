---
title: "ncl_hstopi(3)"
name: "ncl_hstopi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_hstopi/"
---

HSTOPI - Specifies various INTEGER parameters to be used by the Histogram utility. 

<h2>Synopsis</h2>CALL HSTOPI (STRING, PARAM1, PARAM2, ICOL, LCOL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_hstopi (char *string, int param1, int param2, 
 int *icol, int lcol)
<h2>Description</h2><dl COMPACT><dt>STRING
<dd>Character, input -- Selects an internal parameter. The possibilities are: 

 
'COL=ON'&nbsp;<wbr>or&nbsp;<wbr>'COL=OFF' 
 
'CLA=ON'&nbsp;<wbr>or&nbsp;<wbr>'CLA=OFF' 

 If an option is turned 'ON', then the remaining HSTOPI arguments can be used to override the default settings of that option. 

 If the option is 'OFF', then the remaining arguments of the HSTOPI call can be any dummy values. Option settings will be returned to their default values. 

 The following options are defined by this subroutine:
<dl COMPACT><dd><dl COMPACT><dt>COL
<dd>This option turns the use of color OFF, or ON. If it is ON, then eight color indices are assigned to the various parts of the histogram as described by the INTEGER array ICOL. Arguments ICOL and LCOL must be set, PARAM1 and PARAM2 can have dummy values.
<dt>CLA
<dd>This option allows the size and orientation of class labels to be altered. If 'CLA=ON', the size of the label characters is set using argument PARAM1, and the orientation is set by argument PARAM2. Arguments ICOL and LCOL can have dummy values. If 'CLA=OFF', defaults are used which cause medium sized characters to be written in the horizontal direction.</dl></dl><dt>PARAM1
<dd>Integer, input -- Specifies the character height of class labels. 

 When 'CLA=ON'; 1 = small, 2 = medium, 3 = large; default is 2 when 'CLA=OFF'.
<dt>PARAM2
<dd>Integer, input -- Specifies the character orientation of class labels. 

 If 'CLA=ON', labels can vary from 0 (horizontal) to 90 (vertical) degrees. Vertical is the default when 'CLA=OFF'.
<dt>ICOL
<dd>Integer, input -- Assigns a set of RGB color indices to the eight components of a histogram graphic when 'COL=ON'. 

 ICOL(1) = color index used for area fill of 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>histogram bars of dataset 1. 
 ICOL(2) = color index used for area fill of 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>histogram bars of dataset 2. 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(When two datasets are compared 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>using parameter IFLAG&nbsp;<wbr>=&nbsp;<wbr>3). 
 ICOL(3) = color index used for bar outlines. 
 ICOL(4) = color index used for drawing axes. 
 ICOL(5) = color index used for drawing a median 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>line. 
 ICOL(6) = color index used for text output 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(labels.) 
 ICOL(7) = color index used for titles. 
 ICOL(8) = color index used for drawing the 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>perimeter box. 

 The default color index is 1 for all (when 'COL=OFF'). 

 If 'COL=ON', the color indices and their associated colors are as follows. (These may be changed by specifying an RGB color table prior to your call to HSTOPI. See the man page for GKS routine gscr.) 

 Color Index Color 

 
&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>BLACK 
 
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>WHITE 
 
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>RED 
 
&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GREEN 
 
&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>BLUE 
 
&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CYAN 
 
&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MAGENTA 
 
&nbsp;<wbr>&nbsp;<wbr>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>YELLOW 
 
&nbsp;<wbr>&nbsp;<wbr>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ORANGE
<dt>LCOL
<dd>Integer, input -- Specifies the length of array ICOL. LCOL must be set to 8.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>HSTOPI is called to set parameters of type INTEGER before entry HISTGR is called to generate the histogram. Options are size and orientation of class labels, and setting the colors for various components of the graphic. 

 For a complete list of parameters available in this utility, see the histogram_params man page.
<h2>Examples</h2>Use the command &quot;ncargex thstgr&quot; to generate a three frame example of histogram options. The following code causes the second frame to have an array of colors assigned to the graphic components (argument ICOL.) 

 <pre> REAL RGB(3,15)
 INTEGER COLORS(15)
C
C Define the RGB triples of 15 colors in a data statement.
C (Code omitted for brevity. See the data statement in thstgr.f)
C
C Assign colors to the color indices.
C
 DO 100 I = 1,15
 CALL GSCR(1,I,RGB(1,I),RGB(2,I),RGB(3,I))
 100 CONTINUE
C
C Assign color indices to the 8 components of the graphic.
C
 COLORS(1) = 8
 COLORS(2) = 3
 COLORS(3) = 14
 COLORS(4) = 11
 COLORS(5) = 6
 COLORS(6) = 13
 COLORS(7) = 14
 COLORS(8) = 5
 CALL HSTOPI('COL=ON',3,0,COLORS,8)</pre>Example &quot;ncargex thstmv&quot; shows three examples of histograms with missing values in the input data.
<h2>Access</h2>To use HSTOPI or c_hstopi, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the histogram man page for a description of all Histogram error messages and/or informational messages.
<h2>See Also</h2>Online: histogram, histogram_params, histgr, hstopc, hstopl, hstopr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
