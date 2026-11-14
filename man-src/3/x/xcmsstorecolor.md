---
title: "xcmsstorecolor(3)"
name: "xcmsstorecolor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmsstorecolor/"
description: "XcmsStoreColor, XcmsStoreColors – set colors"
---

<p>XcmsStoreColor, XcmsStoreColors &#8211; set colors </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsStoreColor(Display *<i>display</i>, Colormap <i>colormap</i>, XcmsColor *<i>color</i>);</p>
<dd>Status XcmsStoreColors(Display *<i>display</i>, Colormap <i>colormap</i>, XcmsColor <i>colors</i>[], int <i>ncolors</i>, Bool <i>compression_flags_return</i>[]);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>color</i></p>
<dd>Specifies the color cell and the color to store. Values specified in this <code>XcmsColor</code> structure remain unchanged on return.</p>
<dt><i>colors</i></p>
<dd>Specifies the color specification array of <code>XcmsColor</code> structures, each specifying a color cell and the color to store in that cell. Values specified in the array remain unchanged upon return.</p>
<dt><i>colormap</i></p>
<dd>Specifies the colormap.</p>
<dt><i>compression_flags_return</i></p>
<dd>Returns an array of Boolean values indicating compression status. If a non-NULL pointer is supplied, each element of the array is set to <code>True</code> if the corresponding color was compressed and <code>False</code> otherwise. Pass NULL if the compression status is not useful.</p>
<dt><i>ncolors</i></p>
<dd>Specifies the number of <code>XcmsColor</code> structures in the color-specification array.</dl>
<h2>Description</h2>
<p>The <code>XcmsStoreColor</code> function converts the color specified in the <code>XcmsColor</code> structure into RGB values. It then uses this RGB specification in an <code>XColor</code> structure, whose three flags <code>DoGreen</code>, and <code>DoBlue</code>) are set, in a call to <code>XStoreColor</code> to change the color cell specified by the pixel member of the <code>XcmsColor</code> structure. This pixel value must be a valid index for the specified colormap, and the color cell specified by the pixel value must be a read/write cell. If the pixel value is not a valid index, a <code>BadValue</code> error results. If the color cell is unallocated or is allocated read-only, a <code>BadAccess</code> error results. If the colormap is an installed map for its screen, the changes are visible immediately. </p>
<p> Note that <code>XStoreColor</code> has no return value; therefore, an <code>XcmsSuccess</code> return value from this function indicates that the conversion to RGB succeeded and the call to <code>XStoreColor</code> was made. To obtain the actual color stored, use <code>XcmsQueryColor</code>. Because of the screen&#8217;s hardware limitations or gamut compression, the color stored in the colormap may not be identical to the color specified. </p>
<p> <code>XcmsStoreColor</code> can generate <code>BadAccess</code>, <code>BadColor</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XcmsStoreColors</code> function converts the colors specified in the array of <code>XcmsColor</code> structures into RGB values and then uses these RGB specifications in <code>XColor</code> structures, whose three flags <code>DoGreen</code>, and <code>DoBlue</code>) are set, in a call to <code>XStoreColors</code> to change the color cells specified by the pixel member of the corresponding <code>XcmsColor</code> structure. Each pixel value must be a valid index for the specified colormap, and the color cell specified by each pixel value must be a read/write cell. If a pixel value is not a valid index, a <code>BadValue</code> error results. If a color cell is unallocated or is allocated read-only, a <code>BadAccess</code> error results. If more than one pixel is in error, the one that gets reported is arbitrary. If the colormap is an installed map for its screen, the changes are visible immediately. </p>
<p> Note that <code>XStoreColors</code> has no return value; therefore, an <code>XcmsSuccess</code> return value from this function indicates that conversions to RGB succeeded and the call to <code>XStoreColors</code> was made. To obtain the actual colors stored, use <code>XcmsQueryColors</code>. Because of the screen&#8217;s hardware limitations or gamut compression, the colors stored in the colormap may not be identical to the colors specified. </p>
<p> <code>XcmsStoreColors</code> can generate <code>BadAccess</code>, <code>BadColor</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>A client attempted to free a color map entry that it did not already allocate.</p>
<dt><code>BadAccess</code></p>
<dd>A client attempted to store into a read-only color map entry.</p>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmsalloccolor/">XcmsAllocColor</a>(3), <a href="/docs/linux/man/3-xcmsquerycolor/">XcmsQueryColor</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
