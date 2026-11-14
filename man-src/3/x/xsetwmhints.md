---
title: "xsetwmhints(3)"
name: "xsetwmhints"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetwmhints/"
description: "XAllocWMHints, XSetWMHints, XGetWMHints, XWMHints – allocate window manager hints structure and set or read a window’s WM_HINTS property"
---

<p>XAllocWMHints, XSetWMHints, XGetWMHints, XWMHints &#8211; allocate window manager hints structure and set or read a window&#8217;s WM_HINTS property </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XWMHints *XAllocWMHints(void);</p>
<dd>int XSetWMHints(Display *<i>display</i>, Window <i>w</i>, XWMHints *<i>wmhints</i>);</p>
<dd>XWMHints *XGetWMHints(Display *<i>display</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>wmhints</i></p>
<dd>Specifies the <code>XWMHints</code> structure to be used.</dl>
<h2>Description</h2>
<p>The <code>XAllocWMHints</code> function allocates and returns a pointer to a <code>XWMHints</code> structure. Note that all fields in the <code>XWMHints</code> structure are initially set to zero. If insufficient memory is available, <code>XAllocWMHints</code> returns NULL. To free the memory allocated to this structure, use <code>XFree</code>. </p>
<p> The <code>XSetWMHints</code> function sets the window manager hints that include icon information and location, the initial state of the window, and whether the application relies on the window manager to get keyboard input. </p>
<p> <code>XSetWMHints</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetWMHints</code> function reads the window manager hints and returns NULL if no WM_HINTS property was set on the window or returns a pointer to a <code>XWMHints</code> structure if it succeeds. When finished with the data, free the space used for it by calling <code>XFree</code>. </p>
<p> <code>XGetWMHints</code> can generate a <code>BadWindow</code> error.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt><font SIZE="-1">WM_HINTS</font></p>
<dd>Additional hints set by the client for use by the window manager. The C type of this property is <code>XWMHints</code>.</dl>
<h2>Structures</h2>
<p>The <code>XWMHints</code> structure contains: </p>
<p> /* Window manager hints mask bits */ </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>InputHint</code> </td>
<td> (1L &lt;&lt; 0)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>StateHint</code> </td>
<td> (1L &lt;&lt; 1)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>IconPixmapHint</code> </td>
<td> (1L &lt;&lt; 2)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>IconWindowHint</code> </td>
<td> (1L &lt;&lt; 3)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>IconPositionHint</code> </td>
<td> (1L &lt;&lt; 4)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>IconMaskHint</code> </td>
<td> (1L &lt;&lt; 5)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>WindowGroupHint</code> </td>
<td> (1L &lt;&lt; 6)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>XUrgencyHint</code> </td>
<td> (1L &lt;&lt; 8)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>AllHints</code> </td>
<td> (InputHint| </p>
<p>&nbsp;StateHint| </p>
<p>&nbsp;IconPixmapHint| </p>
<p>&nbsp;IconWindowHint| </p>
<p>&nbsp;IconPositionHint| </p>
<p>&nbsp;IconMaskHint| </p>
<p>&nbsp;WindowGroupHint)
</td>
</tr>
</table>
<p> /* Values */ </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;marks which fields in this structure are defined&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool input;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;does this application rely on the window manager to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get keyboard input?&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int initial_state;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;see below&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pixmap icon_pixmap;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pixmap to be used as icon&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window icon_window;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;window to be used as icon&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int icon_x, icon_y;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;initial position of icon&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pixmap icon_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pixmap to be used as mask for icon_pixmap&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XID window_group;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;id of related window group&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;this structure may be extended in the future&nbsp;*/ } XWMHints; </p>
<p> The input member is used to communicate to the window manager the input focus model used by the application. Applications that expect input but never explicitly set focus to any of their subwindows (that is, use the push model of focus management), such as X Version 10 style applications that use real-estate driven focus, should set this member to <code>True</code>. Similarly, applications that set input focus to their subwindows only when it is given to their top-level window by a window manager should also set this member to <code>True</code>. Applications that manage their own input focus by explicitly setting focus to one of their subwindows whenever they want keyboard input (that is, use the pull model of focus management) should set this member to <code>False</code>. Applications that never expect any keyboard input also should set this member to <code>False</code>. </p>
<p> Pull model window managers should make it possible for push model applications to get input by setting input focus to the top-level windows of applications whose input member is <code>True</code>. Push model window managers should make sure that pull model applications do not break them by resetting input focus to <code>PointerRoot</code> when it is appropriate (for example, whenever an application whose input member is <code>False</code> sets input focus to one of its subwindows). </p>
<p> The definitions for the initial_state flag are: </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>WithdrawnState</code> </td>
<td> 0 </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>NormalState</code> </td>
<td> 1 </td>
<td> /* most applications start this way */
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>IconicState</code> </td>
<td> 3 </td>
<td> /* application wants to start as an icon */
</td>
</tr>
</table>
<p> The icon_mask specifies which pixels of the icon_pixmap should be used as the icon. This allows for nonrectangular icons. Both icon_pixmap and icon_mask must be bitmaps. The icon_window lets an application provide a window for use as an icon for window managers that support such use. The window_group lets you specify that this window belongs to a group of other windows. For example, if a single application manipulates multiple top-level windows, this allows you to provide enough information that a window manager can iconify all of the windows rather than just the one window. </p>
<p> The <code>UrgencyHint</code> flag, if set in the flags field, indicates that the client deems the window contents to be urgent, requiring the timely response of the user. The window manager will make some effort to draw the user&#8217;s attention to this window while this flag is set. The client must provide some means by which the user can cause the urgency flag to be cleared (either mitigating the condition that made the window urgent or merely shutting off the alarm) or the window to be withdrawn.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface, O&#8217;Reilly and Associates, Sebastopol, 1991.</i></p>
