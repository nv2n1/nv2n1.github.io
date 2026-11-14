---
title: "xtranslatecoordinates(3)"
name: "xtranslatecoordinates"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtranslatecoordinates/"
description: "XTranslateCoordinates – translate window coordinates"
---

<p>XTranslateCoordinates &#8211; translate window coordinates </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Bool XTranslateCoordinates(Display *<i>display</i>, Window <i>src_w</i>, <i>dest_w</i>, int <i>src_x</i>, int <i>src_y</i>, int *<i>dest_x_return</i>, int *<i>dest_y_return</i>, Window *<i>child_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>child_return</i></p>
<dd>Returns the child if the coordinates are contained in a mapped child of the destination window.</p>
<dt><i>dest_w</i></p>
<dd>Specifies the destination window.</p>
<dt><i>dest_x_return</i></p>
<dd>
<dt><i>dest_y_return</i></p>
<dd>Return the x and y coordinates within the destination window.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>src_w</i></p>
<dd>Specifies the source window.</p>
<dt><i>src_x</i></p>
<dd>
<dt><i>src_y</i></p>
<dd>Specify the x and y coordinates within the source window.</dl>
<h2>Description</h2>
<p>If <code>XTranslateCoordinates</code> returns <code>True</code>, it takes the src_x and src_y coordinates relative to the source window&#8217;s origin and returns these coordinates to dest_x_return and dest_y_return relative to the destination window&#8217;s origin. If <code>XTranslateCoordinates</code> returns <code>False</code>, src_w and dest_w are on different screens, and dest_x_return and dest_y_return are zero. If the coordinates are contained in a mapped child of dest_w, that child is returned to child_return. Otherwise, child_return is set to <code>None</code>. </p>
<p> <code>XTranslateCoordinates</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
