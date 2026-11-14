---
title: "ncl_gsasf(3)"
name: "ncl_gsasf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsasf/"
---

GSASF - (Set aspect source flags) - Sets the aspect source flags that determine whether primitive attributes are to be selected from individual settings or from &quot;bundle tables&quot;.
<h2>Synopsis</h2>CALL GSASF (LASF)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_asfs(const Gasfs *list_asf);
<h2>Description</h2><dl COMPACT><dt>LASF
<dd>(Integer array, input) - An array of settings for the thirteen attributes:
<dl COMPACT><dd><dl COMPACT><dt> 1
<dd>Linetype
<dt> 2
<dd>Linewidth scale factor
<dt> 3
<dd>Polyline color index
<dt> 4
<dd>Marker type
<dt> 5
<dd>Marker size scale factor
<dt> 6
<dd>Polymarker color index
<dt> 7
<dd>Text font and precision
<dt> 8
<dd>Character expansion factor
<dt> 9
<dd>Character spacing
<dt>10
<dd>Text color index
<dt>11
<dd>Fill area interior style
<dt>12
<dd>Fill area style index
<dt>13
<dd>Fill area color index</dl></dl>
 

 Each value of LASF is either &quot;0&quot; (for &quot;bundled&quot;) or &quot;1&quot; (for &quot;individual&quot;).</dl><h2>Usage</h2>In NCAR Graphics all attribute aspect source flags are defaulted to &quot;individual&quot; (all values for LASF are &quot;1&quot;). It is advised that for dependable results when using NCAR Graphics these values remain in their default settings. Some GKS packages default these values to &quot;bundled&quot;, so, if one expects to use such a package, it would be precautionary to call GSASF to set all aspect source flags to &quot;1&quot; before calling other GKS functions.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gqasf, gsln, gslwsc, gsplci, gsmk, gsmksc, gspmci, gstxfp, gschxp, gstxsp, gstxci, gsfais, gsfasi, gsfaci, gqln, gqlwsc, gqplci, gqmk, gqmksc, gqpmci, gqtxfp, gqchxp, gqtxsp, gqtxci, gqfais, gqfasi, gqfaci,, gset_asfs 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
