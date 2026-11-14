---
title: "xsetwmclientmachine(3)"
name: "xsetwmclientmachine"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetwmclientmachine/"
description: "XSetWMClientMachine, XGetWMClientMachine – set or read a window’s WM_CLIENT_MACHINE property"
---

<p>XSetWMClientMachine, XGetWMClientMachine &#8211; set or read a window&#8217;s WM_CLIENT_MACHINE property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XSetWMClientMachine(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop</i>);</p>
<dd>Status XGetWMClientMachine(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>text_prop</i></p>
<dd>Specifies the <code>XTextProperty</code> structure to be used.</p>
<dt><i>text_prop_return</i></p>
<dd>Returns the <code>XTextProperty</code> structure.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XSetWMClientMachine</code> convenience function calls <code>XSetTextProperty</code> to set the WM_CLIENT_MACHINE property. </p>
<p> The <code>XGetWMClientMachine</code> convenience function performs an <code>XGetTextProperty</code> on the WM_CLIENT_MACHINE property. It returns a nonzero status on success; otherwise, it returns a zero status.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_CLIENT_MACHINE</font></p>
<dd>The string name of the machine on which the client application is running.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
