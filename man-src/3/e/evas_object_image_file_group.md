---
title: "evas_object_image_file_group(3)"
name: "evas_object_image_file_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image_file_group/"
description: "Image Object File Functions – Functions that write to or retrieve images from files."
---

<p>Image Object File Functions &#8211; Functions that write to or retrieve images from files. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_image_file_set</code> (<code>Evas_Object</code> *obj, const char *file, const char *key)<br />
 <i>Sets the filename and key of the given image object. </i><br />
 EAPI void <code>evas_object_image_file_get</code> (const <code>Evas_Object</code> *obj, const char **file, const char **key)<br />
 <i>Retrieves the filename and key of the given image object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that write to or retrieve images from files.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_image_file_get (const <code>Evas_Object</code> * obj, const char ** file, const char ** key)</h3>
<p>Retrieves the filename and key of the given image object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>file</i> Location to store the image filename, or NULL.<br />
 <i>key</i> Location to store the image key, or NULL.</dl>
<h3>EAPI void evas_object_image_file_set (<code>Evas_Object</code> * obj, const char * file, const char * key)</h3>
<p>Sets the filename and key of the given image object. </p>
<p> If the file supports multiple data stored in it as eet, you can specify the key to be used as the index of the image in this file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>file</i> The image filename.<br />
 <i>key</i> The image key in file, or NULL.</dl>
<p> References EVAS_COLORSPACE_ARGB8888, EVAS_LOAD_ERROR_GENERIC, and EVAS_LOAD_ERROR_NONE.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
