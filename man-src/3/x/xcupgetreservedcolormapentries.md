---
title: "xcupgetreservedcolormapentries(3)"
name: "xcupgetreservedcolormapentries"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcupgetreservedcolormapentries/"
description: "XcupGetReservedColormapEntries – list colormap entries reserved by the system"
---

<p>XcupGetReservedColormapEntries &#8211; list colormap entries reserved by the system </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/Xcup.h&gt;
<dl COMPACT><dt><dd>Status <code>XcupGetReservedColormapEntries</code>(Display *<i>display</i>,
int <i>screen</i>, XColor **<i>colors_out</i>, int *<i>ncolors</i>);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>screen</i></p>
<dd>Screen number on the host server.</p>
<dt><i>colors_out</i></p>
<dd>Returns the values reserved by the server.</p>
<dt><i>ncolors</i></p>
<dd>Returns the number of items in <i>colors_out</i>.</dl>
<h2>Description</h2>
<p>The <i>XcupGetReservedColormapEntries</i> function returns a list of colormap entries (pixels) that are reserved by the system. This list will, at a minimum, contain entries for the BlackPixel and WhitePixel of the specified screen. Use <i>XFree</i> to free <i>colors_out.</i> </p>
<p> To minimize colormap flash, an application which installs its own private colormap should query the special colors by calling <i>XCupGetReservedColormapEntries</i>, and can then store those entries (in the proper location) in its private colormap using <i>XCupStoreColors</i>.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/3Xext-XcupQueryVersion/">XcupQueryVersion</a></code>(3Xext), <code><a href="//www.systutorials.com/docs/linux/man/3Xext-XcupStoreColors/">XcupStoreColors</a></code>(3Xext), <code><a href="//www.systutorials.com/docs/linux/man/3X11-XFree/">XFree</a></code>(3X11),<br />
 <i>Colormap Utilization Policy and Extension</i></p>
