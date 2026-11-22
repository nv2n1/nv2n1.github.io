---
title: "xsettransientforhint(3)"
name: "xsettransientforhint"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsettransientforhint/"
description: "XSetTransientForHint, XGetTransientForHint – set or read a window’s WM_TRANSIENT_FOR property"
---

<p>XSetTransientForHint, XGetTransientForHint &#8211; set or read a window&#8217;s WM_TRANSIENT_FOR property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetTransientForHint(Display *<i>display</i>, Window <i>w</i>, Window <i>prop_window</i>);</dd>
<dd>Status XGetTransientForHint(Display *<i>display</i>, Window <i>w</i>, Window *<i>prop_window_return</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>w</i></dt>
<dd>Specifies the window.</dd>
<dt><i>prop_window</i></dt>
<dd>Specifies the window that the WM_TRANSIENT_FOR property is to be set to.</dd>
<dt><i>prop_window_return</i></dt>
<dd>Returns the WM_TRANSIENT_FOR property of the specified window.</dd></dl>
<h2>Description</h2>
<p>The <code>XSetTransientForHint</code> function sets the WM_TRANSIENT_FOR property of the specified window to the specified prop_window. </p>
<p> <code>XSetTransientForHint</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetTransientForHint</code> function returns the WM_TRANSIENT_FOR property for the specified window. It returns a nonzero status on success; otherwise, it returns a zero status. </p>
<p> <code>XGetTransientForHint</code> can generate a <code>BadWindow</code> error.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt>WM_TRANSIENT_FOR</dt>
<dd>Set by application programs to indicate to the window manager that a transient top-level window, such as a dialog box.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></dt>
<dd>The server failed to allocate the requested resource or server memory.</dd>
<dt><code>BadWindow</code></dt>
<dd>A value for a Window argument does not name a defined Window.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
