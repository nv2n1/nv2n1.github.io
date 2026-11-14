---
title: "xdbedeallocatebackbuffername(3)"
name: "xdbedeallocatebackbuffername"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdbedeallocatebackbuffername/"
description: "XdbeDeallocateBackBufferName – frees a DBE buffer."
---

<p>XdbeDeallocateBackBufferName &#8211; frees a DBE buffer. </p>
<h2>Synopsis</h2>
<p>#include &lt;X11/extensions/Xdbe.h&gt; </p>
<p> Status XdbeDeallocateBackBufferName(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*dpy,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XdbeBackBuffer buffer)</p>
<h2>Description</h2>
<p>This function frees a drawable ID, buffer, that was obtained via <code>XdbeAllocateBackBufferName().</code> The buffer must be a valid name for the back buffer of a window, or a protocol error results.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt>BadBuffer</p>
<dd>The specified buffer is not associated with a window.</dl>
<h2>See Also</h2>
<p>DBE, <i>XdbeAllocateBackBufferName(),</i> <i>XdbeBeginIdiom(),</i> <i>XdbeEndIdiom(),</i> <i>XdbeFreeVisualInfo(),</i> <i>XdbeGetBackBufferAttributes(),</i> <i>XdbeGetVisualInfo(),</i> <i>XdbeQueryExtension(),</i> <i>XdbeSwapBuffers().</i></p>
