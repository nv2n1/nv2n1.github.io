---
title: "ncl_gstxfp(3)"
name: "ncl_gstxfp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gstxfp/"
---

GSTXFP (Set text font and precision) - sets the text font and precision.
<h2>Synopsis</h2>CALL GSTXFP (FONT, PREC)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_text_font_prec(const Gtext_font_prec *text_font_prec);
<h2>Description</h2><dl COMPACT><dt>FONT
<dd>(Integer, Input) - Specifies the text font to be used in subsequent calls to the GTX output primitive. Options are:
<dl COMPACT><dd><dl COMPACT><dt> 1
<dd>ASCII font (default)
<dt> -2
<dd>Hershey cartographic Roman
<dt> -3
<dd>Hershey cartographic Greek
<dt> -4
<dd>Hershey simplex Roman
<dt> -5
<dd>Hershey simplex Greek
<dt> -6
<dd>Hershey simplex script
<dt> -7
<dd>Hershey complex Roman
<dt> -8
<dd>Hershey complex Greek
<dt> -9
<dd>Hershey complex script
<dt>-10
<dd>Hershey complex italic
<dt>-11
<dd>Hershey complex Cyrillic
<dt>-12
<dd>Hershey duplex Roman
<dt>-13
<dd>Hershey triplex Roman
<dt>-14
<dd>Hershey triplex italic
<dt>-15
<dd>Hershey Gothic German
<dt>-16
<dd>Hershey Gothic English
<dt>-17
<dd>Hershey Gothic Italian
<dt>-18
<dd>Hershey math symbols
<dt>-19
<dd>Hershey symbol set 1
<dt>-20
<dd>Hershey symbol set 2</dl>
 

 The Hershey fonts are not standardized by GKS but are locally implemented in NCAR GKS-0A. GKS requires that such locally implemented fonts be assigned negative font numbers. To view the Hershey fonts, look at the plots produced from the PLOTCHAR example (execute &quot;ncargex epltch&quot; to get a metafile) and examine the plot titled &quot;PLCHHQ - FONTCAP DATABASES ADDED 6/90&quot;. The font numbers there are the absolute values of the value for FONT described here (PLOTCHAR has no need to follow the strictures that GKS imposes on font names for GSTXFP).</dl><dt>PREC
<dd>(Integer, Input) - Gives the precision used in subsequent calls to the GTX output primitive for font type FONT. Options are:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>String precision (good). This is the GKS default.
<dt>1
<dd>Character precision (better).
<dt>2
<dd>Stroke precision (best). This is the default for NCAR GSK-0A.</dl></dl>
</dl><h2>Usage</h2>If one accesses the Hershey fonts via GSTXFP and GTX, then the characters are not stroked until viewing time. If one accesses the Hershey fonts via PLOTCHAR, then the characters are stroked by PLOTCHAR itself. This can make a significant difference in metafile sizes.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_text_font_prec 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
