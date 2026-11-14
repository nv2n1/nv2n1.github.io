---
title: "ecore_x_window_focus_functions(3)"
name: "ecore_x_window_focus_functions"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_focus_functions/"
description: "X Window Focus Functions – Functions that give the focus to an X Window."
---

<p>X Window Focus Functions &#8211; Functions that give the focus to an X Window. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_focus</code> (Ecore_X_Window win)<br />
 <i>Sets the focus to the window </i>win.<br />
 EAPI void <code>ecore_x_window_focus_at_time</code> (Ecore_X_Window win, Ecore_X_Time t)<br />
 <i>Sets the focus to the given window at a specific time. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_focus_get</code> (void)<br />
 <i>gets the focus to the window </i>win.</p>
<h2>Detailed Description</h2>
<p>Functions that give the focus to an X Window.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_focus (Ecore_X_Window win)</h3>
<p>Sets the focus to the window win. </p>
<p> Sets the focus to the window window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to focus.</dl>
<h3>EAPI void ecore_x_window_focus_at_time (Ecore_X_Window win, Ecore_X_Time t)</h3>
<p>Sets the focus to the given window at a specific time. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to focus.<br />
 <i>t</i> When to set the focus to the window.</dl>
<h3>EAPI Ecore_X_Window ecore_x_window_focus_get (void)</h3>
<p>gets the focus to the window win. </p>
<p> Gets the window that has focus. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window that has focus.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
