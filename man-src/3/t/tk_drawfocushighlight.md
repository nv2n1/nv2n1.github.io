---
title: "tk_drawfocushighlight(3)"
name: "tk_drawfocushighlight"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_drawfocushighlight/"
description: "Tk_DrawFocusHighlight – draw the traversal highlight ring for a widget"
---

<p>Tk_DrawFocusHighlight &#8211; draw the traversal highlight ring for a widget </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_DrawFocusHighlight(</code><i>tkwin, gc, width, drawable</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Window for which the highlight is being drawn. Used to retrieve the window&#8217;s dimensions, among other things.</p>
<dd>GC <i>gc</i> (in) Graphics context to use for drawing the highlight.</p>
<dd>int <i>width</i> (in) Width of the highlight ring, in pixels.</p>
<dd>Drawable <i>drawable</i> (in) Drawable in which to draw the highlight; usually an offscreen pixmap for double buffering. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_DrawFocusHighlight</code> is a utility procedure that draws the traversal highlight ring for a widget. It is typically invoked by widgets during redisplay. </p>
<h2>Keywords</h2>
<p>focus, traversal highlight</p>
