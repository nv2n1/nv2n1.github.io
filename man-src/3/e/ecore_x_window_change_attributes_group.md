---
title: "ecore_x_window_change_attributes_group(3)"
name: "ecore_x_window_change_attributes_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_change_attributes_group/"
description: "X Window Change Attributes Functions – Functions that change the attributes of a window."
---

<p>X Window Change Attributes Functions &#8211; Functions that change the attributes of a window. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_pixmap_set</code> (Ecore_X_Window window, Ecore_X_Pixmap pixmap)<br />
 <i>Sets the background pixmap of the given window. </i><br />
 EAPI void <code>ecore_x_window_background_color_set</code> (Ecore_X_Window window, unsigned short red, unsigned short green, unsigned short blue)<br />
 <i>Sets the background color of the given window. </i><br />
 EAPI void <code>ecore_x_window_pixel_gravity_set</code> (Ecore_X_Window window, Ecore_X_Gravity gravity)<br />
 <i>Sets the bit gravity of the given window. </i><br />
 EAPI void <code>ecore_x_window_gravity_set</code> (Ecore_X_Window window, Ecore_X_Gravity gravity)<br />
 <i>Sets the gravity of the given window. </i><br />
 EAPI void <code>ecore_x_window_override_set</code> (Ecore_X_Window window, int override_redirect)<br />
 <i>Sets the override attribute of the given window. </i><br />
 EAPI void <code>ecore_x_window_cursor_show</code> (Ecore_X_Window window, int show)<br />
 <i>Shows the cursor of the given window. </i><br />
 EAPI void <code>ecore_x_window_cursor_set</code> (Ecore_X_Window window, Ecore_X_Cursor cursor)<br />
 <i>Sets the cursor of the given window. </i><br />
 EAPI void <code>ecore_x_window_container_manage</code> (Ecore_X_Window window)<br />
 <i>Todo. </i><br />
 EAPI void <code>ecore_x_window_client_manage</code> (Ecore_X_Window window)<br />
 <i>Todo. </i><br />
 EAPI void <code>ecore_x_window_sniff</code> (Ecore_X_Window window)<br />
 <i>Todo. </i><br />
 EAPI void <code>ecore_x_window_client_sniff</code> (Ecore_X_Window window)<br />
 <i>Todo. </i></p>
<h2>Detailed Description</h2>
<p>Functions that change the attributes of a window.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_background_color_set (Ecore_X_Window window, unsigned short red, unsigned short green, unsigned short blue)</h3>
<p>Sets the background color of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>red</i> The red component of the color to set to.<br />
 <i>green</i> The green component of the color to set to.<br />
 <i>blue</i> The blue component of the color to set to.</dl>
<h3>EAPI void ecore_x_window_client_manage (Ecore_X_Window window)</h3>
<p>Todo. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.</dl>
<h3>EAPI void ecore_x_window_client_sniff (Ecore_X_Window window)</h3>
<p>Todo. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.</dl>
<h3>EAPI void ecore_x_window_container_manage (Ecore_X_Window window)</h3>
<p>Todo. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.</dl>
<h3>EAPI void ecore_x_window_cursor_set (Ecore_X_Window window, Ecore_X_Cursor cursor)</h3>
<p>Sets the cursor of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>cursor</i> The given cursor.</dl>
<h3>EAPI void ecore_x_window_cursor_show (Ecore_X_Window window, int show)</h3>
<p>Shows the cursor of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>show</i> If set to 0, hide the cursor. Show it otherwise.</dl>
<h3>EAPI void ecore_x_window_gravity_set (Ecore_X_Window window, Ecore_X_Gravity gravity)</h3>
<p>Sets the gravity of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>gravity</i> The gravity.</dl>
<h3>EAPI void ecore_x_window_override_set (Ecore_X_Window window, int override_redirect)</h3>
<p>Sets the override attribute of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>override_redirect</i> The override_redirect boolean.</dl>
<h3>EAPI void ecore_x_window_pixel_gravity_set (Ecore_X_Window window, Ecore_X_Gravity gravity)</h3>
<p>Sets the bit gravity of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>gravity</i> The gravity.</dl>
<h3>EAPI void ecore_x_window_pixmap_set (Ecore_X_Window window, Ecore_X_Pixmap pixmap)</h3>
<p>Sets the background pixmap of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>pixmap</i> The pixmap to set to.</dl>
<h3>EAPI void ecore_x_window_sniff (Ecore_X_Window window)</h3>
<p>Todo. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
