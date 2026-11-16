---
title: "xsettextproperty(3)"
name: "xsettextproperty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsettextproperty/"
description: "XSetTextProperty, XGetTextProperty – set and read text properties"
---

<p>XSetTextProperty, XGetTextProperty &#8211; set and read text properties </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XSetTextProperty(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop</i>, Atom <i>property</i>);</dd>
<dd>Status XGetTextProperty(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>text_prop_return</i>, Atom <i>property</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>property</i></dt>
<dd>Specifies the property name.</dd>
<dt><i>text_prop</i></dt>
<dd>Specifies the <code>XTextProperty</code> structure to be used.</dd>
<dt><i>text_prop_return</i></dt>
<dd>Returns the <code>XTextProperty</code> structure.</dd></dl>
<h2>Description</h2>
<p>The <code>XSetTextProperty</code> function replaces the existing specified property for the named window with the data, type, format, and number of items determined by the value field, the encoding field, the format field, and the nitems field, respectively, of the specified <code>XTextProperty</code> structure. If the property does not already exist, <code>XSetTextProperty</code> sets it for the specified window. </p>
<p> <code>XSetTextProperty</code> can generate <code>BadAlloc</code>, <code>BadAtom</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XGetTextProperty</code> function reads the specified property from the window and stores the data in the returned <code>XTextProperty</code> structure. It stores the data in the value field, the type of the data in the encoding field, the format of the data in the format field, and the number of items of data in the nitems field. An extra byte containing null (which is not included in the nitems member) is stored at the end of the value field of text_prop_return. The particular interpretation of the property&#8217;s encoding and data as text is left to the calling application. If the specified property does not exist on the window, <code>XGetTextProperty</code> sets the value field to NULL, the encoding field to <code>None</code>, the format field to zero, and the nitems field to zero. </p>
<p> If it was able to read and store the data in the <code>XTextProperty</code> structure, <code>XGetTextProperty</code> returns a nonzero status; otherwise, it returns a zero status. </p>
<p> <code>XGetTextProperty</code> can generate <code>BadAtom</code> and <code>BadWindow</code> errors.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_CLIENT_MACHINE</font></dt>
<dd>The string name of the machine on which the client application is running.</dd>
<dt><font SIZE="-1">WM_COMMAND</font></dt>
<dd>The command and arguments, null-separated, used to invoke the application.</dd>
<dt><font SIZE="-1">WM_ICON_NAME</font></dt>
<dd>The name to be used in an icon.</dd>
<dt><font SIZE="-1">WM_NAME</font></dt>
<dd>The name of the application.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></dt>
<dd>The server failed to allocate the requested resource or server memory.</dd>
<dt><code>BadAtom</code></dt>
<dd>A value for an Atom argument does not name a defined Atom.</dd>
<dt><code>BadValue</code></dt>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dd>
<dt><code>BadWindow</code></dt>
<dd>A value for a Window argument does not name a defined Window.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
