---
title: "tk_getpixels(3)"
name: "tk_getpixels"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getpixels/"
description: "Tk_GetPixelsFromObj, Tk_GetPixels, Tk_GetMMFromObj, Tk_GetScreenMM – translate between strings and screen units"
---

<p>Tk_GetPixelsFromObj, Tk_GetPixels, Tk_GetMMFromObj, Tk_GetScreenMM &#8211; translate between strings and screen units </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetPixelsFromObj(</code><i>interp, tkwin, objPtr, intPtr</i><code>)</code>
int
<code>Tk_GetPixels(</code><i>interp, tkwin, string, intPtr</i><code>)</code>
int
<code>Tk_GetMMFromObj(</code><i>interp, tkwin, objPtr, doublePtr</i><code>)</code>
int
<code>Tk_GetScreenMM(</code><i>interp, tkwin, string, doublePtr</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tk_Window <i>tkwin</i> (in) Window whose screen geometry determines the conversion between absolute units and pixels.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) String value specifies a distance on the screen; internal rep will be modified to cache converted distance.</p>
<dd>const char <i>*string</i> (in) Same as <i>objPtr</i> except specification of distance is passed as a string.</p>
<dd>int <i>*intPtr</i> (out) Pointer to location in which to store converted distance in pixels.</p>
<dd>double <i>*doublePtr</i> (out) Pointer to location in which to store converted distance in millimeters. </p>
</dl>
<h2>Description</h2>
<p>These procedures take as argument a specification of distance on the screen (<i>objPtr</i> or <i>string</i>) and compute the corresponding distance either in integer pixels or floating-point millimeters. In either case, <i>objPtr</i> or <i>string</i> specifies a screen distance as a floating-point number followed by one of the following characters that indicates units:</p>
<dl COMPACT>
<dt>&lt;none&gt;</p>
<dd>The number specifies a distance in pixels.</p>
<dt><code>c</code></p>
<dd>The number specifies a distance in centimeters on the screen.</p>
<dt><code>i</code></p>
<dd>The number specifies a distance in inches on the screen.</p>
<dt><code>m</code></p>
<dd>The number specifies a distance in millimeters on the screen.</p>
<dt><code>p</code></p>
<dd>The number specifies a distance in printer&#8217;s points (1/72 inch) on the screen.</dl>
<p> <code>Tk_GetPixelsFromObj</code> converts the value of <i>objPtr</i> to the nearest even number of pixels and stores that value at <i>*intPtr</i>. It returns <code>TCL_OK</code> under normal circumstances. If an error occurs (e.g. <i>objPtr</i> contains a number followed by a character that is not one of the ones above) then <code>TCL_ERROR</code> is returned and an error message is left in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. <code>Tk_GetPixelsFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetPixelsFromObj</code> with the same <i>objPtr</i>. </p>
<p> <code>Tk_GetPixels</code> is identical to <code>Tk_GetPixelsFromObj</code> except that the screen distance is specified with a string instead of an object. This prevents <code>Tk_GetPixels</code> from caching the return value, so <code>Tk_GetAnchor</code> is less efficient than <code>Tk_GetPixelsFromObj</code>. </p>
<p> <code>Tk_GetMMFromObj</code> and <code>Tk_GetScreenMM</code> are similar to <code>Tk_GetPixelsFromObj</code> and <code>Tk_GetPixels</code> (respectively) except that they convert the screen distance to millimeters and store a double-precision floating-point result at <i>*doublePtr</i>. </p>
<h2>Keywords</h2>
<p>centimeters, convert, inches, millimeters, pixels, points, screen units</p>
