---
title: "xdbegetbackbufferattributes(3)"
name: "xdbegetbackbufferattributes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdbegetbackbufferattributes/"
description: "XdbeGetBackBufferAttributes – returns attributes of a DBE buffer."
---

<p>XdbeGetBackBufferAttributes &#8211; returns attributes of a DBE buffer. </p>
<h2>Synopsis</h2>
<p>#include &lt;X11/extensions/Xdbe.h&gt; </p>
<p> XdbeBackBufferAttributes *XdbeGetBackBufferAttributes(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*dpy,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XdbeBackBuffer buffer)</p>
<h2>Description</h2>
<p>This function returns the attributes associated with the specified buffer. </p>
<p> The <i>XdbeBackBufferAttributes</i> structure has the following fields: </p>
<dl COMPACT>
<dd>Window window window that buffer belongs to</dl>
<p> If buffer is not a valid <i>XdbeBackBuffer,</i> window returns None. </p>
<p> The returned <i>XdbeBackBufferAttributes</i> structure can be freed with the Xlib function <code>Xfree().</code></p>
<h2>See Also</h2>
<p>DBE, <i>XdbeAllocateBackBufferName(),</i> <i>XdbeBeginIdiom(),</i> <i>XdbeDeallocateBackBufferName(),</i> <i>XdbeEndIdiom(),</i> <i>XdbeFreeVisualInfo(),</i> <i>XdbeGetVisualInfo(),</i> <i>XdbeQueryExtension(),</i> <i>XdbeSwapBuffers().</i></p>
