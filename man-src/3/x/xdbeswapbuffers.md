---
title: "xdbeswapbuffers(3)"
name: "xdbeswapbuffers"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdbeswapbuffers/"
---

XdbeSwapBuffers - swaps front and back DBE buffers. 

<h2>Synopsis</h2>#include &lt;X11/extensions/Xdbe.h&gt; 

 Status XdbeSwapBuffers( 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*dpy, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XdbeSwapInfo&nbsp;*swap_info, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;num_windows)
<h2>Description</h2>This function swaps the front and back buffers for a list of windows. The argument <i>num_windows</i> specifies how many windows are to have their buffers swapped; it is the number of elements in the <i>swap_info</i> array. The argument <i>swap_info</i> specifies the information needed per window to do the swap. 

 The <i>XdbeSwapInfo</i> structure has the following fields: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swap_window 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XdbeSwapAction&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swap_action 

 <i>swap_window</i> specifies the window for which to swap buffers. <i>swap_action</i> specifies the swap action to use for this <i>swap_window.</i> 

 <i>swap_action</i> determines what will happen to the new back buffer of the <i>swap_window</i> it is paired with in the list in addition to making the old back buffer become visible. The defined actions are as follows: 

<dl COMPACT><dt>XdbeUndefined
<dd>The contents of the new back buffer become undefined. This may be the most efficient action since it allows the implementation to discard the contents of the buffer if it needs to.
<dt>XdbeBackground
<dd>The unobscured region of the new back buffer will be tiled with the window background. The background action allows devices to use a fast clear capability during a swap.
<dt>XdbeUntouched
<dd>The unobscured region of the new back buffer will be unmodified by the swap.
<dt>XdbeCopied
<dd>The unobscured region of the new back buffer will be the contents of the old back buffer</dl><h2>Errors</h2><dl COMPACT><dt>BadMatch
<dd>A non-double-buffered window was specified or a window was specified twice.
<dt>BadWindow
<dd>An invalid window was specified.
<dt>BadValue
<dd>An invalid swap action was specified.</dl><h2>See Also</h2>DBE, <i>XdbeAllocateBackBufferName(),</i> <i>XdbeBeginIdiom(),</i> <i>XdbeDeallocateBackBufferName(),</i> <i>XdbeEndIdiom(),</i> <i>XdbeFreeVisualInfo(),</i> <i>XdbeGetBackBufferAttributes(),</i> <i>XdbeGetVisualInfo(),</i> <i>XdbeQueryExtension().</i>
