---
title: "tk_getvisual(3)"
name: "tk_getvisual"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getvisual/"
description: "Tk_GetVisual – translate from string to visual"
---

<p>Tk_GetVisual &#8211; translate from string to visual </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Visual *
<code>Tk_GetVisual(</code><i>interp, tkwin, string, depthPtr, colormapPtr</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which the visual will be used.</p>
<dd>const char <i>*string</i> (in) String that identifies the desired visual. See below for valid formats.</p>
<dd>int <i>*depthPtr</i> (out) Depth of returned visual gets stored here.</p>
<dd>Colormap <i>*colormapPtr</i> (out) If non-NULL then a suitable colormap for visual is found and its identifier is stored here.
</dl>
<h2>Description</h2>
<p><code>Tk_GetVisual</code> takes a string description of a visual and finds a suitable X Visual for use in <i>tkwin</i>, if there is one. It returns a pointer to the X Visual structure for the visual and stores the number of bits per pixel for it at <i>*depthPtr</i>. If <i>string</i> is unrecognizable or if no suitable visual could be found, then NULL is returned and <code>Tk_GetVisual</code> leaves an error message in <i>interp-&gt;result</i>. If <i>colormap</i> is non-NULL then <code>Tk_GetVisual</code> also locates an appropriate colormap for use with the result visual and stores its X identifier at <i>*colormapPtr</i>. </p>
<p> The <i>string</i> argument specifies the desired visual in one of the following ways:</p>
<dl COMPACT>
<dt><i>class depth</i></p>
<dd>The string consists of a class name followed by an integer depth, with any amount of white space (including none) in between. <i>class</i> selects what sort of visual is desired and must be one of <code>directcolor</code>, <code>grayscale</code>, <code>greyscale</code>, <code>pseudocolor</code>, <code>staticcolor</code>, <code>staticgray</code>, <code>staticgrey</code>, or <code>truecolor</code>, or a unique abbreviation. <i>depth</i> specifies how many bits per pixel are needed for the visual. If possible, <code>Tk_GetVisual</code> will return a visual with this depth; if there is no visual of the desired depth then <code>Tk_GetVisual</code> looks first for a visual with greater depth, then one with less depth.</p>
<dt><code>default</code></p>
<dd>Use the default visual for <i>tkwin</i>&#8216;s screen.</p>
<dt><i>pathName</i></p>
<dd>Use the visual for the window given by <i>pathName</i>. <i>pathName</i> must be the name of a window on the same screen as <i>tkwin</i>.</p>
<dt><i>number</i></p>
<dd>Use the visual whose X identifier is <i>number</i>.</p>
<dt><code>best</code> ?<i>depth</i>?</p>
<dd>Choose the &#8220;best possible&#8221; visual, using the following rules, in decreasing order of priority:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>(a)</p>
<dd>a visual that has exactly the desired depth is best, followed by a visual with greater depth than requested (but as little extra as possible), followed by a visual with less depth than requested (but as great a depth as possible);</p>
<dt>(b)</p>
<dd>if no <i>depth</i> is specified, then the deepest available visual is chosen;</p>
<dt>(c)</p>
<dd><code>pseudocolor</code> is better than <code>truecolor</code> or <code>directcolor</code>, which are better than <code>staticcolor</code>, which is better than <code>staticgray</code> or <code>grayscale</code>;</p>
<dt>(d)</p>
<dd>the default visual for the screen is better than any other visual.</dl>
</dl>
</dl>
<h2>Credits</h2>
<p>The idea for <code>Tk_GetVisual</code>, and the first implementation, came from Paul Mackerras.</p>
<h2>Keywords</h2>
<p>colormap, screen, visual</p>
