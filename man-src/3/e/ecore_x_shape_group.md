---
title: "ecore_x_shape_group(3)"
name: "ecore_x_shape_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_shape_group/"
description: "X Shape extension – Functions that use the shape extension of the X server to change shape of given windows."
---

<p>X Shape extension &#8211; Functions that use the shape extension of the X server to change shape of given windows. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_shape_mask_set</code> (Ecore_X_Window dest_win, Ecore_X_Pixmap source_mask)<br />
 <i>Sets the shape of the given window to the given pixmap. </i><br />
 EAPI void <code>ecore_x_window_shape_rectangle_set</code> (Ecore_X_Window dest_win, int x, int y, int width, int height)<br />
 <i>Sets the shape of the given window to a rectangle. </i><br />
 EAPI void <code>ecore_x_window_shape_rectangles_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the ShapeGetRectangles request. </i><br />
 EAPI void <code>ecore_x_window_shape_rectangles_get_fetch</code> (void)<br />
 <i>Gets the reply of the ShapeGetRectangles request sent by </i><code>ecore_x_window_shape_rectangles_get_prefetch()</code>.<br />
 EAPI Ecore_X_Rectangle * <code>ecore_x_window_shape_rectangles_get</code> (Ecore_X_Window window __UNUSED__, int *num_ret)<br />
 <i>To document. </i></p>
<h2>Detailed Description</h2>
<p>Functions that use the shape extension of the X server to change shape of given windows.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_shape_mask_set (Ecore_X_Window dest_win, Ecore_X_Pixmap source_mask)</h3>
<p>Sets the shape of the given window to the given pixmap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest_win</i> The given window.<br />
 <i>source_mask</i> A 2-bit depth pixmap that provides the new shape of the window.</dl>
<p> Sets the shape of the window dest_win to the pixmap source_mask.</p>
<h3>EAPI void ecore_x_window_shape_rectangle_set (Ecore_X_Window dest_win, int x, int y, int width, int height)</h3>
<p>Sets the shape of the given window to a rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest_win</i> The given window.<br />
 <i>x</i> The X coordinate of the top left corner of the rectangle.<br />
 <i>y</i> The Y coordinate of the top left corner of the rectangle.<br />
 <i>width</i> The width of the rectangle.<br />
 <i>height</i> The height of the rectangle.</dl>
<p> Sets the shape of the window dest_win to a rectangle defined by x, y, width and height.</p>
<h3>EAPI Ecore_X_Rectangle* ecore_x_window_shape_rectangles_get (Ecore_X_Window window __UNUSED__, int * num_ret)</h3>
<p>To document. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.<br />
 <i>num_ret</i> To document.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>To document.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_window_shape_rectangles_get_prefetch()</code>, which sends the ShapeGetRectangles request, then <code>ecore_x_window_shape_rectangles_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_window_shape_rectangles_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the ShapeGetRectangles request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Requested window.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
