---
title: "tk_getvrootgeometry(3)"
name: "tk_getvrootgeometry"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getvrootgeometry/"
description: "Tk_GetVRootGeometry – Get location and size of virtual root for window"
---

<p>Tk_GetVRootGeometry &#8211; Get location and size of virtual root for window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_GetVRootGeometry(</code><i>tkwin, xPtr, yPtr, widthPtr, heightPtr</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window whose virtual root is to be queried.</p>
<dd>int <i>xPtr</i> (out) Points to word in which to store x-offset of virtual root.</p>
<dd>int <i>yPtr</i> (out) Points to word in which to store y-offset of virtual root.</p>
<dd>int <i>widthPtr</i> (out) Points to word in which to store width of virtual root.</p>
<dd>int <i>heightPtr</i> (out) Points to word in which to store height of virtual root. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetVRootGeometry</code> returns geometry information about the virtual root window associated with <i>tkwin</i>. The &#8220;associated&#8221; virtual root is the one in which <i>tkwin</i>&#8216;s nearest top-level ancestor (or <i>tkwin</i> itself if it is a top-level window) has been reparented by the window manager. This window is identified by a <code>__SWM_ROOT</code> or <code>__WM_ROOT</code> property placed on the top-level window by the window manager. If <i>tkwin</i> is not associated with a virtual root (e.g. because the window manager does not use virtual roots) then *<i>xPtr</i> and *<i>yPtr</i> will be set to 0 and *<i>widthPtr</i> and *<i>heightPtr</i> will be set to the dimensions of the screen containing <i>tkwin</i>. </p>
<h2>Keywords</h2>
<p>geometry, height, location, virtual root, width, window manager</p>
