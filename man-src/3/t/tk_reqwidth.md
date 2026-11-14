---
title: "tk_reqwidth(3)"
name: "tk_reqwidth"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_reqwidth/"
description: "Tk_WindowId, Tk_Parent, Tk_Display, Tk_DisplayName, Tk_ScreenNumber, Tk_Screen, Tk_X, Tk_Y, Tk_Width, Tk_Height, Tk_Changes, Tk_Attributes, Tk_IsContainer, Tk_IsEmbedded, Tk_IsMapped, Tk_IsTopLevel..."
---

<p>Tk_WindowId, Tk_Parent, Tk_Display, Tk_DisplayName, Tk_ScreenNumber, Tk_Screen, Tk_X, Tk_Y, Tk_Width, Tk_Height, Tk_Changes, Tk_Attributes, Tk_IsContainer, Tk_IsEmbedded, Tk_IsMapped, Tk_IsTopLevel, Tk_ReqWidth, Tk_ReqHeight, Tk_MinReqWidth, Tk_MinReqHeight, Tk_InternalBorderLeft, Tk_InternalBorderRight, Tk_InternalBorderTop, Tk_InternalBorderBottom, Tk_Visual, Tk_Depth, Tk_Colormap, Tk_Interp &#8211; retrieve information from Tk&#8217;s local data structure </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Window
<code>Tk_WindowId</code>(<i>tkwin</i>)
Tk_Window
<code>Tk_Parent</code>(<i>tkwin</i>)
Display *
<code>Tk_Display</code>(<i>tkwin</i>)
const char *
<code>Tk_DisplayName</code>(<i>tkwin</i>)
int
<code>Tk_ScreenNumber</code>(<i>tkwin</i>)
Screen *
<code>Tk_Screen</code>(<i>tkwin</i>)
int
<code>Tk_X</code>(<i>tkwin</i>)
int
<code>Tk_Y</code>(<i>tkwin</i>)
int
<code>Tk_Width</code>(<i>tkwin</i>)
int
<code>Tk_Height</code>(<i>tkwin</i>)
XWindowChanges *
<code>Tk_Changes</code>(<i>tkwin</i>)
XSetWindowAttributes *
<code>Tk_Attributes</code>(<i>tkwin</i>)
int
<code>Tk_IsContainer</code>(<i>tkwin</i>)
int
<code>Tk_IsEmbedded</code>(<i>tkwin</i>)
int
<code>Tk_IsMapped</code>(<i>tkwin</i>)
int
<code>Tk_IsTopLevel</code>(<i>tkwin</i>)
int
<code>Tk_ReqWidth</code>(<i>tkwin</i>)
int
<code>Tk_ReqHeight</code>(<i>tkwin</i>)
int
<code>Tk_MinReqWidth</code>(<i>tkwin</i>)
int
<code>Tk_MinReqHeight</code>(<i>tkwin</i>)
int
<code>Tk_InternalBorderLeft</code>(<i>tkwin</i>)
int
<code>Tk_InternalBorderRight</code>(<i>tkwin</i>)
int
<code>Tk_InternalBorderTop</code>(<i>tkwin</i>)
int
<code>Tk_InternalBorderBottom</code>(<i>tkwin</i>)
Visual *
<code>Tk_Visual</code>(<i>tkwin</i>)
int
<code>Tk_Depth</code>(<i>tkwin</i>)
Colormap
<code>Tk_Colormap</code>(<i>tkwin</i>)
Tcl_Interp *
<code>Tk_Interp</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_WindowId</code> and the other names listed above are all macros that return fields from Tk&#8217;s local data structure for <i>tkwin</i>. None of these macros requires any interaction with the server; it is safe to assume that all are fast. </p>
<p> <code>Tk_WindowId</code> returns the X identifier for <i>tkwin</i>, or <code>NULL</code> if no X window has been created for <i>tkwin</i> yet. </p>
<p> <code>Tk_Parent</code> returns Tk&#8217;s token for the logical parent of <i>tkwin</i>. The parent is the token that was specified when <i>tkwin</i> was created, or NULL for main windows. </p>
<p> <code>Tk_Interp</code> returns the Tcl interpreter associated with a <i>tkwin</i> or NULL if there is an error. </p>
<p> <code>Tk_Display</code> returns a pointer to the Xlib display structure corresponding to <i>tkwin</i>. <code>Tk_DisplayName</code> returns an ASCII string identifying <i>tkwin</i>&#8216;s display. <code>Tk_ScreenNumber</code> returns the index of <i>tkwin</i>&#8216;s screen among all the screens of <i>tkwin</i>&#8216;s display. <code>Tk_Screen</code> returns a pointer to the Xlib structure corresponding to <i>tkwin</i>&#8216;s screen. </p>
<p> <code>Tk_X</code>, <code>Tk_Y</code>, <code>Tk_Width</code>, and <code>Tk_Height</code> return information about <i>tkwin&#8217;s</i> location within its parent and its size. The location information refers to the upper-left pixel in the window, or its border if there is one. The width and height information refers to the interior size of the window, not including any border. <code>Tk_Changes</code> returns a pointer to a structure containing all of the above information plus a few other fields. <code>Tk_Attributes</code> returns a pointer to an XSetWindowAttributes structure describing all of the attributes of the <i>tkwin</i>&#8216;s window, such as background pixmap, event mask, and so on (Tk keeps track of all this information as it is changed by the application). Note: it is essential that applications use Tk procedures like <code>Tk_ResizeWindow</code> instead of X procedures like <code>XResizeWindow</code>, so that Tk can keep its data structures up-to-date. </p>
<p> <code>Tk_IsContainer</code> returns a non-zero value if <i>tkwin</i> is a container, and that some other application may be embedding itself inside <i>tkwin</i>. </p>
<p> <code>Tk_IsEmbedded</code> returns a non-zero value if <i>tkwin</i> is not a free-standing window, but rather is embedded in some other application. </p>
<p> <code>Tk_IsMapped</code> returns a non-zero value if <i>tkwin</i> is mapped and zero if <i>tkwin</i> is not mapped. </p>
<p> <code>Tk_IsTopLevel</code> returns a non-zero value if <i>tkwin</i> is a top-level window (its X parent is the root window of the screen) and zero if <i>tkwin</i> is not a top-level window. </p>
<p> <code>Tk_ReqWidth</code> and <code>Tk_ReqHeight</code> return information about the window&#8217;s requested size. These values correspond to the last call to <code>Tk_GeometryRequest</code> for <i>tkwin</i>. </p>
<p> <code>Tk_MinReqWidth</code> and <code>Tk_MinReqHeight</code> return information about the window&#8217;s minimum requested size. These values correspond to the last call to <code>Tk_SetMinimumRequestSize</code> for <i>tkwin</i>. </p>
<p> <code>Tk_InternalBorderLeft</code>, <code>Tk_InternalBorderRight</code>, <code>Tk_InternalBorderTop</code> and <code>Tk_InternalBorderBottom</code> return the width of one side of the internal border that has been requested for <i>tkwin</i>, or 0 if no internal border was requested. The return value is simply the last value passed to <code>Tk_SetInternalBorder</code> or <code>Tk_SetInternalBorderEx</code> for <i>tkwin</i>. </p>
<p> <code>Tk_Visual</code>, <code>Tk_Depth</code>, and <code>Tk_Colormap</code> return information about the visual characteristics of a window. <code>Tk_Visual</code> returns the visual type for the window, <code>Tk_Depth</code> returns the number of bits per pixel, and <code>Tk_Colormap</code> returns the current colormap for the window. The visual characteristics are normally set from the defaults for the window&#8217;s screen, but they may be overridden by calling <code>Tk_SetWindowVisual</code>. </p>
<h2>Keywords</h2>
<p>attributes, colormap, depth, display, height, geometry manager, identifier, mapped, requested size, screen, top-level, visual, width, window, x, y</p>
