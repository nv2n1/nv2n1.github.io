---
title: "xcreatecolormap(3)"
name: "xcreatecolormap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcreatecolormap/"
description: "XCreateColormap, XCopyColormapAndFree, XFreeColormap, XColor – create, copy, or destroy colormaps and color structure"
---

<p>XCreateColormap, XCopyColormapAndFree, XFreeColormap, XColor &#8211; create, copy, or destroy colormaps and color structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Colormap XCreateColormap(Display *<i>display</i>, Window <i>w</i>, Visual *<i>visual</i>, int <i>alloc</i>);</p>
<dd>Colormap XCopyColormapAndFree(Display *<i>display</i>, Colormap <i>colormap</i>);</p>
<dd>int XFreeColormap(Display *<i>display</i>, Colormap <i>colormap</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>alloc</i></p>
<dd>Specifies the colormap entries to be allocated. You can pass <code>AllocNone</code> or <code>AllocAll</code>.</p>
<dt><i>colormap</i></p>
<dd>Specifies the colormap that you want to create, copy, set, or destroy.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>visual</i></p>
<dd>Specifies a visual type supported on the screen. If the visual type is not one supported by the screen, a <code>BadMatch</code> error results.</p>
<dt><i>w</i></p>
<dd>Specifies the window on whose screen you want to create a colormap.</dl>
<h2>Description</h2>
<p>The <code>XCreateColormap</code> function creates a colormap of the specified visual type for the screen on which the specified window resides and returns the colormap ID associated with it. Note that the specified window is only used to determine the screen. </p>
<p> The initial values of the colormap entries are undefined for the visual classes <code>GrayScale</code>, <code>PseudoColor</code>, and <code>DirectColor</code>. For <code>StaticGray</code>, <code>StaticColor</code>, and <code>TrueColor</code>, the entries have defined values, but those values are specific to the visual and are not defined by X. For <code>StaticGray</code>, <code>StaticColor</code>, and <code>TrueColor</code>, alloc must be <code>AllocNone</code>, or a <code>BadMatch</code> error results. For the other visual classes, if alloc is <code>AllocNone</code>, the colormap initially has no allocated entries, and clients can allocate them. For information about the visual types, see section 3.1. </p>
<p> If alloc is <code>AllocAll</code>, the entire colormap is allocated writable. The initial values of all allocated entries are undefined. For <code>GrayScale</code> and <code>PseudoColor</code>, the effect is as if an <code>XAllocColorCells</code> call returned all pixel values from zero to N &#8211; 1, where N is the colormap entries value in the specified visual. For <code>DirectColor</code>, the effect is as if an <code>XAllocColorPlanes</code> call returned a pixel value of zero and red_mask, green_mask, and blue_mask values containing the same bits as the corresponding masks in the specified visual. However, in all cases, none of these entries can be freed by using <code>XFreeColors</code>. </p>
<p> <code>XCreateColormap</code> can generate <code>BadAlloc</code>, <code>BadMatch</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XCopyColormapAndFree</code> function creates a colormap of the same visual type and for the same screen as the specified colormap and returns the new colormap ID. It also moves all of the client&#8217;s existing allocation from the specified colormap to the new colormap with their color values intact and their read-only or writable characteristics intact and frees those entries in the specified colormap. Color values in other entries in the new colormap are undefined. If the specified colormap was created by the client with alloc set to <code>AllocAll</code>, the new colormap is also created with <code>AllocAll</code>, all color values for all entries are copied from the specified colormap, and then all entries in the specified colormap are freed. If the specified colormap was not created by the client with <code>AllocAll</code>, the allocations to be moved are all those pixels and planes that have been allocated by the client using <code>XAllocColor</code>, <code>XAllocNamedColor</code>, <code>XAllocColorCells</code>, or <code>XAllocColorPlanes</code> and that have not been freed since they were allocated. </p>
<p> <code>XCopyColormapAndFree</code> can generate <code>BadAlloc</code> and <code>BadColor</code> errors. </p>
<p> The <code>XFreeColormap</code> function deletes the association between the colormap resource ID and the colormap and frees the colormap storage. However, this function has no effect on the default colormap for a screen. If the specified colormap is an installed map for a screen, it is uninstalled (see <code>XUninstallColormap</code>). If the specified colormap is defined as the colormap for a window (by <code>XCreateWindow</code>, <code>XSetWindowColormap</code>, or <code>XChangeWindowAttributes</code>), <code>XFreeColormap</code> changes the colormap associated with the window to <code>None</code> and generates a <code>ColormapNotify</code> event. X does not define the colors displayed for a window with a colormap of <code>None</code>. </p>
<p> <code>XFreeColormap</code> can generate a <code>BadColor</code> error.</p>
<h2>Structures</h2>
<p>The <code>XColor</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long pixel;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pixel value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short red, green, blue;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;rgb values&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;DoRed, DoGreen, DoBlue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char pad; } XColor; </p>
<p> The red, green, and blue values are always in the range 0 to 65535 inclusive, independent of the number of bits actually used in the display hardware. The server scales these values down to the range used by the hardware. Black is represented by (0,0,0), and white is represented by (65535,65535,65535). In some functions, the flags member controls which of the red, green, and blue members is used and can be the inclusive OR of zero or more of <code>DoRed</code>, <code>DoGreen</code>, and <code>DoBlue</code>.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xalloccolor/">XAllocColor</a>(3), <a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xquerycolor/">XQueryColor</a>(3), <a href="/docs/linux/man/3-xstorecolors/">XStoreColors</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
