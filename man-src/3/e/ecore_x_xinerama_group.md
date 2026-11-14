---
title: "ecore_x_xinerama_group(3)"
name: "ecore_x_xinerama_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_xinerama_group/"
description: "X Xinerama Extension Functions – Functions related to the X Xinerama extension."
---

<p>X Xinerama Extension Functions &#8211; Functions related to the X Xinerama extension. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_xinerama_query</code> (void)<br />
 <i>Return whether the X server supports the Xinerama Extension. </i><br />
 EAPI void <code>ecore_x_xinerama_query_screens_prefetch</code> (void)<br />
 <i>Sends the XineramaQueryScreens request. </i><br />
 EAPI void <code>ecore_x_xinerama_query_screens_fetch</code> (void)<br />
 <i>Gets the reply of the XineramaQueryScreens request sent by </i><code>ecore_x_xinerama_query_screens_prefetch()</code>.<br />
 EAPI int <code>ecore_x_xinerama_screen_count_get</code> (void)<br />
 <i>Return the number of screens. </i><br />
 EAPI int <code>ecore_x_xinerama_screen_geometry_get</code> (int screen, int *x, int *y, int *width, int *height)<br />
 <i>Get the geometry of the screen. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to the X Xinerama extension.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_xinerama_query (void)</h3>
<p>Return whether the X server supports the Xinerama Extension. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X Xinerama Extension is available, 0 otherwise.</dl>
<p> Return 1 if the X server supports the Fixes Xinerama version 1.1, 0 otherwise.</p>
<h3>EAPI int ecore_x_xinerama_screen_count_get (void)</h3>
<p>Return the number of screens. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The screen count.</dl>
<p> Return the number of screens. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_xinerama_query_screens_prefetch()</code>, which sends the XineramaQueryScreens request, then <code>ecore_x_xinerama_query_screens_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_xinerama_screen_geometry_get (int screen, int * x, int * y, int * width, int * height)</h3>
<p>Get the geometry of the screen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>screen</i> The screen (Unused).<br />
 <i>x</i> The X coordinate of the screen.<br />
 <i>y</i> The Y coordinate of the screen<br />
 <i>width</i> The width of the screen<br />
 <i>height</i> The height of the screen</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Get the geometry of the screen whose number is screen. The returned values are stored in x, y, width and height. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_xinerama_query_screens_prefetch()</code>, which sends the XineramaQueryScreens request, then <code>ecore_x_xinerama_query_screens_fetch()</code>, which gets the reply.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
