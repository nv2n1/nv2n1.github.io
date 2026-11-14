---
title: "xgetwmprotocols(3)"
name: "xgetwmprotocols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetwmprotocols/"
description: "XSetWMProtocols, XGetWMProtocols – set or read a window’s WM_PROTOCOLS property"
---

<p>XSetWMProtocols, XGetWMProtocols &#8211; set or read a window&#8217;s WM_PROTOCOLS property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XSetWMProtocols(Display *<i>display</i>, Window <i>w</i>, Atom *<i>protocols</i>, int <i>count</i>);</p>
<dd>Status XGetWMProtocols(Display *<i>display</i>, Window <i>w</i>, Atom **<i>protocols_return</i>, int *<i>count_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>count</i></p>
<dd>Specifies the number of protocols in the list.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of protocols in the list.</p>
<dt><i>protocols</i></p>
<dd>Specifies the list of protocols.</p>
<dt><i>protocols_return</i></p>
<dd>Returns the list of protocols.</dl>
<h2>Description</h2>
<p>The <code>XSetWMProtocols</code> function replaces the WM_PROTOCOLS property on the specified window with the list of atoms specified by the protocols argument. If the property does not already exist, <code>XSetWMProtocols</code> sets the WM_PROTOCOLS property on the specified window to the list of atoms specified by the protocols argument. The property is stored with a type of ATOM and a format of 32. If it cannot intern the WM_PROTOCOLS atom, <code>XSetWMProtocols</code> returns a zero status. Otherwise, it returns a nonzero status. </p>
<p> <code>XSetWMProtocols</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetWMProtocols</code> function returns the list of atoms stored in the WM_PROTOCOLS property on the specified window. These atoms describe window manager protocols in which the owner of this window is willing to participate. If the property exists, is of type ATOM, is of format 32, and the atom WM_PROTOCOLS can be interned, <code>XGetWMProtocols</code> sets the protocols_return argument to a list of atoms, sets the count_return argument to the number of elements in the list, and returns a nonzero status. Otherwise, it sets neither of the return arguments and returns a zero status. To release the list of atoms, use <code>XFree</code>. </p>
<p> <code>XGetWMProtocols</code> can generate a <code>BadWindow</code> error.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_PROTOCOLS</font></p>
<dd>List of atoms that identify the communications protocols between the client and window manager in which the client is willing to participate.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
