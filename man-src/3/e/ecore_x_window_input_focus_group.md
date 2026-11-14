---
title: "ecore_x_window_input_focus_group(3)"
name: "ecore_x_window_input_focus_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_input_focus_group/"
description: "X Window Input Focus Functions – Functions that manage the focus of an X Window."
---

<p>X Window Input Focus Functions &#8211; Functions that manage the focus of an X Window. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_focus</code> (Ecore_X_Window window)<br />
 <i>Sets the focus to the window </i>window.<br />
 EAPI void <code>ecore_x_window_focus_at_time</code> (Ecore_X_Window window, Ecore_X_Time time)<br />
 <i>Sets the focus to the given window at a specific time. </i><br />
 EAPI void <code>ecore_x_get_input_focus_prefetch</code> (void)<br />
 <i>Sends the GetInputFocus request. </i><br />
 EAPI void <code>ecore_x_get_input_focus_fetch</code> (void)<br />
 <i>Gets the reply of the GetInputFocus request sent by </i><code>ecore_x_get_input_focus_prefetch()</code>.<br />
 EAPI Ecore_X_Window <code>ecore_x_window_focus_get</code> (void)<br />
 <i>Gets the window that has focus. </i></p>
<h2>Detailed Description</h2>
<p>Functions that manage the focus of an X Window.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_focus (Ecore_X_Window window)</h3>
<p>Sets the focus to the window window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to focus.</dl>
<h3>EAPI void ecore_x_window_focus_at_time (Ecore_X_Window window, Ecore_X_Time time)</h3>
<p>Sets the focus to the given window at a specific time. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to focus.<br />
 <i>time</i> When to set the focus to the window.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_focus_get (void)</h3>
<p>Gets the window that has focus. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window that has focus.</dl>
<p> Returns the window that has the focus. If an error aoocured, 0 is returned, otherwise the function returns the window that has focus. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_get_input_focus_prefetch()</code>, which sends the GetInputFocus request, then <code>ecore_x_get_input_focus_fetch()</code>, which gets the reply.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
