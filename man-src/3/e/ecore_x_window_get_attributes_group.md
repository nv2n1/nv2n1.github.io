---
title: "ecore_x_window_get_attributes_group(3)"
name: "ecore_x_window_get_attributes_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_get_attributes_group/"
description: "X Window Get Attributes Functions – Functions that get the attributes of a window."
---

<p>X Window Get Attributes Functions &#8211; Functions that get the attributes of a window. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_get_window_attributes_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetWindowAttributes request. </i><br />
 EAPI void <code>ecore_x_get_window_attributes_fetch</code> (void)<br />
 <i>Gets the reply of the GetWindowAttributes request sent by </i><code>ecore_x_get_window_attributes_prefetch()</code>.<br />
 EAPI int <code>ecore_x_window_attributes_get</code> (Ecore_X_Window window __UNUSED__, Ecore_X_Window_Attributes *att_ret)<br />
 <i>Retrieves the attributes of a window. </i><br />
 EAPI int <code>ecore_x_window_visible_get</code> (Ecore_X_Window window __UNUSED__)<br />
 <i>Finds out whether the given window is currently visible. </i></p>
<h2>Detailed Description</h2>
<p>Functions that get the attributes of a window.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_window_attributes_get (Ecore_X_Window window __UNUSED__, Ecore_X_Window_Attributes * att_ret)</h3>
<p>Retrieves the attributes of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>windows</i> Unused.<br />
 <i>att_ret</i> Pointer to an Ecore_X_Window_Attributes structure in which the attributes of a window are to be stored.</dl>
<p> Retrieves the attributes of a window. If att_ret is NULL, the function does nothing. If an error occurred, att_ret is set to 0. Otherwise, the att_ret structure is filled with the attributes os the requested window. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_window_attributes_prefetch()</code>, which sends the GetWindowAttributes request, then <code>ecore_x_get_window_attributes_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_window_visible_get (Ecore_X_Window window __UNUSED__)</h3>
<p>Finds out whether the given window is currently visible. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the window is visible, otherwise 0.</dl>
<p> Finds out whether the given window is currently visible. If an error occurred, or if the window is not visible, 0 is returned. Otherwise 1 is returned. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_window_attributes_prefetch()</code>, which sends the GetWindowAttributes request, then <code>ecore_x_get_window_attributes_fetch()</code>, which gets the reply.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
