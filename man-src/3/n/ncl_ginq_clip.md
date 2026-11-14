---
title: "ncl_ginq_clip(3)"
name: "ncl_ginq_clip"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_clip/"
description: "ginq_clip (Inquire clipping indicator) – retrieves the current value of the clipping indicator as well as the current clipping rectangle."
---

<p>ginq_clip (Inquire clipping indicator) &#8211; retrieves the current value of the clipping indicator as well as the current clipping rectangle.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_clip(Gint *err_ind, Gclip *clip_ind_rect);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired values cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>clip_ind_rect.clip_ind</p>
<dd>(Output) &#8211; Returns the current value of the clipping indicator as set by default or by a call to gset_clip_ind.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GIND_NO_CLIP</p>
<dd>Clipping is off, or deactivated.</p>
<dt>GIND_CLIP</p>
<dd>Clipping is on. Data outside of the world coordinate window will not be plotted.</dl>
</dl>
<dt>clip_ind_rect.clip_rect</p>
<dd>(Glimit, Output) &#8211; Four normalized device coordinates providing the corner points of the current clipping rectangle.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>set(3NCARG),</code> <code>gset_clip_ind(3NCARG),</code> <code>gset_win(3NCARG),</code> <code>gsel_norm_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
