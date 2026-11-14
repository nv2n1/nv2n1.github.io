---
title: "edje(3)"
name: "edje"
section: "3"
letter: "e"
url: "/docs/linux/man/3-edje/"
description: "edje.c – Edje Graphical Design Library."
---

<h2 class="name">NAME</h2>
<p> edje.c &#8211; Edje Graphical Design Library. </p>
<h2>SYNOPSIS</h2>
<h3>Functions</h3>
<p> EAPI int <code>edje_init</code> (void)<br />
 <i>Initialize the EDJE library. </i><br />
 EAPI int <code>edje_shutdown</code> (void)<br />
 <i>Shutdown the EDJE library. </i><br />
 EAPI void <code>edje_frametime_set</code> (double t)<br />
 <i>Set the frametime. </i><br />
 EAPI double <code>edje_frametime_get</code> (void)<br />
 <i>Get the frametime. </i><br />
 EAPI void <code>edje_freeze</code> (void)<br />
 <i>Freeze all Edje objects in the current process. </i><br />
 EAPI void <code>edje_thaw</code> (void)<br />
 <i>Thaw all Edje objects in the current process. </i><br />
 EAPI Evas_List * <code>edje_file_collection_list</code> (const char *file)<br />
 <i>Get a list of groups in an edje file. </i><br />
 EAPI void <code>edje_file_collection_list_free</code> (Evas_List *lst)<br />
 <i>Free file collection list. </i><br />
 EAPI int <code>edje_file_group_exists</code> (const char *file, const char *glob)<br />
 <i>Determine whether a group matching glob exists in an edje file. </i><br />
 EAPI char * <code>edje_file_data_get</code> (const char *file, const char *key)<br />
 <i>Get data from the file level data block of an edje file. </i><br />
 EAPI void <code>edje_color_class_set</code> (const char *color_class, int r, int g, int b, int a, int r2, int g2, int b2, int a2, int r3, int g3, int b3, int a3)<br />
 <i>Set Edje color class. </i><br />
 EAPI void <code>edje_color_class_del</code> (const char *color_class) </p>
<p> EAPI Evas_List * <code>edje_color_class_list</code> (void)<br />
 <i>Lists all color classes known about by the current process. </i><br />
 EAPI void <code>edje_text_class_set</code> (const char *text_class, const char *font, Evas_Font_Size size)<br />
 <i>Set the Edje text class. </i><br />
 EAPI void <code>edje_text_class_del</code> (const char *text_class) </p>
<p> EAPI Evas_List * <code>edje_text_class_list</code> (void)<br />
 <i>Lists all text classes known about by the current process. </i><br />
 EAPI void <code>edje_extern_object_min_size_set</code> (Evas_Object *obj, Evas_Coord minw, Evas_Coord minh)<br />
 <i>Set the object minimum size. </i><br />
 EAPI void <code>edje_extern_object_max_size_set</code> (Evas_Object *obj, Evas_Coord maxw, Evas_Coord maxh)<br />
 <i>Set the object maximum size. </i><br />
 EAPI void <code>edje_extern_object_aspect_set</code> (Evas_Object *obj, Edje_Aspect_Control aspect, Evas_Coord aw, Evas_Coord ah)<br />
 <i>Set the object aspect size. </i><br />
 EAPI Evas_Object * <code>edje_object_add</code> (Evas *evas)<br />
 <i>Constructs the Edje object. </i><br />
 EAPI const char * <code>edje_object_data_get</code> (const Evas_Object *obj, const char *key)<br />
 <i>Get Edje object data. </i><br />
 EAPI int <code>edje_object_file_set</code> (Evas_Object *obj, const char *file, const char *group)<br />
 <i>Sets the EET file and group to load obj</i> from.<br />
 EAPI void <code>edje_object_file_get</code> (const Evas_Object *obj, const char **file, const char **group)<br />
 <i>Get the file and group name that obj</i> was loaded from.<br />
 EAPI int <code>edje_object_load_error_get</code> (const Evas_Object *obj)<br />
 <i>Gets the Edje load error. </i><br />
 EAPI void <code>edje_object_signal_emit</code> (Evas_Object *obj, const char *emission, const char *source)<br />
 <i>Send a signal to the Edje object. </i><br />
 EAPI void <code>edje_object_play_set</code> (Evas_Object *obj, int play)<br />
 <i>Set the Edje to play or pause. </i><br />
 EAPI int <code>edje_object_play_get</code> (const Evas_Object *obj)<br />
 <i>Get the Edje play/pause state. </i><br />
 EAPI void <code>edje_object_animation_set</code> (Evas_Object *obj, int on)<br />
 <i>Set Animation state. </i><br />
 EAPI int <code>edje_object_animation_get</code> (const Evas_Object *obj)<br />
 <i>Get the animation state. </i><br />
 EAPI int <code>edje_object_freeze</code> (Evas_Object *obj)<br />
 <i>Freeze object. </i><br />
 EAPI int <code>edje_object_thaw</code> (Evas_Object *obj)<br />
 <i>Thaw object. </i><br />
 EAPI void <code>edje_object_color_class_set</code> (Evas_Object *obj, const char *color_class, int r, int g, int b, int a, int r2, int g2, int b2, int a2, int r3, int g3, int b3, int a3)<br />
 <i>Sets the object color class. </i><br />
 EAPI void <code>edje_object_color_class_del</code> (Evas_Object *obj, const char *color_class) </p>
<p> EAPI void <code>edje_object_text_class_set</code> (Evas_Object *obj, const char *text_class, const char *font, Evas_Font_Size size)<br />
 <i>Sets Edje text class. </i><br />
 EAPI void <code>edje_object_size_min_get</code> (const Evas_Object *obj, Evas_Coord *minw, Evas_Coord *minh)<br />
 <i>Get the minimum size for an object. </i><br />
 EAPI void <code>edje_object_size_max_get</code> (const Evas_Object *obj, Evas_Coord *maxw, Evas_Coord *maxh)<br />
 <i>Get the maximum size for an object. </i><br />
 EAPI void <code>edje_object_calc_force</code> (Evas_Object *obj)<br />
 <i>Force a Size/Geometry calculation. </i><br />
 EAPI void <code>edje_object_size_min_calc</code> (Evas_Object *obj, Evas_Coord *minw, Evas_Coord *minh)<br />
 <i>Calculate minimum size. </i><br />
 EAPI void <code>edje_object_size_min_restricted_calc</code> (Evas_Object *obj, Evas_Coord *minw, Evas_Coord *minh, Evas_Coord restrictedw, Evas_Coord restrictedh)<br />
 <i>Calculate minimum size. </i><br />
 EAPI int <code>edje_object_part_exists</code> (const Evas_Object *obj, const char *part)<br />
 <i>Check if Edje part exists. </i><br />
 EAPI const Evas_Object * <code>edje_object_part_object_get</code> (const Evas_Object *obj, const char *part)<br />
 <i>Gets the Evas_Object corresponding to a given part. </i><br />
 EAPI void <code>edje_object_part_geometry_get</code> (const Evas_Object *obj, const char *part, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Get the geometry of an Edje part. </i><br />
 EAPI void <code>edje_object_part_text_set</code> (Evas_Object *obj, const char *part, const char *text)<br />
 <i>Sets the text for an object part. </i><br />
 EAPI const char * <code>edje_object_part_text_get</code> (const Evas_Object *obj, const char *part)<br />
 <i>Returns the text of the object part. </i><br />
 EAPI void <code>edje_object_part_swallow</code> (Evas_Object *obj, const char *part, Evas_Object *obj_swallow)<br />
 <i>Swallows an object into the edje. </i><br />
 EAPI void <code>edje_object_part_unswallow</code> (Evas_Object *obj, Evas_Object *obj_swallow)<br />
 <i>Unswallow an object. </i><br />
 EAPI Evas_Object * <code>edje_object_part_swallow_get</code> (const Evas_Object *obj, const char *part)<br />
 <i>Get the object currently swallowed by a part. </i><br />
 EAPI const char * <code>edje_object_part_state_get</code> (const Evas_Object *obj, const char *part, double *val_ret)<br />
 <i>Returns the state of the Edje part. </i><br />
 EAPI int <code>edje_object_part_drag_dir_get</code> (const Evas_Object *obj, const char *part)<br />
 <i>Determine dragable directions. </i><br />
 EAPI void <code>edje_object_part_drag_value_set</code> (Evas_Object *obj, const char *part, double dx, double dy)<br />
 <i>Set the dragable object location. </i><br />
 EAPI void <code>edje_object_part_drag_value_get</code> (const Evas_Object *obj, const char *part, double *dx, double *dy)<br />
 <i>Get the dragable object location. </i><br />
 EAPI void <code>edje_object_part_drag_size_set</code> (Evas_Object *obj, const char *part, double dw, double dh)<br />
 <i>Set the dragable object size. </i><br />
 EAPI void <code>edje_object_part_drag_size_get</code> (const Evas_Object *obj, const char *part, double *dw, double *dh)<br />
 <i>Get the dragable object size. </i><br />
 EAPI void <code>edje_object_part_drag_step_set</code> (Evas_Object *obj, const char *part, double dx, double dy)<br />
 <i>Sets the drag step increment. </i><br />
 EAPI void <code>edje_object_part_drag_step_get</code> (const Evas_Object *obj, const char *part, double *dx, double *dy)<br />
 <i>Gets the drag step increment values. </i><br />
 EAPI void <code>edje_object_part_drag_page_set</code> (Evas_Object *obj, const char *part, double dx, double dy)<br />
 <i>Sets the page step increments. </i><br />
 EAPI void <code>edje_object_part_drag_page_get</code> (const Evas_Object *obj, const char *part, double *dx, double *dy)<br />
 <i>Gets the page step increments. </i><br />
 EAPI void <code>edje_object_part_drag_step</code> (Evas_Object *obj, const char *part, double dx, double dy)<br />
 <i>Steps the dragable x,y steps. </i><br />
 EAPI void <code>edje_object_part_drag_page</code> (Evas_Object *obj, const char *part, double dx, double dy)<br />
 <i>Pages x,y steps. </i><br />
 EAPI void <code>edje_object_signal_callback_add</code> (Evas_Object *obj, const char *emission, const char *source, void(*func)(void *data, Evas_Object *o, const char *emission, const char *source), void *data)<br />
 <i>Add a callback for a signal emitted by obj</i>.<br />
 EAPI void * <code>edje_object_signal_callback_del</code> (Evas_Object *obj, const char *emission, const char *source, void(*func)(void *data, Evas_Object *o, const char *emission, const char *source))<br />
 <i>Remove a callback from an object. </i></p>
<h2>Detailed Description</h2>
<p> Edje Graphical Design Library. </p>
<p> These routines are used for Edje.</p>
<h2>Function Documentation</h2>
<h3>void edje_color_class_del (const char * color_class)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>color_class</i> Deletes any values at the process level for the specified color class.</dl>
<h3>Evas_List * edje_color_class_list (void)</h3>
<p> Lists all color classes known about by the current process. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A list of color class names (strings). These strings and the list must be free()&#8217;d by the caller.</dl>
<h3>EAPI void edje_color_class_set (const char * color_class, int r, int g, int b, int a, int r2, int g2, int b2, int a2, int r3, int g3, int b3, int a3)</h3>
<p> Set Edje color class. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>color_class</i><br />
 <i>r</i> Object Red value<br />
 <i>g</i> Object Green value<br />
 <i>b</i> Object Blue value<br />
 <i>a</i> Object Alpha value<br />
 <i>r2</i> Outline Red value<br />
 <i>g2</i> Outline Green value<br />
 <i>b2</i> Outline Blue value<br />
 <i>a2</i> Outline Alpha value<br />
 <i>r3</i> Shadow Red value<br />
 <i>g3</i> Shadow Green value<br />
 <i>b3</i> Shadow Blue value<br />
 <i>a3</i> Shadow Alpha value</dl>
<p> Sets the color values for a process level color class. This will cause all edje parts in the current process that have the specified color class to have their colors multiplied by these values. (Object level color classes set by <code>edje_object_color_class_set()</code> will override the values set by this function). </p>
<p> The first color is the object, the second is the text outline, and the third is the text shadow. (Note that the second two only apply to text parts)</p>
<h3>EAPI void edje_extern_object_aspect_set (Evas_Object * obj, Edje_Aspect_Control aspect, Evas_Coord aw, Evas_Coord ah)</h3>
<p> Set the object aspect size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>aspect</i> The aspect control axes<br />
 <i>aw</i> The aspect radio width<br />
 <i>ah</i> The aspect ratio height</dl>
<p> This sets the desired aspect ratio to keep an object that will be swallowed by Edje. The width and height define a preferred size ASPECT and the object may be scaled to be larger or smaller, but retaining the relative scale of both aspect width and height.</p>
<h3>EAPI void edje_extern_object_max_size_set (Evas_Object * obj, Evas_Coord maxw, Evas_Coord maxh)</h3>
<p> Set the object maximum size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>maxw</i> The maximum width<br />
 <i>maxh</i> The maximum height</dl>
<p> This sets the maximum size restriction for the object.</p>
<h3>EAPI void edje_extern_object_min_size_set (Evas_Object * obj, Evas_Coord minw, Evas_Coord minh)</h3>
<p> Set the object minimum size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>minw</i> The minimum width<br />
 <i>minh</i> The minimum height</dl>
<p> This sets the minimum size restriction for the object.</p>
<h3>EAPI Evas_List * edje_file_collection_list (const char * file)</h3>
<p> Get a list of groups in an edje file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>file</i> The path to the edje file</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The Evas_List of group names (char *)</dl>
<p> Note: the list must be freed using <code>edje_file_collection_list_free()</code> when you are done with it.</p>
<h3>EAPI void edje_file_collection_list_free (Evas_List * lst)</h3>
<p> Free file collection list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>lst</i> The Evas_List of groups</dl>
<p> Frees the list returned by <code>edje_file_collection_list()</code>.</p>
<h3>EAPI char * edje_file_data_get (const char * file, const char * key)</h3>
<p> Get data from the file level data block of an edje file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>file</i> The path to the .edj file<br />
 <i>key</i> The data key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The string value of the data</dl>
<p> If an edje file is built from the following edc: </p>
<p> data { item: &#8216;key1&#8217; &#8216;value1&#8217;; item: &#8216;key2&#8217; &#8216;value2&#8217;; } collections { &#8230; } </p>
<p> Then, edje_file_data_get(&#8216;key1&#8217;) will return &#8216;value1&#8217;</p>
<h3>EAPI int edje_file_group_exists (const char * file, const char * glob)</h3>
<p> Determine whether a group matching glob exists in an edje file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>file</i> The file path<br />
 <i>glob</i> A glob to match on</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if a match is found, 0 otherwise</dl>
<h3>EAPI double edje_frametime_get (void)</h3>
<p> Get the frametime. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The frametime</dl>
<p> Returns the frametime in seconds, by default this is 1/30.</p>
<h3>EAPI void edje_frametime_set (double t)</h3>
<p> Set the frametime. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>t</i> The frametime</dl>
<p> Sets the global frametime in seconds, by default this is 1/30.</p>
<h3>EAPI void edje_freeze (void)</h3>
<p> Freeze all Edje objects in the current process. </p>
<p> See <code>edje_object_freeze()</code> for more. </p>
<p> References edje_object_freeze().</p>
<h3>EAPI int edje_init (void)</h3>
<p> Initialize the EDJE library. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The new init count.</dl>
<h3>EAPI Evas_Object * edje_object_add (Evas * evas)</h3>
<p> Constructs the Edje object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>evas</i> A valid Evas handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The Evas_Object pointer.</dl>
<p> Creates the Edje smart object, returning the Evas_Object handle.</p>
<h3>EAPI int edje_object_animation_get (const Evas_Object * obj)</h3>
<p> Get the animation state. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on Error or if not animated </p>
<p>&nbsp;<wbr>1 if animated&nbsp;<wbr></dl>
<h3>EAPI void edje_object_animation_set (Evas_Object * obj, int on)</h3>
<p> Set Animation state. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>on</i> Animation State</dl>
<p> Stop or start an Edje animation.</p>
<h3>EAPI void edje_object_calc_force (Evas_Object * obj)</h3>
<p> Force a Size/Geometry calculation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle</dl>
<p> Forces the object obj to recalculation layout regardless of freeze/thaw.</p>
<h3>void edje_object_color_class_del (Evas_Object * obj, const char * color_class)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>color_class</i> Deletes any values at the object level for the specified object and color class.</dl>
<h3>EAPI void edje_object_color_class_set (Evas_Object * obj, const char * color_class, int r, int g, int b, int a, int r2, int g2, int b2, int a2, int r3, int g3, int b3, int a3)</h3>
<p> Sets the object color class. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>color_class</i><br />
 <i>r</i> Object Red value<br />
 <i>g</i> Object Green value<br />
 <i>b</i> Object Blue value<br />
 <i>a</i> Object Alpha value<br />
 <i>r2</i> Outline Red value<br />
 <i>g2</i> Outline Green value<br />
 <i>b2</i> Outline Blue value<br />
 <i>a2</i> Outline Alpha value<br />
 <i>r3</i> Shadow Red value<br />
 <i>g3</i> Shadow Green value<br />
 <i>b3</i> Shadow Blue value<br />
 <i>a3</i> Shadow Alpha value</dl>
<p> Sets the color values for an object level color class. This will cause all edje parts in the specified object that have the specified color class to have their colors multiplied by these values. </p>
<p> The first color is the object, the second is the text outline, and the third is the text shadow. (Note that the second two only apply to text parts)</p>
<h3>EAPI const char * edje_object_data_get (const Evas_Object * obj, const char * key)</h3>
<p> Get Edje object data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>key</i> The data key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The data string</dl>
<p> This fetches data specified at the object level. </p>
<p> In EDC this comes from a data block within the group block that <i>obj</i> was loaded from. E.g. </p>
<pre><code>
collections
{
    group
    {
    name:
        'a_group';
        data
        {
        item:
            'key1' 'value1';
        item:
            'key2' 'value2';
        }
    }
}
</code></pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void edje_object_file_get (const Evas_Object * obj, const char ** file, const char ** group)</h3>
<p> Get the file and group name that <i>obj</i> was loaded from. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>file</i> A pointer to store a pointer to the filename in<br />
 <i>group</i> A pointer to store a pointer to the group name in</dl>
<p> This gets the EET file location and group for the given Evas_Object. If <i>obj</i> is either not an edje file, or has not had its file/group set using <code>edje_object_file_set()</code>, then both <i>file</i> and <i>group</i> will be set to NULL. </p>
<p> It is valid to pass in NULL for either <i>file</i> or <i>group</i> if you are not interested in one of the values.</p>
<h3>EAPI int edje_object_file_set (Evas_Object * obj, const char * file, const char * group)</h3>
<p> Sets the EET file and group to load <i>obj</i> from. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>file</i> The path to the EET file<br />
 <i>group</i> The group name in the Edje</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on Error </p>
<p>&nbsp;<wbr>1 on Success and sets EDJE_LOAD_ERROR_NONE</dl>
<p> Edje uses EET files, conventionally ending in .edj, to store object descriptions. A single file contains multiple named groups. This function specifies the file and group name to load <i>obj</i> from.</p>
<h3>EAPI int edje_object_freeze (Evas_Object * obj)</h3>
<p> Freeze object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The frozen state </p>
<p>&nbsp;<wbr>0 on Error</dl>
<p> This puts all changes on hold. Successive freezes will nest, requiring an equal number of thaws. </p>
<p> Referenced by edje_freeze().</p>
<h3>EAPI int edje_object_load_error_get (const Evas_Object * obj)</h3>
<p> Gets the Edje load error. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The Edje load error: </p>
<p>&nbsp;<wbr>0: No Error </p>
<p>&nbsp;<wbr>1: Generic Error </p>
<p>&nbsp;<wbr>2: Does not Exist </p>
<p>&nbsp;<wbr>3: Permission Denied </p>
<p>&nbsp;<wbr>4: Resource Allocation Failed </p>
<p>&nbsp;<wbr>5: Corrupt File </p>
<p>&nbsp;<wbr>6: Unknown Format </p>
<p>&nbsp;<wbr>7: Incompatible File&nbsp;<wbr></dl>
<h3>EAPI int edje_object_part_drag_dir_get (const Evas_Object * obj, const char * part)</h3>
<p> Determine dragable directions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0: Not dragable </p>
<p>&nbsp;<wbr>1: Dragable in X direction </p>
<p>&nbsp;<wbr>2: Dragable in Y direction </p>
<p>&nbsp;<wbr>3: Dragable in X&nbsp;<wbr>&amp;&nbsp;<wbr>Y directions&nbsp;<wbr></dl>
<h3>EAPI void edje_object_part_drag_page (Evas_Object * obj, const char * part, double dx, double dy)</h3>
<p> Pages x,y steps. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dx</i> The x step<br />
 <i>dy</i> The y step</dl>
<p> Pages x,y where the increment is defined by edje_object_part_drag_page_set. </p>
<p>&nbsp;<wbr>WARNING: Paging is bugged!&nbsp;<wbr></p>
<h3>EAPI void edje_object_part_drag_page_get (const Evas_Object * obj, const char * part, double * dx, double * dy)</h3>
<p> Gets the page step increments. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dx</i> The dx page increment pointer<br />
 <i>dy</i> The dy page increment pointer</dl>
<p> Gets the x,y page step increments for the dragable object.</p>
<h3>EAPI void edje_object_part_drag_page_set (Evas_Object * obj, const char * part, double dx, double dy)</h3>
<p> Sets the page step increments. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dx</i> The x page step increment<br />
 <i>dy</i> The y page step increment</dl>
<p> Sets the x,y page step increment values.</p>
<h3>EAPI void edje_object_part_drag_size_get (const Evas_Object * obj, const char * part, double * dw, double * dh)</h3>
<p> Get the dragable object size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dw</i> The drag width pointer<br />
 <i>dh</i> The drag height pointer</dl>
<p> Gets the dragable object size.</p>
<h3>EAPI void edje_object_part_drag_size_set (Evas_Object * obj, const char * part, double dw, double dh)</h3>
<p> Set the dragable object size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dw</i> The drag width<br />
 <i>dh</i> The drag height</dl>
<p> Sets the size of the dragable object.</p>
<h3>EAPI void edje_object_part_drag_step (Evas_Object * obj, const char * part, double dx, double dy)</h3>
<p> Steps the dragable x,y steps. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dx</i> The x step<br />
 <i>dy</i> The y step</dl>
<p> Steps x,y where the step increment is the amount set by edje_object_part_drag_step_set.</p>
<h3>EAPI void edje_object_part_drag_step_get (const Evas_Object * obj, const char * part, double * dx, double * dy)</h3>
<p> Gets the drag step increment values. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part<br />
 <i>dx</i> The x step increment pointer<br />
 <i>dy</i> The y step increment pointer</dl>
<p> Gets the x and y step increments for the dragable object.</p>
<h3>EAPI void edje_object_part_drag_step_set (Evas_Object * obj, const char * part, double dx, double dy)</h3>
<p> Sets the drag step increment. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dx</i> The x step ammount<br />
 <i>dy</i> The y step ammount</dl>
<p> Sets the x,y step increments for a dragable object.</p>
<h3>EAPI void edje_object_part_drag_value_get (const Evas_Object * obj, const char * part, double * dx, double * dy)</h3>
<p> Get the dragable object location. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dx</i> The X value pointer<br />
 <i>dy</i> The Y value pointer</dl>
<p> Gets the drag location values.</p>
<h3>EAPI void edje_object_part_drag_value_set (Evas_Object * obj, const char * part, double dx, double dy)</h3>
<p> Set the dragable object location. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>dx</i> The x value<br />
 <i>dy</i> The y value</dl>
<p> Places the dragable object at the given location.</p>
<h3>EAPI int edje_object_part_exists (const Evas_Object * obj, const char * part)</h3>
<p> Check if Edje part exists. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name to check</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on Error </p>
<p>&nbsp;<wbr>1 if Edje part exists&nbsp;<wbr></dl>
<h3>EAPI void edje_object_part_geometry_get (const Evas_Object * obj, const char * part, Evas_Coord * x, Evas_Coord * y, Evas_Coord * w, Evas_Coord * h)</h3>
<p> Get the geometry of an Edje part. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The Edje part<br />
 <i>x</i> The x coordinate pointer<br />
 <i>y</i> The y coordinate pointer<br />
 <i>w</i> The width pointer<br />
 <i>h</i> The height pointer</dl>
<p> Gets the geometry of an Edje part </p>
<p> It is valid to pass NULL as any of <i>x</i>, <i>y</i>, <i>w</i> or <i>h</i>, whose values you are uninterested in.</p>
<h3>EAPI const Evas_Object * edje_object_part_object_get (const Evas_Object * obj, const char * part)</h3>
<p> Gets the Evas_Object corresponding to a given part. </p>
<p> You should never modify the state of the returned object (with evas_object_move() or evas_object_hide() for example), but you can safely query info about its current state (with evas_object_visible_get() or evas_object_color_get() for example) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The Edje part</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns the Evas_Object corresponding to the given part, or NULL on failure (if the part doesn&#8217;t exist)</dl>
<h3>EAPI const char * edje_object_part_state_get (const Evas_Object * obj, const char * part, double * val_ret)</h3>
<p> Returns the state of the Edje part. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>val_ret</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The part state: </p>
<p>&nbsp;<wbr>&#8216;default&#8217;&nbsp;<wbr>for the default state </p>
<p>&nbsp;<wbr>&#8221;&nbsp;<wbr>for other states&nbsp;<wbr></dl>
<h3>EAPI void edje_object_part_swallow (Evas_Object * obj, const char * part, Evas_Object * obj_swallow)</h3>
<p> Swallows an object into the edje. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name<br />
 <i>obj_swallow</i> The object to swallow</dl>
<p> Swallows the object into the edje part so that all geometry changes for the part affect the swallowed object. (e.g. resize, move, show, raise/lower, etc.). </p>
<p> If an object has already been swallowed into this part, then it will first be unswallowed before the new object is swallowed.</p>
<h3>EAPI Evas_Object * edje_object_part_swallow_get (const Evas_Object * obj, const char * part)</h3>
<p> Get the object currently swallowed by a part. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The swallowed object, or NULL if there is none.</dl>
<h3>EAPI const char * edje_object_part_text_get (const Evas_Object * obj, const char * part)</h3>
<p> Returns the text of the object part. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>part</i> The part name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The text string</dl>
<h3>EAPI void edje_object_part_text_set (Evas_Object * obj, const char * part, const char * text)</h3>
<p> Sets the text for an object part. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas Object handle<br />
 <i>part</i> The part name<br />
 <i>text</i> The text string</dl>
<h3>EAPI void edje_object_part_unswallow (Evas_Object * obj, Evas_Object * obj_swallow)</h3>
<p> Unswallow an object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>obj_swallow</i> The swallowed object</dl>
<p> Causes the edje to regurgitate a previously swallowed object. :)</p>
<h3>EAPI int edje_object_play_get (const Evas_Object * obj)</h3>
<p> Get the Edje play/pause state. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 if Edje not connected, Edje delete_me, or Edje paused </p>
<p>&nbsp;<wbr>1 if Edje set to play&nbsp;<wbr></dl>
<h3>EAPI void edje_object_play_set (Evas_Object * obj, int play)</h3>
<p> Set the Edje to play or pause. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>play</i> Play instruction (1 to play, 0 to pause)</dl>
<p> This sets the Edje to play or pause depending on the parameter. This has no effect if the Edje is already in that state.</p>
<h3>EAPI void edje_object_signal_callback_add (Evas_Object * obj, const char * emission, const char * source, void(*)(void *data, Evas_Object *o, const char *emission, const char *source) func, void * data)</h3>
<p> Add a callback for a signal emitted by <i>obj</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>emission</i> The signal name<br />
 <i>source</i> The signal source<br />
 <i>func</i> The callback function to be executed when the signal is emitted<br />
 <i>data</i> A pointer to data to pass in to the callback function</dl>
<p> Connects a callback function to a signal emitted by <i>obj</i>. In EDC, a program can emit a signal as follows: </p>
<p>program<br />
{<br />
name:<br />
    &#8217;emit_example&#8217;;<br />
action:<br />
    SIGNAL_EMIT &#8216;a_signal&#8217; &#8216;a_source&#8217;;<br />
}</p>
<p> Assuming a function with the following declaration is definded: </p>
<p>void cb_signal(void *data, Evas_Object *o, const char *emission, const char *source);</p>
<p> a callback is attached using: </p>
<pre>
 edje_object_callback_add(obj, 'a_signal', 'a_source', cb_signal, data);
</pre>
<p> Here, <i>data</i> is an arbitrary pointer to be used as desired. Note that <i>emission</i> and <i>source</i> correspond respectively to first and second parameters to the SIGNAL_EMIT action. </p>
<p> Internal edje signals can also be attached to, and globs can be in either the emission or source name. e.g. </p>
<p>edje_object_callback_add(obj, &#8216;mouse,down,*&#8217;, &#8216;button.*&#8217;, NULL);</p>
<p> Here, any mouse down events on an edje part whose name begins with &#8216;button.&#8217; will trigger the callback. The actual signal and source name will be passed in to the <i>emission</i> and <i>source</i> parameters of the callback function. (e.g. &#8216;mouse,down,2&#8217; and &#8216;button.close&#8217;).</p>
<h3>EAPI void* edje_object_signal_callback_del (Evas_Object * obj, const char * emission, const char * source, void(*)(void *data, Evas_Object *o, const char *emission, const char *source) func)</h3>
<p> Remove a callback from an object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>emission</i> the emission string<br />
 <i>source</i> the source string<br />
 <i>func</i> the callback function</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the data pointer</dl>
<p> Removes a callback from an object. The parameters <i>emission</i>, <i>source</i> and <i>func</i> must match exactly those passed to a previous call to <code>edje_object_signal_callback_add()</code>. The data pointer that was passed to this call will be returned.</p>
<h3>EAPI void edje_object_signal_emit (Evas_Object * obj, const char * emission, const char * source)</h3>
<p> Send a signal to the Edje object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A vaild Evas_Object handle<br />
 <i>emission</i> The signal<br />
 <i>source</i> The signal source</dl>
<p> This sends a signal to the edje object. </p>
<p> An edje program can respond to a signal by specifying matching &#8216;signal&#8217; and &#8216;source&#8217; fields. </p>
<p> E.g. </p>
<pre>
 edje_object_signal_emit(obj, 'a_signal', '');
</pre>
<p> will trigger a program whose edc is: </p>
<pre><code>
program
{
name:
    'a_program';
signal:
    'a_signal';
source:
    '';
action:
    ...
}
</code></pre>
<p> FIXME should this signal be sent to children also?</p>
<h3>EAPI void edje_object_size_max_get (const Evas_Object * obj, Evas_Coord * maxw, Evas_Coord * maxh)</h3>
<p> Get the maximum size for an object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>maxw</i> Maximum width pointer<br />
 <i>maxh</i> Maximum height pointer</dl>
<p> Gets the object&#8217;s maximum size values from the Edje. These are set to zero if no Edje is connected to the Evas Object.</p>
<h3>EAPI void edje_object_size_min_calc (Evas_Object * obj, Evas_Coord * minw, Evas_Coord * minh)</h3>
<p> Calculate minimum size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>minw</i> Minimum width pointer<br />
 <i>minh</i> Minimum height pointer</dl>
<p> Calculates the object&#8217;s minimum size ?! </p>
<p> References edje_object_size_min_restricted_calc().</p>
<h3>EAPI void edje_object_size_min_get (const Evas_Object * obj, Evas_Coord * minw, Evas_Coord * minh)</h3>
<p> Get the minimum size for an object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>minw</i> Minimum width pointer<br />
 <i>minh</i> Minimum height pointer</dl>
<p> Gets the object&#8217;s minimum size values from the Edje. These are set to zero if no Edje is connected to the Evas Object.</p>
<h3>EAPI void edje_object_size_min_restricted_calc (Evas_Object * obj, Evas_Coord * minw, Evas_Coord * minh, Evas_Coord restrictedw, Evas_Coord restrictedh)</h3>
<p> Calculate minimum size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>minw</i> Minimum width pointer<br />
 <i>minh</i> Minimum height pointer<br />
 <i>restrictedw</i> Do not allow object min width calc to be less than this<br />
 <i>restrictedh</i> Do not allow object min height calc to be less than this</dl>
<p> Calculates the object&#8217;s minimum size ?! </p>
<p> Referenced by edje_object_size_min_calc().</p>
<h3>EAPI void edje_object_text_class_set (Evas_Object * obj, const char * text_class, const char * font, Evas_Font_Size size)</h3>
<p> Sets Edje text class. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle<br />
 <i>text_class</i> The text class name<br />
 <i>font</i> Font name<br />
 <i>size</i> Font Size</dl>
<p> Sets the text class for the Edje.</p>
<h3>EAPI int edje_object_thaw (Evas_Object * obj)</h3>
<p> Thaw object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>obj</i> A valid Evas_Object handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The frozen state </p>
<p>&nbsp;<wbr>0 on Error</dl>
<p> This allows frozen changes to occur. </p>
<p> Referenced by edje_thaw().</p>
<h3>EAPI int edje_shutdown (void)</h3>
<p> Shutdown the EDJE library. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The new init count.</dl>
<h3>void edje_text_class_del (const char * text_class)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>text_class</i> Deletes any values at the process level for the specified text class.</dl>
<h3>Evas_List * edje_text_class_list (void)</h3>
<p> Lists all text classes known about by the current process. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A list of text class names (strings). These strings are stringshares and the list must be free()&#8217;d by the caller.</dl>
<h3>EAPI void edje_text_class_set (const char * text_class, const char * font, Evas_Font_Size size)</h3>
<p> Set the Edje text class. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>text_class</i> The text class name ?!<br />
 <i>font</i> The font name<br />
 <i>size</i> The font size</dl>
<p> This sets updates all edje members which belong to this text class with the new font attributes.</p>
<h3>EAPI void edje_thaw (void)</h3>
<p> Thaw all Edje objects in the current process. </p>
<p> See <code>edje_object_thaw()</code> for more. </p>
<p> References edje_object_thaw().</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Edje from the source code. </p>
<h2>Index</h2>
