---
title: "ecore_x_window_configure_group(3)"
name: "ecore_x_window_configure_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_configure_group/"
description: "X Window Configure Functions – Functions to configure X windows."
---

<p>X Window Configure Functions &#8211; Functions to configure X windows. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_configure</code> (Ecore_X_Window window, Ecore_X_Window_Configure_Mask mask, int x, int y, int width, int height, int border_width, Ecore_X_Window sibling, int stack_mode)<br />
 <i>Configures the given window with the given mask. </i><br />
 EAPI void <code>ecore_x_window_move</code> (Ecore_X_Window window, int x, int y)<br />
 <i>Moves a window to the position </i>x, y.<br />
 EAPI void <code>ecore_x_window_resize</code> (Ecore_X_Window window, int width, int height)<br />
 <i>Resizes a window. </i><br />
 EAPI void <code>ecore_x_window_move_resize</code> (Ecore_X_Window window, int x, int y, int width, int height)<br />
 <i>Moves and resizes a window. </i><br />
 EAPI void <code>ecore_x_window_border_width_set</code> (Ecore_X_Window window, int border_width)<br />
 <i>Sets the width of the border of the given window. </i><br />
 EAPI void <code>ecore_x_window_raise</code> (Ecore_X_Window window)<br />
 <i>Raises the given window. </i><br />
 EAPI void <code>ecore_x_window_lower</code> (Ecore_X_Window window)<br />
 <i>Lowers the given window. </i></p>
<h2>Detailed Description</h2>
<p>Functions to configure X windows.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_border_width_set (Ecore_X_Window window, int border_width)</h3>
<p>Sets the width of the border of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>border_width</i> The new border width.</dl>
<h3>EAPI void ecore_x_window_configure (Ecore_X_Window window, Ecore_X_Window_Configure_Mask mask, int x, int y, int width, int height, int border_width, Ecore_X_Window sibling, int stack_mode)</h3>
<p>Configures the given window with the given mask. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>mask</i> The given mask.<br />
 <i>x</i> The X coordinate of the window.<br />
 <i>y</i> The Y coordinate of the window.<br />
 <i>width</i> The width of the window.<br />
 <i>height</i> The height of the window.<br />
 <i>border_width</i> The border width of the window.<br />
 <i>sibling</i> The sibling window of the window.<br />
 <i>stack_mode</i> The stack mode of the window.</dl>
<h3>EAPI void ecore_x_window_lower (Ecore_X_Window window)</h3>
<p>Lowers the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to lower.</dl>
<h3>EAPI void ecore_x_window_move (Ecore_X_Window window, int x, int y)</h3>
<p>Moves a window to the position x, y. </p>
<p> The position is relative to the upper left hand corner of the parent window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to move.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.</dl>
<h3>EAPI void ecore_x_window_move_resize (Ecore_X_Window window, int x, int y, int width, int height)</h3>
<p>Moves and resizes a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to move and resize.<br />
 <i>x</i> New X position of the window.<br />
 <i>y</i> New Y position of the window.<br />
 <i>width</i> New width of the window.<br />
 <i>height</i> New height of the window.</dl>
<h3>EAPI void ecore_x_window_raise (Ecore_X_Window window)</h3>
<p>Raises the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to raise.</dl>
<h3>EAPI void ecore_x_window_resize (Ecore_X_Window window, int width, int height)</h3>
<p>Resizes a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to resize.<br />
 <i>width</i> New width of the window.<br />
 <i>height</i> New height of the window.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
