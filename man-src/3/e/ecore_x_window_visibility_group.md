---
title: "ecore_x_window_visibility_group(3)"
name: "ecore_x_window_visibility_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_visibility_group/"
description: "X Window Visibility Functions – Functions to change the visibility of X windows."
---

<p>X Window Visibility Functions &#8211; Functions to change the visibility of X windows. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_show</code> (Ecore_X_Window window)<br />
 <i>Shows a window. </i><br />
 EAPI void <code>ecore_x_window_hide</code> (Ecore_X_Window window)<br />
 <i>Hides a window. </i><br />
 EAPI int <code>ecore_x_window_visible_get</code> (Ecore_X_Window win)<br />
 <i>Finds out whether the given window is currently visible. </i></p>
<h2>Detailed Description</h2>
<p>Functions to change the visibility of X windows.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_hide (Ecore_X_Window window)</h3>
<p>Hides a window. </p>
<p> Synonymous to &#8216;unmapping&#8217; a window in X Window System terminology. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to hide.</dl>
<h3>EAPI void ecore_x_window_show (Ecore_X_Window window)</h3>
<p>Shows a window. </p>
<p> Synonymous to &#8216;mapping&#8217; a window in X Window System terminology. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to show.</dl>
<h3>EAPI int ecore_x_window_visible_get (Ecore_X_Window win)</h3>
<p>Finds out whether the given window is currently visible. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the window is visible, otherwise 0.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
