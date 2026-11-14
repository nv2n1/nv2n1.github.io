---
title: "ecore_x_window_create_group(3)"
name: "ecore_x_window_create_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_create_group/"
description: "X Window Creation Functions – Functions that can be used to create an X window."
---

<p>X Window Creation Functions &#8211; Functions that can be used to create an X window. </p>
<h3>Functions</h3>
<p>EAPI Ecore_X_Window <code>ecore_x_window_new</code> (Ecore_X_Window parent, int x, int y, int width, int height)<br />
 <i>Creates a new window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_override_new</code> (Ecore_X_Window parent, int x, int y, int width, int height)<br />
 <i>Creates a window with the override redirect attribute set to </i>True.<br />
 EAPI Ecore_X_Window <code>ecore_x_window_input_new</code> (Ecore_X_Window parent, int x, int y, int width, int height)<br />
 <i>Creates a new input window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_manager_argb_new</code> (Ecore_X_Window parent, int x, int y, int width, int height)<br />
 <i>Creates a new window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_argb_new</code> (Ecore_X_Window parent, int x, int y, int width, int height)<br />
 <i>Creates a new window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_override_argb_new</code> (Ecore_X_Window parent, int x, int y, int width, int height)<br />
 <i>Creates a window with the override redirect attribute set to </i>True.</p>
<h2>Detailed Description</h2>
<p>Functions that can be used to create an X window.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_X_Window ecore_x_window_argb_new (Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>Creates a new window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>width</i> Width.<br />
 <i>height</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>w</i> Width.<br />
 <i>h</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<p> Referenced by ecore_evas_software_x11_16_new(), and ecore_evas_software_x11_new().</p>
<h3>EAPI Ecore_X_Window ecore_x_window_input_new (Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>Creates a new input window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>w</i> Width.<br />
 <i>h</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_manager_argb_new (Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>Creates a new window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>width</i> Width.<br />
 <i>height</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>w</i> Width.<br />
 <i>h</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_new (Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>Creates a new window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>w</i> Width.<br />
 <i>h</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<p> References ecore_x_window_defaults_set(). </p>
<p> Referenced by ecore_evas_software_x11_16_new(), ecore_evas_software_x11_new(), and ecore_evas_xrender_x11_new().</p>
<h3>EAPI Ecore_X_Window ecore_x_window_override_argb_new (Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>Creates a window with the override redirect attribute set to True. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>width</i> Width.<br />
 <i>height</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>w</i> Width.<br />
 <i>h</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_override_new (Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>Creates a window with the override redirect attribute set to True. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> The parent window to use. If parent is 0, the root window of the default display is used.<br />
 <i>x</i> X position.<br />
 <i>y</i> Y position.<br />
 <i>w</i> Width.<br />
 <i>h</i> Height.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new window handle.</dl>
<p> Referenced by ecore_x_init().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
