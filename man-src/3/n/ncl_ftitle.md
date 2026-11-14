---
title: "ncl_ftitle(3)"
name: "ncl_ftitle"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ftitle/"
---

FTITLE - Used for unscrolled movie or video titles. It reads, from standard input, the information necessary to define the desired title frames, and then calls STITLE to create those frames. 

<h2>Synopsis</h2>CALL FTITLE (MTST)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ftitle (int mtst)
<h2>Description</h2><dl COMPACT><dt>MTST
<dd>(an input expression of type INTEGER) is a switch indicating whether this is a &quot;real&quot; run or a &quot;practice&quot; run:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>means &quot;real run&quot;.
<dt>1
<dd>means &quot;practice run&quot;.</dl></dl><dd>During real runs, each title frame is repeated as many times as necessary to display it for a user-specified time period (at 'NFS' frames per second). Blank frames are placed before the first title frame ('TM1' seconds worth of them), between consecutive title frames ('TM2' seconds worth of them), and after the last title frame ('TM2' + 'TM3' seconds worth of them). Blank frames are to allow for splicing. 

 If the user has turned on fade-in (by setting the internal parameter 'FIN' non-zero), and/or fade-out (by setting the internal parameter 'FOU' non-zero), the required fade-in and fade-out frames will be generated, as well. 

 During practice runs, each title frame will occur from one to three times (once for fade-in, once for the stationary holding time, and once for fade-out); each of these frames will have a legend indicating how many seconds the frame represents in a real run. Each sequence of blank frames will be replaced by a single frame with a message indicating how many seconds worth of blank frames it represents.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>FTITLE reads data from the unit specified by the internal parameter 'ICU', which has the default value 5, to specify standard input; this parameter can be given a different value to specify that another unit should be read instead. 

 The input data are read in groups. Each group represents one title frame. There can be any number of groups. FTITLE keeps processing groups until a group with NCDS = 0 is read or an end-of-file is encountered. A group consists of the following:
<dl COMPACT><dt>&bull;
<dd>A header line from which variables NCDS, TIME, and SIZE are read, using the FORTRAN format &quot;(I5,2F5.1)&quot;.
<dd>NCDS is the number of text lines that follow. If NCDS = 0, FTITLE quits (returns to the calling routine without doing anything else).
<dd>TIME is the time, in seconds, that the title frame should be displayed (not including fade-in and fade-out, if any).
<dd>SIZE is the desired character size, given as a multiplier of the default height specified by the value of the internal parameter 'PSZ', the default value of which is 21 (out of 1023). Values of SIZE from .75 to 2.5 are recommended.
<dt>&bull;
<dd>Text lines, each containing one line of the title frame. PLOTCHAR function codes may be used as specified in the documentation for that package. Characters should not appear beyond column 80.</dl>
 

 The internal parameters 'ALN', 'BGB', 'BGC', 'BGF', 'BGG', 'BGR', 'FGB', 'FGC', 'FGF', 'FGG', 'FGR', 'FIN', 'FOU', 'GSZ', 'ICO', 'ICU', 'LOG', 'LX1', 'LX2', 'LY1', 'LY2', 'MAP', 'NFS', 'NXE', 'NXS', 'ORV', 'PSZ', 'SBK', 'SFG', 'TM1', 'TM2', 'TM3', 'VPB', 'VPL', 'VPR', 'VPT', and 'WID' all affect the behavior of FTITLE in one way or another. Some of these have been mentioned above; all are described in the &quot;man&quot; page for &quot;scrolled_title_params&quot;. 

 Example: Suppose the input file contains the following three lines 

 <pre> 3 3. 1.5
A
Frame
of Titles</pre>The resulting title frame has three lines of text. It is displayed for three seconds. Characters have a size of 1.5 times the default character size. 

 FTITLE allows a maximum of 80 characters per line of text including Plotchar function codes. No more than 120 lines of text can be displayed on a single frame. Titles are centered horizontally unless you have changed the value of the internal parameter 'ICO'. Vertical spacing is automatically determined using the current value of the internal parameter 'GSZ'. 

 For more detailed control of titles, use the routine STITLE, which can be used to generate either fixed or scrolled titles.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: slex02.
<h2>Access</h2>To use FTITLE or c_ftitle, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the scrolled_title man page for a description of all Scrolled_title error messages and/or informational messages.
<h2>See Also</h2>Online: plotchar, scrolled_title, scrolled_title_params, slgeti, slgetr, slogap, slrset, slseti, slsetr, stitle, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
