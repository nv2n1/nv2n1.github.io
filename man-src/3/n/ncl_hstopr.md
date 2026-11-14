---
title: "ncl_hstopr(3)"
name: "ncl_hstopr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_hstopr/"
---

HSTOPR - Specifies various REAL arrays to be used by the the Histogram utility. 

<h2>Synopsis</h2>CALL HSTOPR (STRING,ARRAY,LARR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_hstopr (char *string, float *array, int larr)
<h2>Description</h2><dl COMPACT><dt>STRING
<dd>Character, input -- Selects an internal parameter. The possibilities are: 

 
&nbsp;<wbr>&nbsp;<wbr>'WIN=ON'&nbsp;<wbr>or&nbsp;<wbr>'WIN=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'SPA=ON'&nbsp;<wbr>or&nbsp;<wbr>'SPA=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'MVA=ON'&nbsp;<wbr>or&nbsp;<wbr>'MVA=OFF' 

 WIN defines the portion of the frame that will receive the histogram. SPA determines the spacing between histogram bars. MVA requests a test to detect input special values which denote missing data.
<dt>ARRAY
<dd>Real, input -- It has a different use depending upon which parameter is specified by argument STRING. See the examples following argument LARR.
<dt>LARR
<dd>Integer, input -- Dimension of ARRAY. 

 The following arrays may be defined by this routine: 

 Windowing: 

 <pre>STRING is 'WIN=ON'
LARR = 4
<a HREF="//www.systutorials.com/docs/linux/man/1-ARRAY/">ARRAY</a>(1) = XMIN
<a HREF="//www.systutorials.com/docs/linux/man/2-ARRAY/">ARRAY</a>(2) = XMAX
<a HREF="//www.systutorials.com/docs/linux/man/3-ARRAY/">ARRAY</a>(3) = YMIN
<a HREF="//www.systutorials.com/docs/linux/man/4-ARRAY/">ARRAY</a>(4) = YMAX</pre><dd>These coordinates define a rectangular region of the total frame in NDC's where the current histogram is to be plotted. The range of allowed values is between 0. and 1. in both dimensions. 

 For example, XMIN=0., XMAX=.5, YMIN=.5, and YMAX=1. would specify the upper left quadrant of the frame. 

 IF 'WIN=OFF', the default window for the histogram will be the entire frame. 

 Spacing: 

 <pre>STRING is 'SPA=ON'
LARR = 2
<a HREF="//www.systutorials.com/docs/linux/man/1-ARRAY/">ARRAY</a>(1) = SPAC
<a HREF="//www.systutorials.com/docs/linux/man/2-ARRAY/">ARRAY</a>(2) = OVERLP</pre><dd>SPAC determines the spacing of histogram bars between 0. (no spacing) and 4. (maximum spacing). Default spacing is SPAC = 2.0. 

 OVERLP determines the overlap of adjacent histogram bars when two datasets are compared. Valid values are -4.0 (maximum overlap) to 4.0 (little or no overlap). The Default is 0. 

 When STRING = 'SPA=OFF', there is no spacing or overlap. 

 Detecting missing values: 

 <pre>STRING is 'MVA=ON'
LARR = 2
<a HREF="//www.systutorials.com/docs/linux/man/1-ARRAY/">ARRAY</a>(1) = SETMVA
<a HREF="//www.systutorials.com/docs/linux/man/2-ARRAY/">ARRAY</a>(2) = SETEPS</pre><dd>SETMVA is the special value used to denote missing data. The default value is -9999. 

 SETEPS is an epsilon to use in the special value test. If the difference between a data point and SETMVA is less than SETEPS, then the data point is assumed to be a missing value. The Default is 1.E-10. 

 When STRING = 'MVA=OFF', there is no testing for missing values.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>HSTOPR is called to set parameters of type REAL before entry HISTGR is called to generate the histogram. Options are the portion of the frame to receive the graphic, and the amount of spacing and overlap of histogram bars. 

 For a complete list of parameters available in this utility, see the histogram_params man page.
<h2>Examples</h2>Use the command &quot;ncargex thstgr&quot; to generate a three frame example of histogram options. The following code defined the window and bar spacing of plot 1 on frame 3. 

 <pre>C
C Plot 1 goes into the top left quadrant of the frame.
C
C ARR7 coordinates are XMIN, XMAX, YMIN, YMAX.
C
 <a HREF="//www.systutorials.com/docs/linux/man/1-ARR7/">ARR7</a>(1) = 0.
 <a HREF="//www.systutorials.com/docs/linux/man/2-ARR7/">ARR7</a>(2) = .5
 <a HREF="//www.systutorials.com/docs/linux/man/3-ARR7/">ARR7</a>(3) = .5
 <a HREF="//www.systutorials.com/docs/linux/man/4-ARR7/">ARR7</a>(4) = 1.
 CALL HSTOPR('WIN=ON',ARR7,4)
C
 <a HREF="//www.systutorials.com/docs/linux/man/1-SPAC/">SPAC</a>(1) = 3.0
 <a HREF="//www.systutorials.com/docs/linux/man/2-SPAC/">SPAC</a>(2) = 0.0
 CALL HSTOPR('SPA=ON',SPAC,2)</pre>Example &quot;ncargex thstmv&quot; shows three examples of histograms with missing values in the input data.
<h2>Access</h2>To use HSTOPR or c_hstopr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the histogram man page for a description of all Histogram error messages and/or informational messages.
<h2>See Also</h2>Online: histogram, histogram_params, hstopc, hstopi, hstopl, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
