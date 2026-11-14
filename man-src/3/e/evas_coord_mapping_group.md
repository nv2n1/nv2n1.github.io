---
title: "evas_coord_mapping_group(3)"
name: "evas_coord_mapping_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_coord_mapping_group/"
description: "Evas Coordinate Mapping Functions – Functions that are used to map coordinates from the canvas to the screen or the screen to the canvas."
---

<p>Evas Coordinate Mapping Functions &#8211; Functions that are used to map coordinates from the canvas to the screen or the screen to the canvas. </p>
<h3>Functions</h3>
<p>EAPI Evas_Coord <code>evas_coord_screen_x_to_world</code> (const <code>Evas</code> *e, int x)<br />
 <i>Convert/scale an ouput screen co-ordinate into canvas co-ordinates. </i><br />
 EAPI Evas_Coord <code>evas_coord_screen_y_to_world</code> (const <code>Evas</code> *e, int y)<br />
 <i>Convert/scale an ouput screen co-ordinate into canvas co-ordinates. </i><br />
 EAPI int <code>evas_coord_world_x_to_screen</code> (const <code>Evas</code> *e, Evas_Coord x)<br />
 <i>Convert/scale a canvas co-ordinate into output screen co-ordinates. </i><br />
 EAPI int <code>evas_coord_world_y_to_screen</code> (const <code>Evas</code> *e, Evas_Coord y)<br />
 <i>Convert/scale a canvas co-ordinate into output screen co-ordinates. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to map coordinates from the canvas to the screen or the screen to the canvas.</p>
<h2>Function Documentation</h2>
<h3>EAPI Evas_Coord evas_coord_screen_x_to_world (const <code>Evas</code> * e, int x)</h3>
<p>Convert/scale an ouput screen co-ordinate into canvas co-ordinates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>x</i> The screen/output x co-ordinate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The screen co-ordinate translated to canvas unit co-ordinates</dl>
<p> This function takes in a horizontal co-ordinate as the x parameter and converts it into canvas units, accounting for output size, viewport size and location, returning it as the function return value. If e is invalid, the results are undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 extern int screen_x;
 Evas_Coord canvas_x;
 canvas_x = evas_coord_screen_x_to_world(evas, screen_x);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI Evas_Coord evas_coord_screen_y_to_world (const <code>Evas</code> * e, int y)</h3>
<p>Convert/scale an ouput screen co-ordinate into canvas co-ordinates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>y</i> The screen/output y co-ordinate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The screen co-ordinate translated to canvas unit co-ordinates</dl>
<p> This function takes in a vertical co-ordinate as the y parameter and converts it into canvas units, accounting for output size, viewport size and location, returning it as the function return value. If e is invalid, the results are undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 extern int screen_y;
 Evas_Coord canvas_y;
 canvas_y = evas_coord_screen_y_to_world(evas, screen_y);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI int evas_coord_world_x_to_screen (const <code>Evas</code> * e, Evas_Coord x)</h3>
<p>Convert/scale a canvas co-ordinate into output screen co-ordinates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>x</i> The canvas x co-ordinate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The output/screen co-ordinate translated to output co-ordinates</dl>
<p> This function takes in a horizontal co-ordinate as the x parameter and converts it into output units, accounting for output size, viewport size and location, returning it as the function return value. If e is invalid, the results are undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 int screen_x;
 extern Evas_Coord canvas_x;
 screen_x = evas_coord_world_x_to_screen(evas, canvas_x);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI int evas_coord_world_y_to_screen (const <code>Evas</code> * e, Evas_Coord y)</h3>
<p>Convert/scale a canvas co-ordinate into output screen co-ordinates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>y</i> The canvas y co-ordinate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The output/screen co-ordinate translated to output co-ordinates</dl>
<p> This function takes in a vertical co-ordinate as the x parameter and converts it into output units, accounting for output size, viewport size and location, returning it as the function return value. If e is invalid, the results are undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 int screen_y;
 extern Evas_Coord canvas_y;
 screen_y = evas_coord_world_y_to_screen(evas, canvas_y);</pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
