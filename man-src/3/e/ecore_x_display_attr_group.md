---
title: "ecore_x_display_attr_group(3)"
name: "ecore_x_display_attr_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_display_attr_group/"
description: "X Display Attributes – Functions that set and retrieve X display attributes."
---

<p>X Display Attributes &#8211; Functions that set and retrieve X display attributes. </p>
<h3>Functions</h3>
<p>EAPI Ecore_X_Display * <code>ecore_x_display_get</code> (void)<br />
 <i>Retrieves the Ecore_X_Display handle used for the current X connection. </i><br />
 EAPI int <code>ecore_x_fd_get</code> (void)<br />
 <i>Retrieves the X display file descriptor. </i><br />
 EAPI void <code>ecore_x_double_click_time_set</code> (double t)<br />
 <i>Sets the timeout for a double and triple clicks to be flagged. </i><br />
 EAPI double <code>ecore_x_double_click_time_get</code> (void)<br />
 <i>Retrieves the double and triple click flag timeout. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set and retrieve X display attributes.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_X_Display* ecore_x_display_get (void)</h3>
<p>Retrieves the Ecore_X_Display handle used for the current X connection. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current X display.</dl>
<p> Referenced by ecore_evas_gl_x11_new(), ecore_evas_software_x11_16_new(), ecore_evas_software_x11_new(), and ecore_evas_xrender_x11_new().</p>
<h3>EAPI double ecore_x_double_click_time_get (void)</h3>
<p>Retrieves the double and triple click flag timeout. </p>
<p> See <code>ecore_x_double_click_time_set</code> for more information. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The timeout for double clicks in seconds.</dl>
<h3>EAPI void ecore_x_double_click_time_set (double t)</h3>
<p>Sets the timeout for a double and triple clicks to be flagged. </p>
<p> This sets the time between clicks before the double_click flag is set in a button down event. If 3 clicks occur within double this time, the triple_click flag is also set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>t</i> The time in seconds</dl>
<h3>EAPI int ecore_x_fd_get (void)</h3>
<p>Retrieves the X display file descriptor. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current X display file descriptor.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
