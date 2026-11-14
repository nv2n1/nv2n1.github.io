---
title: "ncl_scrolled_title(3)"
name: "ncl_scrolled_title"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_scrolled_title/"
---

Scrolled_title - Creates movie titles. The titles can be scrolled, faded in, and/or faded out. Foreground and background colors can be specified.

<h2>Synopsis</h2>

The package Scrolled_title has eight user entry points, as follows: FTITLE, STITLE, SLGETI, SLGETR, SLOGAP, SLSETI, SLSETR, and SLRSET.
<dl><dt>FTITLE
<dd>stands for &quot;fixed titles&quot; and is used when the following conditions are met:
<dl><dd><dl><dt>&bull;
<dd>Each group of text lines is to fit on one frame (no scrolling).
<dt>&bull;
<dd>All test lines in a group are to be written in the same color.
<dt>&bull;
<dd>Vertical spacing of text lines is to be done automatically.
<dt>&bull;
<dd>Text lines are to be centered horizontally.
<dt>&bull;
<dd>There are to be no more than 80 characters per text line (including Plotchar &quot;function codes&quot;).
<dt>&bull;
<dd>In production mode, blank frames are to be generated before and after each group of title frames.
<dt>&bull;
<dd>No more than 120 text lines are to be displayed on a single frame.</dl></dl><dt>STITLE
<dd>stands for &quot;scrolled titles&quot; and is used when the above conditions are not met.
<dt>SLOGAP
<dd>is used to generate blank-frame gaps in a manner consistent with FTITLE.
<dt>SLSETI and SLSETR
<dd>are used to set the values of &quot;internal parameters&quot; whose values affect the behavior of FTITLE and/or STITLE.
<dt>SLGETI and SLGETR
<dd>are used to retrieve the current values of internal parameters.
<dt>SLRSET
<dd>is ued to reset the values of all internal parameters of STITLE to the original defaults.</dl>

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 c_ftitle 
 c_stitle 
 c_slogap 
 c_slseti 
 c_slsetr 
 c_slgeti 
 c_slgetr 
 c_slrset

<h2>Access</h2>

To use Scrolled_title routines, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>Messages</h2>

The error messages described can be written to the output unit by routines in the package Scrolled_title. Unless otherwise indicated, these errors are fatal and cause the user's program to terminate execution. 

 FTITLE - PREMATURE EOF ON CARD INPUT UNIT 

 FTITLE has encountered an end-of-file on the card input in a place where one should not have been. 

 FTITLE - READ ERROR ON CARD INPUT UNIT 

 FTITLE has executed a FORTRAN READ statement and the &quot;ERR=...&quot; exit has been taken. 

 FTITLE - TOO MANY INPUT CARDS IN GROUP 

 The first card of a title group contains a value of NCDS greater than 120. FTITLE can't handle that many lines. 

 FTITLE - UNCLEARED PRIOR ERROR 

 When FTITLE was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it. 

 SLBKGD - ERROR RETURN FROM GQFACI: i 
 SLBKGD - ERROR RETURN FROM GQFAIS: I 

 A GKS routine has returned a non-zero error flag with value &quot;i&quot;. This most likely means that GKS is in the wrong state. 

 SLGCLR - TOO MANY COLORS DEFINED 

 More than 256 colors have been made known to STITLE. It has no room in which to maintain information about them all. 

 SLGETI - UNCLEARED PRIOR ERROR 

 When SLGETI was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it. 

 SLGETR -- INVALID KEYWORD: xxx 

 The first argument in a call to SLGETR is not the name of one of the known internal parameters of STITLE. This error message can occur as the result of a call to SLGETI. 

 SLGETR - UNCLEARED PRIOR ERROR 

 When SLGETR was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it. 

 SLGWID - ERROR RETURN FROM GQACWK: i 

 A GKS routine has returned a non-zero error flag with value &quot;i&quot;. This most likely means that GKS is in the wrong state. 

 SLGWID - NO ACTIVE WORKSTATIONS 

 STITLE uses the routine SLGWID to determine the ID of the first active workstation (to use in calls dealing with color) and it has found that there are currently no active workstations at all. 

 SLOGAP - ERROR RETURN FROM GQTXCI: i 

 A GKS routine has returned a non-zero error flag with value &quot;i&quot;. This most likely means that GKS is in the wrong state. 

 SLOGAP - UNCLEARED PRIOR ERROR 

 When SLOGAP was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it. 

 SLRSET - UNCLEARED PRIOR ERROR 

 When SLOGAP was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it. 

 SLSCLR - TOO MANY COLORS DEFINED 

 More than 256 colors have been made known to STITLE. It has no room in which to maintain information about them all. 

 SLSETI - UNCLEARED PRIOR ERROR 

 When SLSETI was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it. 

 SLSETR -- INVALID KEYWORD: xxx 

 The first argument in a call to SLSETR is not the name of one of the known internal parameters of STITLE. This error message can occur as the result of a call to SLSETI. 

 SLSETR - UNCLEARED PRIOR ERROR 

 When SLSETR was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it. 

 STITLE - ERROR RETURN FROM GQCLIP: i 
 STITLE - ERROR RETURN FROM GQCNTN: i 
 STITLE - ERROR RETURN FROM GQPLCI: i 
 STITLE - ERROR RETURN FROM GQPMCI: i 
 STITLE - ERROR RETURN FROM GQTXCI: i 

 A GKS routine has returned a non-zero error flag with value &quot;i&quot;. This most likely means that GKS is in the wrong state. 

 STITLE - UNCLEARED PRIOR ERROR 

 When STITLE was called, there was an unrecovered outstanding error. The routine does not continue; it forces the error message to be printed and then substitutes this one for it.

<h2>See Also</h2>

Online: ftitle, scrolled_title_params.m slgeti, slgetr, slogap, slrset, slseti, slsetr, stitle, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
