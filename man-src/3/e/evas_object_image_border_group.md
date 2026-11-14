---
title: "evas_object_image_border_group(3)"
name: "evas_object_image_border_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image_border_group/"
description: "Image Object Border Functions – Functions that adjust the unscaled image border of image objects."
---

<p>Image Object Border Functions &#8211; Functions that adjust the unscaled image border of image objects. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_image_border_set</code> (<code>Evas_Object</code> *obj, int l, int r, int t, int b)<br />
 <i>Sets how much of each border of the given image object is not to be scaled. </i><br />
 EAPI void <code>evas_object_image_border_get</code> (const <code>Evas_Object</code> *obj, int *l, int *r, int *t, int *b)<br />
 <i>Retrieves how much of each border of the given image object is not to be scaled. </i></p>
<h2>Detailed Description</h2>
<p>Functions that adjust the unscaled image border of image objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_image_border_get (const <code>Evas_Object</code> * obj, int * l, int * r, int * t, int * b)</h3>
<p>Retrieves how much of each border of the given image object is not to be scaled. </p>
<p> See <code>evas_object_image_border_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>l</i> Location to store the left border width in, or NULL.<br />
 <i>r</i> Location to store the right border width in, or NULL.<br />
 <i>t</i> Location to store the top border width in, or NULL.<br />
 <i>b</i> Location to store the bottom border width in, or NULL.</dl>
<h3>EAPI void evas_object_image_border_set (<code>Evas_Object</code> * obj, int l, int r, int t, int b)</h3>
<p>Sets how much of each border of the given image object is not to be scaled. </p>
<p> When rendering, the image may be scaled to fit the size of the image object. This function sets what area around the border of the image is not to be scaled. This sort of function is useful for widget theming, where, for example, buttons may be of varying sizes, but the border size must remain constant. </p>
<p> The units used for l, r, t and b are output units. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>l</i> Distance of the left border that is not to be stretched.<br />
 <i>r</i> Distance of the right border that is not to be stretched.<br />
 <i>t</i> Distance of the top border that is not to be stretched.<br />
 <i>b</i> Distance of the bottom border that is not to be stretched.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
