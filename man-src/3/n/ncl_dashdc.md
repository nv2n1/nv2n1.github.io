---
title: "ncl_dashdc(3)"
name: "ncl_dashdc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dashdc/"
---

DASHDC - Defines a dash pattern with labels. If DASHDC is called when the &quot;quick&quot; version of Dashline is used, an error exit results. 

<h2>Synopsis</h2>CALL DASHDC (IPAT,JCRT,JSIZE)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dashdc (char *ipat, int jcrt, int jsize)
<h2>Description</h2><dl COMPACT><dt>IPAT
<dd>(an input constant or variable of type CHARACTER) specifies the dash pattern to be used. Although IPAT is of arbitrary length, 60 characters seems to be a practical limit. This pattern is repeated for successive line segments until the full line is drawn. A dollar sign in IPAT indicates solid; an apostrophe indicates a gap; blanks are ignored. Any character in IPAT which is not a dollar sign, apostrophe, or blank is considered to be part of a line label. Each line label can be at most 15 characters in length. Sufficient white space is reserved in the dashed line for writing line labels.
<dt>JCRT
<dd>(an input expression of type INTEGER) specifies that the length to be assigned to each increment of the line pattern is (JCRT/1023.) NDCs (Normalized Device Coordinates). Each increment is either a gap (represented by a dollar sign in IPAT) or a line segment (represented by an apostrophe in IPAT). JCRT must be greater than or equal to 1.
<dt>JSIZE
<dd>(an input expression of type INTEGER) specifies the width of the plotted characters, as follows:
<dl COMPACT><dd><dl COMPACT><dt> 0
<dd>.0078 NDCs
<dt> 1
<dd>.0117 NDCs
<dt> 2
<dd>.0156 NDCs
<dt> 3
<dd>.0234 NDCs
<dt>&gt;3
<dd>JSIZE/1023. NDCs</dl></dl>
</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdashc, tdashp, tdashs, fcoord1, fcoord2, fdldashc, fdldashd.
<h2>Usage</h2>DASHDC may be called to define a dash pattern for any of the four versions of Dashline except the &quot;quick&quot; version; if you call it when the &quot;quick&quot; version is in use, an error exit will result. 

 A dash pattern defined by a call to DASHDC will supersede one defined by an earlier call to DASHDB or DASHDC.
<h2>Access</h2>To use DASHDC or c_dashdc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashline, dashline_params, curved, dashdb, frstd, lastd, lined, reset, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
