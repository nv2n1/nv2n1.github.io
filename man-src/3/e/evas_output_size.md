---
title: "evas_output_size(3)"
name: "evas_output_size"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_output_size/"
description: "Evas Output and Viewport Resizing Functions – Functions that set and retrieve the output and viewport size of an evas."
---

<p>Evas Output and Viewport Resizing Functions &#8211; Functions that set and retrieve the output and viewport size of an evas. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_output_size_set</code> (<code>Evas</code> *e, int w, int h)<br />
 <i>Sets the output size of the render engine of the given evas. </i><br />
 EAPI void <code>evas_output_size_get</code> (const <code>Evas</code> *e, int *w, int *h)<br />
 <i>Retrieve the output size of the render engine of the given evas. </i><br />
 EAPI void <code>evas_output_viewport_set</code> (<code>Evas</code> *e, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the output viewport of the given evas in evas units. </i><br />
 EAPI void <code>evas_output_viewport_get</code> (const <code>Evas</code> *e, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Get the render engine&#8217;s output viewport co-ordinates in canvas units. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set and retrieve the output and viewport size of an evas.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_output_size_get (const <code>Evas</code> * e, int * w, int * h)</h3>
<p>Retrieve the output size of the render engine of the given evas. </p>
<p> The output size is given in whatever the output units are for the engine. </p>
<p> If either w or h is NULL, then it is ignored. If e is invalid, the returned results are undefined. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.<br />
 <i>w</i> The pointer to an integer to store the width in.<br />
 <i>h</i> The pointer to an integer to store the height in.</dl>
<h3>EAPI void evas_output_size_set (<code>Evas</code> * e, int w, int h)</h3>
<p>Sets the output size of the render engine of the given evas. </p>
<p> The evas will render to a rectangle of the given size once this function is called. The output size is independent of the viewport size. The viewport will be stretched to fill the given rectangle. </p>
<p> The units used for w and h depend on the engine used by the evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.<br />
 <i>w</i> The width in output units, usually pixels.<br />
 <i>h</i> The height in output units, usually pixels.</dl>
<h3>EAPI void evas_output_viewport_get (const <code>Evas</code> * e, Evas_Coord * x, Evas_Coord * y, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Get the render engine&#8217;s output viewport co-ordinates in canvas units. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>x</i> The pointer to a x variable to be filled in<br />
 <i>y</i> The pointer to a y variable to be filled in<br />
 <i>w</i> The pointer to a width variable to be filled in<br />
 <i>h</i> The pointer to a height variable to be filled in</dl>
<p> Calling this function writes the current canvas output viewport size and location values into the variables pointed to by x, y, w and h. On success the variables have the output location and size values written to them in canvas units. Any of x, y, w or h that are NULL will not be written to. If e is invalid, the results are undefined. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 Evas_Coord x, y, width, height;
 evas_output_viewport_get(evas, &amp;x, &amp;y, &amp;w, &amp;h);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void evas_output_viewport_set (<code>Evas</code> * e, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)</h3>
<p>Sets the output viewport of the given evas in evas units. </p>
<p> The output viewport is the area of the evas that will be visible to the viewer. The viewport will be stretched to fit the output target of the evas when rendering is performed. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The coordinate values do not have to map 1-to-1 with the output target. However, it is generally advised that it is done for ease of use.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.<br />
 <i>x</i> The top-left corner x value of the viewport.<br />
 <i>y</i> The top-left corner y value of the viewport.<br />
 <i>w</i> The width of the viewport. Must be greater than 0.<br />
 <i>h</i> The height of the viewport. Must be greater than 0.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
