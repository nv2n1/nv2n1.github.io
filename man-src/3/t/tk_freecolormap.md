---
title: "tk_freecolormap(3)"
name: "tk_freecolormap"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_freecolormap/"
description: "Tk_GetColormap, Tk_PreserveColormap, Tk_FreeColormap – allocate and free colormaps"
---

<p>Tk_GetColormap, Tk_PreserveColormap, Tk_FreeColormap &#8211; allocate and free colormaps </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Colormap
<code>Tk_GetColormap(</code><i>interp, tkwin, string</i><code>)</code>
<code>Tk_PreserveColormap(</code><i>display, colormap</i><code>)</code>
<code>Tk_FreeColormap(</code><i>display, colormap</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which colormap will be used.</p>
<dd>const char <i>*string</i> (in) Selects a colormap: either <code>new</code> or the name of a window with the same screen and visual as <i>tkwin</i>.</p>
<dd>Display <i>*display</i> (in) Display for which <i>colormap</i> was allocated.</p>
<dd>Colormap <i>colormap</i> (in) Colormap to free or preserve; must have been returned by a previous call to <code>Tk_GetColormap</code> or <code>Tk_GetVisual</code>.
</dl>
<h2>Description</h2>
<p>These procedures are used to manage colormaps. <code>Tk_GetColormap</code> returns a colormap suitable for use in <i>tkwin</i>. If its <i>string</i> argument is <code>new</code> then a new colormap is created; otherwise <i>string</i> must be the name of another window with the same screen and visual as <i>tkwin</i>, and the colormap from that window is returned. If <i>string</i> does not make sense, or if it refers to a window on a different screen from <i>tkwin</i> or with a different visual than <i>tkwin</i>, then <code>Tk_GetColormap</code> returns <code>None</code> and leaves an error message in <i>interp</i>&#8216;s result. </p>
<p> <code>Tk_PreserveColormap</code> increases the internal reference count for a colormap previously returned by <code>Tk_GetColormap</code>, which allows the colormap to be stored in several locations without knowing which order they will be released. </p>
<p> <code>Tk_FreeColormap</code> should be called when a colormap returned by <code>Tk_GetColormap</code> is no longer needed. Tk maintains a reference count for each colormap returned by <code>Tk_GetColormap</code>, so there should eventually be one call to <code>Tk_FreeColormap</code> for each call to <code>Tk_GetColormap</code> and each call to <code>Tk_PreserveColormap</code>. When a colormap&#8217;s reference count becomes zero, Tk releases the X colormap. </p>
<p> <code>Tk_GetVisual</code> and <code>Tk_GetColormap</code> work together, in that a new colormap created by <code>Tk_GetVisual</code> may later be returned by <code>Tk_GetColormap</code>. The reference counting mechanism for colormaps includes both procedures, so callers of <code>Tk_GetVisual</code> must also call <code>Tk_FreeColormap</code> to release the colormap. If <code>Tk_GetColormap</code> is called with a <i>string</i> value of <code>new</code> then the resulting colormap will never be returned by <code>Tk_GetVisual</code>; however, it can be used in other windows by calling <code>Tk_GetColormap</code> with the original window&#8217;s name as <i>string</i>.</p>
<h2>Keywords</h2>
<p>colormap, visual</p>
