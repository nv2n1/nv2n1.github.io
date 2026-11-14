---
title: "xquerypointer(3)"
name: "xquerypointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xquerypointer/"
description: "XQueryPointer – get pointer coordinates"
---

<p>XQueryPointer &#8211; get pointer coordinates </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Bool XQueryPointer(Display *<i>display</i>, Window <i>w</i>, Window *<i>root_return</i>, Window *<i>child_return</i>, int *<i>root_x_return</i>, int *<i>root_y_return</i>, int *<i>win_x_return</i>, int *<i>win_y_return</i>, unsigned int *<i>mask_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>child_return</i></p>
<dd>Returns the child window that the pointer is located in, if any.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>mask_return</i></p>
<dd>Returns the current state of the modifier keys and pointer buttons.</p>
<dt><i>root_return</i></p>
<dd>Returns the root window that the pointer is in.</p>
<dt><i>root_x_return</i></p>
<dd>
<dt><i>root_y_return</i></p>
<dd>Return the pointer coordinates relative to the root window&#8217;s origin.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>win_x_return</i></p>
<dd>
<dt><i>win_y_return</i></p>
<dd>Return the pointer coordinates relative to the specified window.</dl>
<h2>Description</h2>
<p>The <code>XQueryPointer</code> function returns the root window the pointer is logically on and the pointer coordinates relative to the root window&#8217;s origin. If <code>XQueryPointer</code> returns <code>False</code>, the pointer is not on the same screen as the specified window, and <code>XQueryPointer</code> returns <code>None</code> to child_return and zero to win_x_return and win_y_return. If <code>XQueryPointer</code> returns <code>True</code>, the pointer coordinates returned to win_x_return and win_y_return are relative to the origin of the specified window. In this case, <code>XQueryPointer</code> returns the child that contains the pointer, if any, or else <code>None</code> to child_return. </p>
<p> <code>XQueryPointer</code> returns the current logical state of the keyboard buttons and the modifier keys in mask_return. It sets mask_return to the bitwise inclusive OR of one or more of the button or modifier key bitmasks to match the current state of the mouse buttons and the modifier keys. </p>
<p> <code>XQueryPointer</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xgetwindowattributes/">XGetWindowAttributes</a>(3), <a href="/docs/linux/man/3-xquerytree/">XQueryTree</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
