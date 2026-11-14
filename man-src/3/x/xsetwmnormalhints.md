---
title: "xsetwmnormalhints(3)"
name: "xsetwmnormalhints"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetwmnormalhints/"
description: "XAllocSizeHints, XSetWMNormalHints, XGetWMNormalHints, XSetWMSizeHints, XGetWMSizeHints, XSizeHints – allocate size hints structure and set or read a window’s WM_NORMAL_HINTS property"
---

<p>XAllocSizeHints, XSetWMNormalHints, XGetWMNormalHints, XSetWMSizeHints, XGetWMSizeHints, XSizeHints &#8211; allocate size hints structure and set or read a window&#8217;s WM_NORMAL_HINTS property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XSizeHints *XAllocSizeHints(void);</p>
<dd>void XSetWMNormalHints(Display *<i>display</i>, Window <i>w</i>, XSizeHints *<i>hints</i>);</p>
<dd>Status XGetWMNormalHints(Display *<i>display</i>, Window <i>w</i>, XSizeHints *<i>hints_return</i>, long *<i>supplied_return</i>);</p>
<dd>void XSetWMSizeHints(Display *<i>display</i>, Window <i>w</i>, XSizeHints *<i>hints</i>, Atom <i>property</i>);</p>
<dd>Status XGetWMSizeHints(Display *<i>display</i>, Window <i>w</i>, XSizeHints *<i>hints_return</i>, long *<i>supplied_return</i>, Atom <i>property</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>hints</i></p>
<dd>Specifies the size hints for the window in its normal state.</p>
<dt><i>hints</i></p>
<dd>Specifies the <code>XSizeHints</code> structure to be used.</p>
<dt><i>hints_return</i></p>
<dd>Returns the size hints for the window in its normal state.</p>
<dt><i>property</i></p>
<dd>Specifies the property name.</p>
<dt><i>supplied_return</i></p>
<dd>Returns the hints that were supplied by the user.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XAllocSizeHints</code> function allocates and returns a pointer to a <code>XSizeHints</code> structure. Note that all fields in the <code>XSizeHints</code> structure are initially set to zero. If insufficient memory is available, <code>XAllocSizeHints</code> returns NULL. To free the memory allocated to this structure, use <code>XFree</code>. </p>
<p> The <code>XSetWMNormalHints</code> function replaces the size hints for the WM_NORMAL_HINTS property on the specified window. If the property does not already exist, <code>XSetWMNormalHints</code> sets the size hints for the WM_NORMAL_HINTS property on the specified window. The property is stored with a type of WM_SIZE_HINTS and a format of 32. </p>
<p> <code>XSetWMNormalHints</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetWMNormalHints</code> function returns the size hints stored in the WM_NORMAL_HINTS property on the specified window. If the property is of type WM_SIZE_HINTS, is of format 32, and is long enough to contain either an old (pre-ICCCM) or new size hints structure, <code>XGetWMNormalHints</code> sets the various fields of the <code>XSizeHints</code> structure, sets the supplied_return argument to the list of fields that were supplied by the user (whether or not they contained defined values), and returns a nonzero status. Otherwise, it returns a zero status. </p>
<p> If <code>XGetWMNormalHints</code> returns successfully and a pre-ICCCM size hints property is read, the supplied_return argument will contain the following bits: </p>
<p> (USPosition|USSize|PPosition|PSize|PMinSize|<br />
&nbsp;PMaxSize|PResizeInc|PAspect) </p>
<p> If the property is large enough to contain the base size and window gravity fields as well, the supplied_return argument will also contain the following bits: </p>
<p> PBaseSize|PWinGravity </p>
<p> <code>XGetWMNormalHints</code> can generate a PN BadWindow error. </p>
<p> The <code>XSetWMSizeHints</code> function replaces the size hints for the specified property on the named window. If the specified property does not already exist, <code>XSetWMSizeHints</code> sets the size hints for the specified property on the named window. The property is stored with a type of WM_SIZE_HINTS and a format of 32. To set a window&#8217;s normal size hints, you can use the <code>XSetWMNormalHints</code> function. </p>
<p> <code>XSetWMSizeHints</code> can generate <code>BadAlloc</code>, <code>BadAtom</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XGetWMSizeHints</code> function returns the size hints stored in the specified property on the named window. If the property is of type WM_SIZE_HINTS, is of format 32, and is long enough to contain either an old (pre-ICCCM) or new size hints structure, <code>XGetWMSizeHints</code> sets the various fields of the <code>XSizeHints</code> structure, sets the supplied_return argument to the list of fields that were supplied by the user (whether or not they contained defined values), and returns a nonzero status. Otherwise, it returns a zero status. To get a window&#8217;s normal size hints, you can use the <code>XGetWMNormalHints</code> function. </p>
<p> If <code>XGetWMSizeHints</code> returns successfully and a pre-ICCCM size hints property is read, the supplied_return argument will contain the following bits: </p>
<p> (USPosition|USSize|PPosition|PSize|PMinSize|<br />
&nbsp;PMaxSize|PResizeInc|PAspect) </p>
<p> If the property is large enough to contain the base size and window gravity fields as well, the supplied_return argument will also contain the following bits: </p>
<p> PBaseSize|PWinGravity </p>
<p> <code>XGetWMSizeHints</code> can generate <code>BadAtom</code> and <code>BadWindow</code> errors.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_NORMAL_HINTS</font></p>
<dd>Size hints for a window in its normal state. The C type of this property is <code>XSizeHints</code>.</dl>
<h2>Structures</h2>
<p>The <code>XSizeHints</code> structure contains: </p>
<p> /* Size hints mask bits */ </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>USPosition</code> </td>
<td> (1L &lt;&lt; 0) </td>
<td> /* user specified x, y */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>USSize</code> </td>
<td> (1L &lt;&lt; 1) </td>
<td> /* user specified width, height */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PPosition</code> </td>
<td> (1L &lt;&lt; 2) </td>
<td> /* program specified position */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PSize</code> </td>
<td> (1L &lt;&lt; 3) </td>
<td> /* program specified size */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PMinSize</code> </td>
<td> (1L &lt;&lt; 4) </td>
<td> /* program specified minimum size */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PMaxSize</code> </td>
<td> (1L &lt;&lt; 5) </td>
<td> /* program specified maximum size */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PResizeInc</code> </td>
<td> (1L &lt;&lt; 6) </td>
<td> /* program specified resize increments */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PAspect</code> </td>
<td> (1L &lt;&lt; 7) </td>
<td> /* program specified min and max aspect ratios */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PBaseSize</code> </td>
<td> (1L &lt;&lt; 8) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PWinGravity</code> </td>
<td> (1L &lt;&lt; 9) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>PAllHints</code> </td>
<td> (PPosition| </p>
<p>&nbsp;PSize| </p>
<p>&nbsp;PMinSize| </p>
<p>&nbsp;PMaxSize| </p>
<p>&nbsp;PResizeInc| </p>
<p>&nbsp;PAspect) </td>
<td>
</td>
</tr>
</table>
<p> /* Values */ </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;marks which fields in this structure are defined&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int x, y;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obsolete&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int width, height;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obsolete&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int min_width, min_height;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int max_width, max_height;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int width_inc, height_inc;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int x;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;numerator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int y;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;denominator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;min_aspect, max_aspect;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int base_width, base_height;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int win_gravity;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;this structure may be extended in the future&nbsp;*/ } XSizeHints; </p>
<p> The x, y, width, and height members are now obsolete and are left solely for compatibility reasons. The min_width and min_height members specify the minimum window size that still allows the application to be useful. The max_width and max_height members specify the maximum window size. The width_inc and height_inc members define an arithmetic progression of sizes (minimum to maximum) into which the window prefers to be resized. The min_aspect and max_aspect members are expressed as ratios of x and y, and they allow an application to specify the range of aspect ratios it prefers. The base_width and base_height members define the desired size of the window. The window manager will interpret the position of the window and its border width to position the point of the outer rectangle of the overall window specified by the win_gravity member. The outer rectangle of the window includes any borders or decorations supplied by the window manager. In other words, if the window manager decides to place the window where the client asked, the position on the parent window&#8217;s border named by the win_gravity will be placed where the client window would have been placed in the absence of a window manager. </p>
<p> Note that use of the <code>PAllHints</code> macro is highly discouraged.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface, O&#8217;Reilly and Associates,</i></p>
