---
title: "ncl_slogap(3)"
name: "ncl_slogap"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_slogap/"
---

SLOGAP - Generates TIME seconds worth of blank frames in a manner consistent with FTITLE.

<h2>Synopsis</h2>

CALL SLOGAP (TIME,MTST)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_slogap (float time, int mtst)

<h2>Description</h2>

<dl><dt>TIME
<dd>(an input expression of type REAL) specifies the number of seconds worth of blank frames to be generated.
<dt>MTST
<dd>(an input expression of type INTEGER) is a switch to indicate whether this is a &quot;real&quot; run or a &quot;practice&quot; run.
<dl><dd><dl><dt>0
<dd>means &quot;real run&quot;.
<dt>1
<dd>means &quot;practice run&quot;.</dl></dl><dd>During real runs, the blank frames themselves are created. 

 During practice runs, a single frame is created with a legend saying how many seconds of blank frames it stands for.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to output blank frames in a manner consistent with FTITLE.

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: slex02.

<h2>Access</h2>

To use SLOGAP or c_slogap, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the scrolled_title man page for a description of all Scrolled_title error messages and/or informational messages.

<h2>See Also</h2>

Online: ftitle, scrolled_title, scrolled_title_params, slgeti, slgetr, slrset, slseti, slsetr, stitle, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
