---
title: "tk_getrootcoords(3)"
name: "tk_getrootcoords"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getrootcoords/"
description: "Tk_GetRootCoords – Compute root-window coordinates of window"
---

<p>Tk_GetRootCoords &#8211; Compute root-window coordinates of window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_GetRootCoords</code>(<i>tkwin, xPtr, yPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>int <i>*xPtr</i> (out) Pointer to location in which to store root-window x-coordinate corresponding to left edge of <i>tkwin</i>&#8216;s border.</p>
<dd>int <i>*yPtr</i> (out) Pointer to location in which to store root-window y-coordinate corresponding to top edge of <i>tkwin</i>&#8216;s border.
</dl>
<h2>Description</h2>
<p>This procedure scans through the structural information maintained by Tk to compute the root-window coordinates corresponding to the upper-left corner of <i>tkwin</i>&#8216;s border. If <i>tkwin</i> has no border, then <code>Tk_GetRootCoords</code> returns the root-window coordinates corresponding to location (0,0) in <i>tkwin</i>. <code>Tk_GetRootCoords</code> is relatively efficient, since it does not have to communicate with the X server.</p>
<h2>Keywords</h2>
<p>coordinates, root window</p>
