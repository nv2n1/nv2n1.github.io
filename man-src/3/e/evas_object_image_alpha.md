---
title: "evas_object_image_alpha(3)"
name: "evas_object_image_alpha"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image_alpha/"
description: "Image Object Image Alpha Functions – Functions that change the alpha of an image object."
---

<p>Image Object Image Alpha Functions &#8211; Functions that change the alpha of an image object. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_image_alpha_set</code> (<code>Evas_Object</code> *obj, Evas_Bool has_alpha)<br />
 <i>Enable or disable alpha channel of the given image object. </i><br />
 EAPI Evas_Bool <code>evas_object_image_alpha_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the alpha channel setting of the given image object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that change the alpha of an image object.</p>
<h2>Function Documentation</h2>
<h3>EAPI Evas_Bool evas_object_image_alpha_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the alpha channel setting of the given image object. </p>
<p> This function returns 1 if the image object&#8217;s alpha channel is being used, or 0 otherwise. </p>
<p> See <code>evas_object_image_alpha_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the alpha channel data is being used.</dl>
<h3>EAPI void evas_object_image_alpha_set (<code>Evas_Object</code> * obj, Evas_Bool has_alpha)</h3>
<p>Enable or disable alpha channel of the given image object. </p>
<p> This function sets a flag on an image object indicating whether or not to use alpha channel data. A value of 1 indicates to use alpha channel data, and 0 indicates to ignore any alpha channel data. Note that this has nothing to do with an object&#8217;s color as manipulated by <code>evas_object_color_set()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>has_alpha</i> Whether to use alpha channel data or not.</dl>
<p> References evas_object_image_data_update_add().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
