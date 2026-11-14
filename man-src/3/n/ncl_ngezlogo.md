---
title: "ncl_ngezlogo(3)"
name: "ncl_ngezlogo"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngezlogo/"
---

NGEZLOGO - Draws various NCAR and UCAR logos, the default being to draw an NCAR logo of reasonable size in the lower right corner of a plot. 

<h2>Synopsis</h2>CALL NGEZLOGO()
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ngezlogo()
<h2>Usage</h2>Call this subroutine to produce a logo. By default a call to this subroutine will draw an NCAR logo of reasonable size in the lower right corner of the plot. This will be a full-color logo for PostScript output, otherwise it will be a one-color logo. 

 Calls to the ngmisc paramter setting routines NGSETI and NGSETR can be used for more control over the ouput. Calls to these routines can reproduce the functionality of the subroutine NGLOGO, except that the requested logo will be plotted to all active workstations, rather than a specified one. Here is a list of control parameters and what they do:
<dl COMPACT><dd><dl COMPACT><dt>'LT'
<dd>- Use with NGSETI to specify the logo type. See the documentation for NGLOGO for a list of the logo types, or execute &quot;ncargex miex01&quot; for an example plot that lists the logo types. Default is 1.
<dt>'OS'
<dd>- Use with NGSETR to specify the logo size in normalized device coordinates (a number between 0. and 1.). For example, a size specification of 0.1 would give a logo size one-tenth the maximum plot height. Default is 0.07.
<dt>'OX'
<dd>- Use with NGSETR to specify the logo X-coordinate position in normalized device coordinates. Default is 0.93.
<dt>'OY'
<dd>- Use with NGSETR to specify the logo Y-coordinate position in normalized device coordinates. Default is 0.05.
<dt>'LC'
<dd>- Use with NGSETI to specify the logo color (except in the case of an NCAR logo being plotted to a PostScript workstation, in which case you will get the full-color logo). Default is 1.
<dt>'LB'
<dd>- Use with NGSETI to specify the secondary logo color (this is applicable only for logo type 5, in which case the secondary color is used for the text string &quot;UCAR&quot;). Default is 1.</dl></dl><h2>Examples</h2><pre><code>CALL NGEZLOGO()
Plots an NCAR logo on all active workstations in the lower right
corner of the plot.  In the case of PostScript output, a full-color
logo will be produced, otherwise a one-color logo will be produced.
Logo of type 2:

CALL NGSETI('LT',2)

CALL NGEZLOGO()</code></pre> Plots a UCAR logo (just the star) in the lower right corner of the plot.</dl><dt>More complete example:
<dd><dl COMPACT><dd>CALL NGSETI('LT',5) 
 CALL NGSETR('OX',0.5) 
 CALL NGSETR('OY',0.5) 
 CALL NGSETR('OS',0.1) 
 CALL NGSETI('LC',2) 
 CALL NGSETI('LB',3) 
 CALL NGEZLOGO() <pre><code>Plots a logo of type 5 (UCAR star with text &quot;UCAR&quot;) in the middle
of the plot with size one-tenth the maximum plot height using color
index 2 for the star and color index 3 for the text.
</code></pre>
<h2>Access</h2>To use NGEZLOGO or c_ngezlogo, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: nglogo, ngseti, ngsetr (3NCARG), 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2002 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
