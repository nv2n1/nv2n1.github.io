---
title: "xcreatewindow(3)"
name: "xcreatewindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcreatewindow/"
description: "XCreateWindow, XCreateSimpleWindow, XSetWindowAttributes – create windows and window attributes structure"
---

<p>XCreateWindow, XCreateSimpleWindow, XSetWindowAttributes &#8211; create windows and window attributes structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Window XCreateWindow(Display *<i>display</i>, Window <i>parent</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int <i>border_width</i>, int <i>depth</i>, unsigned int <i>class</i>, Visual *<i>visual</i>, unsigned long <i>valuemask</i>, XSetWindowAttributes *<i>attributes</i>);</p>
<dd>Window XCreateSimpleWindow(Display *<i>display</i>, Window <i>parent</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int <i>border_width</i>, unsigned long <i>border</i>, unsigned long <i>background</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>attributes</i></p>
<dd>Specifies the structure from which the values (as specified by the value mask) are to be taken. The value mask should have the appropriate bits set to indicate which attributes have been set in the structure.</p>
<dt><i>background</i></p>
<dd>Specifies the background pixel value of the window. </p>
<dt><i>border</i></p>
<dd>Specifies the border pixel value of the window.</p>
<dt><i>border_width</i></p>
<dd>Specifies the width of the created window&#8217;s border in pixels.</p>
<dt><i>class</i></p>
<dd>Specifies the created window&#8217;s class. You can pass <code>InputOutput</code>, <code>InputOnly</code>, or <code>CopyFromParent</code>. A class of <code>CopyFromParent</code> means the class is taken from the parent.</p>
<dt><i>depth</i></p>
<dd>Specifies the window&#8217;s depth. A depth of <code>CopyFromParent</code> means the depth is taken from the parent.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>parent</i></p>
<dd>Specifies the parent window.</p>
<dt><i>valuemask</i></p>
<dd>Specifies which window attributes are defined in the attributes argument. This mask is the bitwise inclusive OR of the valid attribute mask bits. If valuemask is zero, the attributes are ignored and are not referenced.</p>
<dt><i>visual</i></p>
<dd>Specifies the visual type. A visual of <code>CopyFromParent</code> means the visual type is taken from the parent.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which are the created window&#8217;s inside dimensions and do not include the created window&#8217;s borders.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which are the top-left outside corner of the window&#8217;s borders and are relative to the inside of the parent window&#8217;s borders.</dl>
<h2>Description</h2>
<p>The <code>XCreateWindow</code> function creates an unmapped subwindow for a specified parent window, returns the window ID of the created window, and causes the X server to generate a <code>CreateNotify</code> event. The created window is placed on top in the stacking order with respect to siblings. </p>
<p> The coordinate system has the X axis horizontal and the Y axis vertical with the origin [0, 0] at the upper-left corner. Coordinates are integral, in terms of pixels, and coincide with pixel centers. Each window and pixmap has its own coordinate system. For a window, the origin is inside the border at the inside, upper-left corner. </p>
<p> The border_width for an <code>InputOnly</code> window must be zero, or a <code>BadMatch</code> error results. For class <code>InputOutput</code>, the visual type and depth must be a combination supported for the screen, or a <code>BadMatch</code> error results. The depth need not be the same as the parent, but the parent must not be a window of class <code>InputOnly</code>, or a <code>BadMatch</code> error results. For an <code>InputOnly</code> window, the depth must be zero, and the visual must be one supported by the screen. If either condition is not met, a <code>BadMatch</code> error results. The parent window, however, may have any depth and class. If you specify any invalid window attribute for a window, a <code>BadMatch</code> error results. </p>
<p> The created window is not yet displayed (mapped) on the user&#8217;s display. To display the window, call <code>XMapWindow</code>. The new window initially uses the same cursor as its parent. A new cursor can be defined for the new window by calling <code>XDefineCursor</code>. The window will not be visible on the screen unless it and all of its ancestors are mapped and it is not obscured by any of its ancestors. </p>
<p> <code>XCreateWindow</code> can generate <code>BadAlloc</code> <code>BadColor</code>, <code>BadCursor</code>, <code>BadMatch</code>, <code>BadPixmap</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XCreateSimpleWindow</code> function creates an unmapped <code>InputOutput</code> subwindow for a specified parent window, returns the window ID of the created window, and causes the X server to generate a <code>CreateNotify</code> event. The created window is placed on top in the stacking order with respect to siblings. Any part of the window that extends outside its parent window is clipped. The border_width for an <code>InputOnly</code> window must be zero, or a <code>BadMatch</code> error results. <code>XCreateSimpleWindow</code> inherits its depth, class, and visual from its parent. All other window attributes, except background and border, have their default values. </p>
<p> <code>XCreateSimpleWindow</code> can generate <code>BadAlloc</code>, <code>BadMatch</code>, <code>BadValue</code>, and <code>BadWindow</code> errors.</p>
<h2>Structures</h2>
<p>The <code>XSetWindow</code>Attributes structure contains: </p>
<p> /* Window attribute value mask bits */ </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBackPixmap</code> </td>
<td> (1L&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBackPixel</code> </td>
<td> (1L&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBorderPixmap</code> </td>
<td> (1L&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBorderPixel</code> </td>
<td> (1L&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBitGravity</code> </td>
<td> (1L&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWWinGravity</code> </td>
<td> (1L&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBackingStore</code> </td>
<td> (1L&lt;&lt;6)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBackingPlanes</code> </td>
<td> (1L&lt;&lt;7)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWBackingPixel</code> </td>
<td> (1L&lt;&lt;8)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWOverrideRedirect</code> </td>
<td> (1L&lt;&lt;9)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWSaveUnder</code> </td>
<td> (1L&lt;&lt;10)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWEventMask</code> </td>
<td> (1L&lt;&lt;11)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWDontPropagate</code> </td>
<td> (1L&lt;&lt;12)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWColormap</code> </td>
<td> (1L&lt;&lt;13)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>CWCursor</code> </td>
<td> (1L&lt;&lt;14)
</td>
</tr>
</table>
<p> /* Values */ </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pixmap background_pixmap;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;background, None, or ParentRelative&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long background_pixel;&nbsp;/*&nbsp;background pixel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pixmap border_pixmap;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;border of the window or CopyFromParent&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long border_pixel;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;border pixel value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bit_gravity;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;one of bit gravity values&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int win_gravity;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;one of the window gravity values&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int backing_store;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;NotUseful, WhenMapped, Always&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long backing_planes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;planes to be preserved if possible&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long backing_pixel;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;value to use in restoring planes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool save_under;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;should bits under be saved?&nbsp;(popups)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long event_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;set of events that should be saved&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long do_not_propagate_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;set of events that should not propagate&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool override_redirect;&nbsp;/*&nbsp;boolean value for override_redirect&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Colormap colormap;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;color map to be associated with window&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Cursor cursor;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;cursor to be displayed&nbsp;(or None)&nbsp;*/ } XSetWindowAttributes; </p>
<p> For a detailed explanation of the members of this structure, see <i>Xlib &#8211; C Language X Interface</i>.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadCursor</code></p>
<dd>A value for a Cursor argument does not name a defined Cursor.</p>
<dt><code>BadMatch</code></p>
<dd>The values do not exist for an <code>InputOnly</code> window.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadPixmap</code></p>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xconfigurewindow/">XConfigureWindow</a>(3), <a href="/docs/linux/man/3-xdefinecursor/">XDefineCursor</a>(3), <a href="/docs/linux/man/3-xdestroywindow/">XDestroyWindow</a>(3), <a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a>(3), <a href="/docs/linux/man/3-xraisewindow/">XRaiseWindow</a>(3), <a href="/docs/linux/man/3-xunmapwindow/">XUnmapWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
