---
title: "ecore_x_window_geometry_group(3)"
name: "ecore_x_window_geometry_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_geometry_group/"
description: "X Window Geometry Functions – Functions that change or retrieve the geometry of X windows."
---

<p>X Window Geometry Functions &#8211; Functions that change or retrieve the geometry of X windows. </p>
<h3>Functions</h3>
<p>EAPI Ecore_X_Window <code>ecore_x_window_at_xy_get</code> (int x, int y)<br />
 <i>Retrieves the top, visible window at the given location. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_at_xy_with_skip_get</code> (int x, int y, Ecore_X_Window *skip, int skip_num)<br />
 <i>Retrieves the top, visible window at the given location, but skips the windows in the list. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_at_xy_begin_get</code> (Ecore_X_Window begin, int x, int y)<br />
 <i>Retrieves the top, visible window at the given location, but begins at the </i>begin window instead of the root one.<br />
 EAPI void <code>ecore_x_window_size_get</code> (Ecore_X_Window window, int *width, int *height)<br />
 <i>Retrieves the size of the given window. </i><br />
 EAPI void <code>ecore_x_window_geometry_get</code> (Ecore_X_Window window, int *x, int *y, int *width, int *height)<br />
 <i>Retrieves the geometry of the given window. </i><br />
 EAPI int <code>ecore_x_window_border_width_get</code> (Ecore_X_Window win)<br />
 <i>Retrieves the width of the border of the given window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_shadow_tree_at_xy_with_skip_get</code> (Ecore_X_Window base, int x, int y, Ecore_X_Window *skip, int skip_num)<br />
 <i>Retrieves the top, visible window at the given location, but skips the windows in the list. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_shadow_parent_get</code> (Ecore_X_Window root, Ecore_X_Window win)<br />
 <i>Retrieves the parent window a given window has. </i><br />
 EAPI void <code>ecore_x_window_shadow_tree_flush</code> (void)<br />
 <i>Flushes the window shadow tree so nothing is stored. </i><br />
 EAPI void <code>ecore_x_window_move</code> (Ecore_X_Window win, int x, int y)<br />
 <i>Moves a window to the position </i>x, y.<br />
 EAPI void <code>ecore_x_window_resize</code> (Ecore_X_Window win, int w, int h)<br />
 <i>Resizes a window. </i><br />
 EAPI void <code>ecore_x_window_move_resize</code> (Ecore_X_Window win, int x, int y, int w, int h)<br />
 <i>Moves and resizes a window. </i><br />
 EAPI void <code>ecore_x_window_border_width_set</code> (Ecore_X_Window win, int width)<br />
 <i>Sets the width of the border of the given window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_root_get</code> (Ecore_X_Window win)<br />
 <i>Retrieves the root window a given window is on. </i></p>
<h2>Detailed Description</h2>
<p>Functions that change or retrieve the geometry of X windows.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_X_Window ecore_x_window_at_xy_begin_get (Ecore_X_Window begin, int x, int y)</h3>
<p>Retrieves the top, visible window at the given location, but begins at the begin window instead of the root one. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>begin</i> The window from which we begin.<br />
 <i>x</i> The given X position.<br />
 <i>y</i> The given Y position.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window at that position.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_at_xy_get (int x, int y)</h3>
<p>Retrieves the top, visible window at the given location. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> The given X position.<br />
 <i>y</i> The given Y position.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window at that position.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_at_xy_with_skip_get (int x, int y, Ecore_X_Window * skip, int skip_num)</h3>
<p>Retrieves the top, visible window at the given location, but skips the windows in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> The given X position.<br />
 <i>y</i> The given Y position.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window at that position.</dl>
<h3>EAPI int ecore_x_window_border_width_get (Ecore_X_Window win)</h3>
<p>Retrieves the width of the border of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Width of the border of win.</dl>
<p> References ecore_x_drawable_border_width_get().</p>
<h3>EAPI void ecore_x_window_border_width_set (Ecore_X_Window win, int width)</h3>
<p>Sets the width of the border of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.<br />
 <i>width</i> The new border width.</dl>
<h3>EAPI void ecore_x_window_geometry_get (Ecore_X_Window win, int * x, int * y, int * w, int * h)</h3>
<p>Retrieves the geometry of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.<br />
 <i>x</i> Pointer to an integer in which the X position is to be stored.<br />
 <i>y</i> Pointer to an integer in which the Y position is to be stored.<br />
 <i>w</i> Pointer to an integer in which the width is to be stored.<br />
 <i>h</i> Pointer to an integer in which the height is to be stored.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_drawable_geometry_get_prefetch()</code>, which sends the GetGeometry request, then <code>ecore_x_drawable_geometry_get_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.<br />
 <i>x</i> Pointer to an integer in which the X position is to be stored.<br />
 <i>y</i> Pointer to an integer in which the Y position is to be stored.<br />
 <i>w</i> Pointer to an integer in which the width is to be stored.<br />
 <i>h</i> Pointer to an integer in which the height is to be stored.</dl>
<p> References ecore_x_drawable_geometry_get().</p>
<h3>EAPI void ecore_x_window_move (Ecore_X_Window win, int x, int y)</h3>
<p>Moves a window to the position x, y. </p>
<p> The position is relative to the upper left hand corner of the parent window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to move.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.</dl>
<h3>EAPI void ecore_x_window_move_resize (Ecore_X_Window win, int x, int y, int w, int h)</h3>
<p>Moves and resizes a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to move and resize.<br />
 <i>x</i> New X position of the window.<br />
 <i>y</i> New Y position of the window.<br />
 <i>w</i> New width of the window.<br />
 <i>h</i> New height of the window.</dl>
<h3>EAPI void ecore_x_window_resize (Ecore_X_Window win, int w, int h)</h3>
<p>Resizes a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to resize.<br />
 <i>w</i> New width of the window.<br />
 <i>h</i> New height of the window.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_root_get (Ecore_X_Window win)</h3>
<p>Retrieves the root window a given window is on. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to get the root window of</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The root window of win</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_shadow_parent_get (Ecore_X_Window root, Ecore_X_Window win)</h3>
<p>Retrieves the parent window a given window has. </p>
<p> This uses the shadow window tree. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window of win &#8211; if 0, this will be automatically determined with extra processing overhead<br />
 <i>win</i> The window to get the parent window of</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The parent window of win</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_shadow_tree_at_xy_with_skip_get (Ecore_X_Window base, int x, int y, Ecore_X_Window * skip, int skip_num)</h3>
<p>Retrieves the top, visible window at the given location, but skips the windows in the list. </p>
<p> This uses a shadow tree built from the window tree that is only updated the first time <code>ecore_x_window_shadow_tree_at_xy_with_skip_get()</code> is called, or the next time it is called after a <code>ecore_x_window_shadow_tree_flush()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>base</i> The base window to start searching from (normally root).<br />
 <i>x</i> The given X position.<br />
 <i>y</i> The given Y position.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window at that position.</dl>
<h3>EAPI void ecore_x_window_size_get (Ecore_X_Window win, int * w, int * h)</h3>
<p>Retrieves the size of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.<br />
 <i>w</i> Pointer to an integer into which the width is to be stored.<br />
 <i>h</i> Pointer to an integer into which the height is to be stored.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_drawable_geometry_get_prefetch()</code>, which sends the GetGeometry request, then <code>ecore_x_drawable_geometry_get_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.<br />
 <i>w</i> Pointer to an integer into which the width is to be stored.<br />
 <i>h</i> Pointer to an integer into which the height is to be stored.</dl>
<p> References ecore_x_drawable_geometry_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
