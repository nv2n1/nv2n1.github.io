---
title: "ncl_gqasf(3)"
name: "ncl_gqasf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqasf/"
---

GQASF - (Inquire aspect source flags) - Inquires the values for the aspect source flags that determine whether primitive attributes are to be selected from individual settings or from &quot;bundle tables&quot;.
<h2>Synopsis</h2>CALL GQASF (ERRIND,LASF)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_asfs(Gint *err_ind, Gasfs *list_asf);
<h2>Description</h2><dl COMPACT><dt>ERRIND
</dt><dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
</dd><dt>LASF
</dt><dd>(Integer array, output) - An array of settings for the thirteen attributes:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt> 1
</dt><dd>Linetype
</dd><dt> 2
</dt><dd>Linewidth scale factor
</dd><dt> 3
</dt><dd>Polyline color index
</dd><dt> 4
</dt><dd>Marker type
</dd><dt> 5
</dt><dd>Marker size scale factor
</dd><dt> 6
</dt><dd>Polymarker color index
</dd><dt> 7
</dt><dd>Text font and precision
</dd><dt> 8
</dt><dd>Character expansion factor
</dd><dt> 9
</dt><dd>Character spacing
</dd><dt>10
</dt><dd>Text color index
</dd><dt>11
</dt><dd>Fill area interior style
</dd><dt>12
</dt><dd>Fill area style index
</dd><dt>13
</dt><dd>Fill area color index</dd></dl></dl>
 

 Each value of LASF is either &quot;0&quot; (for &quot;bundled&quot;) or &quot;1&quot; (for &quot;individual&quot;).</dl><h2>Usage</h2>In NCAR Graphics all attribute aspect source flags are defaulted to &quot;individual&quot; (all values for LASF are &quot;1&quot;). It is advised that for dependable results when using NCAR Graphics these values remain in their default settings. Some GKS packages default these values to &quot;bundled&quot;. GQASF can be called to determine the values of all aspect source flags.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gsasf, gsln, gslwsc, gsplci, gsmk, gsmksc, gspmci, gstxfp, gschxp, gstxsp, gstxci, gsfais, gsfasi, gsfaci, gqln, gqlwsc, gqplci, gqmk, gqmksc, gqpmci, gqtxfp, gqchxp, gqtxsp, gqtxci, gqfais, gqfasi, gqfaci,, ginq_asfs 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
