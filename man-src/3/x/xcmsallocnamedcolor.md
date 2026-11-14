---
title: "xcmsallocnamedcolor(3)"
name: "xcmsallocnamedcolor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmsallocnamedcolor/"
description: "XcmsAllocColor, XcmsAllocNamedColor – allocate colors"
---

<p>XcmsAllocColor, XcmsAllocNamedColor &#8211; allocate colors </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsAllocColor(Display *<i>display</i>, Colormap <i>colormap</i>, XcmsColor *<i>color_in_out</i>, XcmsColorFormat <i>result_format</i>);</p>
<dd>Status XcmsAllocNamedColor(Display *<i>display</i>, Colormap <i>colormap</i>, char *<i>color_string</i>, XcmsColor *<i>color_screen_return</i>, XcmsColor *<i>color_exact_return</i>, XcmsColorFormat <i>result_format</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>colormap</i></p>
<dd>Specifies the colormap.</p>
<dt><i>color_exact_return</i></p>
<dd>Returns the color specification parsed from the color string or parsed from the corresponding string found in a color-name database.</p>
<dt><i>color_in_out</i></p>
<dd>Specifies the color to allocate and returns the pixel and color that is actually used in the colormap.</p>
<dt><i>color_screen_return</i></p>
<dd>Returns the pixel value of the color cell and color specification that actually is stored for that cell. Specifies the color string whose color definition structure is to be returned.</p>
<dt><i>result_format</i></p>
<dd>Specifies the color format for the returned color specification.</dl>
<h2>Description</h2>
<p>The <code>XcmsAllocColor</code> function is similar to <code>XAllocColor</code> except the color can be specified in any format. The <code>XcmsAllocColor</code> function ultimately calls <code>XAllocColor</code> to allocate a read-only color cell (colormap entry) with the specified color. <code>XcmsAllocColor</code> first converts the color specified to an RGB value and then passes this to <code>XAllocColor</code>. <code>XcmsAllocColor</code> returns the pixel value of the color cell and the color specification actually allocated. This returned color specification is the result of converting the RGB value returned by <code>XAllocColor</code> into the format specified with the result_format argument. If there is no interest in a returned color specification, unnecessary computation can be bypassed if result_format is set to <code>XcmsRGBFormat</code>. The corresponding colormap cell is read-only. If this routine returns <code>XcmsFailure</code>, the color_in_out color specification is left unchanged. </p>
<p> <code>XcmsAllocColor</code> can generate a <code>BadColor</code> errors. </p>
<p> The <code>XcmsAllocNamedColor</code> function is similar to <code>XAllocNamedColor</code> except that the color returned can be in any format specified. This function ultimately calls <code>XAllocColor</code> to allocate a read-only color cell with the color specified by a color string. The color string is parsed into an <code>XcmsColor</code> structure (see <code>XcmsLookupColor</code>), converted to an RGB value, and finally passed to <code>XAllocColor</code>. If the color name is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. </p>
<p> This function returns both the color specification as a result of parsing (exact specification) and the actual color specification stored (screen specification). This screen specification is the result of converting the RGB value returned by <code>XAllocColor</code> into the format specified in result_format. If there is no interest in a returned color specification, unnecessary computation can be bypassed if result_format is set to <code>XcmsRGBFormat</code>. If color_screen_return and color_exact_return point to the same structure, the pixel field will be set correctly, but the color values are undefined. </p>
<p> <code>XcmsAllocNamedColor</code> can generate a <code>BadColor</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmsquerycolor/">XcmsQueryColor</a>(3), <a href="/docs/linux/man/3-xcmsstorecolor/">XcmsStoreColor</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
