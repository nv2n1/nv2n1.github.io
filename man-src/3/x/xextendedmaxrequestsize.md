---
title: "xextendedmaxrequestsize(3)"
name: "xextendedmaxrequestsize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xextendedmaxrequestsize/"
description: "AllPlanes, BlackPixel, WhitePixel, ConnectionNumber, DefaultColormap, DefaultDepth, XListDepths, DefaultGC, DefaultRootWindow, DefaultScreenOfDisplay, DefaultScreen, DefaultVisual, DisplayCells, Di..."
---

<p>AllPlanes, BlackPixel, WhitePixel, ConnectionNumber, DefaultColormap, DefaultDepth, XListDepths, DefaultGC, DefaultRootWindow, DefaultScreenOfDisplay, DefaultScreen, DefaultVisual, DisplayCells, DisplayPlanes, DisplayString, XMaxRequestSize, XExtendedMaxRequestSize, LastKnownRequestProcessed, NextRequest, ProtocolVersion, ProtocolRevision, QLength, RootWindow, ScreenCount, ScreenOfDisplay, ServerVendor, VendorRelease &#8211; Display macros and functions </p>
<h2>Syntax</h2>
<p>unsigned long AllPlanes;</p>
<dl COMPACT>
<dd>unsigned long BlackPixel(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>unsigned long WhitePixel(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int ConnectionNumber(Display *<i>display</i>);</p>
<dd>Colormap DefaultColormap(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int DefaultDepth(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int *XListDepths(Display *<i>display</i>, int <i>screen_number</i>, int <i>count_return</i>);</p>
<dd>GC DefaultGC(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>Window DefaultRootWindow(Display *<i>display</i>);</p>
<dd>Screen *DefaultScreenOfDisplay(Display *<i>display</i>);</p>
<dd>int DefaultScreen(Display *<i>display</i>);</p>
<dd>Visual *DefaultVisual(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int DisplayCells(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int DisplayPlanes(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>char *DisplayString(Display *<i>display</i>);</p>
<dd>long XMaxRequestSize(Display *<i>display</i>)</p>
<dd>long XExtendedMaxRequestSize(Display *<i>display</i>)</p>
<dd>unsigned long LastKnownRequestProcessed(Display *<i>display</i>);</p>
<dd>unsigned long NextRequest(Display *<i>display</i>);</p>
<dd>int ProtocolVersion(Display *<i>display</i>);</p>
<dd>int ProtocolRevision(Display *<i>display</i>);</p>
<dd>int QLength(Display *<i>display</i>);</p>
<dd>Window RootWindow(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int ScreenCount(Display *<i>display</i>);</p>
<dd>Screen *ScreenOfDisplay(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>char *ServerVendor(Display *<i>display</i>)</p>
<dd>int VendorRelease(Display *<i>display</i>)</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>screen_number</i></p>
<dd>Specifies the appropriate screen number on the host server.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of depths.</dl>
<h2>Description</h2>
<p>The <code>AllPlanes</code> macro returns a value with all bits set to 1 suitable for use in a plane argument to a procedure. </p>
<p> The <code>BlackPixel</code> macro returns the black pixel value for the specified screen. </p>
<p> The <code>WhitePixel</code> macro returns the white pixel value for the specified screen. </p>
<p> The <code>ConnectionNumber</code> macro returns a connection number for the specified display. </p>
<p> The <code>DefaultColormap</code> macro returns the default colormap ID for allocation on the specified screen. </p>
<p> The <code>DefaultDepth</code> macro returns the depth (number of planes) of the default root window for the specified screen. </p>
<p> The <code>XListDepths</code> function returns the array of depths that are available on the specified screen. If the specified screen_number is valid and sufficient memory for the array can be allocated, <code>XListDepths</code> sets count_return to the number of available depths. Otherwise, it does not set count_return and returns NULL. To release the memory allocated for the array of depths, use <code>XFree</code>. </p>
<p> The <code>DefaultGC</code> macro returns the default GC for the root window of the specified screen. </p>
<p> The <code>DefaultRootWindow</code> macro returns the root window for the default screen. </p>
<p> The <code>DefaultScreenOfDisplay</code> macro returns the default screen of the specified display. </p>
<p> The <code>DefaultScreen</code> macro returns the default screen number referenced in the <code>XOpenDisplay</code> routine. </p>
<p> The <code>DefaultVisual</code> macro returns the default visual type for the specified screen. </p>
<p> The <code>DisplayCells</code> macro returns the number of entries in the default colormap. </p>
<p> The <code>DisplayPlanes</code> macro returns the depth of the root window of the specified screen. </p>
<p> The <code>DisplayString</code> macro returns the string that was passed to <code>XOpenDisplay</code> when the current display was opened. </p>
<p> The <code>XMaxRequestSize</code> function returns the maximum request size (in 4-byte units) supported by the server without using an extended-length protocol encoding. Single protocol requests to the server can be no larger than this size unless an extended-length protocol encoding is supported by the server. The protocol guarantees the size to be no smaller than 4096 units (16384 bytes). Xlib automatically breaks data up into multiple protocol requests as necessary for the following functions: <code>XDrawPoints</code>, <code>XDrawRectangles</code>, <code>XDrawSegments</code>, <code>XFillArcs</code>, <code>XFillRectangles</code>, and <code>XPutImage</code>. </p>
<p> The <code>XExtendedMaxRequestSize</code> function returns zero if the specified display does not support an extended-length protocol encoding; otherwise, it returns the maximum request size (in 4-byte units) supported by the server using the extended-length encoding. The Xlib functions <code>XDrawLines</code>, <code>XDrawArcs</code>, <code>XFillPolygon</code>, <code>XChangeProperty</code>, <code>XSetClipRectangles</code>, and <code>XSetRegion</code> will use the extended-length encoding as necessary, if supported by the server. Use of the extended-length encoding in other Xlib functions (for example, <code>XDrawPoints</code>, <code>XDrawRectangles</code>, <code>XDrawSegments</code>, <code>XFillArcs</code>, <code>XFillRectangles</code>, <code>XPutImage</code>) is permitted but not required; an Xlib implementation may choose to split the data across multiple smaller requests instead. </p>
<p> The <code>LastKnownRequestProcessed</code> macro extracts the full serial number of the last request known by Xlib to have been processed by the X server. </p>
<p> The <code>NextRequest</code> macro extracts the full serial number that is to be used for the next request. </p>
<p> The <code>ProtocolVersion</code> macro returns the major version number (11) of the X protocol associated with the connected display. </p>
<p> The <code>ProtocolRevision</code> macro returns the minor protocol revision number of the X server. </p>
<p> The <code>QLength</code> macro returns the length of the event queue for the connected display. </p>
<p> The <code>RootWindow</code> macro returns the root window. </p>
<p> The <code>ScreenCount</code> macro returns the number of available screens. </p>
<p> The <code>ScreenOfDisplay</code> macro returns a pointer to the screen of the specified display. </p>
<p> The <code>ServerVendor</code> macro returns a pointer to a null-terminated string that provides some identification of the owner of the X server implementation. </p>
<p> The <code>VendorRelease</code> macro returns a number related to a vendor&#8217;s release of the X server.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-blackpixelofscreen/">BlackPixelOfScreen</a>(3), <a href="/docs/linux/man/3-imagebyteorder/">ImageByteOrder</a>(3), <a href="/docs/linux/man/3-iscursorkey/">IsCursorKey</a>(3), <a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
