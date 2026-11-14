---
title: "xiconsize(3)"
name: "xiconsize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xiconsize/"
description: "XAllocIconSize, XSetIconSizes, XGetIconSizes, XIconSize – allocate icon size structure and set or read a window’s WM_ICON_SIZES property"
---

<p>XAllocIconSize, XSetIconSizes, XGetIconSizes, XIconSize &#8211; allocate icon size structure and set or read a window&#8217;s WM_ICON_SIZES property </p>
<h2>Syntax</h2>
<p>XIconSize *XAllocIconSize(void); </p>
<p> int XSetIconSizes(Display *<i>display</i>, Window <i>w</i>, XIconSize *<i>size_list</i>, int <i>count</i>); </p>
<p> Status XGetIconSizes(Display *<i>display</i>, Window <i>w</i>, XIconSize **<i>size_list_return</i>, int <i>count_return</i>);</p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>count</i></p>
<dd>Specifies the number of items in the size list.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of items in the size list.</p>
<dt><i>size_list</i></p>
<dd>Specifies the size list.</p>
<dt><i>size_list_return</i></p>
<dd>Returns the size list.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XAllocIconSize</code> function allocates and returns a pointer to a <code>XIconSize</code> structure. Note that all fields in the <code>XIconSize</code> structure are initially set to zero. If insufficient memory is available, <code>XAllocIconSize</code> returns NULL. To free the memory allocated to this structure, use <code>XFree</code>. </p>
<p> The <code>XSetIconSizes</code> function is used only by window managers to set the supported icon sizes. </p>
<p> <code>XSetIconSizes</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetIconSizes</code> function returns zero if a window manager has not set icon sizes; otherwise, it return nonzero. <code>XGetIconSizes</code> should be called by an application that wants to find out what icon sizes would be most appreciated by the window manager under which the application is running. The application should then use <code>XSetWMHints</code> to supply the window manager with an icon pixmap or window in one of the supported sizes. To free the data allocated in size_list_return, use <code>XFree</code>. </p>
<p> <code>XGetIconSizes</code> can generate a <code>BadWindow</code> error.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_ICON_SIZES</font></p>
<dd>The window manager may set this property on the root window to specify the icon sizes it supports. The C type of this property is <code>XIconSize</code>.</dl>
<h2>Structures</h2>
<p>The <code>XIconSize</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int min_width, min_height;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int max_width, max_height;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int width_inc, height_inc; } XIconSize; </p>
<p> The width_inc and height_inc members define an arithmetic progression of sizes (minimum to maximum) that represent the supported icon sizes.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
