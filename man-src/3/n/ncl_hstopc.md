---
title: "ncl_hstopc(3)"
name: "ncl_hstopc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_hstopc/"
---

HSTOPC - Specifies various CHARACTER variables to be used by the Histogram utility. 

<h2>Synopsis</h2>CALL HSTOPC (STRING,STRNG2,NUMBER,ILCH)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_hstopc (char *string, char *strng2, int number, 
 int ilch)
<h2>Description</h2><dl COMPACT><dt>STRING
<dd>Character, input -- Selects an internal parameter. The possibilities are: 

 
&nbsp;<wbr>&nbsp;<wbr>'FOR=ON'&nbsp;<wbr>or&nbsp;<wbr>'FOR=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'TIT=ON'&nbsp;<wbr>or&nbsp;<wbr>'TIT=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'LAB=ON'&nbsp;<wbr>or&nbsp;<wbr>'LAB=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'PTI=ON'&nbsp;<wbr>or&nbsp;<wbr>'PTI=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'FQN=ON'&nbsp;<wbr>or&nbsp;<wbr>'FQN=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'CHR=ON, or&nbsp;<wbr>'CHR=OFF' 

 If an option is turned 'ON' then the STRNG2, NUMBER, and ILCH arguments can be used to override the default settings of that option. 

 If the value of a STRING option is 'OFF' then the next three arguments of the HSTOPC call can be any dummy value. Option settings will be returned to their default values. 

 The following options are defined by this subroutine:
<dl COMPACT><dd><dl COMPACT><dt>FOR
<dd>Format for class labels. The 'FOR=OFF' default is 
&nbsp;<wbr>'(G10.3)'. Although class values are real numbers, integer formats are allowed, in which case HISTGR will convert from real to integer before plotting labels.
<dt>TIT
<dd>A main title of up to 96 characters. Only 45 characters are written per line so up to 3 lines may be written. The 'TIT=OFF' default is no title.
<dt>LAB
<dd>A label for the class interval (histogram bar) axis. The 'LAB=OFF' default value is 'CLASS INTERVALS' when the HSTOPL option 'MID=OFF' is selected, and 'CLASS MIDVALUES' when 'MID=ON'. 

 In order to delete this axis label, select 'LAB=ON' for STRING and 'NOLABEL' for STRNG2.
<dt>PTI
<dd>The percent axis label. Default value when 'PTI=OFF' is 'PERCENT OCCURRENCE' when IFLAG = 0, or 1, and 'PERCENT of MAXIMUM' when IFLAG = 2, or 3.
<dt>FQN
<dd>The frequency axis label. The 'FQN=OFF' default value is 'FREQUENCY'. 

 In order to delete this axis label, select 'FQN=ON' for STRING and 'NOLABEL' for STRNG2.
<dt>CHR
<dd>A concatenated string of alphanumeric class interval labels. The default value is a set of internally computed numeric class labels.</dl></dl><dt>STRNG2
<dd>Character, input -- A string of up to 45 characters. 

 
&nbsp;<wbr>'FOR=ON', STRNG2 is a format for the class labels. 

 
&nbsp;<wbr>'TIT=ON', STRNG2 is a histogram main title. 

 
&nbsp;<wbr>'LAB=ON', STRNG2 is a label for the class interval axis. 

 
&nbsp;<wbr>'PTI=ON', STRNG2 is a label for the percentage axis. 

 
&nbsp;<wbr>'FQN=ON', STRNG2 is a label for the frequency axis. 

 
&nbsp;<wbr>'CHR=ON', STRNG2 is a concatenated string of class labels. 

 The length of this character string will be NUMBER*ILCH, where NUMBER is the number of class intervals and ILCH is the number of characters in the interval label.
<dt>NUMBER
<dd>Integer, input -- It only applies to the following options: 

 
&nbsp;<wbr>'FOR=ON', NUMBER specifies the maximum number of class intervals (histogram bars) that will be labeled. The default values ('FOR=OFF') are 9 labels for vertical bars and 15 labels for horizontal bars. 

 
&nbsp;<wbr>'CHR=ON', NUMBER must be set to NCLASS, an argument of the next call to be made to routine HISTGR. 

 NUMBER is not used under any other option setting. 

 Calls to HSTOPC with either 'FOR=ON' or 'CHR=ON' may be performed in any order; the parameters set by NUMBER are mutually exclusive.
<dt>ILCH
<dd>Integer, input -- It only applies in the following instance. 

 If 'CHR=ON', ILCH specifys the number of characters in each label of a class interval (histogram bar). ILCH cannot be greater than 15.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>HSTOPC is called to set parameters of type CHARACTER before entry HISTGR is called to generate the histogram. Options are main and axes titles, class interval (bar) labels, and class interval formats. 

 For a complete list of parameters available in this utility, see the histogram_params man page.
<h2>Examples</h2>Use the command &quot;ncargex thstgr&quot; to generate a three frame example of histogram options. The following code causes the second frame to have a class interval axis of 12 intervals, each with a 3 character label that specifies a month of the year. 

 PARAMETER (NCLASS=12, ILCH=3) 
 CHARACTER*55 MON 
 MON='JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC' 
 CALL HSTOPC('CHR=ON',MON,12,3) 

 Example &quot;ncargex thstmv&quot; shows three examples of histograms with missing values in the input data.
<h2>Access</h2>To use HSTOPC or c_hstopc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the histogram man page for a description of all Histogram error messages and/or informational messages.
<h2>See Also</h2>Online: histogram, histogram_params, histgr, hstopi, hstopl, hstopr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
