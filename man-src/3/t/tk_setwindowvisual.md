---
title: "tk_setwindowvisual(3)"
name: "tk_setwindowvisual"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_setwindowvisual/"
description: "Tk_SetWindowVisual – change visual characteristics of window"
---

<p>Tk_SetWindowVisual &#8211; change visual characteristics of window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_SetWindowVisual</code>(<i>tkwin, visual, depth, colormap</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>Visual <i>*visual</i> (in) New visual type to use for <i>tkwin</i>.</p>
<dd>int <i>depth</i> (in) Number of bits per pixel desired for <i>tkwin</i>.</p>
<dd>Colormap <i>colormap</i> (in) New colormap for <i>tkwin</i>, which must be compatible with <i>visual</i> and <i>depth</i>. </p>
</dl>
<h2>Description</h2>
<p>When Tk creates a new window it assigns it the default visual characteristics (visual, depth, and colormap) for its screen. <code>Tk_SetWindowVisual</code> may be called to change them. <code>Tk_SetWindowVisual</code> must be called before the window has actually been created in X (e.g. before <code>Tk_MapWindow</code> or <code>Tk_MakeWindowExist</code> has been invoked for the window). The safest thing is to call <code>Tk_SetWindowVisual</code> immediately after calling <code>Tk_CreateWindow</code>. If <i>tkwin</i> has already been created before <code>Tk_SetWindowVisual</code> is called then it returns 0 and does not make any changes; otherwise it returns 1 to signify that the operation completed successfully. </p>
<p> Note: <code>Tk_SetWindowVisual</code> should not be called if you just want to change a window&#8217;s colormap without changing its visual or depth; call <code>Tk_SetWindowColormap</code> instead. </p>
<h2>Keywords</h2>
<p>colormap, depth, visual</p>
