---
title: "evas_object_image(3)"
name: "evas_object_image"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_image/"
description: "Image Object Functions – Functions used to create and manipulate image objects."
---

<p>Image Object Functions &#8211; Functions used to create and manipulate image objects. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_Object</code> * <code>evas_object_image_add</code> (<code>Evas</code> *e)<br />
 <i>Creates a new image object on the given evas. </i><br />
 EAPI int <code>evas_object_image_load_error_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves a number representing any error that occurred during the last load of the given image object. </i><br />
 EAPI Evas_Bool <code>evas_object_image_save</code> (const <code>Evas_Object</code> *obj, const char *file, const char *key, const char *flags)<br />
 <i>Save the given image object to a file. </i><br />
 EAPI void <code>evas_object_image_pixels_dirty_set</code> (<code>Evas_Object</code> *obj, Evas_Bool dirty)<br />
 <i>Mark whether the given image object is dirty (needs to be redrawn). </i><br />
 EAPI Evas_Bool <code>evas_object_image_pixels_dirty_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether the given image object is dirty (needs to be redrawn). </i></p>
<h2>Detailed Description</h2>
<p>Functions used to create and manipulate image objects. </p>
<p> Note &#8211; Image objects may return or accept &#8216;image data&#8217; in multiple formats. This is based on the colorspace of an object. Here is a rundown on formats: </p>
<p> EVAS_COLORSPACE_ARGB8888: </p>
<p> This pixel format is a linear block of pixels, starting at the top-left row by row until the bottom right of the image or pixel region. All pixels are 32-bit unsigned int&#8217;s with the high-byte being alpha and the low byte being blue in the format ARGB. Alpha may or may not be used by evas depending on the alpha flag of the image, but if not used, should be set to 0xff anyway. </p>
<p> This colorspace uses premultiplied alpha. That means that R, G and B cannot exceed A in value. The conversion from non-premultiplied colorspace is: </p>
<p> R = (r * a) / 255; G = (g * a) / 255; B = (b * a) / 255; </p>
<p> So 50% transparent blue will be: 0x80000080. This will not be &#8216;dark&#8217; &#8211; just 50% transparent. Values are 0 == black, 255 == solid or full red, green or blue. </p>
<p> EVAS_COLORSPACE_YCBCR422P601_PL: </p>
<p> This is a pointer-list indirected set of YUV (YCbCr) pixel data. This means that the data returned or set is not actual pixel data, but pointers TO lines of pixel data. The list of pointers will first be N rows of pointers to the Y plane &#8211; pointing to the first pixel at the start of each row in the Y plane. N is the height of the image data in pixels. Each pixel in the Y, U and V planes is 1 byte exactly, packed. The next N / 2 pointers will point to rows in the U plane, and the next N / 2 pointers will point to the V plane rows. U and V planes are half the horizontal and vertical resolution of the U plane. </p>
<p> Row order is top to bottom and row pixels are stored left to right. </p>
<p> There is a limitation that these images MUST be a multiple of 2 pixels in size horizontally or vertically. This is due to the U and V planes being half resolution. Also note that this assumes the itu601 YUV colorspace specification. This is defined for standard television and mpeg streams. HDTV may use the itu709 specification. </p>
<p> Values are 0 to 255, indicating full or no signal in that plane respectively. </p>
<p> EVAS_COLORSPACE_YCBCR422P709_PL: </p>
<p> Not implemented yet. </p>
<p> EVAS_COLORSPACE_RGB565_A5P: </p>
<p> In the process of being implemented in 1 engine only. This may change. </p>
<p> This is a pointer to image data for 16-bit half-word pixel data in 16bpp RGB 565 format (5 bits red, 6 bits green, 5 bits blue), with the high-byte containing red and the low byte containing blue, per pixel. This data is packed row by row from the top-left to the bottom right. </p>
<p> If the image has an alpha channel enabled there will be an extra alpha plane after the color pixel plane. If not, then this data will not exist and should not be accessed in any way. This plane is a set of pixels with 1 byte per pixel defining the alpha values of all pixels in the image from the top-left to the bottom right of the image, row by row. Even though the values of the alpha pixels can be 0 to 255, only values 0 through to 32 are used, 32 being solid and 0 being transparent. </p>
<p> RGB values can be 0 to 31 for red and blue and 0 to 63 for green, with 0 being black and 31 or 63 being full red, green or blue respectively. This colorspace is also pre-multiplied like EVAS_COLORSPACE_ARGB8888 so: </p>
<p> R = (r * a) / 32; G = (g * a) / 32; B = (b * a) / 32;</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Object</code>* evas_object_image_add (<code>Evas</code> * e)</h3>
<p>Creates a new image object on the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The created image object.</dl>
<h3>EAPI int evas_object_image_load_error_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves a number representing any error that occurred during the last load of the given image object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A value giving the last error that occurred. It should be one of the EVAS_LOAD_ERROR_* values. EVAS_LOAD_ERROR_NONE is returned if there was no error.</dl>
<h3>EAPI Evas_Bool evas_object_image_pixels_dirty_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves whether the given image object is dirty (needs to be redrawn). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Whether the image is dirty.</dl>
<h3>EAPI void evas_object_image_pixels_dirty_set (<code>Evas_Object</code> * obj, Evas_Bool dirty)</h3>
<p>Mark whether the given image object is dirty (needs to be redrawn). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>dirty</i> Whether the image is dirty.</dl>
<h3>EAPI Evas_Bool evas_object_image_save (const <code>Evas_Object</code> * obj, const char * file, const char * key, const char * flags)</h3>
<p>Save the given image object to a file. </p>
<p> Note that you should pass the filename extension when saving. If the file supports multiple data stored in it as eet, you can specify the key to be used as the index of the image in this file. </p>
<p> You can specify some flags when saving the image. Currently acceptable flags are quality and compress. Eg.: &#8216;quality=100 compress=9&#8217; </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given image object.<br />
 <i>file</i> The filename to be used to save the image.<br />
 <i>key</i> The image key in file, or NULL.<br />
 <i>flags</i> String containing the flags to be used.</dl>
<p> References EVAS_COLORSPACE_ARGB8888.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
