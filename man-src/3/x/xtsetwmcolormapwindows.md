---
title: "xtsetwmcolormapwindows(3)"
name: "xtsetwmcolormapwindows"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetwmcolormapwindows/"
description: "XtSetWMColormapWindows – Set the value of the WM_COLORMAP_WINDOWS property"
---

<p>XtSetWMColormapWindows &#8211; Set the value of the WM_COLORMAP_WINDOWS property </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtSetWMColormapWindows(Widget <i>widget</i>, Widget* <i>list</i>, Cardinal <i>count</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget on whose window the WM_COLORMAP_WINDOWS property will be stored. Must be of class Core or any subclass thereof.</p>
<dt><i>list</i></p>
<dd>Specifies a list of widgets whose windows are are potentially to be listed in the WM_COLORMAP_WINDOWS property.</p>
<dt><i>count</i></p>
<dd>Specifies the number of widgets in <i>list</i>.</dl>
<h2>Description</h2>
<p><code>XtSetWMColormapWindows</code> returns immediately if <i>widget</i> is not realized or if <i>count</i> is zero. Otherwise, <code>XtSetWMColormapWindows</code> constructs an ordered list of windows by examining each widget in <i>list</i> in turn and ignoring the widget if it is not realized, or adding the widget&#8217;s window to the window list if the widget is realized and its colormap resource is different from the colormap resources of all widgets whose windows are already on the window list. </p>
<p> Finally, <code>XtSetWMColormapWindows</code> stores the resulting window list in the WM_COLORMAP_WINDOWS property on the specified widget&#8217;s window.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
