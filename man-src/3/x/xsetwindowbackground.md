---
title: "xsetwindowbackground(3)"
name: "xsetwindowbackground"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetwindowbackground/"
description: "XChangeWindowAttributes, XSetWindowBackground, XSetWindowBackgroundPixmap, XSetWindowBorder, XSetWindowBorderPixmap, XSetWindowColormap – change window attributes"
---

<p>XChangeWindowAttributes, XSetWindowBackground, XSetWindowBackgroundPixmap, XSetWindowBorder, XSetWindowBorderPixmap, XSetWindowColormap &#8211; change window attributes </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XChangeWindowAttributes(Display *<i>display</i>, Window <i>w</i>, unsigned long <i>valuemask</i>, XSetWindowAttributes *<i>attributes</i>);</p>
<dd>int XSetWindowBackground(Display *<i>display</i>, Window <i>w</i>, unsigned long <i>background_pixel</i>);</p>
<dd>int XSetWindowBackgroundPixmap(Display *<i>display</i>, Window <i>w</i>, Pixmap <i>background_pixmap</i>);</p>
<dd>int XSetWindowBorder(Display *<i>display</i>, Window <i>w</i>, unsigned long <i>border_pixel</i>);</p>
<dd>int XSetWindowBorderPixmap(Display *<i>display</i>, Window <i>w</i>, Pixmap <i>border_pixmap</i>);</p>
<dd>int XSetWindowColormap(Display *<i>display</i>, Window <i>w</i>, Colormap <i>colormap</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>attributes</i></p>
<dd>Specifies the structure from which the values (as specified by the value mask) are to be taken. The value mask should have the appropriate bits set to indicate which attributes have been set in the structure.</p>
<dt><i>background_pixel</i></p>
<dd>Specifies the pixel that is to be used for the background.</p>
<dt><i>background_pixmap</i></p>
<dd>Specifies the background pixmap, <code>ParentRelative</code>, or <code>None</code>.</p>
<dt><i>border_pixel</i></p>
<dd>Specifies the entry in the colormap.</p>
<dt><i>border_pixmap</i></p>
<dd>Specifies the border pixmap or <code>CopyFromParent</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>valuemask</i></p>
<dd>Specifies which window attributes are defined in the attributes argument. This mask is the bitwise inclusive OR of the valid attribute mask bits. If valuemask is zero, the attributes are ignored and are not referenced.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>colormap</i></p>
<dd>Specifies the colormap.</dl>
<h2>Description</h2>
<p>Depending on the valuemask, the <code>XChangeWindowAttributes</code> function uses the window attributes in the <code>XSetWindowAttributes</code> structure to change the specified window attributes. Changing the background does not cause the window contents to be changed. To repaint the window and its background, use <code>XClearWindow</code>. Setting the border or changing the background such that the border tile origin changes causes the border to be repainted. Changing the background of a root window to <code>None</code> or <code>ParentRelative</code> restores the default background pixmap. Changing the border of a root window to <code>CopyFromParent</code> restores the default border pixmap. Changing the win-gravity does not affect the current position of the window. Changing the backing-store of an obscured window to <code>WhenMapped</code> or <code>Always</code>, or changing the backing-planes, backing-pixel, or save-under of a mapped window may have no immediate effect. Changing the colormap of a window (that is, defining a new map, not changing the contents of the existing map) generates a <code>ColormapNotify</code> event. Changing the colormap of a visible window may have no immediate effect on the screen because the map may not be installed (see <code>XInstallColormap</code>). Changing the cursor of a root window to <code>None</code> restores the default cursor. Whenever possible, you are encouraged to share colormaps. </p>
<p> Multiple clients can select input on the same window. Their event masks are maintained separately. When an event is generated, it is reported to all interested clients. However, only one client at a time can select for <code>SubstructureRedirectMask</code>, <code>ResizeRedirectMask</code>, and <code>ButtonPressMask</code>. If a client attempts to select any of these event masks and some other client has already selected one, a <code>BadAccess</code> error results. There is only one do-not-propagate-mask for a window, not one per client. </p>
<p> <code>XChangeWindowAttributes</code> can generate <code>BadAccess</code>, <code>BadColor</code>, <code>BadCursor</code>, <code>BadMatch</code>, <code>BadPixmap</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XSetWindowBackground</code> function sets the background of the window to the specified pixel value. Changing the background does not cause the window contents to be changed. <code>XSetWindowBackground</code> uses a pixmap of undefined size filled with the pixel value you passed. If you try to change the background of an <code>InputOnly</code> window, a <code>BadMatch</code> error results. </p>
<p> <code>XSetWindowBackground</code> can generate <code>BadMatch</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XSetWindowBackgroundPixmap</code> function sets the background pixmap of the window to the specified pixmap. The background pixmap can immediately be freed if no further explicit references to it are to be made. If <code>ParentRelative</code> is specified, the background pixmap of the window&#8217;s parent is used, or on the root window, the default background is restored. If you try to change the background of an <code>InputOnly</code> window, a <code>BadMatch</code> error results. If the background is set to <code>None</code>, the window has no defined background. </p>
<p> <code>XSetWindowBackgroundPixmap</code> can generate <code>BadMatch</code>, <code>BadPixmap</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XSetWindowBorder</code> function sets the border of the window to the pixel value you specify. If you attempt to perform this on an <code>InputOnly</code> window, a <code>BadMatch</code> error results. </p>
<p> <code>XSetWindowBorder</code> can generate <code>BadMatch</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XSetWindowBorderPixmap</code> function sets the border pixmap of the window to the pixmap you specify. The border pixmap can be freed immediately if no further explicit references to it are to be made. If you specify <code>CopyFromParent</code>, a copy of the parent window&#8217;s border pixmap is used. If you attempt to perform this on an <code>InputOnly</code> window, a <code>BadMatch</code> error results. </p>
<p> <code>XSetWindowBorderPixmap</code> can generate <code>BadMatch</code>, <code>BadPixmap</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XSetWindowColormap</code> function sets the specified colormap of the specified window. The colormap must have the same visual type as the window, or a <code>BadMatch</code> error results. </p>
<p> <code>XSetWindowColormap</code> can generate <code>BadColor</code>, <code>BadMatch</code>, and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>A client attempted to free a color map entry that it did not already allocate.</p>
<dt><code>BadAccess</code></p>
<dd>A client attempted to store into a read-only color map entry.</p>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadCursor</code></p>
<dd>A value for a Cursor argument does not name a defined Cursor.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window locks this attribute.</p>
<dt><code>BadPixmap</code></p>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xconfigurewindow/">XConfigureWindow</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xdestroywindow/">XDestroyWindow</a>(3), <a href="/docs/linux/man/3-xinstallcolormap/">XInstallColormap</a>(3), <a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a>(3), <a href="/docs/linux/man/3-xraisewindow/">XRaiseWindow</a>(3), <a href="/docs/linux/man/3-xunmapwindow/">XUnmapWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
