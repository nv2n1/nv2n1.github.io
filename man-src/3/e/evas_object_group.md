---
title: "evas_object_group(3)"
name: "evas_object_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_group/"
description: "Generic Object Functions – Functions that manipulate generic evas objects."
---

<p>Generic Object Functions &#8211; Functions that manipulate generic evas objects. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_del</code> (<code>Evas_Object</code> *obj)<br />
 <i>Deletes the given evas object and frees its memory. </i><br />
 EAPI void <code>evas_object_move</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y)<br />
 <i>Moves the given evas object to the given location. </i><br />
 EAPI void <code>evas_object_resize</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Changes the size of the given evas object. </i><br />
 EAPI void <code>evas_object_geometry_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the position and rectangular size of the given evas object. </i><br />
 EAPI void <code>evas_object_color_set</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a)<br />
 <i>Sets the general colour of the given evas object to the given colour. </i><br />
 EAPI void <code>evas_object_color_get</code> (const <code>Evas_Object</code> *obj, int *r, int *g, int *b, int *a)<br />
 <i>Retrieves the general colour of the given evas object. </i><br />
 EAPI void <code>evas_object_anti_alias_set</code> (<code>Evas_Object</code> *obj, Evas_Bool anti_alias)<br />
 <i>Sets whether or not the given evas object is to be drawn anti_aliased. </i><br />
 EAPI Evas_Bool <code>evas_object_anti_alias_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether or not the given evas object is to be drawn anti_aliased. </i><br />
 EAPI void <code>evas_object_scale_set</code> (<code>Evas_Object</code> *obj, double scale)<br />
 <i>Sets the scaling factor for an evas object. </i><br />
 EAPI double <code>evas_object_scale_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the scaling factor for the given evas object. </i><br />
 EAPI void <code>evas_object_color_interpolation_set</code> (<code>Evas_Object</code> *obj, int color_space)<br />
 <i>Sets the color_space to be used for linear interpolation of colors. </i><br />
 EAPI int <code>evas_object_color_interpolation_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the current value of the color space used for linear interpolation. </i><br />
 EAPI void <code>evas_object_render_op_set</code> (<code>Evas_Object</code> *obj, Evas_Render_Op render_op)<br />
 <i>Sets the render_op to be used for rendering the evas object. </i><br />
 EAPI Evas_Render_Op <code>evas_object_render_op_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the current value of the operation used for rendering the evas object. </i><br />
 EAPI <code>Evas</code> * <code>evas_object_evas_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the evas that the given evas object is on. </i><br />
 EAPI const char * <code>evas_object_type_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the name of the type of the given evas object. </i><br />
 EAPI void <code>evas_object_precise_is_inside_set</code> (<code>Evas_Object</code> *obj, Evas_Bool precise)<br />
 <i>Set whether to use a precise (usually expensive) point collision detection. </i><br />
 EAPI Evas_Bool <code>evas_object_precise_is_inside_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to use a precise point collision detection. </i></p>
<h2>Detailed Description</h2>
<p>Functions that manipulate generic evas objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI Evas_Bool evas_object_anti_alias_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves whether or not the given evas object is to be drawn anti_aliased. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the object is to be anti_aliased. 0 otherwise.</dl>
<h3>EAPI void evas_object_anti_alias_set (<code>Evas_Object</code> * obj, Evas_Bool anti_alias)</h3>
<p>Sets whether or not the given evas object is to be drawn anti_aliased. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>anti_alias.</i> 1 if the object is to be anti_aliased, 0 otherwise.</dl>
<h3>EAPI void evas_object_color_get (const <code>Evas_Object</code> * obj, int * r, int * g, int * b, int * a)</h3>
<p>Retrieves the general colour of the given evas object. </p>
<p> Note that if any of r, g, b or a are NULL, then the NULL parameters are ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>r</i> Pointer to an integer in which to store the red component of the colour.<br />
 <i>g</i> Pointer to an integer in which to store the green component of the colour.<br />
 <i>b</i> Pointer to an integer in which to store the blue component of the colour.<br />
 <i>a</i> Pointer to an integer in which to store the alpha component of the colour.</dl>
<h3>EAPI int evas_object_color_interpolation_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the current value of the color space used for linear interpolation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>EVAS_COLOR_SPACE_ARGB or EVAS_COLOR_SPACE_AHSV.</dl>
<h3>EAPI void evas_object_color_interpolation_set (<code>Evas_Object</code> * obj, int color_space)</h3>
<p>Sets the color_space to be used for linear interpolation of colors. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>color_space,one</i> of EVAS_COLOR_SPACE_ARGB or EVAS_COLOR_SPACE_AHSV.</dl>
<h3>EAPI void evas_object_color_set (<code>Evas_Object</code> * obj, int r, int g, int b, int a)</h3>
<p>Sets the general colour of the given evas object to the given colour. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>r</i> The red component of the given colour.<br />
 <i>g</i> The green component of the given colour.<br />
 <i>b</i> The blue component of the given colour.<br />
 <i>a</i> The alpha component of the given colour.</dl>
<h3>EAPI void evas_object_del (<code>Evas_Object</code> * obj)</h3>
<p>Deletes the given evas object and frees its memory. </p>
<p> The object&#8217;s &#8216;free&#8217; callback is called when this function is called. If the object currently has the focus, its &#8216;focus out&#8217; callback is also called. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> References EVAS_CALLBACK_DEL, EVAS_CALLBACK_FOCUS_OUT, EVAS_CALLBACK_FREE, evas_object_clip_unset(), evas_object_hide(), and evas_object_name_set().</p>
<h3>EAPI <code>Evas</code>* evas_object_evas_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the evas that the given evas object is on. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The evas that the object is on.</dl>
<h3>EAPI void evas_object_geometry_get (const <code>Evas_Object</code> * obj, Evas_Coord * x, Evas_Coord * y, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Retrieves the position and rectangular size of the given evas object. </p>
<p> Note that if any of x, y, w or h are NULL, the NULL parameters are ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>x</i> Pointer to an integer in which to store the X coordinate of the object.<br />
 <i>y</i> Pointer to an integer in which to store the Y coordinate of the object.<br />
 <i>w</i> Pointer to an integer in which to store the width of the object.<br />
 <i>h</i> Pointer to an integer in which to store the height of the object.</dl>
<p> Referenced by evas_object_smart_move_children_relative().</p>
<h3>EAPI void evas_object_move (<code>Evas_Object</code> * obj, Evas_Coord x, Evas_Coord y)</h3>
<p>Moves the given evas object to the given location. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>x</i> X position to move the object to, in canvas units.<br />
 <i>y</i> Y position to move the object to, in canvas units.</dl>
<p> Referenced by evas_object_smart_move_children_relative().</p>
<h3>EAPI Evas_Bool evas_object_precise_is_inside_get (const <code>Evas_Object</code> * obj)</h3>
<p>Determine whether an object is set to use a precise point collision detection. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given object.</dl>
<h3>EAPI void evas_object_precise_is_inside_set (<code>Evas_Object</code> * obj, Evas_Bool precise)</h3>
<p>Set whether to use a precise (usually expensive) point collision detection. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given object.<br />
 <i>precise</i> wheter to use a precise point collision detection or not The default value is false.</dl>
<h3>EAPI Evas_Render_Op evas_object_render_op_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the current value of the operation used for rendering the evas object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>one of the enumerated values in Evas_Render_Op.</dl>
<p> References EVAS_RENDER_BLEND.</p>
<h3>EAPI void evas_object_render_op_set (<code>Evas_Object</code> * obj, Evas_Render_Op render_op)</h3>
<p>Sets the render_op to be used for rendering the evas object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>render_op</i> one of the Evas_Render_Op values.</dl>
<h3>EAPI void evas_object_resize (<code>Evas_Object</code> * obj, Evas_Coord w, Evas_Coord h)</h3>
<p>Changes the size of the given evas object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>w</i> The new width of the evas object.<br />
 <i>h</i> The new height of the evas object.</dl>
<h3>EAPI double evas_object_scale_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the scaling factor for the given evas object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The scaling factor.</dl>
<h3>EAPI void evas_object_scale_set (<code>Evas_Object</code> * obj, double scale)</h3>
<p>Sets the scaling factor for an evas object. </p>
<p> Does not affect all objects. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>scale.</i> The scaling factor. 1.0 == none.</dl>
<h3>EAPI const char* evas_object_type_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the name of the type of the given evas object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
