---
title: "xstorecolors(3)"
name: "xstorecolors"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xstorecolors/"
description: "XStoreColors, XStoreColor, XStoreNamedColor – set colors"
---

<p>XStoreColors, XStoreColor, XStoreNamedColor &#8211; set colors </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XStoreColors(Display *<i>display</i>, Colormap <i>colormap</i>, XColor <i>color</i>[], int <i>ncolors</i>);</p>
<dd>int XStoreColor(Display *<i>display</i>, Colormap <i>colormap</i>, XColor *<i>color</i>);</p>
<dd>int XStoreNamedColor(Display *<i>display</i>, Colormap <i>colormap</i>, char *<i>color</i>, unsigned long <i>pixel</i>, int <i>flags</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>color</i></p>
<dd>Specifies the pixel and RGB values or the color name string (for example, red).</p>
<dt><i>color</i></p>
<dd>Specifies an array of color definition structures to be stored.</p>
<dt><i>colormap</i></p>
<dd>Specifies the colormap.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>flags</i></p>
<dd>Specifies which red, green, and blue components are set.</p>
<dt><i>ncolors</i></p>
<dd>Specifies the number of <code>XColor</code> structures in the color definition array.</p>
<dt><i>pixel</i></p>
<dd>Specifies the entry in the colormap.</dl>
<h2>Description</h2>
<p>The <code>XStoreColors</code> function changes the colormap entries of the pixel values specified in the pixel members of the <code>XColor</code> structures. You specify which color components are to be changed by setting <code>DoRed</code>, <code>DoGreen</code>, and/or <code>DoBlue</code> in the flags member of the <code>XColor</code> structures. If the colormap is an installed map for its screen, the changes are visible immediately. <code>XStoreColors</code> changes the specified pixels if they are allocated writable in the colormap by any client, even if one or more pixels generates an error. If a specified pixel is not a valid index into the colormap, a <code>BadValue</code> error results. If a specified pixel either is unallocated or is allocated read-only, a <code>BadAccess</code> error results. If more than one pixel is in error, the one that gets reported is arbitrary. </p>
<p> <code>XStoreColors</code> can generate <code>BadAccess</code>, <code>BadColor</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XStoreColor</code> function changes the colormap entry of the pixel value specified in the pixel member of the <code>XColor</code> structure. You specified this value in the pixel member of the <code>XColor</code> structure. This pixel value must be a read/write cell and a valid index into the colormap. If a specified pixel is not a valid index into the colormap, a <code>BadValue</code> error results. <code>XStoreColor</code> also changes the red, green, and/or blue color components. You specify which color components are to be changed by setting <code>DoRed</code>, <code>DoGreen</code>, and/or <code>DoBlue</code> in the flags member of the <code>XColor</code> structure. If the colormap is an installed map for its screen, the changes are visible immediately. </p>
<p> <code>XStoreColor</code> can generate <code>BadAccess</code>, <code>BadColor</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XStoreNamedColor</code> function looks up the named color with respect to the screen associated with the colormap and stores the result in the specified colormap. The pixel argument determines the entry in the colormap. The flags argument determines which of the red, green, and blue components are set. You can set this member to the bitwise inclusive OR of the bits <code>DoRed</code>, <code>DoGreen</code>, and <code>DoBlue</code>. If the color name is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. If the specified pixel is not a valid index into the colormap, a <code>BadValue</code> error results. If the specified pixel either is unallocated or is allocated read-only, a <code>BadAccess</code> error results. </p>
<p> <code>XStoreNamedColor</code> can generate <code>BadAccess</code>, <code>BadColor</code>, <code>BadName</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>A client attempted to free a color map entry that it did not already allocate.</p>
<dt><code>BadAccess</code></p>
<dd>A client attempted to store into a read-only color map entry.</p>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadName</code></p>
<dd>A font or color of the specified name does not exist.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xalloccolor/">XAllocColor</a>(3), <a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3), <a href="/docs/linux/man/3-xquerycolor/">XQueryColor</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
