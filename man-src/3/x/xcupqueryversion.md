---
title: "xcupqueryversion(3)"
name: "xcupqueryversion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcupqueryversion/"
description: "XcupQueryVersion – Returns TOG-CUP protocol version supported by the X server"
---

<p>XcupQueryVersion &#8211; Returns TOG-CUP protocol version supported by the X server </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/Xcup.h&gt;
<dl COMPACT><dt><dd>Status <code>XcupQueryVersion</code>(Display *<i>display</i>,
int *<i>major_version_return</i>, int *<i>minor_version_return</i>);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server</p>
<dt><i>major_version_return</i></p>
<dd>Returns the major version supported by the server</p>
<dt><i>minor_version_return</i></p>
<dd>Returns the minor version supported by the server</dl>
<h2>Description</h2>
<p><i>XcupQueryVersion</i> sets <i>major_version_return</i> and <i>minor_version_return</i> to the major and minor TOG-CUP protocol version supported by the server. If the TOG-CUP library is compatible with the version returned by the server, it returns nonzero. If the server does not support the TOG-CUP extension, or if there was an error during communications with the server, or if the server and library protocol versions are incompatible, it returns zero. No other Xcup functions may be called before this function. If a client violates this rule, the effects of all subsequent Xcup calls that it makes are undefined. </p>
<p> To get the list of reserved colormap entries, use <i>XcupGetReservedColormapEntries.</i> </p>
<p> To allocate one or more read-only color cells with RGB values, use <i>XcupStoreColors.</i></p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/3Xext-XcupGetReservedColormapEntries/">XcupGetReservedColormapEntries</a></code>(3Xext), <code><a href="//www.systutorials.com/docs/linux/man/3Xext-XcupStoreColors/">XcupStoreColors</a></code>(3Xext),<br />
 <i>Colormap Utilization Policy and Extension</i></p>
