---
title: "ecore_x_pixmap_group(3)"
name: "ecore_x_pixmap_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_pixmap_group/"
description: "X Pixmap Functions – Functions that operate on pixmaps."
---

<p>X Pixmap Functions &#8211; Functions that operate on pixmaps. </p>
<h3>Functions</h3>
<p>EAPI Ecore_X_Pixmap <code>ecore_x_pixmap_new</code> (Ecore_X_Window win, int w, int h, int dep)<br />
 <i>Creates a new pixmap. </i><br />
 EAPI void <code>ecore_x_pixmap_del</code> (Ecore_X_Pixmap pmap)<br />
 <i>Deletes the reference to the given pixmap. </i><br />
 EAPI void <code>ecore_x_pixmap_paste</code> (Ecore_X_Pixmap pmap, Ecore_X_Drawable dest, Ecore_X_GC gc, int sx, int sy, int w, int h, int dx, int dy)<br />
 <i>Pastes a rectangular area of the given pixmap onto the given drawable. </i><br />
 EAPI void <code>ecore_x_pixmap_geometry_get</code> (Ecore_X_Pixmap pmap, int *x, int *y, int *w, int *h)<br />
 <i>Retrieves the size of the given pixmap. </i><br />
 EAPI int <code>ecore_x_pixmap_depth_get</code> (Ecore_X_Pixmap pmap)<br />
 <i>Retrieves the depth of the given pixmap. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on pixmaps.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_pixmap_del (Ecore_X_Pixmap pmap)</h3>
<p>Deletes the reference to the given pixmap. </p>
<p> If no other clients have a reference to the given pixmap, the server will destroy it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pmap</i> The given pixmap.</dl>
<h3>EAPI int ecore_x_pixmap_depth_get (Ecore_X_Pixmap pmap)</h3>
<p>Retrieves the depth of the given pixmap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pmap</i> The given pixmap.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The depth of the pixmap.</dl>
<p> References ecore_x_drawable_depth_get().</p>
<h3>EAPI void ecore_x_pixmap_geometry_get (Ecore_X_Pixmap pmap, int * x, int * y, int * w, int * h)</h3>
<p>Retrieves the size of the given pixmap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pmap</i> The given pixmap.<br />
 <i>x</i> Pointer to an integer in which to store the X position.<br />
 <i>y</i> Pointer to an integer in which to store the Y position.<br />
 <i>w</i> Pointer to an integer in which to store the width.<br />
 <i>h</i> Pointer to an integer in which to store the height.</dl>
<p> References ecore_x_drawable_geometry_get().</p>
<h3>EAPI Ecore_X_Pixmap ecore_x_pixmap_new (Ecore_X_Window win, int w, int h, int dep)</h3>
<p>Creates a new pixmap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> Window used to determine which screen of the display the pixmap should be created on. If 0, the default root window is used.<br />
 <i>w</i> Width of the new pixmap.<br />
 <i>h</i> Height of the new pixmap.<br />
 <i>dep</i> Depth of the pixmap. If 0, the default depth of the default screen is used.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>New pixmap.</dl>
<h3>EAPI void ecore_x_pixmap_paste (Ecore_X_Pixmap pmap, Ecore_X_Drawable dest, Ecore_X_GC gc, int sx, int sy, int w, int h, int dx, int dy)</h3>
<p>Pastes a rectangular area of the given pixmap onto the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pmap</i> The given pixmap.<br />
 <i>dest</i> The given drawable.<br />
 <i>gc</i> The graphics context which governs which operation will be used to paste the area onto the drawable.<br />
 <i>sx</i> The X position of the area on the pixmap.<br />
 <i>sy</i> The Y position of the area on the pixmap.<br />
 <i>w</i> The width of the area.<br />
 <i>h</i> The height of the area.<br />
 <i>dx</i> The X position at which to paste the area on dest.<br />
 <i>dy</i> The Y position at which to paste the area on dest.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
