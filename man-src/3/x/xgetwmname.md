---
title: "xgetwmname(3)"
name: "xgetwmname"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetwmname/"
description: "XSetWMName, XGetWMName, XStoreName, XFetchName – set or read a window’s WM_NAME property"
---

<p>XSetWMName, XGetWMName, XStoreName, XFetchName &#8211; set or read a window&#8217;s WM_NAME property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XSetWMName(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop</i>);</p>
<dd>Status XGetWMName(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop_return</i>);</p>
<dd>int XStoreName(Display *<i>display</i>, Window <i>w</i>, char *<i>window_name</i>);</p>
<dd>Status XFetchName(Display *<i>display</i>, Window <i>w</i>, char **<i>window_name_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>text_prop</i></p>
<dd>Specifies the <code>XTextProperty</code> structure to be used.</p>
<dt><i>text_prop_return</i></p>
<dd>Returns the <code>XTextProperty</code> structure.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>window_name</i></p>
<dd>Specifies the window name, which should be a null-terminated string.</p>
<dt><i>window_name_return</i></p>
<dd>Returns the window name, which is a null-terminated string.</dl>
<h2>Description</h2>
<p>The <code>XSetWMName</code> convenience function calls <code>XSetTextProperty</code> to set the WM_NAME property. </p>
<p> The <code>XGetWMName</code> convenience function calls <code>XGetTextProperty</code> to obtain the WM_NAME property. It returns a nonzero status on success; otherwise, it returns a zero status. </p>
<p> The <code>XStoreName</code> function assigns the name passed to window_name to the specified window. A window manager can display the window name in some prominent place, such as the title bar, to allow users to identify windows easily. Some window managers may display a window&#8217;s name in the window&#8217;s icon, although they are encouraged to use the window&#8217;s icon name if one is provided by the application. If the string is not in the Host Portable Character Encoding, the result is implementation-dependent. </p>
<p> <code>XStoreName</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XFetchName</code> function returns the name of the specified window. If it succeeds, it returns a nonzero status; otherwise, no name has been set for the window, and it returns zero. If the WM_NAME property has not been set for this window, <code>XFetchName</code> sets window_name_return to NULL. If the data returned by the server is in the Latin Portable Character Encoding, then the returned string is in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. When finished with it, a client must free the window name string using <code>XFree</code>. </p>
<p> <code>XFetchName</code> can generate a <code>BadWindow</code> error.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_NAME</font></p>
<dd>The name of the application.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
