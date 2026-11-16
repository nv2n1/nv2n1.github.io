---
title: "xdbeallocatebackbuffername(3)"
name: "xdbeallocatebackbuffername"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdbeallocatebackbuffername/"
---

XdbeAllocateBackBufferName - allocates a DBE buffer. 

<h2>Synopsis</h2>#include &lt;X11/extensions/Xdbe.h&gt; 

 XdbeBackBuffer XdbeAllocateBackBufferName( 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*dpy, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;window, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XdbeSwapAction swap_action)
<h2>Description</h2>This function returns a drawable ID used to refer to the back buffer of the specified window. The swap_action is a hint to indicate the swap action that will likely be used in subsequent calls to <b>XdbeSwapBuffers().</b> The actual swap action used in calls to <b>XdbeSwapBuffers()</b> does not have to be the same as the swap_action passed to this function, though clients are encouraged to provide accurate information whenever possible.
<h2>Errors</h2><dl COMPACT><dt>BadAlloc
</dt><dd></dd><dt>BadIDChoice
</dt><dd></dd><dt>BadMatch
</dt><dd>The specified window is not an InputOutput window or its visual does not support DBE.
</dd><dt>BadValue
</dt><dd>An invalid swap action was specified.
</dd><dt>BadWindow
</dt><dd>An invalid window was specified.</dd></dl><h2>See Also</h2>DBE, <i>XdbeBeginIdiom(),</i> <i>XdbeDeallocateBackBufferName(),</i> <i>XdbeEndIdiom(),</i> <i>XdbeFreeVisualInfo(),</i> <i>XdbeGetBackBufferAttributes(),</i> <i>XdbeGetVisualInfo(),</i> <i>XdbeQueryExtension(),</i> <i>XdbeSwapBuffers().</i>
