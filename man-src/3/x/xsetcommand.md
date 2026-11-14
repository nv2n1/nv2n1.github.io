---
title: "xsetcommand(3)"
name: "xsetcommand"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetcommand/"
description: "XSetCommand, XGetCommand – set or read a window’s WM_COMMAND property"
---

<p>XSetCommand, XGetCommand &#8211; set or read a window&#8217;s WM_COMMAND property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetCommand(Display *<i>display</i>, Window <i>w</i>, char **<i>argv</i>, int <i>argc</i>);</p>
<dd>Status XGetCommand(Display *<i>display</i>, Window <i>w</i>, char ***<i>argv_return</i>, int *<i>argc_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>argc</i></p>
<dd>Specifies the number of arguments.</p>
<dt><i>argc_return</i></p>
<dd>Returns the number of arguments returned.</p>
<dt><i>argv</i></p>
<dd>Specifies the application&#8217;s argument list.</p>
<dt><i>argv_return</i></p>
<dd>Returns the application&#8217;s argument list.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XSetCommand</code> function sets the command and arguments used to invoke the application. (Typically, argv is the argv array of your main program.) If the strings are not in the Host Portable Character Encoding, the result is implementation-dependent. </p>
<p> <code>XSetCommand</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetCommand</code> function reads the WM_COMMAND property from the specified window and returns a string list. If the WM_COMMAND property exists, it is of type STRING and format 8. If sufficient memory can be allocated to contain the string list, <code>XGetCommand</code> fills in the argv_return and argc_return arguments and returns a nonzero status. Otherwise, or if any other error is encountered, it returns a zero status. If the data returned by the server is in the Latin Portable Character Encoding, then the returned strings are in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. To free the memory allocated to the string list, use <code>XFreeStringList</code>.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_COMMAND</font></p>
<dd>The command and arguments, null-separated, used to invoke the application.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
