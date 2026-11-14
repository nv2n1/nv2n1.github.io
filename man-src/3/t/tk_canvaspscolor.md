---
title: "tk_canvaspscolor(3)"
name: "tk_canvaspscolor"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_canvaspscolor/"
description: "Tk_CanvasPsY, Tk_CanvasPsBitmap, Tk_CanvasPsColor, Tk_CanvasPsFont, Tk_CanvasPsPath, Tk_CanvasPsStipple – utility procedures for generating Postscript for canvases"
---

<p>Tk_CanvasPsY, Tk_CanvasPsBitmap, Tk_CanvasPsColor, Tk_CanvasPsFont, Tk_CanvasPsPath, Tk_CanvasPsStipple &#8211; utility procedures for generating Postscript for canvases </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
double
<code>Tk_CanvasPsY</code>(<i>canvas, canvasY</i>)
int
<code>Tk_CanvasPsBitmap</code>(<i>interp, canvas, bitmap, x, y, width, height</i>)
int
<code>Tk_CanvasPsColor</code>(<i>interp, canvas, colorPtr</i>)
int
<code>Tk_CanvasPsFont</code>(<i>interp, canvas, tkFont</i>)
<code>Tk_CanvasPsPath</code>(<i>interp, canvas, coordPtr, numPoints</i>)
int
<code>Tk_CanvasPsStipple</code>(<i>interp, canvas, bitmap</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Canvas <i>canvas</i> (in) A token that identifies a canvas widget for which Postscript is being generated.</p>
<dd>double <i>canvasY</i> (in) Y-coordinate in the space of the canvas.</p>
<dd>Tcl_Interp <i>*interp</i> (in/out) A Tcl interpreter; Postscript is appended to its result, or the result may be replaced with an error message.</p>
<dd>Pixmap <i>bitmap</i> (in) Bitmap to use for generating Postscript.</p>
<dd>int <i>x</i> (in) X-coordinate within <i>bitmap</i> of left edge of region to output.</p>
<dd>int <i>y</i> (in) Y-coordinate within <i>bitmap</i> of top edge of region to output.</p>
<dd>int <i>width</i> (in) Width of region of bitmap to output, in pixels.</p>
<dd>int <i>height</i> (in) Height of region of bitmap to output, in pixels.</p>
<dd>XColor <i>*colorPtr</i> (in) Information about color value to set in Postscript.</p>
<dd>Tk_Font <i>tkFont</i> (in) Font for which Postscript is to be generated.</p>
<dd>double <i>*coordPtr</i> (in) Pointer to an array of coordinates for one or more points specified in canvas coordinates. The order of values in <i>coordPtr</i> is x1, y1, x2, y2, x3, y3, and so on.</p>
<dd>int <i>numPoints</i> (in) Number of points at <i>coordPtr</i>. </p>
</dl>
<h2>Description</h2>
<p>These procedures are called by canvas type managers to carry out common functions related to generating Postscript. Most of the procedures take a <i>canvas</i> argument, which refers to a canvas widget for which Postscript is being generated. </p>
<p> <code>Tk_CanvasPsY</code> takes as argument a y-coordinate in the space of a canvas and returns the value that should be used for that point in the Postscript currently being generated for <i>canvas</i>. Y coordinates require transformation because Postscript uses an origin at the lower-left corner whereas X uses an origin at the upper-left corner. Canvas x coordinates can be used directly in Postscript without transformation. </p>
<p> <code>Tk_CanvasPsBitmap</code> generates Postscript to describe a region of a bitmap. The Postscript is generated in proper image data format for Postscript, i.e., as data between angle brackets, one bit per pixel. The Postscript is appended to <i>interp-&gt;result</i> and <code>TCL_OK</code> is returned unless an error occurs, in which case <code>TCL_ERROR</code> is returned and <i>interp-&gt;result</i> is overwritten with an error message. </p>
<p> <code>Tk_CanvasPsColor</code> generates Postscript to set the current color to correspond to its <i>colorPtr</i> argument, taking into account any color map specified in the <code>postscript</code> command. It appends the Postscript to <i>interp-&gt;result</i> and returns <code>TCL_OK</code> unless an error occurs, in which case <code>TCL_ERROR</code> is returned and <i>interp-&gt;result</i> is overwritten with an error message. </p>
<p> <code>Tk_CanvasPsFont</code> generates Postscript that sets the current font to match <i>tkFont</i> as closely as possible. <code>Tk_CanvasPsFont</code> takes into account any font map specified in the <code>postscript</code> command, and it does the best it can at mapping X fonts to Postscript fonts. It appends the Postscript to <i>interp-&gt;result</i> and returns <code>TCL_OK</code> unless an error occurs, in which case <code>TCL_ERROR</code> is returned and <i>interp-&gt;result</i> is overwritten with an error message. </p>
<p> <code>Tk_CanvasPsPath</code> generates Postscript to set the current path to the set of points given by <i>coordPtr</i> and <i>numPoints</i>. It appends the resulting Postscript to <i>interp-&gt;result</i>. </p>
<p> <code>Tk_CanvasPsStipple</code> generates Postscript that will fill the current path in stippled fashion. It uses <i>bitmap</i> as the stipple pattern and the current Postscript color; ones in the stipple bitmap are drawn in the current color, and zeroes are not drawn at all. The Postscript is appended to <i>interp-&gt;result</i> and <code>TCL_OK</code> is returned, unless an error occurs, in which case <code>TCL_ERROR</code> is returned and <i>interp-&gt;result</i> is overwritten with an error message. </p>
<h2>Keywords</h2>
<p>bitmap, canvas, color, font, path, Postscript, stipple</p>
