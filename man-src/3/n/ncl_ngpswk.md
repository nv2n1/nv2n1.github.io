---
title: "ncl_ngpswk(3)"
name: "ncl_ngpswk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngpswk/"
---

NGPSWK - returns the workstation type, suitable for use as the third argument in a call to the NCAR GKS routine GOPWK, for the PostScript workstation whose attributes are specified in the function arguments.

<h2>Synopsis</h2>

CALL NGPSWK(PSTYPE, ORIENT, COLOR)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngpswk(char *pstype, char *orient, char *color)

<h2>Description</h2>

<dl><dt>PSTYPE
<dd>(an input variable of type CHARACTER) specifying the type of the PostScript file. It can be one of:
<dl><dd><dl><dt>'PS'
<dd>regular PostScript
<dt>'EPS'
<dd>Encapsulated PostScript (can have only a single picture).
<dt>'EPSI'
<dd>Encapsulated PostScript Interchange format (an EPS file containing a preview bitmap).</dl></dl><dt>ORIENT
<dd>(an input variable of type CHARACTER) specifying the orientation of the output plot. It can be one of:
<dl><dd><dl><dt>'PORTRAIT'
<dd>portrait orientation (long side of page is vertical).
<dt>'LANDSCAPE'
<dd>landscape orientation (long side of the page is horizontal).</dl></dl><dt>COLOR
<dd>(an input variable of type CHARACTER) specifying whether the plot will be color or monochrome. It can be one of:
<dl><dd><dl><dt>'MONOCHROME'
<dd>the plot with be plotted with all graphics objects being plotted using the foreground color.
<dt>'COLOR'
<dd>the plot will be plotted using color, if available, or intensities obtained from the NTSC color to black-and-white intensity mapping if gray-scale is available.</dl></dl>
</dl>

<h2>C-Binding Description</h2>

The C binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

In specifying the arguments, only enough characters need be entered so that the values can be differentiated. For example, to specify color, using 'C' as the third argument would be sufficient. Either upper case or lower case is accepted.

<h2>Examples</h2>

The invocation: <pre> IWK = NGPSWK('EPS', 'LANDSCAPE', 'COLOR')</pre>would return the value &quot;27&quot; for IWK. This is the workstation type that would be used as the third argument in a call to the GKS function GOPWK for a workstation that would produce Encapsulated color Postscript in landscape mode.

<h2>Access</h2>

To use NGPSWK or c_ngpswk, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

Warning messages will be issued if one calls NGPSWK with unrecognizable arguments. The value 'PS' is used if the first argument is unrecognized; the value 'PORTRAIT' is used if the second argument is unrecognized; the value 'COLOR' is used if the third argument is unrecognized.

<h2>See Also</h2>

Online: gopwk(3NCARG), ncarg_gks(3NCARG), ncarg_cbind(3NCARG) 

 Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version;

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
