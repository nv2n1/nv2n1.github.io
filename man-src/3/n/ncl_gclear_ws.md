---
title: "ncl_gclear_ws(3)"
name: "ncl_gclear_ws"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclear_ws/"
description: "gclear_ws (Clear workstation) – clears a workstation."
---

<p>gclear_ws (Clear workstation) &#8211; clears a workstation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gclear_ws(Gint ws_id, Gctrl_flag ctrl_flag);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</p>
<dd>(Input) &#8211; A number identifying the workstation to be cleared. ws_id must be the same as that used in some previous gopen_ws call.</p>
<dt>ctrl_flag</p>
<dd>(Input) &#8211; Clear the workstation display surface. Options are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GFLAG_COND</p>
<dd>Check to see if the display surface is empty. If so, do not issue a clear surface command.</p>
<dt>GFLAG_ALWAYS</p>
<dd>Issue a clear surface command whether the surface has been written to or not.</dl>
</dl>
</dl>
<h2>Usage</h2>
<p>For workstations of type &quot;1&quot; (CGM), gclear_ws is interpreted as a picture termination in CGM generation. If ctrl_flag = GFLAG_COND and no output primitives have been written in the current picture, then a call to gclear_ws is a &quot;do nothing&quot;; otherwise, it generates an END PICTURE element (as well as other picture initializing elements). If ctrl_flag = GFLAG_ALWAYS, then a call to gclear_ws generates an END PICTURE. </p>
<p> For workstations of types &quot;7&quot; or &quot;8&quot; (see the man page for gopen_ws for a description of workstation types) clear workstations erases all primitives that appear on the screen. </p>
<p> For all other workstation types, clear workstation simply updates the workstation.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gopen_ws(3NCARG),</code> <code>gactivate_ws(3NCARG),</code> <code>gdeactivate_ws(3NCARG),</code> <code>gclose_ws(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
