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
</dt><dd>(Integer, Input) - Specifies the text font to be used in subsequent calls to the GTX output primitive. Options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt> 1
</dt><dd>ASCII font (default)
</dd><dt> -2
</dt><dd>Hershey cartographic Roman
</dd><dt> -3
</dt><dd>Hershey cartographic Greek
</dd><dt> -4
</dt><dd>Hershey simplex Roman
</dd><dt> -5
</dt><dd>Hershey simplex Greek
</dd><dt> -6
</dt><dd>Hershey simplex script
</dd><dt> -7
</dt><dd>Hershey complex Roman
</dd><dt> -8
</dt><dd>Hershey complex Greek
</dd><dt> -9
</dt><dd>Hershey complex script
</dd><dt>-10
</dt><dd>Hershey complex italic
</dd><dt>-11
</dt><dd>Hershey complex Cyrillic
</dd><dt>-12
</dt><dd>Hershey duplex Roman
</dd><dt>-13
</dt><dd>Hershey triplex Roman
</dd><dt>-14
</dt><dd>Hershey triplex italic
</dd><dt>-15
</dt><dd>Hershey Gothic German
</dd><dt>-16
</dt><dd>Hershey Gothic English
</dd><dt>-17
</dt><dd>Hershey Gothic Italian
</dd><dt>-18
</dt><dd>Hershey math symbols
</dd><dt>-19
</dt><dd>Hershey symbol set 1
</dd><dt>-20
</dt><dd>Hershey symbol set 2</dd></dl>
 

 The Hershey fonts are not standardized by GKS but are locally implemented in NCAR GKS-0A. GKS requires that such locally implemented fonts be assigned negative font numbers. To view the Hershey fonts, look at the plots produced from the PLOTCHAR example (execute &quot;ncargex epltch&quot; to get a metafile) and examine the plot titled &quot;PLCHHQ - FONTCAP DATABASES ADDED 6/90&quot;. The font numbers there are the absolute values of the value for FONT described here (PLOTCHAR has no need to follow the strictures that GKS imposes on font names for GSTXFP).</dl><dt>PREC
</dt><dd>(Integer, Input) - Gives the precision used in subsequent calls to the GTX output primitive for font type FONT. Options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>0
</dt><dd>String precision (good). This is the GKS default.
</dd><dt>1
</dt><dd>Character precision (better).
</dd><dt>2
</dt><dd>Stroke precision (best). This is the default for NCAR GSK-0A.</dd></dl></dl>
</dl><h2>Usage</h2>If one accesses the Hershey fonts via GSTXFP and GTX, then the characters are not stroked until viewing time. If one accesses the Hershey fonts via PLOTCHAR, then the characters are stroked by PLOTCHAR itself. This can make a significant difference in metafile sizes.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_text_font_prec 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
