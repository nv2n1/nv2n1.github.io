---
title: "evas_pointer_group(3)"
name: "evas_pointer_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_pointer_group/"
description: "Evas Pointer Functions – Functions that deal with the status of the pointer."
---

<p>Evas Pointer Functions &#8211; Functions that deal with the status of the pointer. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_pointer_output_xy_get</code> (const <code>Evas</code> *e, int *x, int *y)<br />
 <i>This function returns the current known pointer co-ordinates. </i><br />
 EAPI void <code>evas_pointer_canvas_xy_get</code> (const <code>Evas</code> *e, Evas_Coord *x, Evas_Coord *y)<br />
 <i>This function returns the current known pointer co-ordinates. </i><br />
 EAPI int <code>evas_pointer_button_down_mask_get</code> (const <code>Evas</code> *e)<br />
 <i>Returns a bitmask with the mouse buttons currently pressed, set to 1. </i><br />
 EAPI Evas_Bool <code>evas_pointer_inside_get</code> (const <code>Evas</code> *e)<br />
 <i>Returns whether the mouse pointer is logically inside the canvas. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with the status of the pointer.</p>
<h2>Function Documentation</h2>
<h3>EAPI int evas_pointer_button_down_mask_get (const <code>Evas</code> * e)</h3>
<p>Returns a bitmask with the mouse buttons currently pressed, set to 1. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A bitmask of the currently depressed buttons on the cavas</dl>
<p> Calling this function will return a 32-bit integer with the appropriate bits set to 1 that correspond to a mouse button being depressed. This limits Evas to a mouse devices with a maximum of 32 buttons, but that is generally in excess of any host system&#8217;s pointing device abilities. </p>
<p> A canvas by default begins with no mouse buttons being pressed and only calls to <code>evas_event_feed_mouse_down()</code>, evas_event_feed_mouse_down_data(), <code>evas_event_feed_mouse_up()</code> and evas_event_feed_mouse_up_data() will alter that. </p>
<p> The least significant bit corresponds to the first mouse button (button 1) and the most significant bit corresponds to the last mouse button (button 32). </p>
<p> If e is not a valid canvas, the return value is undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 int button_mask, i;
 button_mask = evas_pointer_button_down_mask_get(evas);
 printf('Buttons currently pressed:);
 for (i = 0; i &lt; 32; i++)
 {
 if ((button_mask &amp; (1 &lt;&lt; i)) != 0) printf('Button %i, i + 1);
 }</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void evas_pointer_canvas_xy_get (const <code>Evas</code> * e, Evas_Coord * x, Evas_Coord * y)</h3>
<p>This function returns the current known pointer co-ordinates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>x</i> The pointer to a Evas_Coord to be filled in<br />
 <i>y</i> The pointer to a Evas_Coord to be filled in</dl>
<p> This function returns the current known canvas unit co-ordinates of the mouse pointer and sets the contents of the Evas_Coords pointed to by x and y to contain these co-ordinates. If e is not a valid canvas the results of this function are undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 Evas_Coord mouse_x, mouse_y;
 evas_pointer_output_xy_get(evas, &amp;mouse_x, &amp;mouse_y);
 printf('Mouse is at canvas position %f, %f, mouse_x, mouse_y);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI Evas_Bool evas_pointer_inside_get (const <code>Evas</code> * e)</h3>
<p>Returns whether the mouse pointer is logically inside the canvas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An integer that is 1 if the mouse is inside the canvas, 0 otherwise</dl>
<p> When this function is called it will return a value of either 0 or 1, depending on if <code>evas_event_feed_mouse_in()</code>, evas_event_feed_mouse_in_data(), or <code>evas_event_feed_mouse_out()</code>, evas_event_feed_mouse_out_data() have been called to feed in a mouse enter event into the canvas. </p>
<p> A return value of 1 indicates the mouse is logically inside the canvas, and 0 implies it is logically outside the canvas. </p>
<p> A canvas begins with the mouse being assumed outside (0). </p>
<p> If e is not a valid canvas, the return value is undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 if (evas_pointer_inside_get(evas)) printf('Mouse is in!);
 else printf('Mouse is out!);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void evas_pointer_output_xy_get (const <code>Evas</code> * e, int * x, int * y)</h3>
<p>This function returns the current known pointer co-ordinates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>x</i> The pointer to an integer to be filled in<br />
 <i>y</i> The pointer to an integer to be filled in</dl>
<p> This function returns the current known screen/output co-ordinates of the mouse pointer and sets the contents of the integers pointed to by x and y to contain these co-ordinates. If e is not a valid canvas the results of this function are undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 int mouse_x, mouse_y;
 evas_pointer_output_xy_get(evas, &amp;mouse_x, &amp;mouse_y);
 printf('Mouse is at screen position %i, %i, mouse_x, mouse_y);</pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
