---
title: "xmovewindow(3)"
name: "xmovewindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmovewindow/"
description: "XConfigureWindow, XMoveWindow, XResizeWindow, XMoveResizeWindow, XSetWindowBorderWidth, XWindowChanges – configure windows and window changes structure"
---

<p>XConfigureWindow, XMoveWindow, XResizeWindow, XMoveResizeWindow, XSetWindowBorderWidth, XWindowChanges &#8211; configure windows and window changes structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XConfigureWindow(Display *<i>display</i>, Window <i>w</i>, unsigned <i>value_mask</i>, XWindowChanges *<i>changes</i>);</p>
<dd>int XMoveWindow(Display *<i>display</i>, Window <i>w</i>, int <i>x</i>, <i>y</i>);</p>
<dd>int XResizeWindow(Display *<i>display</i>, Window <i>w</i>, unsigned <i>width</i>, unsigned <i>height</i>);</p>
<dd>int XMoveResizeWindow(Display *<i>display</i>, Window <i>w</i>, int <i>x</i>, int <i>y</i>, unsigned <i>width</i>, unsigned <i>height</i>);</p>
<dd>int XSetWindowBorderWidth(Display *<i>display</i>, Window <i>w</i>, unsigned <i>width</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>value_mask</i></p>
<dd>Specifies which values are to be set using information in the values structure. This mask is the bitwise inclusive OR of the valid configure window values bits.</p>
<dt><i>values</i></p>
<dd>Specifies the <code>XWindowChanges</code> structure.</p>
<dt><i>w</i></p>
<dd>Specifies the window to be reconfigured, moved, or resized..</p>
<dt><i>width</i></p>
<dd>Specifies the width of the window border.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which are the interior dimensions of the window.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which define the new location of the top-left pixel of the window&#8217;s border or the window itself if it has no border or define the new position of the window relative to its parent.</dl>
<h2>Description</h2>
<p>The <code>XConfigureWindow</code> function uses the values specified in the <code>XWindowChanges</code> structure to reconfigure a window&#8217;s size, position, border, and stacking order. Values not specified are taken from the existing geometry of the window. </p>
<p> If a sibling is specified without a stack_mode or if the window is not actually a sibling, a <code>BadMatch</code> error results. Note that the computations for <code>BottomIf</code>, <code>TopIf</code>, and <code>Opposite</code> are performed with respect to the window&#8217;s final geometry (as controlled by the other arguments passed to <code>XConfigureWindow</code>), not its initial geometry. Any backing store contents of the window, its inferiors, and other newly visible windows are either discarded or changed to reflect the current screen contents (depending on the implementation). </p>
<p> <code>XConfigureWindow</code> can generate <code>BadMatch</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XMoveWindow</code> function moves the specified window to the specified x and y coordinates, but it does not change the window&#8217;s size, raise the window, or change the mapping state of the window. Moving a mapped window may or may not lose the window&#8217;s contents depending on if the window is obscured by nonchildren and if no backing store exists. If the contents of the window are lost, the X server generates <code>Expose</code> events. Moving a mapped window generates <code>Expose</code> events on any formerly obscured windows. </p>
<p> If the override-redirect flag of the window is <code>False</code> and some other client has selected <code>SubstructureRedirectMask</code> on the parent, the X server generates a <code>ConfigureRequest</code> event, and no further processing is performed. Otherwise, the window is moved. </p>
<p> <code>XMoveWindow</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XResizeWindow</code> function changes the inside dimensions of the specified window, not including its borders. This function does not change the window&#8217;s upper-left coordinate or the origin and does not restack the window. Changing the size of a mapped window may lose its contents and generate <code>Expose</code> events. If a mapped window is made smaller, changing its size generates <code>Expose</code> events on windows that the mapped window formerly obscured. </p>
<p> If the override-redirect flag of the window is <code>False</code> and some other client has selected <code>SubstructureRedirectMask</code> on the parent, the X server generates a <code>ConfigureRequest</code> event, and no further processing is performed. If either width or height is zero, a <code>BadValue</code> error results. </p>
<p> <code>XResizeWindow</code> can generate <code>BadValue</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XMoveResizeWindow</code> function changes the size and location of the specified window without raising it. Moving and resizing a mapped window may generate an <code>Expose</code> event on the window. Depending on the new size and location parameters, moving and resizing a window may generate <code>Expose</code> events on windows that the window formerly obscured. </p>
<p> If the override-redirect flag of the window is <code>False</code> and some other client has selected <code>SubstructureRedirectMask</code> on the parent, the X server generates a <code>ConfigureRequest</code> event, and no further processing is performed. Otherwise, the window size and location are changed. </p>
<p> <code>XMoveResizeWindow</code> can generate <code>BadValue</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XSetWindowBorderWidth</code> function sets the specified window&#8217;s border width to the specified width. </p>
<p> <code>XSetWindowBorderWidth</code> can generate a <code>BadWindow</code> error.</p>
<h2>Structures</h2>
<p>The <code>XWindowChanges</code> structure contains: </p>
<p> /* Configure window value mask bits */ </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWX</code> </td>
<td> (1&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWY</code> </td>
<td> (1&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWWidth</code> </td>
<td> (1&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWHeight</code> </td>
<td> (1&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBorderWidth</code> </td>
<td> (1&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWSibling</code> </td>
<td> (1&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWStackMode</code> </td>
<td> (1&lt;&lt;6)
</td>
</tr>
</table>
<p> /* Values */ </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int x, y;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int width, height;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int border_width;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window sibling;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int stack_mode; } XWindowChanges; </p>
<p> The x and y members are used to set the window&#8217;s x and y coordinates, which are relative to the parent&#8217;s origin and indicate the position of the upper-left outer corner of the window. The width and height members are used to set the inside size of the window, not including the border, and must be nonzero, or a <code>BadValue</code> error results. Attempts to configure a root window have no effect. </p>
<p> The border_width member is used to set the width of the border in pixels. Note that setting just the border width leaves the outer-left corner of the window in a fixed position but moves the absolute position of the window&#8217;s origin. If you attempt to set the border-width attribute of an <code>InputOnly</code> window nonzero, a <code>BadMatch</code> error results. </p>
<p> The sibling member is used to set the sibling window for stacking operations. The stack_mode member is used to set how the window is to be restacked and can be set to <code>Above</code>, <code>Below</code>, <code>TopIf</code>, <code>BottomIf</code>, or <code>Opposite</code>.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xdestroywindow/">XDestroyWindow</a>(3), <a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a>(3), <a href="/docs/linux/man/3-xraisewindow/">XRaiseWindow</a>(3), <a href="/docs/linux/man/3-xunmapwindow/">XUnmapWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
