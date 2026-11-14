---
title: "ncl_histogram(3)"
name: "ncl_histogram"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_histogram/"
---

Histogram - This utility is used to generate histograms. Histograms or bar charts are used to show the distribution of values in a like-sample dataset. The individual values are sorted by size into a number of value ranges called class intervals. The number of samples out of the total which fall into a class interval are represented as a histogram bar height. The height of each histogram bar is proportional to the number of samples in that class interval. 

 Various options are available including the specification of class values, spacing between histogram bars, shading of bars, windowing (i.e. scaling), specification of color, labels, titles, etc. One can also detect and ignore missing data which has been assigned a special value. Options are set by calls to routines HSTOPL, HSTOPR, HSTOPC, and HSTOPI. A call to routine HISTGR then generates the histogram. 

<h2>Synopsis</h2>HISTGR - Generates histograms with many options available via input arguments and internal parameter selections. 

 HSTOPC - Sets values of internal parameters of type character. 

 HSTOPI - Sets values of internal parameters of type integer. 

 HSTOPL - Sets values of internal parameters of type logical. Specifically, HSTOPL is used to turn options &quot;OFF&quot;, or &quot;ON&quot;. 

 HSTOPR - Sets values of internal parameters of type real.
<h2>C-Binding Synopsis</h2>c_histgr 
 c_hstopc 
 c_hstopi 
 c_hstopl 
 c_hstopr
<h2>Access</h2>To use the Histogram C or Fortran routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>The possible error messages are as follows:
<dl COMPACT><dt>HISTGR - NPTS LESS THAN 1
<dd>The argument NPTS, number of binable values, has been entered in error.
<dt>HISTGR - NCLASS LESS THAN 1
<dd>NCLASS, the number of histogram bars, has been entered in error.
<dt>HISTGR - NPTS .GT. NDIM
<dd>The argument NPTS, number of binable values, is larger than the array dimension size. Reduce NPTS or modify the code to increase the array dimension size. Set NDIM in the code to the new array dimension size.
<dt>HISTGR - NWRK .LT. NDIM+3*NCLASS+3
<dd>The argument NWRK, the dimension size of the work array, is incorrect. Recompute it according to the above formula.
<dt>HISTGR - NCLASS .NE. NPTS (IFLAG=2)
<dd>IFLAG = 2 signals a special case in which the input data has already been accumulated into class intervals. Therefore, the number of data values, NPTS, and the number of histogram bars, NCLASS, must be equal.
<dt>HISTGR - NCLASS .NE. NPTS (IFLAG=3)
<dd>IFLAG = 3 signals a special case in which the input data has already been accumulated into class intervals. Therefore, the number of data values, NPTS, and the number of histogram bars, NCLASS, must be equal. (IFLAG = 3 differs from the IFLAG = 2 case only in the fact that two histograms are to be displayed instead of one.)
<dt>HISTGR - NCLASS MUST EQUAL NPTS
<dd>This is a redundant test on whether the number of input data values, NPTS, equals the number of bars, NCLASS, when the IFLAG option is 2 or 3.
<dt>HISTGR - IFLAG NOT SPECIFIED OR INVALID
<dd>HISTGR argument IFLAG is not one of the legal values of 0, 1, 2, or 3.
<dt>HISTGR - MIN. X-VALUE .EQ. MAX. X-VALUE
<dd>A histogram has no width. This probably means the values of HISTGR argument CLASS have been entered in error.
<dt>HISTGR - MAXIMUM Y-VALUE .EQ. 0.0
<dd>A histogram has no data. The histogram is plotted with a Y range of .02. This probably means the HISTGR argument DAT1 had all zero values.
<dt>HISTGR - WINDOW OPTION ERROR, RANGE IS 0. - 1.
<dd>The internal parameter options that define the part of the frame where the histogram is to be drawn have been entered incorrectly.
<dt>HSTOPC - UNDEFINED OPTION
<dd><dt>HSTOPI - UNDEFINED OPTION
<dd><dt>HSTOPL - UNDEFINED OPTION
<dd><dt>HSTOPR - UNDEFINED OPTION
<dd>Either an internal parameter name or value is incorrect. Check the spelling in the calls to whichever routine is cited.
<dt>HSTOPI - LCOL MUST EQUAL 8
<dd>The number of color indices input to HSTOPI cannot exceed 8.
<dt>HSTOPR - INVALID SPACING PARAMETER
<dd>Either the spacing of histogram bars, or the overlap of bars from two histograms, is outside of the legal range. Valid values for spacing of bars are 0.0 (no spacing) to 4.0 (maximum spacing.) Valid values used to set overlap of adjacent histogram bars when comparing two datasets in one histogram are -4.0 (maximum overlap) to 4.0 (little or no overlap.)</dl><h2>See Also</h2>Online: histgr, histogram_params, hstopc, hstopi, hstopl, hstopr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
