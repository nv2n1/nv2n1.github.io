---
title: "xwarppointer(3)"
name: "xwarppointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwarppointer/"
description: "XWarpPointer – move pointer"
---

<p>XWarpPointer &#8211; move pointer </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XWarpPointer(Display *<i>display</i>, Window <i>src_w</i>, Window <i>dest_w</i>, int <i>src_x</i>, int <i>src_y</i>, unsigned int <i>src_width</i>, unsigned int <i>src_height</i>, int <i>dest_x</i>, int <i>dest_y</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dest_w</i></p>
<dd>Specifies the destination window or <code>None</code>.</p>
<dt><i>dest_x</i></p>
<dd>
<dt><i>dest_y</i></p>
<dd>Specify the x and y coordinates within the destination window.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>src_x</i></p>
<dd>
<dt><i>src_y</i></p>
<dd>
<dt><i>src_width</i></p>
<dd>
<dt><i>src_height</i></p>
<dd>Specify a rectangle in the source window.</p>
<dt><i>src_w</i></p>
<dd>Specifies the source window or <code>None</code>.</dl>
<h2>Description</h2>
<p>If dest_w is <code>None</code>, <code>XWarpPointer</code> moves the pointer by the offsets (dest_x, dest_y) relative to the current position of the pointer. If dest_w is a window, <code>XWarpPointer</code> moves the pointer to the offsets (dest_x, dest_y) relative to the origin of dest_w. However, if src_w is a window, the move only takes place if the window src_w contains the pointer and if the specified rectangle of src_w contains the pointer. </p>
<p> The src_x and src_y coordinates are relative to the origin of src_w. If src_height is zero, it is replaced with the current height of src_w minus src_y. If src_width is zero, it is replaced with the current width of src_w minus src_x. </p>
<p> There is seldom any reason for calling this function. The pointer should normally be left to the user. If you do use this function, however, it generates events just as if the user had instantaneously moved the pointer from one position to another. Note that you cannot use <code>XWarpPointer</code> to move the pointer outside the confine_to window of an active pointer grab. An attempt to do so will only move the pointer as far as the closest edge of the confine_to window. </p>
<p> <code>XWarpPointer</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xsetinputfocus/">XSetInputFocus</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
