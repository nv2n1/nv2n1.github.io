---
title: "tk_setgrid(3)"
name: "tk_setgrid"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_setgrid/"
description: "Tk_SetGrid, Tk_UnsetGrid – control the grid for interactive resizing"
---

<p>Tk_SetGrid, Tk_UnsetGrid &#8211; control the grid for interactive resizing </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_SetGrid</code>(<i>tkwin, reqWidth, reqHeight, widthInc, heightInc</i>)
<code>Tk_UnsetGrid</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>int <i>reqWidth</i> (in) Width in grid units that corresponds to the pixel dimension <i>tkwin</i> has requested via <code>Tk_GeometryRequest</code>.</p>
<dd>int <i>reqHeight</i> (in) Height in grid units that corresponds to the pixel dimension <i>tkwin</i> has requested via <code>Tk_GeometryRequest</code>.</p>
<dd>int <i>widthInc</i> (in) Width of one grid unit, in pixels.</p>
<dd>int <i>heightInc</i> (in) Height of one grid unit, in pixels. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_SetGrid</code> turns on gridded geometry management for <i>tkwin</i>&#8216;s toplevel window and specifies the geometry of the grid. <code>Tk_SetGrid</code> is typically invoked by a widget when its <code>setGrid</code> option is true. It restricts interactive resizing of <i>tkwin</i>&#8216;s toplevel window so that the space allocated to the toplevel is equal to its requested size plus or minus even multiples of <i>widthInc</i> and <i>heightInc</i>. Furthermore, the <i>reqWidth</i> and <i>reqHeight</i> values are passed to the window manager so that it can report the window&#8217;s size in grid units during interactive resizes. If <i>tkwin</i>&#8216;s configuration changes (e.g., the size of a grid unit changes) then the widget should invoke <code>Tk_SetGrid</code> again with the new information. </p>
<p> <code>Tk_UnsetGrid</code> cancels gridded geometry management for <i>tkwin</i>&#8216;s toplevel window. </p>
<p> For each toplevel window there can be at most one internal window with gridding enabled. If <code>Tk_SetGrid</code> or <code>Tk_UnsetGrid</code> is invoked when some other window is already controlling gridding for <i>tkwin</i>&#8216;s toplevel, the calls for the new window have no effect. </p>
<p> See the <code>wm</code> manual entry for additional information on gridded geometry management. </p>
<h2>Keywords</h2>
<p>grid, window, window manager</p>
