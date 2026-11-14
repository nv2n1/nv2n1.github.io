---
title: "evas_object_image_scale(3)"
name: "evas_object_image_scale"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image_scale/"
description: "Image Object Image Scaling Functions – Functions that change the scaling quality of an image object."
---

<p>Image Object Image Scaling Functions &#8211; Functions that change the scaling quality of an image object. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_image_smooth_scale_set</code> (<code>Evas_Object</code> *obj, Evas_Bool smooth_scale)<br />
 <i>Sets whether to use of high-quality image scaling algorithm of the given image object. </i><br />
 EAPI Evas_Bool <code>evas_object_image_smooth_scale_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether the given image object is using use a high-quality image scaling algorithm. </i></p>
<h2>Detailed Description</h2>
<p>Functions that change the scaling quality of an image object.</p>
<h2>Function Documentation</h2>
<h3>EAPI Evas_Bool evas_object_image_smooth_scale_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves whether the given image object is using use a high-quality image scaling algorithm. </p>
<p> See <code>evas_object_image_smooth_scale_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether smooth scale is being used.</dl>
<h3>EAPI void evas_object_image_smooth_scale_set (<code>Evas_Object</code> * obj, Evas_Bool smooth_scale)</h3>
<p>Sets whether to use of high-quality image scaling algorithm of the given image object. </p>
<p> When enabled, a higher quality image scaling algorithm is used when scaling images to sizes other than the source image. This gives better results but is more computationally expensive. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>smooth_scale</i> Whether to use smooth scale or not.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
