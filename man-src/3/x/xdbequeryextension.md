---
title: "xdbequeryextension(3)"
name: "xdbequeryextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdbequeryextension/"
---

XdbeQueryExtension - returns the version of DBE supported by the server. 

<h2>Synopsis</h2>#include &lt;X11/extensions/Xdbe.h&gt; 

 Status XdbeQueryExtension( 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;*dpy, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*major_version_return, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*minor_version_return)
<h2>Description</h2>Sets <i>major_version_return</i> and <i>minor_version_return</i> to the major and minor DBE protocol version supported by the server. If the DBE library is compatible with the version returned by the server, this function returns non-zero. If <i>dpy</i> does not support the DBE extension, or if there was an error during communication with the server, or if the server and library protocol versions are incompatible, this function returns zero. No other Xdbe functions may be called before this function. If a client violates this rule, the effects of all subsequent Xdbe calls that it makes are undefined.
<h2>See Also</h2>DBE, <i>XdbeAllocateBackBufferName(),</i> <i>XdbeBeginIdiom(),</i> <i>XdbeDeallocateBackBufferName(),</i> <i>XdbeEndIdiom(),</i> <i>XdbeFreeVisualInfo(),</i> <i>XdbeGetBackBufferAttributes(),</i> <i>XdbeGetVisualInfo(),</i> <i>XdbeSwapBuffers().</i>
