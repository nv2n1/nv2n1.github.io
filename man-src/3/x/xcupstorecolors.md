---
title: "xcupstorecolors(3)"
name: "xcupstorecolors"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcupstorecolors/"
description: "XcupStoreColors – initialize shareable colormap entries at specific locations"
---

<p>XcupStoreColors &#8211; initialize shareable colormap entries at specific locations </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/Xcup.h&gt;
<dl COMPACT><dt><dd>Status <code>XcupStoreColors</code>(Display *<i>display</i>, Colormap <i>colormap</i>,
XColor *<i>colors_in_out</i>, int <i>ncolors</i>);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server</p>
<dt><i>colormap</i></p>
<dd>Specifies the colormap</p>
<dt><i>colors_in_out</i></p>
<dd>Specifies and returns the values actually used in the colormap</p>
<dt><i>ncolors</i></p>
<dd>Specifies the number of items in colors_in_out</dl>
<h2>Description</h2>
<p>The <i>XcupStoreColors</i> function changes the colormap entries of the pixel values in the pixel members of the XColor structures. The colormap entries are allocated as if an AllocColor has been used instead, i.e. the colors are read-only (shareable). <i>XcupStoreColors</i> returns the number of colors that were successfully allocated in the colormap. </p>
<p> A <i>Value</i> error is generated if a pixel is not a valid index into the colormap. A <i>BadMatch</i> error is generated if the colormap does not belong to a GrayScale, PseudoColor, or DirectColor visual. </p>
<p> Applications which allocate many colors in a screen&#8217;s default colormap, e.g. a color-cube or a gray-ramp, should allocate them with <i>XCupStoreColors</i>. By using XCupStoreColors the colors will be allocated sharable (read-only) and any other application which allocates the same color will share that color cell.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/3Xext-XcupQueryVersion/">XcupQueryVersion</a></code>(3Xext), <code><a href="//www.systutorials.com/docs/linux/man/3Xext-XcupGetReservedColormapEntries/">XcupGetReservedColormapEntries</a></code>(3Xext),<br />
 <i>Colormap Utilization Policy and Extension</i></p>
