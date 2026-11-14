---
title: "xdbegetvisualinfo(3)"
name: "xdbegetvisualinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdbegetvisualinfo/"
---

XdbeGetVisualInfo - Get dbe Visual Informations 

<h2>Synopsis</h2>#include &lt;X11/extensions/Xdbe.h&gt; 

 XdbeScreenVisualInfo *XdbeGetVisualInfo( 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;<wbr>&nbsp;*dpy, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Drawable&nbsp;*screen_specifiers, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*num_screens)
<h2>Description</h2>This function returns information about which visuals support double buffering. The argument <i>num_screens</i> specifies how many elements there are in the <i>screen_specifiers</i> list. Each drawable in <i>screen_specifiers</i> designates a screen for which the supported visuals are being requested. If <i>num_screens</i> is zero, information for all screens is requested. In this case, upon return from this function, <i>num_screens</i> will be set to the number of screens that were found. If an error occurs, this function returns NULL, else it returns a pointer to a list of <i>XdbeScreenVisualInfo</i> structures of length <i>num_screens.</i> The nth element in the returned list corresponds to the nth drawable in the <i>screen_specifiers</i> list, unless <i>num_screens</i> was passed in with the value zero, in which case the nth element in the returned list corresponds to the nth screen of the server, starting with screen zero. The <i>XdbeScreenVisualInfo</i> structure has the following fields: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XdbeVisualInfo&nbsp;*visinfo 

 <i>count</i> specifies the number of items in <i>visinfo.</i> <i>visinfo</i> specifies a list of visuals, depths, and performance hints for this screen. 

 The <i>XdbeVisualInfo</i> structure has the following fields: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VisualID visual 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;depth 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perflevel 

 <i>visual</i> specifies one visual ID that supports double-buffering. <i>depth</i> specifies the depth of the visual. <i>perflevel</i> is a performance hint. 

 The only operation defined on a <i>perflevel</i> is comparison to a <i>perflevel</i> of another visual on the same screen. The visual having the higher <i>perflevel</i> is likely to have better double-buffering graphics performance than the visual having the lower <i>perflevel.</i> Nothing can be deduced from the following: the magnitude of the difference of two <i>perflevels,</i> a <i>perflevel</i> value in isolation, or comparing <i>perflevels</i> from different servers. 

<h2>Errors</h2><dl COMPACT><dt>BadDrawable
<dd>One or more values passed in <i>screen_specifiers</i> is not a valid drawable.</dl><h2>See Also</h2>DBE, <i>XdbeAllocateBackBufferName(),</i> <i>XdbeBeginIdiom(),</i> <i>XdbeDeallocateBackBufferName(),</i> <i>XdbeEndIdiom(),</i> <i>XdbeFreeVisualInfo(),</i> <i>XdbeGetBackBufferAttributes(),</i> <i>XdbeQueryExtension(),</i> <i>XdbeSwapBuffers().</i>
