---
title: "ecore_x_window_save_set_group(3)"
name: "ecore_x_window_save_set_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_save_set_group/"
description: "X Window Change Save Set Functions – Functions that either inserts or deletes the specified window from the client’s save-set."
---

<p>X Window Change Save Set Functions &#8211; Functions that either inserts or deletes the specified window from the client&#8217;s save-set. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_save_set_add</code> (Ecore_X_Window window)<br />
 <i>Inserts the window in the client&#8217;s save-set. </i><br />
 EAPI void <code>ecore_x_window_save_set_del</code> (Ecore_X_Window window)<br />
 <i>Deletes the window from the client&#8217;s save-set. </i></p>
<h2>Detailed Description</h2>
<p>Functions that either inserts or deletes the specified window from the client&#8217;s save-set.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_save_set_add (Ecore_X_Window window)</h3>
<p>Inserts the window in the client&#8217;s save-set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to insert in the client&#8217;s save-set.</dl>
<h3>EAPI void ecore_x_window_save_set_del (Ecore_X_Window window)</h3>
<p>Deletes the window from the client&#8217;s save-set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to delete from the client&#8217;s save-set.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
