---
title: "evas_object_image_size(3)"
name: "evas_object_image_size"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image_size/"
description: "Image Object Image Size Functions – Functions that change the size of the image used by an image object."
---

<p>Image Object Image Size Functions &#8211; Functions that change the size of the image used by an image object. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_image_size_set</code> (<code>Evas_Object</code> *obj, int w, int h)<br />
 <i>Sets the size of the given image object. </i><br />
 EAPI void <code>evas_object_image_size_get</code> (const <code>Evas_Object</code> *obj, int *w, int *h)<br />
 <i>Retrieves the size of the given image object. </i><br />
 EAPI int <code>evas_object_image_stride_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the row stride of the given image object,. </i></p>
<h2>Detailed Description</h2>
<p>Functions that change the size of the image used by an image object.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_image_size_get (const <code>Evas_Object</code> * obj, int * w, int * h)</h3>
<p>Retrieves the size of the given image object. </p>
<p> See <code>evas_object_image_size_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>w</i> Location to store the width of the image in, or NULL.<br />
 <i>h</i> Location to store the height of the image in, or NULL.</dl>
<h3>EAPI void evas_object_image_size_set (<code>Evas_Object</code> * obj, int w, int h)</h3>
<p>Sets the size of the given image object. </p>
<p> This function will scale down or crop the image so that it is treated as if it were at the given size. If the size given is smaller than the image, it will be cropped. If the size given is larger, then the image will be treated as if it were in the upper left hand corner of a larger image that is otherwise transparent. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>w</i> The new width of the image.<br />
 <i>h</i> The new height of the image.</dl>
<h3>EAPI int evas_object_image_stride_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the row stride of the given image object,. </p>
<p> The row stride is the number of units between the start of a row and the start of the next row. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The stride of the image.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
