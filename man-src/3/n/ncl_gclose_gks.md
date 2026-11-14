---
title: "ncl_gclose_gks(3)"
name: "ncl_gclose_gks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclose_gks/"
description: "gclose_gks (Close GSK) – closes the GKS package."
---

<p>gclose_gks (Close GSK) &#8211; closes the GKS package.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gclose_gks( void );</p>
<h2>Usage</h2>
<p>A call to gclose_gks insures that the graphics package is properly terminated. No graphics calls depending on GKS should be made during the time that GKS is closed. If output to a CGM has been the exclusive requirement of the graphics job, and the SPPS entry c_opngks has been used to open GKS and to open and activate a CGM workstation, then c_clsgks can be used to deactivate and close the CGM workstation, and to close GKS, making a direct call to gclose_gks unnecessary in that case.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gopen_gks(3NCARG),</code> <code>gopen_ws(3NCARG),</code> <code>gactivate_ws(3NCARG),</code> <code>gdeactivate_ws(3NCARG),</code> <code>gclose_ws(3NCARG),</code> <code>gupwk(3NCARG),</code> <code>opngks(3NCARG),</code> <code>clsgks(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
