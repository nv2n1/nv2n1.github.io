---
title: "evas_object_gradient_group(3)"
name: "evas_object_gradient_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_gradient_group/"
description: "Evas Gradient Object Functions – Functions that work on evas gradient objects."
---

<p>Evas Gradient Object Functions &#8211; Functions that work on evas gradient objects. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_Object</code> * <code>evas_object_gradient_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a gradient object to the given evas. </i><br />
 EAPI void <code>evas_object_gradient_color_stop_add</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a, int delta)<br />
 <i>Adds a color stop to the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_alpha_stop_add</code> (<code>Evas_Object</code> *obj, int a, int delta)<br />
 <i>Adds an alpha stop to the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_clear</code> (<code>Evas_Object</code> *obj)<br />
 <i>Deletes all stops set for the given evas gradient object or any set data. </i><br />
 EAPI void <code>evas_object_gradient_color_data_set</code> (<code>Evas_Object</code> *obj, void *data, int len, Evas_Bool has_alpha)<br />
 <i>Sets color data for the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_alpha_data_set</code> (<code>Evas_Object</code> *obj, void *data, int len)<br />
 <i>Sets alpha data for the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_fill_angle_set</code> (<code>Evas_Object</code> *obj, Evas_Angle angle)<br />
 <i>Sets the angle at which the given evas gradient object&#8217;s fill sits clockwise from vertical. </i><br />
 EAPI Evas_Angle <code>evas_object_gradient_fill_angle_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the angle at which the given evas gradient object&#8217;s fill sits clockwise from the vertical. </i><br />
 EAPI void <code>evas_object_gradient_fill_spread_set</code> (<code>Evas_Object</code> *obj, int spread)<br />
 <i>Sets the tiling mode for the given evas gradient object&#8217;s fill. </i><br />
 EAPI int <code>evas_object_gradient_fill_spread_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spread (tiling mode) for the given gradient object&#8217;s fill. </i><br />
 EAPI void <code>evas_object_gradient_angle_set</code> (<code>Evas_Object</code> *obj, Evas_Angle angle)<br />
 <i>Sets the angle at which the given evas gradient sits, relative to whatever intrinsic orientation of the grad type. </i><br />
 EAPI Evas_Angle <code>evas_object_gradient_angle_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the angle at which the given evas gradient object sits rel to its intrinsic orientation. </i><br />
 EAPI void <code>evas_object_gradient_offset_set</code> (<code>Evas_Object</code> *obj, float offset)<br />
 <i>Sets the offset of the given evas gradient object&#8217;s spectrum. </i><br />
 EAPI float <code>evas_object_gradient_offset_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spectrum&#8217;s offset. </i><br />
 EAPI void <code>evas_object_gradient_direction_set</code> (<code>Evas_Object</code> *obj, int direction)<br />
 <i>Sets the direction of the given evas gradient object&#8217;s spectrum. </i><br />
 EAPI int <code>evas_object_gradient_direction_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the evas gradient object&#8217;s spectrum direction. </i><br />
 EAPI void <code>evas_object_gradient2_color_np_stop_insert</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a, float pos)<br />
 <i>Inserts a color stop to the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient2_clear</code> (<code>Evas_Object</code> *obj)<br />
 <i>Deletes all stops set for the given evas gradient object or any set data. </i><br />
 EAPI void <code>evas_object_gradient2_fill_spread_set</code> (<code>Evas_Object</code> *obj, int spread)<br />
 <i>Sets the tiling mode for the given evas gradient object&#8217;s fill. </i><br />
 EAPI int <code>evas_object_gradient2_fill_spread_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spread (tiling mode) for the given gradient object&#8217;s fill. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_gradient2_linear_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a gradient object to the given evas. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_gradient2_radial_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a gradient object to the given evas. </i></p>
<h2>Detailed Description</h2>
<p>Functions that work on evas gradient objects. </p>
<p> The following example shows how</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_gradient2_clear (<code>Evas_Object</code> * obj)</h3>
<p>Deletes all stops set for the given evas gradient object or any set data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<h3>EAPI void evas_object_gradient2_color_np_stop_insert (<code>Evas_Object</code> * obj, int r, int g, int b, int a, float pos)</h3>
<p>Inserts a color stop to the given evas gradient object. </p>
<p> The pos parameter determines where along the unit interval [0,1] the color is to be inserted. The r,g,b,a data are assumed input as being NON-PREMULTIPLIED. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>r</i> Red component of the given color.<br />
 <i>g</i> Green component of the given color.<br />
 <i>b</i> Blue component of the given color.<br />
 <i>a</i> Alpha component of the given color.<br />
 <i>pos</i> The pos in [0,1] of this stop.</dl>
<h3>EAPI int evas_object_gradient2_fill_spread_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the spread (tiling mode) for the given gradient object&#8217;s fill. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current spread mode of the gradient object.</dl>
<p> References EVAS_TEXTURE_REPEAT.</p>
<h3>EAPI void evas_object_gradient2_fill_spread_set (<code>Evas_Object</code> * obj, int spread)</h3>
<p>Sets the tiling mode for the given evas gradient object&#8217;s fill. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>spread</i> One of EVAS_TEXTURE_REFLECT, EVAS_TEXTURE_REPEAT, EVAS_TEXTURE_RESTRICT, or EVAS_TEXTURE_PAD.</dl>
<h3>EAPI <code>Evas_Object</code>* evas_object_gradient2_linear_add (<code>Evas</code> * e)</h3>
<p>Adds a gradient object to the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new evas gradient object if successful. Otherwise, NULL.</dl>
<h3>EAPI <code>Evas_Object</code>* evas_object_gradient2_radial_add (<code>Evas</code> * e)</h3>
<p>Adds a gradient object to the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new evas gradient object if successful. Otherwise, NULL.</dl>
<h3>EAPI <code>Evas_Object</code>* evas_object_gradient_add (<code>Evas</code> * e)</h3>
<p>Adds a gradient object to the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new evas gradient object if successful. Otherwise, NULL.</dl>
<h3>EAPI void evas_object_gradient_alpha_data_set (<code>Evas_Object</code> * obj, void * data, int len)</h3>
<p>Sets alpha data for the given evas gradient object. </p>
<p> If alpha data is so set, any existing gradient stops will be cleared, The data is not copied, so if it was allocated, do not free it while it&#8217;s set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>data</i> The alpha data to be set, in a8 format.<br />
 <i>len</i> The length of the data pointer &#8211; multiple of the pixel size.</dl>
<h3>EAPI void evas_object_gradient_alpha_stop_add (<code>Evas_Object</code> * obj, int a, int delta)</h3>
<p>Adds an alpha stop to the given evas gradient object. </p>
<p> The delta parameter determines the proportion of the gradient object that is to be set to the alpha value. </p>
<p> Alphas are added from the top downwards. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>a</i> Alpha value.<br />
 <i>delta</i> Proportion of the gradient object that is this alpha.</dl>
<h3>EAPI Evas_Angle evas_object_gradient_angle_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the angle at which the given evas gradient object sits rel to its intrinsic orientation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current angle if successful. 0.0 otherwise.</dl>
<h3>EAPI void evas_object_gradient_angle_set (<code>Evas_Object</code> * obj, Evas_Angle angle)</h3>
<p>Sets the angle at which the given evas gradient sits, relative to whatever intrinsic orientation of the grad type. </p>
<p> Used mostly by &#8216;linear&#8217; kinds of gradients. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>angle</i> Angle in degrees. Can be negative.</dl>
<h3>EAPI void evas_object_gradient_clear (<code>Evas_Object</code> * obj)</h3>
<p>Deletes all stops set for the given evas gradient object or any set data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<h3>EAPI void evas_object_gradient_color_data_set (<code>Evas_Object</code> * obj, void * data, int len, Evas_Bool has_alpha)</h3>
<p>Sets color data for the given evas gradient object. </p>
<p> If data is so set, any existing gradient stops will be deleted, The data is not copied, so if it was allocated, do not free it while it&#8217;s set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>data</i> The color data to be set. Should be in argb32 pixel format.<br />
 <i>len</i> The length of the data pointer &#8211; multiple of the pixel size.<br />
 <i>has_alpha</i> A flag indicating if the data has alpha or not.</dl>
<h3>EAPI void evas_object_gradient_color_stop_add (<code>Evas_Object</code> * obj, int r, int g, int b, int a, int delta)</h3>
<p>Adds a color stop to the given evas gradient object. </p>
<p> The delta parameter determines the proportion of the gradient object that is to be set to the color. For instance, if red is added with delta set to 2, and green is added with delta set to 1, two-thirds will be red or reddish and one-third will be green or greenish. </p>
<p> Colors are added from the top downwards. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>r</i> Red component of the given color.<br />
 <i>g</i> Green component of the given color.<br />
 <i>b</i> Blue component of the given color.<br />
 <i>a</i> Alpha component of the given color.<br />
 <i>delta</i> Proportion of the gradient object that is this color.</dl>
<h3>EAPI int evas_object_gradient_direction_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the evas gradient object&#8217;s spectrum direction. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current gradient direction if successful. 1 otherwise.</dl>
<h3>EAPI void evas_object_gradient_direction_set (<code>Evas_Object</code> * obj, int direction)</h3>
<p>Sets the direction of the given evas gradient object&#8217;s spectrum. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>direction</i> Values are either 1 (the default) or -1.</dl>
<h3>EAPI Evas_Angle evas_object_gradient_fill_angle_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the angle at which the given evas gradient object&#8217;s fill sits clockwise from the vertical. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current angle if successful. 0.0 otherwise.</dl>
<h3>EAPI void evas_object_gradient_fill_angle_set (<code>Evas_Object</code> * obj, Evas_Angle angle)</h3>
<p>Sets the angle at which the given evas gradient object&#8217;s fill sits clockwise from vertical. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>angle</i> Angle in degrees. Can be negative.</dl>
<h3>EAPI int evas_object_gradient_fill_spread_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the spread (tiling mode) for the given gradient object&#8217;s fill. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current spread mode of the gradient object.</dl>
<p> References EVAS_TEXTURE_REFLECT.</p>
<h3>EAPI void evas_object_gradient_fill_spread_set (<code>Evas_Object</code> * obj, int spread)</h3>
<p>Sets the tiling mode for the given evas gradient object&#8217;s fill. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>spread</i> One of EVAS_TEXTURE_REFLECT, EVAS_TEXTURE_REPEAT, EVAS_TEXTURE_RESTRICT, EVAS_TEXTURE_RESTRICT_REFLECT, EVAS_TEXTURE_RESTRICT_REPEAT, or EVAS_TEXTURE_PAD.</dl>
<h3>EAPI float evas_object_gradient_offset_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the spectrum&#8217;s offset. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current gradient offset if successful. 0.0 otherwise.</dl>
<h3>EAPI void evas_object_gradient_offset_set (<code>Evas_Object</code> * obj, float offset)</h3>
<p>Sets the offset of the given evas gradient object&#8217;s spectrum. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas gradient object.<br />
 <i>offset</i> Values can be negative.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
