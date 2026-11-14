---
title: "xcmsquerycolors(3)"
name: "xcmsquerycolors"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmsquerycolors/"
description: "XcmsQueryColor, XcmsQueryColors, XcmsLookupColor – obtain color values"
---

<p>XcmsQueryColor, XcmsQueryColors, XcmsLookupColor &#8211; obtain color values </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsQueryColor(Display *<i>display</i>, Colormap <i>colormap</i>, XcmsColor *<i>color_in_out</i>, XcmsColorFormat <i>result_format</i>);</p>
<dd>Status XcmsQueryColors(Display *<i>display</i>, Colormap <i>colormap</i>, XcmsColor <i>colors_in_out</i>[], unsigned int <i>ncolors</i>, XcmsColorFormat <i>result_format</i>);</p>
<dd>Status XcmsLookupColor(Display *<i>display</i>, Colormap <i>colormap</i>, char *<i>color_string</i>, XcmsColor *<i>color_exact_return</i>, XcmsColor *<i>color_screen_return</i>, XcmsColorFormat <i>result_format</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>colormap</i></p>
<dd>Specifies the colormap.</p>
<dt><i>color_exact_return</i></p>
<dd>Returns the color specification parsed from the color string or parsed from the corresponding string found in a color-name database.</p>
<dt><i>color_in_out</i></p>
<dd>Specifies the pixel member that indicates the color cell to query. The color specification stored for the color cell is returned in this <code>XcmsColor</code> structure.</p>
<dt><i>color_screen_return</i></p>
<dd>Returns the color that can be reproduced on the screen.</p>
<dt><i>color_string</i></p>
<dd>Specifies the color string.</p>
<dt><i>result_format</i></p>
<dd>Specifies the color format for the returned color specifications (color_screen_return and color_exact_return arguments). If the format is <code>XcmsUndefinedFormat</code> and the color string contains a numerical color specification, the specification is returned in the format used in that numerical color specification. If the format is <code>XcmsUndefinedFormat</code> and the color string contains a color name, the specification is returned in the format used to store the color in the database.</p>
<dt><i>ncolors</i></p>
<dd>Specifies the number of <code>XcmsColor</code> structures in the color-specification array.</dl>
<h2>Description</h2>
<p>The <code>XcmsQueryColor</code> function obtains the RGB value for the pixel value in the pixel member of the specified <code>XcmsColor</code> structure and then converts the value to the target format as specified by the result_format argument. If the pixel is not a valid index in the specified colormap, a <code>BadValue</code> error results. The <code>XcmsQueryColors</code> function obtains the RGB values for pixel values in the pixel members of <code>XcmsColor</code> structures and then converts the values to the target format as specified by the result_format argument. If a pixel is not a valid index into the specified colormap, a <code>BadValue</code> error results. If more than one pixel is in error, the one that gets reported is arbitrary. </p>
<p> <code>XcmsQueryColor</code> and <code>XcmsQueryColors</code> can generate <code>BadColor</code> and <code>BadValue</code> errors. </p>
<p> The <code>XcmsLookupColor</code> function looks up the string name of a color with respect to the screen associated with the specified colormap. It returns both the exact color values and the closest values provided by the screen with respect to the visual type of the specified colormap. The values are returned in the format specified by result_format. If the color name is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. <code>XcmsLookupColor</code> returns <code>XcmsSuccess</code> or <code>XcmsSuccessWithCompression</code> if the name is resolved; otherwise, it returns <code>XcmsFailure</code>. If <code>XcmsSuccessWithCompression</code> is returned, the color specification returned in color_screen_return is the result of gamut compression.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmsalloccolor/">XcmsAllocColor</a>(3), <a href="/docs/linux/man/3-xcmsstorecolor/">XcmsStoreColor</a>(3), <a href="/docs/linux/man/3-xquerycolor/">XQueryColor</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
