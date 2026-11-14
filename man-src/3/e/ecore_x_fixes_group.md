---
title: "ecore_x_fixes_group(3)"
name: "ecore_x_fixes_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_fixes_group/"
description: "X Fixes Extension Functions – Functions related to the X Fixes extension."
---

<p>X Fixes Extension Functions &#8211; Functions related to the X Fixes extension. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_xfixes_query</code> (void)<br />
 <i>Return whether the X server supports the Fixes Extension. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new</code> (Ecore_X_Rectangle *rects, int num)<br />
 <i>Create a region from rectangles. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new_from_bitmap</code> (Ecore_X_Pixmap bitmap)<br />
 <i>Create a region from a pixmap. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new_from_window</code> (Ecore_X_Window window, Ecore_X_Region_Type type)<br />
 <i>Create a region from a window. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new_from_gc</code> (Ecore_X_GC gc)<br />
 <i>Create a region from a graphic context. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new_from_picture</code> (Ecore_X_Picture picture)<br />
 <i>Create a region from a picture. </i><br />
 EAPI void <code>ecore_x_region_del</code> (Ecore_X_Region region)<br />
 <i>Destroy a region. </i><br />
 EAPI void <code>ecore_x_region_set</code> (Ecore_X_Region region, Ecore_X_Rectangle *rects, int num)<br />
 <i>Set the content of a region. </i><br />
 EAPI void <code>ecore_x_region_copy</code> (Ecore_X_Region dest, Ecore_X_Region source)<br />
 <i>Copy the content of a region. </i><br />
 EAPI void <code>ecore_x_region_combine</code> (Ecore_X_Region dest, Ecore_X_Region source1, Ecore_X_Region source2)<br />
 <i>Make the union of two regions. </i><br />
 EAPI void <code>ecore_x_region_intersect</code> (Ecore_X_Region dest, Ecore_X_Region source1, Ecore_X_Region source2)<br />
 <i>Make the intersection of two regions. </i><br />
 EAPI void <code>ecore_x_region_subtract</code> (Ecore_X_Region dest, Ecore_X_Region source1, Ecore_X_Region source2)<br />
 <i>Make the substraction of two regions. </i><br />
 EAPI void <code>ecore_x_region_invert</code> (Ecore_X_Region dest, Ecore_X_Rectangle *bounds, Ecore_X_Region source)<br />
 <i>Make the substraction of regions by bounds. </i><br />
 EAPI void <code>ecore_x_region_translate</code> (Ecore_X_Region region, int dx, int dy)<br />
 <i>Translate a region. </i><br />
 EAPI void <code>ecore_x_region_extents</code> (Ecore_X_Region dest, Ecore_X_Region source)<br />
 <i>Extent a region. </i><br />
 EAPI void <code>ecore_x_region_fetch_prefetch</code> (Ecore_X_Region region)<br />
 <i>Sends the XFixesFetchRegion request. </i><br />
 EAPI void <code>ecore_x_region_fetch_fetch</code> (void)<br />
 <i>Gets the reply of the XFixesFetchRegion request sent by ecore_xcb_region_fetch_prefetch(). </i><br />
 EAPI Ecore_X_Rectangle * <code>ecore_x_region_fetch</code> (Ecore_X_Region region __UNUSED__, int *num, Ecore_X_Rectangle *bounds)<br />
 <i>Return the rectangles that compose a region. </i><br />
 EAPI void <code>ecore_x_region_expand</code> (Ecore_X_Region dest, Ecore_X_Region source, unsigned int left, unsigned int right, unsigned int top, unsigned int bottom)<br />
 <i>Expand a region. </i><br />
 EAPI void <code>ecore_x_region_gc_clip_set</code> (Ecore_X_Region region, Ecore_X_GC gc, int x_origin, int y_origin)<br />
 <i>Change clip-mask in a graphic context to the specified region. </i><br />
 EAPI void <code>ecore_x_region_window_shape_set</code> (Ecore_X_Region region, Ecore_X_Window dest, Ecore_X_Shape_Type type, int x_offset, int y_offset)<br />
 <i>Change the shape extension of a window. </i><br />
 EAPI void <code>ecore_x_region_picture_clip_set</code> (Ecore_X_Region region, Ecore_X_Picture picture, int x_origin, int y_origin)<br />
 <i>Change clip-mask in picture to the specified region. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to the X Fixes extension.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_region_combine (Ecore_X_Region dest, Ecore_X_Region source1, Ecore_X_Region source2)</h3>
<p>Make the union of two regions. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> The destination region.<br />
 <i>source1</i> The first source region.<br />
 <i>source2</i> The second source region.</dl>
<p> Replace the contents of dest with the union of source1 and source2.</p>
<h3>EAPI void ecore_x_region_copy (Ecore_X_Region dest, Ecore_X_Region source)</h3>
<p>Copy the content of a region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> The destination region.<br />
 <i>source</i> The source region.</dl>
<p> Replace the contents of dest with the contents of source.</p>
<h3>EAPI void ecore_x_region_del (Ecore_X_Region region)</h3>
<p>Destroy a region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> The region to destroy.</dl>
<p> Destroy the specified region.</p>
<h3>EAPI void ecore_x_region_expand (Ecore_X_Region dest, Ecore_X_Region source, unsigned int left, unsigned int right, unsigned int top, unsigned int bottom)</h3>
<p>Expand a region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> The destination region.<br />
 <i>source</i> The source region.<br />
 <i>left</i> The number of pixels to add on the left.<br />
 <i>right</i> The number of pixels to add on the right.<br />
 <i>top</i> The number of pixels to add at the top.<br />
 <i>bottom</i> The number of pixels to add at the bottom.</dl>
<p> Put in dest the area specified by expanding each rectangle in the source region by the specified number of pixels to the left, right, top and bottom.</p>
<h3>EAPI void ecore_x_region_extents (Ecore_X_Region dest, Ecore_X_Region source)</h3>
<p>Extent a region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> The destination region.<br />
 <i>source</i> The source region.</dl>
<p> The extents of the source region are placed in dest.</p>
<h3>EAPI Ecore_X_Rectangle* ecore_x_region_fetch (Ecore_X_Region region __UNUSED__, int * num, Ecore_X_Rectangle * bounds)</h3>
<p>Return the rectangles that compose a region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> The region (Unused).<br />
 <i>num</i> The number of returned rectangles.<br />
 <i>bounds</i> The returned bounds of the region.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The returned rectangles.</dl>
<p> The region passed to ecore_xcb_region_fetch_prefetch() is returned as a list of rectagles in XY-banded order. </p>
<p> To use this function, you must call before, and in order, ecore_xcb_region_fetch_prefetch(), which sends the XFixesFetchRegion request, then ecore_xcb_region_fetch_fetch(), which gets the reply.</p>
<h3>EAPI void ecore_x_region_fetch_prefetch (Ecore_X_Region region)</h3>
<p>Sends the XFixesFetchRegion request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> Requested region.</dl>
<h3>EAPI void ecore_x_region_gc_clip_set (Ecore_X_Region region, Ecore_X_GC gc, int x_origin, int y_origin)</h3>
<p>Change clip-mask in a graphic context to the specified region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> The region to change.<br />
 <i>gc</i> The clip-mask graphic context.<br />
 <i>x_origin</i> The horizontal translation.<br />
 <i>y_origin</i> The vertical translation.</dl>
<p> Changes clip-mask in gc to the specified region and sets the clip origin with the values of x_origin and y_origin. Output will be clippped to remain contained within the region. The clip origin is interpreted relative to the origin of whatever destination drawable is specified in a graphics request. The region is interpreted relative to the clip origin. Future changes to region have no effect on the gc clip-mask.</p>
<h3>EAPI void ecore_x_region_intersect (Ecore_X_Region dest, Ecore_X_Region source1, Ecore_X_Region source2)</h3>
<p>Make the intersection of two regions. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> The destination region.<br />
 <i>source1</i> The first source region.<br />
 <i>source2</i> The second source region.</dl>
<p> Replace the contents of dest with the intersection of source1 and source2.</p>
<h3>EAPI void ecore_x_region_invert (Ecore_X_Region dest, Ecore_X_Rectangle * bounds, Ecore_X_Region source)</h3>
<p>Make the substraction of regions by bounds. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> The destination region.<br />
 <i>bounds</i> The bounds.<br />
 <i>source</i> The source region.</dl>
<p> The source region is subtracted from the region specified by bounds. The result is placed in dest, replacing its contents.</p>
<h3>EAPI Ecore_X_Region ecore_x_region_new (Ecore_X_Rectangle * rects, int num)</h3>
<p>Create a region from rectangles. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rects</i> The rectangles used to initialize the region.<br />
 <i>num</i> The number of rectangles.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The newly created region.</dl>
<p> Create a region initialized to the specified list of rectangles rects. The rectangles may be specified in any order, their union becomes the region.</p>
<h3>EAPI Ecore_X_Region ecore_x_region_new_from_bitmap (Ecore_X_Pixmap bitmap)</h3>
<p>Create a region from a pixmap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>bitmap</i> The bitmap used to initialize the region.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The newly created region.</dl>
<p> Creates a region initialized to the set of &#8216;one&#8217; pixels in bitmap (which must be of depth 1, else Match error).</p>
<h3>EAPI Ecore_X_Region ecore_x_region_new_from_gc (Ecore_X_GC gc)</h3>
<p>Create a region from a graphic context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>gc</i> The graphic context used to initialize the region.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The newly created region.</dl>
<p> Creates a region initialized from the clip list of gc.</p>
<h3>EAPI Ecore_X_Region ecore_x_region_new_from_picture (Ecore_X_Picture picture)</h3>
<p>Create a region from a picture. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>picture</i> The picture used to initialize the region.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The newly created region.</dl>
<p> Creates a region initialized from the clip list of picture.</p>
<h3>EAPI Ecore_X_Region ecore_x_region_new_from_window (Ecore_X_Window window, Ecore_X_Region_Type type)</h3>
<p>Create a region from a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window used to initialize the region.<br />
 <i>type</i> The type of the region.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The newly created region.</dl>
<p> Creates a region initialized to the specified window region. See the Shape extension for the definition of Bounding and Clip regions.</p>
<h3>EAPI void ecore_x_region_picture_clip_set (Ecore_X_Region region, Ecore_X_Picture picture, int x_origin, int y_origin)</h3>
<p>Change clip-mask in picture to the specified region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> The region.<br />
 <i>picture</i> The picture.<br />
 <i>x_origin</i> The X coordinate of the origin.<br />
 <i>y_origin</i> The Y coordinate of the origin.</dl>
<p> Changes clip-mask in picture to the specified region and sets the clip origin. Input and output will be clipped to remain contained within the region. The clip origin is interpreted relative to the origin of the drawable associated with picture. The region is interpreted relative to the clip origin. Future changes to region have no effect on the picture clip-mask.</p>
<h3>EAPI void ecore_x_region_set (Ecore_X_Region region, Ecore_X_Rectangle * rects, int num)</h3>
<p>Set the content of a region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> The region to destroy.<br />
 <i>rects</i> The rectangles used to set the region.<br />
 <i>num</i> The number of rectangles.</dl>
<p> Replace the current contents of region with the region formed by the union of the rectangles rects.</p>
<h3>EAPI void ecore_x_region_subtract (Ecore_X_Region dest, Ecore_X_Region source1, Ecore_X_Region source2)</h3>
<p>Make the substraction of two regions. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> The destination region.<br />
 <i>source1</i> The first source region.<br />
 <i>source2</i> The second source region.</dl>
<p> Replace the contents of dest with the substraction of source1 by source2.</p>
<h3>EAPI void ecore_x_region_translate (Ecore_X_Region region, int dx, int dy)</h3>
<p>Translate a region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> The region to translate.<br />
 <i>dx</i> The horizontal translation.<br />
 <i>dy</i> The vertical translation.</dl>
<p> The region is translated by dx and dy in place.</p>
<h3>EAPI void ecore_x_region_window_shape_set (Ecore_X_Region region, Ecore_X_Window dest, Ecore_X_Shape_Type type, int x_offset, int y_offset)</h3>
<p>Change the shape extension of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> The region.<br />
 <i>dest</i> The window whose shape is changed.<br />
 <i>type</i> The kind of shape.<br />
 <i>x_offset</i> The horizontal offset.<br />
 <i>y_offset</i> The vertical offset.</dl>
<p> Set the specified Shape extension region of window to region, offset by x_offset and y_offset. Future changes to region have no effect on the window shape.</p>
<h3>EAPI int ecore_x_xfixes_query (void)</h3>
<p>Return whether the X server supports the Fixes Extension. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X Fixes Extension is available, 0 otherwise.</dl>
<p> Return 1 if the X server supports the Fixes Extension version 3.0, 0 otherwise.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
