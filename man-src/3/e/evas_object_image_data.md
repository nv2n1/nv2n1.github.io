---
title: "evas_object_image_data(3)"
name: "evas_object_image_data"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image_data/"
description: "Image Object Image Data Functions – Functions that allow you to access or modify the image pixel data of an image object."
---

<p>Image Object Image Data Functions &#8211; Functions that allow you to access or modify the image pixel data of an image object. </p>
<h3>Functions</h3>
<p>EAPI void * <code>evas_object_image_data_convert</code> (<code>Evas_Object</code> *obj, <code>Evas_Colorspace</code> to_cspace)<br />
 <i>Converts the raw image data of the given image object to the specified colorspace. </i><br />
 EAPI void <code>evas_object_image_data_set</code> (<code>Evas_Object</code> *obj, void *data)<br />
 <i>Sets the raw image data of the given image object. </i><br />
 EAPI void * <code>evas_object_image_data_get</code> (const <code>Evas_Object</code> *obj, Evas_Bool for_writing)<br />
 <i>Get a pointer to the raw image data of the given image object. </i><br />
 EAPI void <code>evas_object_image_preload</code> (const <code>Evas_Object</code> *obj, Evas_Bool cancel)<br />
 <i>Preload image in the background. </i><br />
 EAPI void <code>evas_object_image_data_copy_set</code> (<code>Evas_Object</code> *obj, void *data)<br />
 <i>Replaces the raw image data of the given image object. </i><br />
 EAPI void <code>evas_object_image_data_update_add</code> (<code>Evas_Object</code> *obj, int x, int y, int w, int h)<br />
 <i>Mark a sub-region of the given image object to be redrawn. </i></p>
<h2>Detailed Description</h2>
<p>Functions that allow you to access or modify the image pixel data of an image object.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* evas_object_image_data_convert (<code>Evas_Object</code> * obj, <code>Evas_Colorspace</code> to_cspace)</h3>
<p>Converts the raw image data of the given image object to the specified colorspace. </p>
<p> Note that this function does not modify the raw image data. If the requested colorspace is the same as the image colorspace nothing is done and NULL is returned. You should use <code>evas_object_image_colorspace_get()</code> to check the current image colorspace. </p>
<p> See <code>evas_object_image_colorspace_get</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>to_cspace</i> The colorspace to which the image raw data will be converted.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>data A newly allocated data in the format specified by to_cspace.</dl>
<h3>EAPI void evas_object_image_data_copy_set (<code>Evas_Object</code> * obj, void * data)</h3>
<p>Replaces the raw image data of the given image object. </p>
<p> This function lets the application replace an image object&#8217;s internal pixel buffer with a user-allocated one. For best results, you should generally first call <code>evas_object_image_size_set()</code> with the width and height for the new buffer. </p>
<p> This call is best suited for when you will be using image data with different dimensions than the existing image data, if any. If you only need to modify the existing image in some fashion, then using <code>evas_object_image_data_get()</code> is probably what you are after. </p>
<p> Note that the caller is responsible for freeing the buffer when finished with it, as user-set image data will not be automatically freed when the image object is deleted. </p>
<p> See <code>evas_object_image_data_get</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>data</i> The raw data.</dl>
<h3>EAPI void* evas_object_image_data_get (const <code>Evas_Object</code> * obj, Evas_Bool for_writing)</h3>
<p>Get a pointer to the raw image data of the given image object. </p>
<p> This function returns a pointer to an image object&#8217;s internal pixel buffer, for reading only or read/write. If you request it for writing, the image will be marked dirty so that it gets redrawn at the next update. </p>
<p> This is best suited when you want to modify an existing image, without changing its dimensions. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>for_writing</i> Whether the data being retrieved will be modified.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The raw image data.</dl>
<h3>EAPI void evas_object_image_data_set (<code>Evas_Object</code> * obj, void * data)</h3>
<p>Sets the raw image data of the given image object. </p>
<p> Note that the raw data must be of the same size and colorspace of the image. If data is NULL the current image data will be freed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>data</i> The raw data, or NULL.</dl>
<p> References EVAS_LOAD_ERROR_NONE.</p>
<h3>EAPI void evas_object_image_data_update_add (<code>Evas_Object</code> * obj, int x, int y, int w, int h)</h3>
<p>Mark a sub-region of the given image object to be redrawn. </p>
<p> This function schedules a particular rectangular region of an image object to be updated (redrawn) at the next render. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>x</i> X-offset of the region to be updated.<br />
 <i>y</i> Y-offset of the region to be updated.<br />
 <i>w</i> Width of the region to be updated.<br />
 <i>h</i> Height of the region to be updated.</dl>
<p> References evas_list_append(). </p>
<p> Referenced by evas_object_image_alpha_set().</p>
<h3>EAPI void evas_object_image_preload (const <code>Evas_Object</code> * obj, Evas_Bool cancel)</h3>
<p>Preload image in the background. </p>
<p> This function request the preload of the data image in the background. The worked is queued before being processed. </p>
<p> If cancel is set, it will remove the image from the workqueue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>cancel</i> 0 means add to the workqueue, 1 remove it.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
