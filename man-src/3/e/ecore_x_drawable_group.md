---
title: "ecore_x_drawable_group(3)"
name: "ecore_x_drawable_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_drawable_group/"
description: "X Drawable Functions – Functions that operate on drawables."
---

<p>X Drawable Functions &#8211; Functions that operate on drawables. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_drawable_geometry_get_prefetch</code> (Ecore_X_Drawable drawable)<br />
 <i>Sends the GetGeometry request. </i><br />
 EAPI void <code>ecore_x_drawable_geometry_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetGeometry request sent by </i><code>ecore_x_atom_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_drawable_geometry_get</code> (Ecore_X_Drawable drawable __UNUSED__, int *x, int *y, int *width, int *height)<br />
 <i>Retrieves the geometry of the given drawable. </i><br />
 EAPI int <code>ecore_x_drawable_border_width_get</code> (Ecore_X_Drawable drawable __UNUSED__)<br />
 <i>Retrieves the width of the border of the given drawable. </i><br />
 EAPI int <code>ecore_x_drawable_depth_get</code> (Ecore_X_Drawable drawable __UNUSED__)<br />
 <i>Retrieves the depth of the given drawable. </i><br />
 EAPI void <code>ecore_x_drawable_geometry_get</code> (Ecore_X_Drawable d, int *x, int *y, int *w, int *h)<br />
 <i>Retrieves the geometry of the given drawable. </i><br />
 EAPI int <code>ecore_x_drawable_border_width_get</code> (Ecore_X_Drawable d)<br />
 <i>Retrieves the width of the border of the given drawable. </i><br />
 EAPI int <code>ecore_x_drawable_depth_get</code> (Ecore_X_Drawable d)<br />
 <i>Retrieves the depth of the given drawable. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on drawables.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_drawable_border_width_get (Ecore_X_Drawable d)</h3>
<p>Retrieves the width of the border of the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>d</i> The given drawable.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The border width of the given drawable.</dl>
<p> Referenced by ecore_x_window_border_width_get().</p>
<h3>EAPI int ecore_x_drawable_border_width_get (Ecore_X_Drawable drawable __UNUSED__)</h3>
<p>Retrieves the width of the border of the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>drawable</i> Unused.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The border width of the given drawable.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_drawable_geometry_get_prefetch()</code>, which sends the GetGeometry request, then <code>ecore_x_drawable_geometry_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_drawable_depth_get (Ecore_X_Drawable d)</h3>
<p>Retrieves the depth of the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>d</i> The given drawable.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The depth of the given drawable.</dl>
<p> Referenced by ecore_x_pixmap_depth_get(), and ecore_x_window_depth_get().</p>
<h3>EAPI int ecore_x_drawable_depth_get (Ecore_X_Drawable drawable __UNUSED__)</h3>
<p>Retrieves the depth of the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>drawable</i> Unused.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The depth of the given drawable.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_drawable_geometry_get_prefetch()</code>, which sends the GetGeometry request, then <code>ecore_x_drawable_geometry_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_drawable_geometry_get (Ecore_X_Drawable d, int * x, int * y, int * w, int * h)</h3>
<p>Retrieves the geometry of the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>d</i> The given drawable.<br />
 <i>x</i> Pointer to an integer into which the X position is to be stored.<br />
 <i>y</i> Pointer to an integer into which the Y position is to be stored.<br />
 <i>w</i> Pointer to an integer into which the width is to be stored.<br />
 <i>h</i> Pointer to an integer into which the height is to be stored.</dl>
<p> Referenced by ecore_x_pixmap_geometry_get(), ecore_x_window_geometry_get(), and ecore_x_window_size_get().</p>
<h3>EAPI void ecore_x_drawable_geometry_get (Ecore_X_Drawable drawable __UNUSED__, int * x, int * y, int * width, int * height)</h3>
<p>Retrieves the geometry of the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>drawable</i> Unused.<br />
 <i>x</i> Pointer to an integer into which the X position is to be stored.<br />
 <i>y</i> Pointer to an integer into which the Y position is to be stored.<br />
 <i>width</i> Pointer to an integer into which the width is to be stored.<br />
 <i>height</i> Pointer to an integer into which the height is to be stored.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_drawable_geometry_get_prefetch()</code>, which sends the GetGeometry request, then <code>ecore_x_drawable_geometry_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_drawable_geometry_get_prefetch (Ecore_X_Drawable drawable)</h3>
<p>Sends the GetGeometry request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>drawable</i> Drawable whose characteristics are sought.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
