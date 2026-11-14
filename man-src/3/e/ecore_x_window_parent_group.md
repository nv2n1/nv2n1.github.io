---
title: "ecore_x_window_parent_group(3)"
name: "ecore_x_window_parent_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_parent_group/"
description: "X Window Parent Functions – Functions that retrieve or changes the parent window of a window."
---

<p>X Window Parent Functions &#8211; Functions that retrieve or changes the parent window of a window. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_pointer_xy_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the QueryPointer request. </i><br />
 EAPI void <code>ecore_x_pointer_xy_get_fetch</code> (void)<br />
 <i>Gets the reply of the QueryPointer request sent by ecore_x_query_pointer_prefetch(). </i><br />
 EAPI void <code>ecore_x_pointer_xy_get</code> (Ecore_X_Window window __UNUSED__, int *x, int *y)<br />
 <i>Retrieves the coordinates of the pointer. </i><br />
 EAPI void <code>ecore_x_query_tree_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the QueryTree request. </i><br />
 EAPI void <code>ecore_x_query_tree_fetch</code> (void)<br />
 <i>Gets the reply of the QueryTree request sent by </i><code>ecore_x_query_tree_prefetch()</code>.<br />
 EAPI Ecore_X_Window <code>ecore_x_window_parent_get</code> (Ecore_X_Window window __UNUSED__)<br />
 <i>Retrieves the parent window of the given window. </i><br />
 EAPI Ecore_X_Window * <code>ecore_x_window_children_get</code> (Ecore_X_Window window __UNUSED__, int *num)<br />
 <i>Retrieves the children windows of the given window. </i><br />
 EAPI void <code>ecore_x_window_reparent</code> (Ecore_X_Window win, Ecore_X_Window new_parent, int x, int y)<br />
 <i>Moves a window to within another window at a given position. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_parent_get</code> (Ecore_X_Window win)<br />
 <i>Retrieves the parent window of the given window. </i></p>
<h2>Detailed Description</h2>
<p>Functions that retrieve or changes the parent window of a window.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_pointer_xy_get (Ecore_X_Window window __UNUSED__, int * x, int * y)</h3>
<p>Retrieves the coordinates of the pointer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.<br />
 <i>x</i> The X coordinate of the pointer.<br />
 <i>y</i> The Y coordinate of the pointer.</dl>
<p> Retrieves the coordinates of the pointer. If the window used in ecore_x_query_pointer_prefetch() is not on the same screen than the root window or if an error occured, x and y are set to 0. Otherwise, they are respectively set to the X and Y coordinates of the pointer. </p>
<p> To use this function, you must call before, and in order, ecore_x_query_pointer_prefetch(), which sends the QueryPointer request, then ecore_x_query_pointer_fetch(), which gets the reply.</p>
<h3>EAPI Ecore_X_Window* ecore_x_window_children_get (Ecore_X_Window window __UNUSED__, int * num)</h3>
<p>Retrieves the children windows of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.<br />
 <i>num</i> children windows count.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The children windows.</dl>
<p> Retrieves the children windows of the given window. If an error occured, 0 is returned. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_query_tree_prefetch()</code>, which sends the QueryTree request, then <code>ecore_x_query_tree_fetch()</code>, which gets the reply.</p>
<h3>EAPI Ecore_X_Window ecore_x_window_parent_get (Ecore_X_Window win)</h3>
<p>Retrieves the parent window of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The parent window of win.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_parent_get (Ecore_X_Window window __UNUSED__)</h3>
<p>Retrieves the parent window of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The parent window of window.</dl>
<p> Retrieves the parent window of the given window. If an error occured, 0 is returned. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_query_tree_prefetch()</code>, which sends the QueryTree request, then <code>ecore_x_query_tree_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_window_reparent (Ecore_X_Window win, Ecore_X_Window new_parent, int x, int y)</h3>
<p>Moves a window to within another window at a given position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to reparent.<br />
 <i>new_parent</i> The new parent window.<br />
 <i>x</i> X position within new parent window.<br />
 <i>y</i> Y position within new parent window.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
