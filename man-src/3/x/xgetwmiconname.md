---
title: "xgetwmiconname(3)"
name: "xgetwmiconname"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetwmiconname/"
description: "XSetWMIconName, XGetWMIconName, XSetIconName, XGetIconName – set or read a window’s WM_ICON_NAME property"
---

<p>XSetWMIconName, XGetWMIconName, XSetIconName, XGetIconName &#8211; set or read a window&#8217;s WM_ICON_NAME property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XSetWMIconName(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop</i>);</p>
<dd>Status XGetWMIconName(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop_return</i>);</p>
<dd>int XSetIconName(Display *<i>display</i>, Window <i>w</i>, char *<i>icon_name</i>);</p>
<dd>Status XGetIconName(Display *<i>display</i>, Window <i>w</i>, char **<i>icon_name_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>icon_name</i></p>
<dd>Specifies the icon name, which should be a null-terminated string.</p>
<dt><i>icon_name_return</i></p>
<dd>Returns the window&#8217;s icon name, which is a null-terminated string.</p>
<dt><i>text_prop</i></p>
<dd>Specifies the <code>XTextProperty</code> structure to be used.</p>
<dt><i>text_prop_return</i></p>
<dd>Returns the <code>XTextProperty</code> structure.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XSetWMIconName</code> convenience function calls <code>XSetTextProperty</code> to set the WM_ICON_NAME property. </p>
<p> The <code>XGetWMIconName</code> convenience function calls <code>XGetTextProperty</code> to obtain the WM_ICON_NAME property. It returns a nonzero status on success; otherwise, it returns a zero status. </p>
<p> The <code>XSetIconName</code> function sets the name to be displayed in a window&#8217;s icon. </p>
<p> <code>XSetIconName</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetIconName</code> function returns the name to be displayed in the specified window&#8217;s icon. If it succeeds, it returns a nonzero status; otherwise, if no icon name has been set for the window, it returns zero. If you never assigned a name to the window, <code>XGetIconName</code> sets icon_name_return to NULL. If the data returned by the server is in the Latin Portable Character Encoding, then the returned string is in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. When finished with it, a client must free the icon name string using <code>XFree</code>. </p>
<p> <code>XGetIconName</code> can generate a <code>BadWindow</code> error.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_ICON_NAME</font></p>
<dd>The name to be used in an icon.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
