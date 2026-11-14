---
title: "evas_object_image_fill_group(3)"
name: "evas_object_image_fill_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image_fill_group/"
description: "Image Object Fill Rectangle Functions – Functions that deal with what areas of the image object are to be tiled with the given image."
---

<p>Image Object Fill Rectangle Functions &#8211; Functions that deal with what areas of the image object are to be tiled with the given image. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_image_border_center_fill_set</code> (<code>Evas_Object</code> *obj, Evas_Bool fill)<br />
 <i>Sets if the center part of the given image object (not the border) should be drawn. </i><br />
 EAPI Evas_Bool <code>evas_object_image_border_center_fill_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves if the center of the given image object is to be drawn or not. </i><br />
 EAPI void <code>evas_object_image_fill_set</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the rectangle of the given image object that the image will be drawn to. </i><br />
 EAPI void <code>evas_object_image_fill_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the dimensions of the rectangle of the given image object that the image will be drawn to. </i><br />
 EAPI void <code>evas_object_image_fill_spread_set</code> (<code>Evas_Object</code> *obj, int spread)<br />
 <i>Sets the tiling mode for the given evas image object&#8217;s fill. </i><br />
 EAPI int <code>evas_object_image_fill_spread_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spread (tiling mode) for the given image object&#8217;s fill. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with what areas of the image object are to be tiled with the given image.</p>
<h2>Function Documentation</h2>
<h3>EAPI Evas_Bool evas_object_image_border_center_fill_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves if the center of the given image object is to be drawn or not. </p>
<p> See <code>evas_object_image_fill_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>If the center is to be drawn or not.</dl>
<h3>EAPI void evas_object_image_border_center_fill_set (<code>Evas_Object</code> * obj, Evas_Bool fill)</h3>
<p>Sets if the center part of the given image object (not the border) should be drawn. </p>
<p> When rendering, the image may be scaled to fit the size of the image object. This function sets if the center part of the scaled image is to be drawn or left completely blank. Very useful for frames and decorations. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>fill</i> Whether the center should be drawn.</dl>
<h3>EAPI void evas_object_image_fill_get (const <code>Evas_Object</code> * obj, Evas_Coord * x, Evas_Coord * y, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Retrieves the dimensions of the rectangle of the given image object that the image will be drawn to. </p>
<p> See <code>evas_object_image_fill_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>x</i> Location to store the X coordinate for the top left corner of the image in, or NULL.<br />
 <i>y</i> Location to store the Y coordinate for the top left corner of the image in, or NULL.<br />
 <i>w</i> Location to store the width of the image in, or NULL.<br />
 <i>h</i> Location to store the height of the image in, or NULL.</dl>
<h3>EAPI void evas_object_image_fill_set (<code>Evas_Object</code> * obj, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)</h3>
<p>Sets the rectangle of the given image object that the image will be drawn to. </p>
<p> Note that the image will be tiled around this one rectangle. To have only one copy of the image drawn, x and y must be 0 and w and h need to be the width and height of the image object respectively. </p>
<p> The default values for the fill parameters is x = 0, y = 0, w = 32 and h = 32. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>x</i> The X coordinate for the top left corner of the image.<br />
 <i>y</i> The Y coordinate for the top left corner of the image.<br />
 <i>w</i> The width of the image.<br />
 <i>h</i> The height of the image.</dl>
<h3>EAPI int evas_object_image_fill_spread_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the spread (tiling mode) for the given image object&#8217;s fill. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas image object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current spread mode of the image object.</dl>
<p> References EVAS_TEXTURE_REPEAT.</p>
<h3>EAPI void evas_object_image_fill_spread_set (<code>Evas_Object</code> * obj, int spread)</h3>
<p>Sets the tiling mode for the given evas image object&#8217;s fill. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas image object.<br />
 <i>spread</i> One of EVAS_TEXTURE_REFLECT, EVAS_TEXTURE_REPEAT, EVAS_TEXTURE_RESTRICT, or EVAS_TEXTURE_PAD.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
