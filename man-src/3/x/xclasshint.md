---
title: "xclasshint(3)"
name: "xclasshint"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xclasshint/"
description: "XAllocClassHint, XSetClassHint, XGetClassHint, XClassHint – allocate class hints structure and set or read a window’s WM_CLASS property"
---

<p>XAllocClassHint, XSetClassHint, XGetClassHint, XClassHint &#8211; allocate class hints structure and set or read a window&#8217;s WM_CLASS property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XClassHint *XAllocClassHint(void);</p>
<dd>XSetClassHint(Display *<i>display</i>, Window <i>w</i>, XClassHint *<i>class_hints</i>);</p>
<dd>Status XGetClassHint(Display *<i>display</i>, Window <i>w</i>, XClassHint *<i>class_hints_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>class_hints</i></p>
<dd>Specifies the <code>XClassHint</code> structure that is to be used.</p>
<dt><i>class_hints_return</i></p>
<dd>Returns the <code>XClassHint</code> structure.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XAllocClassHint</code> function allocates and returns a pointer to a <code>XClassHint</code> structure. Note that the pointer fields in the <code>XClassHint</code> structure are initially set to NULL. If insufficient memory is available, <code>XAllocClassHint</code> returns NULL. To free the memory allocated to this structure, use <code>XFree</code>. </p>
<p> The <code>XSetClassHint</code> function sets the class hint for the specified window. If the strings are not in the Host Portable Character Encoding, the result is implementation-dependent. </p>
<p> <code>XSetClassHint</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetClassHint</code> function returns the class hint of the specified window to the members of the supplied structure. If the data returned by the server is in the Latin Portable Character Encoding, then the returned strings are in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. It returns a nonzero status on success; otherwise, it returns a zero status. To free res_name and res_class when finished with the strings, use <code>XFree</code> on each individually. </p>
<p> <code>XGetClassHint</code> can generate a <code>BadWindow</code> error.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_CLASS</font></p>
<dd>Set by application programs to allow window and session managers to obtain the application&#8217;s resources from the resource database.</dl>
<h2>Structures</h2>
<p>The <code>XClassHint</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*res_name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*res_class; } XClassHint; </p>
<p> The res_name member contains the application name, and the res_class member contains the application class. Note that the name set in this property may differ from the name set as WM_NAME. That is, WM_NAME specifies what should be displayed in the title bar and, therefore, can contain temporal information (for example, the name of a file currently in an editor&#8217;s buffer). On the other hand, the name specified as part of WM_CLASS is the formal name of the application that should be used when retrieving the application&#8217;s resources from the resource database.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
