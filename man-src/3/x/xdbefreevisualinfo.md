---
title: "xdbefreevisualinfo(3)"
name: "xdbefreevisualinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdbefreevisualinfo/"
description: "XdbeFreeVisualInfo – frees information returned by XdbeGetVisualInfo()."
---

<p>XdbeFreeVisualInfo &#8211; frees information returned by <code>XdbeGetVisualInfo().</code> </p>
<h2>Synopsis</h2>
<p>#include &lt;X11/extensions/Xdbe.h&gt; </p>
<p> void XdbeFreeVisualInfo(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XdbeScreenVisualInfo&nbsp;*visual_info)</p>
<h2>Description</h2>
<p>This function frees the list of XdbeScreenVisualInfo returned by the function <code>XdbeGetVisualInfo().</code></p>
<h2>See Also</h2>
<p>DBE, <i>XdbeAllocateBackBufferName(),</i> <i>XdbeBeginIdiom(),</i> <i>XdbeDeallocateBackBufferName(),</i> <i>XdbeEndIdiom(),</i> <i>XdbeGetBackBufferAttributes(),</i> <i>XdbeGetVisualInfo(),</i> <i>XdbeQueryExtension(),</i> <i>XdbeSwapBuffers().</i></p>
