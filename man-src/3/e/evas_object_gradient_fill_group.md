---
title: "evas_object_gradient_fill_group(3)"
name: "evas_object_gradient_fill_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_gradient_fill_group/"
description: "Gradient Object Fill Rectangle Functions – Functions that deal with what areas of the gradient object are to be tiled with the gradient."
---

<p>Gradient Object Fill Rectangle Functions &#8211; Functions that deal with what areas of the gradient object are to be tiled with the gradient. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_gradient_fill_set</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the rectangle on the gradient object that the gradient will be drawn to. </i><br />
 EAPI void <code>evas_object_gradient_fill_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the dimensions of the rectangle on the gradient object that the gradient will use as its fill rect. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with what areas of the gradient object are to be tiled with the gradient.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_gradient_fill_get (const <code>Evas_Object</code> * obj, Evas_Coord * x, Evas_Coord * y, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Retrieves the dimensions of the rectangle on the gradient object that the gradient will use as its fill rect. </p>
<p> See <code>evas_object_gradient_fill_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>x</i> Pointer to an Evas_Coord to store the X coordinate in.<br />
 <i>y</i> Pointer to an Evas_Coord to store the Y coordinate in.<br />
 <i>w</i> Pointer to an Evas_Coord to store the width in.<br />
 <i>h</i> Pointer to an Evas_Coord to store the height in.</dl>
<h3>EAPI void evas_object_gradient_fill_set (<code>Evas_Object</code> * obj, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)</h3>
<p>Sets the rectangle on the gradient object that the gradient will be drawn to. </p>
<p> Note that the gradient may be tiled around this one rectangle, according to its spread value &#8211; restrict, repeat, or reflect. To have only one &#8216;cycle&#8217; of the gradient drawn, the spread value must be set to restrict, or x and y must be 0 and w and h need to be the width and height of the gradient object respectively. </p>
<p> The default values for the fill parameters is x = 0, y = 0, w = 32 and h = 32. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>x</i> The X coordinate for the top left corner of the rect.<br />
 <i>y</i> The Y coordinate for the top left corner of the rect.<br />
 <i>w</i> The width of the rect.<br />
 <i>h</i> The height of the rect.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
