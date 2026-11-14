---
title: "evas(3)"
name: "evas"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas/"
description: "Evas.h – These routines are used for Evas library interaction."
---

<p>Evas.h &#8211; These routines are used for Evas library interaction. </p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>_Evas_Transform</code><br />
 <i>An affine or projective coordinate transformation matrix. </i><br />
 struct <code>_Evas_Rectangle</code><br />
 <i>A rectangle. </i><br />
 struct <code>_Evas_Coord_Rectangle</code><br />
 <i>A rectangle in Evas_Coord. </i><br />
 struct <code>_Evas_Smart_Class</code><br />
 <i>a smart object class </i><br />
 struct <code>_Evas_Engine_Info</code><br />
 <i>Generic engine information. </i><br />
 struct <code>_Evas_Event_Mouse_Down</code><br />
 <i>Mouse button press event. </i><br />
 struct <code>_Evas_Event_Mouse_Up</code><br />
 <i>Mouse button release event. </i><br />
 struct <code>_Evas_Event_Mouse_In</code><br />
 <i>Mouse enter event. </i><br />
 struct <code>_Evas_Event_Mouse_Out</code><br />
 <i>Mouse leave event. </i><br />
 struct <code>_Evas_Event_Mouse_Move</code><br />
 <i>Mouse button down event. </i><br />
 struct <code>_Evas_Event_Mouse_Wheel</code><br />
 <i>Wheel event. </i><br />
 struct <code>_Evas_Event_Key_Down</code><br />
 <i>Key press event. </i><br />
 struct <code>_Evas_Event_Key_Up</code><br />
 <i>Key release event. </i><br />
 struct <code>_Evas_Event_Hold</code><br />
 <i>Hold change event. </i></p>
<h3>Defines</h3>
<p>#define <code>EVAS_LOAD_ERROR_NONE</code> 0<br />
 <i>No error on load. </i><br />
 #define <code>EVAS_LOAD_ERROR_GENERIC</code> 1<br />
 <i>A non-specific error occured. </i><br />
 #define <code>EVAS_LOAD_ERROR_DOES_NOT_EXIST</code> 2<br />
 <i>File (or file path) does not exist. </i><br />
 #define <code>EVAS_LOAD_ERROR_PERMISSION_DENIED</code> 3<br />
 <i>Permission deinied to an existing file (or path). </i><br />
 #define <code>EVAS_LOAD_ERROR_RESOURCE_ALLOCATION_FAILED</code> 4<br />
 <i>Allocation of resources failure prevented load. </i><br />
 #define <code>EVAS_LOAD_ERROR_CORRUPT_FILE</code> 5<br />
 <i>File corrupt (but was detected as a known format). </i><br />
 #define <code>EVAS_LOAD_ERROR_UNKNOWN_FORMAT</code> 6<br />
 <i>File is not a known format. </i><br />
 #define <code>EVAS_ALLOC_ERROR_NONE</code> 0<br />
 <i>No allocation error. </i><br />
 #define <code>EVAS_ALLOC_ERROR_FATAL</code> 1<br />
 <i>Allocation failed despite attempts to free up memory. </i><br />
 #define <code>EVAS_ALLOC_ERROR_RECOVERED</code> 2<br />
 <i>Allocation succeeded, but extra memory had to be found by freeing up speculative resources. </i><br />
 #define <code>EVAS_LAYER_MIN</code> -32768<br />
 <i>bottom-most layer number </i><br />
 #define <code>EVAS_LAYER_MAX</code> 32767<br />
 <i>top-most layer number </i><br />
 #define <code>EVAS_PIXEL_FORMAT_NONE</code> 0<br />
 <i>No pixel format. </i><br />
 #define <code>EVAS_PIXEL_FORMAT_ARGB32</code> 1<br />
 <i>ARGB 32bit pixel format with A in the high byte per 32bit pixel word. </i><br />
 #define <code>EVAS_PIXEL_FORMAT_YUV420P_601</code> 2<br />
 <i>YUV 420 Planar format with CCIR 601 color encoding wuth contiguous planes in the order Y, U and V. </i><br />
 #define <code>EVAS_COLOR_SPACE_ARGB</code> 0<br />
 <i>ARGB color space. </i><br />
 #define <code>EVAS_COLOR_SPACE_AHSV</code> 1<br />
 <i>AHSV color space. </i><br />
 #define <code>EVAS_TEXTURE_REFLECT</code> 0<br />
 <i>Gradient and image fill tiling mode &#8211; tiling reflects. </i><br />
 #define <code>EVAS_TEXTURE_REPEAT</code> 1<br />
 <i>tiling repeats </i><br />
 #define <code>EVAS_TEXTURE_RESTRICT</code> 2<br />
 <i>tiling clamps &#8211; range offset ignored </i><br />
 #define <code>EVAS_TEXTURE_RESTRICT_REFLECT</code> 3<br />
 <i>tiling clamps and any range offset reflects </i><br />
 #define <code>EVAS_TEXTURE_RESTRICT_REPEAT</code> 4<br />
 <i>tiling clamps and any range offset repeats </i><br />
 #define <code>EVAS_TEXTURE_PAD</code> 5<br />
 <i>tiling extends with end values </i></p>
<h3>Typedefs</h3>
<p>typedef enum <code>_Evas_Callback_Type</code> <code>Evas_Callback_Type</code><br />
 <i>The type of event to trigger the callback. </i><br />
 typedef enum <code>_Evas_Button_Flags</code> <code>Evas_Button_Flags</code><br />
 <i>Flags for Mouse Button events. </i><br />
 typedef enum <code>_Evas_Event_Flags</code> <code>Evas_Event_Flags</code><br />
 <i>Flags for Events. </i><br />
 typedef enum <code>_Evas_Font_Hinting_Flags</code> <code>Evas_Font_Hinting_Flags</code><br />
 <i>Flags for Font Hinting. </i><br />
 typedef enum <code>_Evas_Colorspace</code> <code>Evas_Colorspace</code><br />
 <i>Colorspaces for pixel data supported by Evas. </i><br />
 typedef struct <code>_Evas_Transform</code> <code>Evas_Transform</code><br />
 <i>An Evas projective or affine transform. </i><br />
 typedef struct <code>_Evas_Rectangle</code> <code>Evas_Rectangle</code><br />
 <i>A generic rectangle handle. </i><br />
 typedef struct <code>_Evas_Coord_Rectangle</code> <code>Evas_Coord_Rectangle</code><br />
 <i>A generic rectangle handle. </i><br />
 typedef struct <code>_Evas_Smart_Class</code> <code>Evas_Smart_Class</code><br />
 <i>A smart object base class. </i><br />
 typedef struct _Evas <code>Evas</code><br />
 <i>An Evas canvas handle. </i><br />
 typedef struct _Evas_Object <code>Evas_Object</code><br />
 <i>An Evas Object handle. </i><br />
 typedef void <code>Evas_Performance</code><br />
 <i>An Evas Performance handle. </i><br />
 typedef struct _Evas_Modifier <code>Evas_Modifier</code><br />
 <i>An Evas Modifier. </i><br />
 typedef struct _Evas_Lock <code>Evas_Lock</code><br />
 <i>An Evas Lock. </i><br />
 typedef struct _Evas_Smart <code>Evas_Smart</code><br />
 <i>An Evas Smart Object handle. </i><br />
 typedef struct _Evas_Native_Surface <code>Evas_Native_Surface</code><br />
 <i>A generic datatype for engine specific native surface information. </i><br />
 typedef unsigned long long <code>Evas_Modifier_Mask</code><br />
 <i>An Evas modifier mask type. </i><br />
 typedef struct _Evas_Pixel_Import_Source <code>Evas_Pixel_Import_Source</code><br />
 <i>A source description of pixels for importing pixels. </i><br />
 typedef struct <code>_Evas_Engine_Info</code> <code>Evas_Engine_Info</code><br />
 <i>A generic Evas Engine information structure. </i><br />
 typedef struct <code>_Evas_Event_Mouse_Down</code> <code>Evas_Event_Mouse_Down</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_MOUSE_DOWN</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Mouse_Up</code> <code>Evas_Event_Mouse_Up</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_MOUSE_UP</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Mouse_In</code> <code>Evas_Event_Mouse_In</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_MOUSE_IN</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Mouse_Out</code> <code>Evas_Event_Mouse_Out</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_MOUSE_OUT</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Mouse_Move</code> <code>Evas_Event_Mouse_Move</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_MOUSE_MOVE</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Mouse_Wheel</code> <code>Evas_Event_Mouse_Wheel</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_MOUSE_WHEEL</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Key_Down</code> <code>Evas_Event_Key_Down</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_KEY_DOWN</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Key_Up</code> <code>Evas_Event_Key_Up</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_KEY_UP</code> event callbacks.<br />
 typedef struct <code>_Evas_Event_Hold</code> <code>Evas_Event_Hold</code><br />
 <i>Event structure for </i><code>EVAS_CALLBACK_HOLD</code> event callbacks.<br />
 typedef struct _Evas_Object_Smart_Clipped_Data <code>Evas_Object_Smart_Clipped_Data</code><br />
 <i>Utilities:. </i></p>
<h3>Enumerations</h3>
<p>enum <code>_Evas_Callback_Type</code> { <code>EVAS_CALLBACK_MOUSE_IN</code>, <code>EVAS_CALLBACK_MOUSE_OUT</code>, <code>EVAS_CALLBACK_MOUSE_DOWN</code>, <code>EVAS_CALLBACK_MOUSE_UP</code>, <code>EVAS_CALLBACK_MOUSE_MOVE</code>, <code>EVAS_CALLBACK_MOUSE_WHEEL</code>, <code>EVAS_CALLBACK_FREE</code>, <code>EVAS_CALLBACK_KEY_DOWN</code>, <code>EVAS_CALLBACK_KEY_UP</code>, <code>EVAS_CALLBACK_FOCUS_IN</code>, <code>EVAS_CALLBACK_FOCUS_OUT</code>, <code>EVAS_CALLBACK_SHOW</code>, <code>EVAS_CALLBACK_HIDE</code>, <code>EVAS_CALLBACK_MOVE</code>, <code>EVAS_CALLBACK_RESIZE</code>, <code>EVAS_CALLBACK_RESTACK</code>, <code>EVAS_CALLBACK_DEL</code>, <code>EVAS_CALLBACK_HOLD</code>, <code>EVAS_CALLBACK_CHANGED_SIZE_HINTS</code>, <code>EVAS_CALLBACK_IMAGE_PRELOADED</code> } </p>
<p> enum <code>_Evas_Button_Flags</code> { <code>EVAS_BUTTON_NONE</code> = 0, <code>EVAS_BUTTON_DOUBLE_CLICK</code> = (1 &lt;&lt; 0), <code>EVAS_BUTTON_TRIPLE_CLICK</code> = (1 &lt;&lt; 1) } </p>
<p> enum <code>_Evas_Event_Flags</code> { <code>EVAS_EVENT_FLAG_NONE</code> = 0, <code>EVAS_EVENT_FLAG_ON_HOLD</code> = (1 &lt;&lt; 0) } </p>
<p> enum <code>_Evas_Font_Hinting_Flags</code> { <code>EVAS_FONT_HINTING_NONE</code>, <code>EVAS_FONT_HINTING_AUTO</code>, <code>EVAS_FONT_HINTING_BYTECODE</code> } </p>
<p> enum <code>_Evas_Colorspace</code> { <code>EVAS_COLORSPACE_ARGB8888</code>, <code>EVAS_COLORSPACE_YCBCR422P601_PL</code>, <code>EVAS_COLORSPACE_YCBCR422P709_PL</code>, <code>EVAS_COLORSPACE_RGB565_A5P</code> } </p>
<p> enum <code>_Evas_Render_Op</code> { <code>EVAS_RENDER_BLEND</code> = 0, <code>EVAS_RENDER_BLEND_REL</code> = 1, <code>EVAS_RENDER_COPY</code> = 2, <code>EVAS_RENDER_COPY_REL</code> = 3, <code>EVAS_RENDER_ADD</code> = 4, <code>EVAS_RENDER_ADD_REL</code> = 5, <code>EVAS_RENDER_SUB</code> = 6, <code>EVAS_RENDER_SUB_REL</code> = 7, <code>EVAS_RENDER_TINT</code> = 8, <code>EVAS_RENDER_TINT_REL</code> = 9, <code>EVAS_RENDER_MASK</code> = 10, <code>EVAS_RENDER_MUL</code> = 11 } </p>
<p> enum <code>_Evas_Object_Pointer_Mode</code> { <code>EVAS_OBJECT_POINTER_MODE_AUTOGRAB</code> } </p>
<h3>Functions</h3>
<p>EAPI int <code>evas_alloc_error</code> (void)<br />
 <i>Return if any allocation errors have occured during the prior function. </i><br />
 EAPI <code>Evas</code> * <code>evas_new</code> (void)<br />
 <i>Creates a new empty evas. </i><br />
 EAPI void <code>evas_free</code> (<code>Evas</code> *e)<br />
 <i>Frees the given evas and any objects created on it. </i><br />
 EAPI int <code>evas_render_method_lookup</code> (const char *name)<br />
 <i>Look up a numeric ID from a string name of a rendering engine. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_render_method_list</code> (void)<br />
 <i>List all the rendering engines compiled into the copy of the Evas library. </i><br />
 EAPI void <code>evas_render_method_list_free</code> (<code>Evas_List</code> *list)<br />
 <i>This function should be called to free a list of engine names. </i><br />
 EAPI void <code>evas_output_method_set</code> (<code>Evas</code> *e, int render_method)<br />
 <i>Sets the output engine for the given evas. </i><br />
 EAPI int <code>evas_output_method_get</code> (const <code>Evas</code> *e)<br />
 <i>Retrieves the number of the output engine used for the given evas. </i><br />
 EAPI <code>Evas_Engine_Info</code> * <code>evas_engine_info_get</code> (const <code>Evas</code> *e)<br />
 <i>Retrieves the current render engine info struct from the given evas. </i><br />
 EAPI void <code>evas_engine_info_set</code> (<code>Evas</code> *e, <code>Evas_Engine_Info</code> *info)<br />
 <i>Applies the engine settings for the given evas from the given </i>Evas_Engine_Info structure.<br />
 EAPI void <code>evas_output_size_set</code> (<code>Evas</code> *e, int w, int h)<br />
 <i>Sets the output size of the render engine of the given evas. </i><br />
 EAPI void <code>evas_output_size_get</code> (const <code>Evas</code> *e, int *w, int *h)<br />
 <i>Retrieve the output size of the render engine of the given evas. </i><br />
 EAPI void <code>evas_output_viewport_set</code> (<code>Evas</code> *e, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the output viewport of the given evas in evas units. </i><br />
 EAPI void <code>evas_output_viewport_get</code> (const <code>Evas</code> *e, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Get the render engine&#8217;s output viewport co-ordinates in canvas units. </i><br />
 EAPI Evas_Coord <code>evas_coord_screen_x_to_world</code> (const <code>Evas</code> *e, int x)<br />
 <i>Convert/scale an ouput screen co-ordinate into canvas co-ordinates. </i><br />
 EAPI Evas_Coord <code>evas_coord_screen_y_to_world</code> (const <code>Evas</code> *e, int y)<br />
 <i>Convert/scale an ouput screen co-ordinate into canvas co-ordinates. </i><br />
 EAPI int <code>evas_coord_world_x_to_screen</code> (const <code>Evas</code> *e, Evas_Coord x)<br />
 <i>Convert/scale a canvas co-ordinate into output screen co-ordinates. </i><br />
 EAPI int <code>evas_coord_world_y_to_screen</code> (const <code>Evas</code> *e, Evas_Coord y)<br />
 <i>Convert/scale a canvas co-ordinate into output screen co-ordinates. </i><br />
 EAPI void <code>evas_pointer_output_xy_get</code> (const <code>Evas</code> *e, int *x, int *y)<br />
 <i>This function returns the current known pointer co-ordinates. </i><br />
 EAPI void <code>evas_pointer_canvas_xy_get</code> (const <code>Evas</code> *e, Evas_Coord *x, Evas_Coord *y)<br />
 <i>This function returns the current known pointer co-ordinates. </i><br />
 EAPI int <code>evas_pointer_button_down_mask_get</code> (const <code>Evas</code> *e)<br />
 <i>Returns a bitmask with the mouse buttons currently pressed, set to 1. </i><br />
 EAPI Evas_Bool <code>evas_pointer_inside_get</code> (const <code>Evas</code> *e)<br />
 <i>Returns whether the mouse pointer is logically inside the canvas. </i><br />
 EAPI void <code>evas_data_attach_set</code> (<code>Evas</code> *e, void *data)<br />
 <i>Attaches a specific pointer to the evas for fetching later. </i><br />
 EAPI void * <code>evas_data_attach_get</code> (const <code>Evas</code> *e)<br />
 <i>Returns the pointer attached by </i><code>evas_data_attach_set()</code>.<br />
 EAPI void <code>evas_damage_rectangle_add</code> (<code>Evas</code> *e, int x, int y, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_obscured_rectangle_add</code> (<code>Evas</code> *e, int x, int y, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_obscured_clear</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_render_updates</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_render_updates_free</code> (<code>Evas_List</code> *updates)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_render</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_norender</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_render_idle_flush</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_rectangle_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a rectangle to the given evas. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_line_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a new evas line object to the given evas. </i><br />
 EAPI void <code>evas_object_line_xy_set</code> (<code>Evas_Object</code> *obj, Evas_Coord x1, Evas_Coord y1, Evas_Coord x2, Evas_Coord y2)<br />
 <i>Sets the coordinates of the end points of the given evas line object. </i><br />
 EAPI void <code>evas_object_line_xy_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x1, Evas_Coord *y1, Evas_Coord *x2, Evas_Coord *y2)<br />
 <i>Retrieves the coordinates of the end points of the given evas line object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_gradient_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a gradient object to the given evas. </i><br />
 EAPI void <code>evas_object_gradient_color_stop_add</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a, int delta)<br />
 <i>Adds a color stop to the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_alpha_stop_add</code> (<code>Evas_Object</code> *obj, int a, int delta)<br />
 <i>Adds an alpha stop to the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_color_data_set</code> (<code>Evas_Object</code> *obj, void *color_data, int len, Evas_Bool has_alpha)<br />
 <i>Sets color data for the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_alpha_data_set</code> (<code>Evas_Object</code> *obj, void *alpha_data, int len)<br />
 <i>Sets alpha data for the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient_clear</code> (<code>Evas_Object</code> *obj)<br />
 <i>Deletes all stops set for the given evas gradient object or any set data. </i><br />
 EAPI void <code>evas_object_gradient_type_set</code> (<code>Evas_Object</code> *obj, const char *type, const char *instance_params)<br />
 <i>Sets the geometric type displayed by the given gradient object. </i><br />
 EAPI void <code>evas_object_gradient_type_get</code> (const <code>Evas_Object</code> *obj, char **type, char **instance_params)<br />
 <i>Retrieves the type name and params of the given gradient object. </i><br />
 EAPI void <code>evas_object_gradient_fill_set</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the rectangle on the gradient object that the gradient will be drawn to. </i><br />
 EAPI void <code>evas_object_gradient_fill_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the dimensions of the rectangle on the gradient object that the gradient will use as its fill rect. </i><br />
 EAPI void <code>evas_object_gradient_fill_angle_set</code> (<code>Evas_Object</code> *obj, Evas_Angle angle)<br />
 <i>Sets the angle at which the given evas gradient object&#8217;s fill sits clockwise from vertical. </i><br />
 EAPI Evas_Angle <code>evas_object_gradient_fill_angle_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the angle at which the given evas gradient object&#8217;s fill sits clockwise from the vertical. </i><br />
 EAPI void <code>evas_object_gradient_fill_spread_set</code> (<code>Evas_Object</code> *obj, int tile_mode)<br />
 <i>Sets the tiling mode for the given evas gradient object&#8217;s fill. </i><br />
 EAPI int <code>evas_object_gradient_fill_spread_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spread (tiling mode) for the given gradient object&#8217;s fill. </i><br />
 EAPI void <code>evas_object_gradient_angle_set</code> (<code>Evas_Object</code> *obj, Evas_Angle angle)<br />
 <i>Sets the angle at which the given evas gradient sits, relative to whatever intrinsic orientation of the grad type. </i><br />
 EAPI Evas_Angle <code>evas_object_gradient_angle_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the angle at which the given evas gradient object sits rel to its intrinsic orientation. </i><br />
 EAPI void <code>evas_object_gradient_direction_set</code> (<code>Evas_Object</code> *obj, int direction)<br />
 <i>Sets the direction of the given evas gradient object&#8217;s spectrum. </i><br />
 EAPI int <code>evas_object_gradient_direction_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the evas gradient object&#8217;s spectrum direction. </i><br />
 EAPI void <code>evas_object_gradient_offset_set</code> (<code>Evas_Object</code> *obj, float offset)<br />
 <i>Sets the offset of the given evas gradient object&#8217;s spectrum. </i><br />
 EAPI float <code>evas_object_gradient_offset_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spectrum&#8217;s offset. </i><br />
 EAPI void <code>evas_object_gradient2_color_np_stop_insert</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a, float pos)<br />
 <i>Inserts a color stop to the given evas gradient object. </i><br />
 EAPI void <code>evas_object_gradient2_fill_spread_set</code> (<code>Evas_Object</code> *obj, int tile_mode)<br />
 <i>Sets the tiling mode for the given evas gradient object&#8217;s fill. </i><br />
 EAPI int <code>evas_object_gradient2_fill_spread_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spread (tiling mode) for the given gradient object&#8217;s fill. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_gradient2_linear_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a gradient object to the given evas. </i><br />
 EAPI void <code>evas_object_gradient2_linear_fill_set</code> (<code>Evas_Object</code> *obj, float x0, float y0, float x1, float y1)<br />
 <i>Sets the start and end points of the linear gradient geometry for the object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_gradient2_radial_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a gradient object to the given evas. </i><br />
 EAPI void <code>evas_object_gradient2_radial_fill_set</code> (<code>Evas_Object</code> *obj, float cx, float cy, float rx, float ry)<br />
 <i>Sets the center and radii of the radial gradient geometry for the object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_polygon_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a new evas polygon object to the given evas. </i><br />
 EAPI void <code>evas_object_polygon_point_add</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y)<br />
 <i>Adds the given point to the given evas polygon object. </i><br />
 EAPI void <code>evas_object_polygon_points_clear</code> (<code>Evas_Object</code> *obj)<br />
 <i>Removes all of the points from the given evas polygon object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_image_add</code> (<code>Evas</code> *e)<br />
 <i>Creates a new image object on the given evas. </i><br />
 EAPI void <code>evas_object_image_file_set</code> (<code>Evas_Object</code> *obj, const char *file, const char *key)<br />
 <i>Sets the filename and key of the given image object. </i><br />
 EAPI void <code>evas_object_image_file_get</code> (const <code>Evas_Object</code> *obj, const char **file, const char **key)<br />
 <i>Retrieves the filename and key of the given image object. </i><br />
 EAPI void <code>evas_object_image_border_set</code> (<code>Evas_Object</code> *obj, int l, int r, int t, int b)<br />
 <i>Sets how much of each border of the given image object is not to be scaled. </i><br />
 EAPI void <code>evas_object_image_border_get</code> (const <code>Evas_Object</code> *obj, int *l, int *r, int *t, int *b)<br />
 <i>Retrieves how much of each border of the given image object is not to be scaled. </i><br />
 EAPI void <code>evas_object_image_border_center_fill_set</code> (<code>Evas_Object</code> *obj, Evas_Bool fill)<br />
 <i>Sets if the center part of the given image object (not the border) should be drawn. </i><br />
 EAPI Evas_Bool <code>evas_object_image_border_center_fill_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves if the center of the given image object is to be drawn or not. </i><br />
 EAPI void <code>evas_object_image_fill_set</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the rectangle of the given image object that the image will be drawn to. </i><br />
 EAPI void <code>evas_object_image_fill_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the dimensions of the rectangle of the given image object that the image will be drawn to. </i><br />
 EAPI void <code>evas_object_image_fill_spread_set</code> (<code>Evas_Object</code> *obj, int tile_mode)<br />
 <i>Sets the tiling mode for the given evas image object&#8217;s fill. </i><br />
 EAPI int <code>evas_object_image_fill_spread_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the spread (tiling mode) for the given image object&#8217;s fill. </i><br />
 EAPI void <code>evas_object_image_size_set</code> (<code>Evas_Object</code> *obj, int w, int h)<br />
 <i>Sets the size of the given image object. </i><br />
 EAPI void <code>evas_object_image_size_get</code> (const <code>Evas_Object</code> *obj, int *w, int *h)<br />
 <i>Retrieves the size of the given image object. </i><br />
 EAPI int <code>evas_object_image_stride_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the row stride of the given image object,. </i><br />
 EAPI int <code>evas_object_image_load_error_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves a number representing any error that occurred during the last load of the given image object. </i><br />
 EAPI void <code>evas_object_image_data_set</code> (<code>Evas_Object</code> *obj, void *data)<br />
 <i>Sets the raw image data of the given image object. </i><br />
 EAPI void * <code>evas_object_image_data_convert</code> (<code>Evas_Object</code> *obj, <code>Evas_Colorspace</code> to_cspace)<br />
 <i>Converts the raw image data of the given image object to the specified colorspace. </i><br />
 EAPI void * <code>evas_object_image_data_get</code> (const <code>Evas_Object</code> *obj, Evas_Bool for_writing)<br />
 <i>Get a pointer to the raw image data of the given image object. </i><br />
 EAPI void <code>evas_object_image_data_copy_set</code> (<code>Evas_Object</code> *obj, void *data)<br />
 <i>Replaces the raw image data of the given image object. </i><br />
 EAPI void <code>evas_object_image_data_update_add</code> (<code>Evas_Object</code> *obj, int x, int y, int w, int h)<br />
 <i>Mark a sub-region of the given image object to be redrawn. </i><br />
 EAPI void <code>evas_object_image_alpha_set</code> (<code>Evas_Object</code> *obj, Evas_Bool has_alpha)<br />
 <i>Enable or disable alpha channel of the given image object. </i><br />
 EAPI Evas_Bool <code>evas_object_image_alpha_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the alpha channel setting of the given image object. </i><br />
 EAPI void <code>evas_object_image_smooth_scale_set</code> (<code>Evas_Object</code> *obj, Evas_Bool smooth_scale)<br />
 <i>Sets whether to use of high-quality image scaling algorithm of the given image object. </i><br />
 EAPI Evas_Bool <code>evas_object_image_smooth_scale_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether the given image object is using use a high-quality image scaling algorithm. </i><br />
 EAPI void <code>evas_object_image_preload</code> (const <code>Evas_Object</code> *obj, Evas_Bool cancel)<br />
 <i>Preload image in the background. </i><br />
 EAPI void <code>evas_object_image_reload</code> (<code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Bool <code>evas_object_image_save</code> (const <code>Evas_Object</code> *obj, const char *file, const char *key, const char *flags)<br />
 <i>Save the given image object to a file. </i><br />
 EAPI Evas_Bool <code>evas_object_image_pixels_import</code> (<code>Evas_Object</code> *obj, <code>Evas_Pixel_Import_Source</code> *pixels)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_image_pixels_get_callback_set</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *o), void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_image_pixels_dirty_set</code> (<code>Evas_Object</code> *obj, Evas_Bool dirty)<br />
 <i>Mark whether the given image object is dirty (needs to be redrawn). </i><br />
 EAPI Evas_Bool <code>evas_object_image_pixels_dirty_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether the given image object is dirty (needs to be redrawn). </i><br />
 EAPI void <code>evas_object_image_load_dpi_set</code> (<code>Evas_Object</code> *obj, double dpi)<br />
 <i>To be documented. </i><br />
 EAPI double <code>evas_object_image_load_dpi_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_image_load_size_set</code> (<code>Evas_Object</code> *obj, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_image_load_scale_down_set</code> (<code>Evas_Object</code> *obj, int scale_down)<br />
 <i>To be documented. </i><br />
 EAPI int <code>evas_object_image_load_scale_down_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_image_colorspace_set</code> (<code>Evas_Object</code> *obj, <code>Evas_Colorspace</code> cspace)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_Colorspace</code> <code>evas_object_image_colorspace_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_image_native_surface_set</code> (<code>Evas_Object</code> *obj, <code>Evas_Native_Surface</code> *surf)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_Native_Surface</code> * <code>evas_object_image_native_surface_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_image_cache_flush</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_image_cache_reload</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_image_cache_set</code> (<code>Evas</code> *e, int size)<br />
 <i>To be documented. </i><br />
 EAPI int <code>evas_image_cache_get</code> (const <code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_text_add</code> (<code>Evas</code> *e)<br />
 <i>Creates a new text </i>Evas_Object on the provided Evas canvas.<br />
 EAPI void <code>evas_object_text_font_source_set</code> (<code>Evas_Object</code> *obj, const char *font)<br />
 <i>To be documented. </i><br />
 EAPI const char * <code>evas_object_text_font_source_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_font_set</code> (<code>Evas_Object</code> *obj, const char *font, Evas_Font_Size size)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_font_get</code> (const <code>Evas_Object</code> *obj, const char **font, Evas_Font_Size *size)<br />
 <i>Query evas for font information of a text </i>Evas_Object.<br />
 EAPI void <code>evas_object_text_text_set</code> (<code>Evas_Object</code> *obj, const char *text)<br />
 <i>Sets the text to be displayed by the given evas text object. </i><br />
 EAPI const char * <code>evas_object_text_text_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the text currently being displayed by the given evas text object. </i><br />
 EAPI Evas_Coord <code>evas_object_text_ascent_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Coord <code>evas_object_text_descent_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Coord <code>evas_object_text_max_ascent_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Coord <code>evas_object_text_max_descent_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Coord <code>evas_object_text_horiz_advance_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Coord <code>evas_object_text_vert_advance_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Coord <code>evas_object_text_inset_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI int <code>evas_object_text_char_pos_get</code> (const <code>Evas_Object</code> *obj, int pos, Evas_Coord *cx, Evas_Coord *cy, Evas_Coord *cw, Evas_Coord *ch)<br />
 <i>Retrieve position and dimension information of a character within a text </i>Evas_Object.<br />
 EAPI int <code>evas_object_text_char_coords_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y, Evas_Coord *cx, Evas_Coord *cy, Evas_Coord *cw, Evas_Coord *ch)<br />
 <i>To be documented. </i><br />
 EAPI Evas_Text_Style_Type <code>evas_object_text_style_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_style_set</code> (<code>Evas_Object</code> *obj, Evas_Text_Style_Type type)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_shadow_color_set</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_shadow_color_get</code> (const <code>Evas_Object</code> *obj, int *r, int *g, int *b, int *a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_glow_color_set</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_glow_color_get</code> (const <code>Evas_Object</code> *obj, int *r, int *g, int *b, int *a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_glow2_color_set</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_glow2_color_get</code> (const <code>Evas_Object</code> *obj, int *r, int *g, int *b, int *a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_outline_color_set</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_outline_color_get</code> (const <code>Evas_Object</code> *obj, int *r, int *g, int *b, int *a)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_text_style_pad_get</code> (const <code>Evas_Object</code> *obj, int *l, int *r, int *t, int *b)<br />
 <i>To be documented. </i><br />
 EAPI int <code>evas_string_char_next_get</code> (const char *str, int pos, int *decoded)<br />
 <i>To be documented. </i><br />
 EAPI int <code>evas_string_char_prev_get</code> (const char *str, int pos, int *decoded)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_font_path_clear</code> (<code>Evas</code> *e)<br />
 <i>Removes all font paths loaded into memory for the given evas. </i><br />
 EAPI void <code>evas_font_path_append</code> (<code>Evas</code> *e, const char *path)<br />
 <i>Appends a font path to the list of font paths used by the given evas. </i><br />
 EAPI void <code>evas_font_path_prepend</code> (<code>Evas</code> *e, const char *path)<br />
 <i>Prepends a font path to the list of font paths used by the given evas. </i><br />
 EAPI const <code>Evas_List</code> * <code>evas_font_path_list</code> (const <code>Evas</code> *e)<br />
 <i>Retrieves the list of font paths used by the given evas. </i><br />
 EAPI void <code>evas_font_cache_flush</code> (<code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_font_cache_set</code> (<code>Evas</code> *e, int size)<br />
 <i>To be documented. </i><br />
 EAPI int <code>evas_font_cache_get</code> (const <code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_font_available_list</code> (const <code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_font_available_list_free</code> (<code>Evas</code> *e, <code>Evas_List</code> *available)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_textblock_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a textblock to the given evas. </i><br />
 EAPI Evas_Textblock_Style * <code>evas_textblock_style_new</code> (void)<br />
 <i>Creates a new textblock style. </i><br />
 EAPI void <code>evas_textblock_style_free</code> (Evas_Textblock_Style *ts)<br />
 <i>Destroys a textblock style. </i><br />
 EAPI void <code>evas_textblock_style_set</code> (Evas_Textblock_Style *ts, const char *text)<br />
 <i>to be documented. </i><br />
 EAPI const char * <code>evas_textblock_style_get</code> (const Evas_Textblock_Style *ts)<br />
 <i>to be documented. </i><br />
 EAPI void <code>evas_object_textblock_style_set</code> (<code>Evas_Object</code> *obj, Evas_Textblock_Style *ts)<br />
 <i>to be documented. </i><br />
 EAPI const Evas_Textblock_Style * <code>evas_object_textblock_style_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>to be documented. </i><br />
 EAPI void <code>evas_object_textblock_text_markup_set</code> (<code>Evas_Object</code> *obj, const char *text)<br />
 <i>to be documented. </i><br />
 EAPI void <code>evas_object_del</code> (<code>Evas_Object</code> *obj)<br />
 <i>Deletes the given evas object and frees its memory. </i><br />
 EAPI const char * <code>evas_object_type_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the name of the type of the given evas object. </i><br />
 EAPI void <code>evas_object_layer_set</code> (<code>Evas_Object</code> *obj, short l)<br />
 <i>Sets the layer of the evas that the given object will be part of. </i><br />
 EAPI short <code>evas_object_layer_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the layer of the evas that the given object is part of. </i><br />
 EAPI void <code>evas_object_raise</code> (<code>Evas_Object</code> *obj)<br />
 <i>Raise </i>obj to the top of its layer.<br />
 EAPI void <code>evas_object_lower</code> (<code>Evas_Object</code> *obj)<br />
 <i>Lower </i>obj to the bottom of its layer.<br />
 EAPI void <code>evas_object_stack_above</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *above)<br />
 <i>Stack </i>obj immediately above above.<br />
 EAPI void <code>evas_object_stack_below</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *below)<br />
 <i>Stack </i>obj immediately below below.<br />
 EAPI <code>Evas_Object</code> * <code>evas_object_above_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Get the evas object above </i>obj.<br />
 EAPI <code>Evas_Object</code> * <code>evas_object_below_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Get the evas object below </i>obj.<br />
 EAPI <code>Evas_Object</code> * <code>evas_object_bottom_get</code> (const <code>Evas</code> *e)<br />
 <i>Get the lowest evas object on the Evas </i>e.<br />
 EAPI <code>Evas_Object</code> * <code>evas_object_top_get</code> (const <code>Evas</code> *e)<br />
 <i>Get the highest evas object on the Evas </i>e.<br />
 EAPI void <code>evas_object_move</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y)<br />
 <i>Moves the given evas object to the given location. </i><br />
 EAPI void <code>evas_object_resize</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Changes the size of the given evas object. </i><br />
 EAPI void <code>evas_object_geometry_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x, Evas_Coord *y, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the position and rectangular size of the given evas object. </i><br />
 EAPI void <code>evas_object_size_hint_min_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size hint for the minimum size. </i><br />
 EAPI void <code>evas_object_size_hint_min_set</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the size hint for the minimum size. </i><br />
 EAPI void <code>evas_object_size_hint_max_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size hint for the maximum size. </i><br />
 EAPI void <code>evas_object_size_hint_max_set</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the size hint for the maximum size. </i><br />
 EAPI void <code>evas_object_size_hint_request_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size request hint. </i><br />
 EAPI void <code>evas_object_size_hint_request_set</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the requested size hint. </i><br />
 EAPI void <code>evas_object_size_hint_aspect_get</code> (const <code>Evas_Object</code> *obj, Evas_Aspect_Control *aspect, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size aspect control hint. </i><br />
 EAPI void <code>evas_object_size_hint_aspect_set</code> (<code>Evas_Object</code> *obj, Evas_Aspect_Control aspect, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the size aspect control hint. </i><br />
 EAPI void <code>evas_object_show</code> (<code>Evas_Object</code> *obj)<br />
 <i>Makes the given evas object visible. </i><br />
 EAPI void <code>evas_object_hide</code> (<code>Evas_Object</code> *obj)<br />
 <i>Makes the given evas object invisible. </i><br />
 EAPI Evas_Bool <code>evas_object_visible_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether or not the given evas object is visible. </i><br />
 EAPI void <code>evas_object_render_op_set</code> (<code>Evas_Object</code> *obj, Evas_Render_Op op)<br />
 <i>Sets the render_op to be used for rendering the evas object. </i><br />
 EAPI Evas_Render_Op <code>evas_object_render_op_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the current value of the operation used for rendering the evas object. </i><br />
 EAPI void <code>evas_object_anti_alias_set</code> (<code>Evas_Object</code> *obj, Evas_Bool antialias)<br />
 <i>Sets whether or not the given evas object is to be drawn anti_aliased. </i><br />
 EAPI Evas_Bool <code>evas_object_anti_alias_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether or not the given evas object is to be drawn anti_aliased. </i><br />
 EAPI void <code>evas_object_scale_set</code> (<code>Evas_Object</code> *obj, double scale)<br />
 <i>Sets the scaling factor for an evas object. </i><br />
 EAPI double <code>evas_object_scale_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the scaling factor for the given evas object. </i><br />
 EAPI void <code>evas_object_color_set</code> (<code>Evas_Object</code> *obj, int r, int g, int b, int a)<br />
 <i>Sets the general colour of the given evas object to the given colour. </i><br />
 EAPI void <code>evas_object_color_get</code> (const <code>Evas_Object</code> *obj, int *r, int *g, int *b, int *a)<br />
 <i>Retrieves the general colour of the given evas object. </i><br />
 EAPI void <code>evas_object_color_interpolation_set</code> (<code>Evas_Object</code> *obj, int color_space)<br />
 <i>Sets the color_space to be used for linear interpolation of colors. </i><br />
 EAPI int <code>evas_object_color_interpolation_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the current value of the color space used for linear interpolation. </i><br />
 EAPI void <code>evas_object_clip_set</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *clip)<br />
 <i>Clip one object to another. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_clip_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Get the object clipping this one (if any). </i><br />
 EAPI void <code>evas_object_clip_unset</code> (<code>Evas_Object</code> *obj)<br />
 <i>Disable clipping for an object. </i><br />
 EAPI const <code>Evas_List</code> * <code>evas_object_clipees_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Return a list of objects currently clipped by a specific object. </i><br />
 EAPI void <code>evas_object_data_set</code> (<code>Evas_Object</code> *obj, const char *key, const void *data)<br />
 <i>Set an attached data pointer to an object with a given string key. </i><br />
 EAPI void * <code>evas_object_data_get</code> (const <code>Evas_Object</code> *obj, const char *key)<br />
 <i>Return an attached data pointer by its given string key. </i><br />
 EAPI void * <code>evas_object_data_del</code> (<code>Evas_Object</code> *obj, const char *key)<br />
 <i>Delete at attached data pointer from an object. </i><br />
 EAPI void <code>evas_object_name_set</code> (<code>Evas_Object</code> *obj, const char *name)<br />
 <i>Sets the name of the given evas object to the given name. </i><br />
 EAPI const char * <code>evas_object_name_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the name of the given evas object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_name_find</code> (const <code>Evas</code> *e, const char *name)<br />
 <i>Retrieves the object on the given evas with the given name. </i><br />
 EAPI <code>Evas</code> * <code>evas_object_evas_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the evas that the given evas object is on. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_top_at_xy_get</code> (const <code>Evas</code> *e, Evas_Coord x, Evas_Coord y, Evas_Bool include_pass_events_objects, Evas_Bool include_hidden_objects)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_top_at_pointer_get</code> (const <code>Evas</code> *e)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_top_in_rectangle_get</code> (const <code>Evas</code> *e, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h, Evas_Bool include_pass_events_objects, Evas_Bool include_hidden_objects)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_objects_at_xy_get</code> (const <code>Evas</code> *e, Evas_Coord x, Evas_Coord y, Evas_Bool include_pass_events_objects, Evas_Bool include_hidden_objects)<br />
 <i>To be documented. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_objects_in_rectangle_get</code> (const <code>Evas</code> *e, Evas_Coord x, Evas_Coord y, Evas_Coord w, Evas_Coord h, Evas_Bool include_pass_events_objects, Evas_Bool include_hidden_objects)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_smart_free</code> (<code>Evas_Smart</code> *s)<br />
 <i>Free an Evas_Smart. </i><br />
 EAPI <code>Evas_Smart</code> * <code>evas_smart_class_new</code> (const <code>Evas_Smart_Class</code> *sc)<br />
 <i>Creates an Evas_Smart from an Evas_Smart_Class. </i><br />
 EAPI const <code>Evas_Smart_Class</code> * <code>evas_smart_class_get</code> (const <code>Evas_Smart</code> *s)<br />
 <i>Get the Evas_Smart_Class of an Evas_Smart. </i><br />
 EAPI void * <code>evas_smart_data_get</code> (const <code>Evas_Smart</code> *s)<br />
 <i>Get the data pointer set on an Evas_Smart. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_smart_add</code> (<code>Evas</code> *e, <code>Evas_Smart</code> *s)<br />
 <i>Instantiates a new smart object described by </i>s.<br />
 EAPI void <code>evas_object_smart_member_add</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *smart_obj)<br />
 <i>Set an evas object as a member of a smart object. </i><br />
 EAPI void <code>evas_object_smart_member_del</code> (<code>Evas_Object</code> *obj)<br />
 <i>Removes a member object from a smart object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_smart_parent_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Gets the smart parent of an Evas_Object. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_object_smart_members_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Gets the list of the member objects of an Evas_Object. </i><br />
 EAPI <code>Evas_Smart</code> * <code>evas_object_smart_smart_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Get the Evas_Smart from which </i>obj was created.<br />
 EAPI void * <code>evas_object_smart_data_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieve user data stored on a smart object. </i><br />
 EAPI void <code>evas_object_smart_data_set</code> (<code>Evas_Object</code> *obj, void *data)<br />
 <i>Store a pointer to user data for a smart object. </i><br />
 EAPI void <code>evas_object_smart_callback_add</code> (<code>Evas_Object</code> *obj, const char *event, void(*func)(void *data, <code>Evas_Object</code> *obj, void *event_info), const void *data)<br />
 <i>Add a callback for the smart event specified by </i>event.<br />
 EAPI void * <code>evas_object_smart_callback_del</code> (<code>Evas_Object</code> *obj, const char *event, void(*func)(void *data, <code>Evas_Object</code> *obj, void *event_info))<br />
 <i>Remove a smart callback. </i><br />
 EAPI void <code>evas_object_smart_callback_call</code> (<code>Evas_Object</code> *obj, const char *event, void *event_info)<br />
 <i>Call any smart callbacks on </i>obj for event.<br />
 EAPI void <code>evas_object_smart_changed</code> (<code>Evas_Object</code> *obj)<br />
 <i>Mark smart object as changed, dirty. </i><br />
 EAPI void <code>evas_object_smart_need_recalculate_set</code> (<code>Evas_Object</code> *obj, Evas_Bool value)<br />
 <i>Set the need_recalculate flag of given smart object. </i><br />
 EAPI Evas_Bool <code>evas_object_smart_need_recalculate_get</code> (<code>Evas_Object</code> *obj)<br />
 <i>Get the current value of need_recalculate flag. </i><br />
 EAPI void <code>evas_object_smart_calculate</code> (<code>Evas_Object</code> *obj)<br />
 <i>Call user provided calculate() and unset need_calculate. </i><br />
 EAPI void <code>evas_event_freeze</code> (<code>Evas</code> *e)<br />
 <i>Freeze all event processing. </i><br />
 EAPI void <code>evas_event_thaw</code> (<code>Evas</code> *e)<br />
 <i>Thaw a canvas out after freezing. </i><br />
 EAPI int <code>evas_event_freeze_get</code> (const <code>Evas</code> *e)<br />
 <i>Return the freeze count of a given canvas. </i><br />
 EAPI void <code>evas_event_feed_mouse_down</code> (<code>Evas</code> *e, int b, <code>Evas_Button_Flags</code> flags, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_mouse_up</code> (<code>Evas</code> *e, int b, <code>Evas_Button_Flags</code> flags, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_mouse_move</code> (<code>Evas</code> *e, int x, int y, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_mouse_in</code> (<code>Evas</code> *e, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_mouse_out</code> (<code>Evas</code> *e, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_mouse_cancel</code> (<code>Evas</code> *e, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_mouse_wheel</code> (<code>Evas</code> *e, int direction, int z, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_key_down</code> (<code>Evas</code> *e, const char *keyname, const char *key, const char *string, const char *compose, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_key_up</code> (<code>Evas</code> *e, const char *keyname, const char *key, const char *string, const char *compose, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_event_feed_hold</code> (<code>Evas</code> *e, int hold, unsigned int timestamp, const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_focus_set</code> (<code>Evas_Object</code> *obj, Evas_Bool focus)<br />
 <i>Sets focus to the given object. </i><br />
 EAPI Evas_Bool <code>evas_object_focus_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Test if the object has focus. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_focus_get</code> (const <code>Evas</code> *e)<br />
 <i>Retrieve the object that currently has focus. </i><br />
 EAPI const <code>Evas_Modifier</code> * <code>evas_key_modifier_get</code> (const <code>Evas</code> *e)<br />
 <i>Returns a handle to the modifiers available in the system. </i><br />
 EAPI const <code>Evas_Lock</code> * <code>evas_key_lock_get</code> (const <code>Evas</code> *e)<br />
 <i>Returns a handle to the locks available in the system. </i><br />
 EAPI Evas_Bool <code>evas_key_modifier_is_set</code> (const <code>Evas_Modifier</code> *m, const char *keyname)<br />
 <i>Checks the state of a given modifier. </i><br />
 EAPI Evas_Bool <code>evas_key_lock_is_set</code> (const <code>Evas_Lock</code> *l, const char *keyname)<br />
 <i>Checks the state of a given lock. </i><br />
 EAPI void <code>evas_key_modifier_add</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Adds the </i>keyname to the current list of modifiers.<br />
 EAPI void <code>evas_key_modifier_del</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Removes the </i>keyname from the current list of modifiers.<br />
 EAPI void <code>evas_key_lock_add</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Adds the </i>keyname to the current list of locks.<br />
 EAPI void <code>evas_key_lock_del</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Removes The </i>keyname from the current list of locks.<br />
 EAPI void <code>evas_key_modifier_on</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Enables or turns on the modifier with name </i>keyname.<br />
 EAPI void <code>evas_key_modifier_off</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Disables or turns off the modifier with name </i>keyname.<br />
 EAPI void <code>evas_key_lock_on</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Enables or turns on the lock with name </i>keyname.<br />
 EAPI void <code>evas_key_lock_off</code> (<code>Evas</code> *e, const char *keyname)<br />
 <i>Disables or turns off the lock with name </i>keyname.<br />
 EAPI <code>Evas_Modifier_Mask</code> <code>evas_key_modifier_mask_get</code> (const <code>Evas</code> *e, const char *keyname)<br />
 <i>Creates a bit mask from the </i>keyname for use with events to check for the presence of the keyname modifier.<br />
 EAPI Evas_Bool <code>evas_object_key_grab</code> (<code>Evas_Object</code> *obj, const char *keyname, <code>Evas_Modifier_Mask</code> modifiers, <code>Evas_Modifier_Mask</code> not_modifiers, Evas_Bool exclusive)<br />
 <i>Requests </i>keyname key events be directed to obj.<br />
 EAPI void <code>evas_object_key_ungrab</code> (<code>Evas_Object</code> *obj, const char *keyname, <code>Evas_Modifier_Mask</code> modifiers, <code>Evas_Modifier_Mask</code> not_modifiers)<br />
 <i>Request that the grab on </i>obj be removed.<br />
 EAPI void <code>evas_object_pass_events_set</code> (<code>Evas_Object</code> *obj, Evas_Bool pass)<br />
 <i>Set an object&#8217;s pass events state. </i><br />
 EAPI Evas_Bool <code>evas_object_pass_events_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to pass events. </i><br />
 EAPI void <code>evas_object_repeat_events_set</code> (<code>Evas_Object</code> *obj, Evas_Bool repeat)<br />
 <i>Set an object&#8217;s repeat events state. </i><br />
 EAPI Evas_Bool <code>evas_object_repeat_events_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to repeat events. </i><br />
 EAPI void <code>evas_object_propagate_events_set</code> (<code>Evas_Object</code> *obj, Evas_Bool prop)<br />
 <i>Set whether events on a smart member object should propagate to its parent. </i><br />
 EAPI Evas_Bool <code>evas_object_propagate_events_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to propagate events. </i><br />
 EAPI void <code>evas_object_pointer_mode_set</code> (<code>Evas_Object</code> *obj, Evas_Object_Pointer_Mode setting)<br />
 <i>Set pointer behavior. </i><br />
 EAPI Evas_Object_Pointer_Mode <code>evas_object_pointer_mode_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine how pointer will behave. </i><br />
 EAPI void <code>evas_object_precise_is_inside_set</code> (<code>Evas_Object</code> *obj, Evas_Bool precise)<br />
 <i>Set whether to use a precise (usually expensive) point collision detection. </i><br />
 EAPI Evas_Bool <code>evas_object_precise_is_inside_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to use a precise point collision detection. </i><br />
 EAPI void <code>evas_object_event_callback_add</code> (<code>Evas_Object</code> *obj, <code>Evas_Callback_Type</code> type, void(*func)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info), const void *data)<br />
 <i>Add a callback function to an object. </i><br />
 EAPI void * <code>evas_object_event_callback_del</code> (<code>Evas_Object</code> *obj, <code>Evas_Callback_Type</code> type, void(*func)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info))<br />
 <i>Delete a callback function from an object. </i><br />
 EAPI void * <code>evas_object_event_callback_del_full</code> (<code>Evas_Object</code> *obj, <code>Evas_Callback_Type</code> type, void(*func)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info), const void *data)<br />
 <i>Delete a callback function from an object. </i><br />
 EAPI void <code>evas_object_intercept_show_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_show_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_hide_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_hide_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_move_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_move_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_resize_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_resize_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_raise_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_raise_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_lower_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_lower_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_stack_above_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *above), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_stack_above_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *above))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_stack_below_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *below), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_stack_below_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *below))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_layer_set_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, int l), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_layer_set_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, int l))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_color_set_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, int r, int g, int b, int a), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_color_set_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, int r, int g, int b, int a))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_clip_set_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *clip), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_clip_set_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *clip))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_object_intercept_clip_unset_callback_add</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj), const void *data)<br />
 <i>To be documented. </i><br />
 EAPI void * <code>evas_object_intercept_clip_unset_callback_del</code> (<code>Evas_Object</code> *obj, void(*func)(void *data, <code>Evas_Object</code> *obj))<br />
 <i>To be documented. </i><br />
 EAPI void <code>evas_color_hsv_to_rgb</code> (float h, float s, float v, int *r, int *g, int *b)<br />
 <i>FIXME: . </i><br />
 EAPI void <code>evas_color_rgb_to_hsv</code> (int r, int g, int b, float *h, float *s, float *v)<br />
 <i>FIXME: . </i><br />
 EAPI void <code>evas_color_argb_premul</code> (int a, int *r, int *g, int *b)<br />
 <i>FIXME: . </i><br />
 EAPI void <code>evas_color_argb_unpremul</code> (int a, int *r, int *g, int *b)<br />
 <i>FIXME: . </i><br />
 EAPI void <code>evas_data_argb_premul</code> (unsigned int *data, unsigned int len)<br />
 <i>FIXME: . </i><br />
 EAPI void <code>evas_data_argb_unpremul</code> (unsigned int *data, unsigned int len)<br />
 <i>FIXME: . </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_smart_clipped_clipper_get</code> (<code>Evas_Object</code> *obj)<br />
 <i>Get the clipper object for the given clipped smart object. </i><br />
 EAPI void <code>evas_object_smart_clipped_smart_set</code> (<code>Evas_Smart_Class</code> *sc)<br />
 <i>Set smart class callbacks so it implements the &#8216;Clipped Smart Object&#8217;. </i><br />
 EAPI void <code>evas_object_smart_clipped_member_add</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *member)<br />
 <i>Add the given member to clipped smart object. </i><br />
 EAPI void <code>evas_object_smart_clipped_member_del</code> (<code>Evas_Object</code> *member)<br />
 <i>Remove the given member from clipped smart object. </i><br />
 EAPI void <code>evas_object_smart_move_children_relative</code> (<code>Evas_Object</code> *obj, Evas_Coord dx, Evas_Coord dy)<br />
 <i>Moves all children objects relative to given offset. </i></p>
<h2>Detailed Description</h2>
<p>These routines are used for Evas library interaction. </p>
<h2>Typedef Documentation</h2>
<h3>typedef struct _Evas_Object_Smart_Clipped_Data <code>Evas_Object_Smart_Clipped_Data</code></h3>
<p>Utilities:. </p>
<p> Every subclass should provide this at the beginning of their own data set with <code>evas_object_smart_data_set()</code>.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>_Evas_Button_Flags</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EVAS_BUTTON_NONE </i></p>
<dd>No extra mouse button data.</p>
<dt><i>EVAS_BUTTON_DOUBLE_CLICK </i></p>
<dd>This mouse button press was the 2nd press of a double click.</p>
<dt><i>EVAS_BUTTON_TRIPLE_CLICK </i></p>
<dd>This mouse button press was the 3rd press of a triple click.</dl>
<h3>enum <code>_Evas_Callback_Type</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EVAS_CALLBACK_MOUSE_IN </i></p>
<dd>Mouse In Event.</p>
<dt><i>EVAS_CALLBACK_MOUSE_OUT </i></p>
<dd>Mouse Out Event.</p>
<dt><i>EVAS_CALLBACK_MOUSE_DOWN </i></p>
<dd>Mouse Button Down Event.</p>
<dt><i>EVAS_CALLBACK_MOUSE_UP </i></p>
<dd>Mouse Button Up Event.</p>
<dt><i>EVAS_CALLBACK_MOUSE_MOVE </i></p>
<dd>Mouse Move Event.</p>
<dt><i>EVAS_CALLBACK_MOUSE_WHEEL </i></p>
<dd>Mouse Wheel Event.</p>
<dt><i>EVAS_CALLBACK_FREE </i></p>
<dd>Object Being Freed (Called after Del).</p>
<dt><i>EVAS_CALLBACK_KEY_DOWN </i></p>
<dd>Key Press Event.</p>
<dt><i>EVAS_CALLBACK_KEY_UP </i></p>
<dd>Key Release Event.</p>
<dt><i>EVAS_CALLBACK_FOCUS_IN </i></p>
<dd>Focus In Event.</p>
<dt><i>EVAS_CALLBACK_FOCUS_OUT </i></p>
<dd>Focus Out Event.</p>
<dt><i>EVAS_CALLBACK_SHOW </i></p>
<dd>Show Event.</p>
<dt><i>EVAS_CALLBACK_HIDE </i></p>
<dd>Hide Event.</p>
<dt><i>EVAS_CALLBACK_MOVE </i></p>
<dd>Move Event.</p>
<dt><i>EVAS_CALLBACK_RESIZE </i></p>
<dd>Resize Event.</p>
<dt><i>EVAS_CALLBACK_RESTACK </i></p>
<dd>Restack Event.</p>
<dt><i>EVAS_CALLBACK_DEL </i></p>
<dd>Object Being Deleted (called before Free).</p>
<dt><i>EVAS_CALLBACK_HOLD </i></p>
<dd>Events go on/off hold.</p>
<dt><i>EVAS_CALLBACK_CHANGED_SIZE_HINTS </i></p>
<dd>Size hints changed event.</p>
<dt><i>EVAS_CALLBACK_IMAGE_PRELOADED </i></p>
<dd>Image as been preloaded.</dl>
<h3>enum <code>_Evas_Colorspace</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EVAS_COLORSPACE_ARGB8888 </i></p>
<dd>ARGB 32 bits per pixel, high-byte is Alpha, accessed 1 32bit word at a time.</p>
<dt><i>EVAS_COLORSPACE_YCBCR422P601_PL </i></p>
<dd>YCbCr 4:2:2 Planar, ITU.BT-601 specifications.</dl>
<p> The data poitned to is just an array of row pointer, pointing to the Y rows, then the Cb, then Cr rows</p>
<dl COMPACT>
<dt><i>EVAS_COLORSPACE_YCBCR422P709_PL </i></p>
<dd>YCbCr 4:2:2 Planar, ITU.BT-709 specifications.</dl>
<p> The data poitned to is just an array of row pointer, pointing to the Y rows, then the Cb, then Cr rows</p>
<dl COMPACT>
<dt><i>EVAS_COLORSPACE_RGB565_A5P </i></p>
<dd>16bit rgb565 + Alpha plane at end &#8211; 5 bits of the 8 being used per alpha byte</dl>
<h3>enum <code>_Evas_Event_Flags</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EVAS_EVENT_FLAG_NONE </i></p>
<dd>No fancy flags set.</p>
<dt><i>EVAS_EVENT_FLAG_ON_HOLD </i></p>
<dd>This event is being delivered but should be put &#8216;on hold&#8217; until the on hold flag is unset.</dl>
<p> the event should be used for informational purposes and maybe some indications visually, but not actually perform anything</p>
<h3>enum <code>_Evas_Font_Hinting_Flags</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EVAS_FONT_HINTING_NONE </i></p>
<dd>No font hinting.</p>
<dt><i>EVAS_FONT_HINTING_AUTO </i></p>
<dd>Automatic font hinting.</p>
<dt><i>EVAS_FONT_HINTING_BYTECODE </i></p>
<dd>Bytecode font hinting.</dl>
<h3>enum <code>_Evas_Object_Pointer_Mode</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EVAS_OBJECT_POINTER_MODE_AUTOGRAB </i></p>
<dd>default, X11-like</dl>
<h3>enum <code>_Evas_Render_Op</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EVAS_RENDER_BLEND </i></p>
<dd>default op: d = d*(1-sa) + s</p>
<dt><i>EVAS_RENDER_BLEND_REL </i></p>
<dd>d = d*(1 &#8211; sa) + s*da</p>
<dt><i>EVAS_RENDER_COPY </i></p>
<dd>d = s</p>
<dt><i>EVAS_RENDER_COPY_REL </i></p>
<dd>d = s*da</p>
<dt><i>EVAS_RENDER_ADD </i></p>
<dd>d = d + s</p>
<dt><i>EVAS_RENDER_ADD_REL </i></p>
<dd>d = d + s*da</p>
<dt><i>EVAS_RENDER_SUB </i></p>
<dd>d = d &#8211; s</p>
<dt><i>EVAS_RENDER_SUB_REL </i></p>
<dd>d = d &#8211; s*da</p>
<dt><i>EVAS_RENDER_TINT </i></p>
<dd>d = d*s + d*(1 &#8211; sa) + s*(1 &#8211; da)</p>
<dt><i>EVAS_RENDER_TINT_REL </i></p>
<dd>d = d*(1 &#8211; sa + s)</p>
<dt><i>EVAS_RENDER_MASK </i></p>
<dd>d = d*sa</p>
<dt><i>EVAS_RENDER_MUL </i></p>
<dd>d = d*s</dl>
<h2>Function Documentation</h2>
<h3>EAPI int evas_alloc_error (void)</h3>
<p>Return if any allocation errors have occured during the prior function. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The allocation error flag</dl>
<p> This function will return if any memory allocation errors occured during, and what kind they were. The return value will be one of EVAS_ALLOC_ERROR_NONE, EVAS_ALLOC_ERROR_FATAL or EVAS_ALLOC_ERROR_RECOVERED with each meaning something different. </p>
<p> EVAS_ALLOC_ERROR_NONE means that no errors occured at all and the function worked as expected. </p>
<p> EVAS_ALLOC_ERROR_FATAL means the function was completely unable to perform its job and will have exited as cleanly as possible. The programmer should consider this as a sign of very low memory and should try and safely recover from the prior functions failure (or try free up memory elsewhere and try again after more memory is freed). </p>
<p> EVAS_ALLOC_ERROR_RECOVERED means that an allocation error occured, but was recovered from by evas finding memory of its own it has allocated and freeing what it sees as not really usefully allocated memory. What is freed may vary. Evas may reduce the resolution of images, free cached images or fonts, trhow out pre-rendered data, reduce the complexity of change lists etc. Evas and the program will function as per normal after this, but this is a sign of low memory, and it is suggested that the program try and identify memory it doesn&#8217;t need, and free it. </p>
<p> Example: </p>
<pre> extern Evas_Object *object;
 void callback (void *data, Evas *e, Evas_Object *obj, void *event_info);
 evas_object_event_callback_add(object, EVAS_CALLBACK_MOUSE_DOWN, callback, NULL);
 if (evas_alloc_error() == EVAS_ALLOC_ERROR_FATAL)
 {
 fprintf(stderr, 'ERROR: Completely unable to attach callabck. Must);
 fprintf(stderr, ' destroy object now as it cannot be used.);
 evas_object_del(object);
 object = NULL;
 fprintf(stderr, 'WARNING: Memory is really low. Cleaning out RAM.);
 my_memory_cleanup();
 }
 if (evas_alloc_error() == EVAS_ALLOC_ERROR_RECOVERED)
 {
 fprintf(stderr, 'WARNING: Memory is really low. Cleaning out RAM.);
 my_memory_cleanup();
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References evas_alloc_error(). </p>
<p> Referenced by evas_alloc_error().</p>
<h3>EAPI void evas_color_argb_premul (int a, int * r, int * g, int * b)</h3>
<p>FIXME: . </p>
<h3>EAPI void evas_color_argb_unpremul (int a, int * r, int * g, int * b)</h3>
<p>FIXME: . </p>
<h3>EAPI void evas_color_hsv_to_rgb (float h, float s, float v, int * r, int * g, int * b)</h3>
<p>FIXME: . </p>
<h3>EAPI void evas_color_rgb_to_hsv (int r, int g, int b, float * h, float * s, float * v)</h3>
<p>FIXME: . </p>
<h3>EAPI void evas_damage_rectangle_add (<code>Evas</code> * e, int x, int y, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References evas_list_append(), _Evas_Rectangle::h, _Evas_Rectangle::w, _Evas_Rectangle::x, and _Evas_Rectangle::y.</p>
<h3>EAPI void evas_data_argb_premul (unsigned int * data, unsigned int len)</h3>
<p>FIXME: . </p>
<h3>EAPI void evas_data_argb_unpremul (unsigned int * data, unsigned int len)</h3>
<p>FIXME: . </p>
<h3>EAPI void* evas_data_attach_get (const <code>Evas</code> * e)</h3>
<p>Returns the pointer attached by <code>evas_data_attach_set()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The canvas to attach the pointer to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The pointer attached</dl>
<h3>EAPI void evas_data_attach_set (<code>Evas</code> * e, void * data)</h3>
<p>Attaches a specific pointer to the evas for fetching later. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The canvas to attach the pointer to<br />
 <i>data</i> The pointer to attach</dl>
<h3>EAPI void evas_event_feed_hold (<code>Evas</code> * e, int hold, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_List::data, EVAS_CALLBACK_HOLD, EVAS_EVENT_FLAG_NONE, evas_list_free(), _Evas_Event_Hold::hold, and _Evas_List::next.</p>
<h3>EAPI void evas_event_feed_key_down (<code>Evas</code> * e, const char * keyname, const char * key, const char * string, const char * compose, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_Event_Key_Down::compose, _Evas_List::data, EVAS_CALLBACK_KEY_DOWN, EVAS_EVENT_FLAG_NONE, _Evas_Event_Key_Down::key, _Evas_Event_Key_Down::keyname, _Evas_List::next, and _Evas_Event_Key_Down::string.</p>
<h3>EAPI void evas_event_feed_key_up (<code>Evas</code> * e, const char * keyname, const char * key, const char * string, const char * compose, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_Event_Key_Up::compose, _Evas_List::data, EVAS_CALLBACK_KEY_UP, EVAS_EVENT_FLAG_NONE, _Evas_Event_Key_Up::key, _Evas_Event_Key_Up::keyname, _Evas_List::next, and _Evas_Event_Key_Up::string.</p>
<h3>EAPI void evas_event_feed_mouse_cancel (<code>Evas</code> * e, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_event_feed_mouse_down (<code>Evas</code> * e, int b, <code>Evas_Button_Flags</code> flags, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_Event_Mouse_Down::button, _Evas_List::data, EVAS_CALLBACK_MOUSE_DOWN, EVAS_EVENT_FLAG_NONE, evas_list_free(), and _Evas_List::next.</p>
<h3>EAPI void evas_event_feed_mouse_in (<code>Evas</code> * e, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_Event_Mouse_In::buttons, _Evas_List::data, EVAS_CALLBACK_MOUSE_IN, EVAS_EVENT_FLAG_NONE, evas_list_find(), evas_list_free(), and _Evas_List::next.</p>
<h3>EAPI void evas_event_feed_mouse_move (<code>Evas</code> * e, int x, int y, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_Event_Mouse_In::buttons, _Evas_Event_Mouse_Out::buttons, _Evas_Event_Mouse_Move::buttons, _Evas_List::data, EVAS_CALLBACK_MOUSE_IN, EVAS_CALLBACK_MOUSE_MOVE, EVAS_CALLBACK_MOUSE_OUT, EVAS_EVENT_FLAG_NONE, evas_list_append(), evas_list_find(), evas_list_free(), evas_list_remove(), and _Evas_List::next.</p>
<h3>EAPI void evas_event_feed_mouse_out (<code>Evas</code> * e, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_Event_Mouse_Out::buttons, _Evas_List::data, EVAS_CALLBACK_MOUSE_OUT, EVAS_EVENT_FLAG_NONE, evas_list_free(), and _Evas_List::next.</p>
<h3>EAPI void evas_event_feed_mouse_up (<code>Evas</code> * e, int b, <code>Evas_Button_Flags</code> flags, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_Event_Mouse_Up::button, _Evas_Event_Mouse_In::buttons, _Evas_Event_Mouse_Out::buttons, _Evas_List::data, EVAS_CALLBACK_MOUSE_IN, EVAS_CALLBACK_MOUSE_OUT, EVAS_CALLBACK_MOUSE_UP, EVAS_EVENT_FLAG_NONE, evas_list_find(), evas_list_free(), and _Evas_List::next.</p>
<h3>EAPI void evas_event_feed_mouse_wheel (<code>Evas</code> * e, int direction, int z, unsigned int timestamp, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_List::data, EVAS_CALLBACK_MOUSE_WHEEL, EVAS_EVENT_FLAG_NONE, evas_list_free(), and _Evas_List::next.</p>
<h3>EAPI <code>Evas_Object</code>* evas_focus_get (const <code>Evas</code> * e)</h3>
<p>Retrieve the object that currently has focus. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The Evas canvas to query focus on.</dl>
<p> Returns the object that currently has focus, NULL otherwise. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_object_focus_set</code> </p>
<p> <code>evas_object_focus_get</code> </p>
<p> <code>evas_object_key_grab</code> </p>
<p> <code>evas_object_key_ungrab</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The object that has focus or NULL is there is not one.</dl>
<h3>EAPI <code>Evas_List</code>* evas_font_available_list (const <code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_font_available_list_free (<code>Evas</code> * e, <code>Evas_List</code> * available)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_font_cache_flush (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI int evas_font_cache_get (const <code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_font_cache_set (<code>Evas</code> * e, int size)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_image_cache_flush (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI int evas_image_cache_get (const <code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_image_cache_reload (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_image_cache_set (<code>Evas</code> * e, int size)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_key_lock_add (<code>Evas</code> * e, const char * keyname)</h3>
<p>Adds the keyname to the current list of locks. </p>
<p> Locks can be keys like caps lock, num lock or scroll lock, as well as user defined. This allows custom locks to be added to the evas system at run time. It is then possible to set and unset the lock for other parts of the program to check and act on. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_lock_get</code> </p>
<p> <code>evas_key_lock_del</code> </p>
<p> <code>evas_key_lock_on</code> </p>
<p> <code>evas_key_lock_off</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the key to remove from the modifier list.</dl>
<h3>EAPI void evas_key_lock_del (<code>Evas</code> * e, const char * keyname)</h3>
<p>Removes The keyname from the current list of locks. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_lock_get</code> </p>
<p> <code>evas_key_lock_add</code> </p>
<p> <code>evas_key_lock_on</code> </p>
<p> <code>evas_key_lock_off</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the key to remove from the lock list.</dl>
<h3>EAPI const <code>Evas_Lock</code>* evas_key_lock_get (const <code>Evas</code> * e)</h3>
<p>Returns a handle to the locks available in the system. </p>
<p> This is required to check for locks with the evas_key_lock_is_set_get function. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_lock_add</code> </p>
<p> <code>evas_key_lock_del</code> </p>
<p> <code>evas_key_lock_on</code> </p>
<p> <code>evas_key_lock_off</code> </p>
<p> evas_key_lock_is_set_get</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_Lock handle to query the lock subsystem with evas_key_lock_is_set_get, or NULL on error.</dl>
<h3>EAPI Evas_Bool evas_key_lock_is_set (const <code>Evas_Lock</code> * l, const char * keyname)</h3>
<p>Checks the state of a given lock. </p>
<p> If the lock is set, such as caps lock, this function returns true. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_lock_get</code> </p>
<p> <code>evas_key_lock_add</code> </p>
<p> <code>evas_key_lock_del</code> </p>
<p> <code>evas_key_lock_on</code> </p>
<p> <code>evas_key_lock_off</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>l</i> The current lock set as returned by evas_key_lock_get.<br />
 <i>keyname</i> The name of the lock to add the the list.<br />
 <i>1</i> if the keyname kock is set, 0 otherwise.</dl>
<h3>EAPI void evas_key_lock_off (<code>Evas</code> * e, const char * keyname)</h3>
<p>Disables or turns off the lock with name keyname. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_lock_get</code> </p>
<p> <code>evas_key_lock_add</code> </p>
<p> <code>evas_key_lock_del</code> </p>
<p> <code>evas_key_lock_on</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the lock to un-set.</dl>
<h3>EAPI void evas_key_lock_on (<code>Evas</code> * e, const char * keyname)</h3>
<p>Enables or turns on the lock with name keyname. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_lock_get</code> </p>
<p> <code>evas_key_lock_add</code> </p>
<p> <code>evas_key_lock_del</code> </p>
<p> <code>evas_key_lock_off</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the lock to set.</dl>
<h3>EAPI void evas_key_modifier_add (<code>Evas</code> * e, const char * keyname)</h3>
<p>Adds the keyname to the current list of modifiers. </p>
<p> Modifiers can be keys like shift, alt and ctrl, as well as user defined. This allows custom modifiers to be added to the evas system as run time. It is then possible to set and unset the modifier for other parts of the program to check and act on. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_modifier_del</code> </p>
<p> <code>evas_key_modifier_get</code> </p>
<p> <code>evas_key_modifier_on</code> </p>
<p> <code>evas_key_modifier_off</code> </p>
<p> evas_key_modifier_is_set_get</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the modifier to add to the list.</dl>
<h3>EAPI void evas_key_modifier_del (<code>Evas</code> * e, const char * keyname)</h3>
<p>Removes the keyname from the current list of modifiers. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_modifier_add</code> </p>
<p> <code>evas_key_modifier_get</code> </p>
<p> <code>evas_key_modifier_on</code> </p>
<p> <code>evas_key_modifier_off</code> </p>
<p> evas_key_modifier_is_set_get</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the key to remove from the modifiers list.</dl>
<h3>EAPI const <code>Evas_Modifier</code>* evas_key_modifier_get (const <code>Evas</code> * e)</h3>
<p>Returns a handle to the modifiers available in the system. </p>
<p> This is required to check for modifiers with the evas_key_modifier_is_set_get function. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_modifier_add</code> </p>
<p> <code>evas_key_modifier_del</code> </p>
<p> <code>evas_key_modifier_on</code> </p>
<p> <code>evas_key_modifier_off</code> </p>
<p> evas_key_modifier_is_set_get</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_Modifier handle to query the modifier subsystem with evas_key_modifier_is_set_get, or NULL on error.</dl>
<h3>EAPI Evas_Bool evas_key_modifier_is_set (const <code>Evas_Modifier</code> * m, const char * keyname)</h3>
<p>Checks the state of a given modifier. </p>
<p> If the modifier is set, such as shift being pressed this function returns true. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_modifier_add</code> </p>
<p> <code>evas_key_modifier_del</code> </p>
<p> <code>evas_key_modifier_get</code> </p>
<p> <code>evas_key_modifier_on</code> </p>
<p> <code>evas_key_modifier_off</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>m</i> The current modifier set as returned by evas_key_modifier_get.<br />
 <i>keyname</i> The name of the key to check its status.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the keyname is on, 0 otherwise.</dl>
<h3>EAPI <code>Evas_Modifier_Mask</code> evas_key_modifier_mask_get (const <code>Evas</code> * e, const char * keyname)</h3>
<p>Creates a bit mask from the keyname for use with events to check for the presence of the keyname modifier. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_modifier_add</code> </p>
<p> <code>evas_key_modifier_get</code> </p>
<p> <code>evas_key_modifier_on</code> </p>
<p> <code>evas_key_modifier_off</code> </p>
<p> evas_key_modifier_is_set_get</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>keyname</i> The name of the modifier to create the mask for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the bit mask or 0 if the keyname wasn&#8217;t registered as a modifier.</dl>
<h3>EAPI void evas_key_modifier_off (<code>Evas</code> * e, const char * keyname)</h3>
<p>Disables or turns off the modifier with name keyname. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_modifier_add</code> </p>
<p> <code>evas_key_modifier_get</code> </p>
<p> <code>evas_key_modifier_on</code> </p>
<p> evas_key_modifier_is_set_get</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the modifier to un-set.</dl>
<h3>EAPI void evas_key_modifier_on (<code>Evas</code> * e, const char * keyname)</h3>
<p>Enables or turns on the modifier with name keyname. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_key_modifier_add</code> </p>
<p> <code>evas_key_modifier_get</code> </p>
<p> <code>evas_key_modifier_off</code> </p>
<p> evas_key_modifier_is_set_get</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>keyname</i> The name of the modifier to set.</dl>
<h3>EAPI void evas_norender (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI <code>Evas_Object</code>* evas_object_above_get (const <code>Evas_Object</code> * obj)</h3>
<p>Get the evas object above obj. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> an Evas_Object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Evas_Object directly above</dl>
<h3>EAPI <code>Evas_Object</code>* evas_object_below_get (const <code>Evas_Object</code> * obj)</h3>
<p>Get the evas object below obj. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> an Evas_Object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Evas_Object directly below</dl>
<h3>EAPI <code>Evas_Object</code>* evas_object_bottom_get (const <code>Evas</code> * e)</h3>
<p>Get the lowest evas object on the Evas e. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> an Evas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the lowest object</dl>
<h3>EAPI Evas_Bool evas_object_focus_get (const <code>Evas_Object</code> * obj)</h3>
<p>Test if the object has focus. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to be tested.</dl>
<p> If the passed object is the currently focused object 1 is returned, 0 otherwise. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_object_focus_set</code> </p>
<p> <code>evas_focus_get</code> </p>
<p> <code>evas_object_key_grab</code> </p>
<p> <code>evas_object_key_ungrab</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the object has the focus, 0 otherwise.</dl>
<h3>EAPI void evas_object_focus_set (<code>Evas_Object</code> * obj, Evas_Bool focus)</h3>
<p>Sets focus to the given object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to be focused or unfocused.<br />
 <i>focus</i> set or remove focus to the object.</dl>
<p> Changing focus only affects where key events go. There can be only one object focused at any time. </p>
<p> If the parameter (focus) is set, the passed object will be set as the currently focused object. It will receive all keyboard events that are not exclusive key grabs on other objects. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_object_focus_get</code> </p>
<p> <code>evas_focus_get</code> </p>
<p> <code>evas_object_key_grab</code> </p>
<p> <code>evas_object_key_ungrab</code></dl>
<p> References EVAS_CALLBACK_FOCUS_IN, and EVAS_CALLBACK_FOCUS_OUT.</p>
<h3>EAPI <code>Evas_Colorspace</code> evas_object_image_colorspace_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References EVAS_COLORSPACE_ARGB8888.</p>
<h3>EAPI void evas_object_image_colorspace_set (<code>Evas_Object</code> * obj, <code>Evas_Colorspace</code> cspace)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI double evas_object_image_load_dpi_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_image_load_dpi_set (<code>Evas_Object</code> * obj, double dpi)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI int evas_object_image_load_scale_down_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_image_load_scale_down_set (<code>Evas_Object</code> * obj, int scale_down)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_image_load_size_set (<code>Evas_Object</code> * obj, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI <code>Evas_Native_Surface</code>* evas_object_image_native_surface_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_image_native_surface_set (<code>Evas_Object</code> * obj, <code>Evas_Native_Surface</code> * surf)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_image_pixels_get_callback_set (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *o) func, void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI Evas_Bool evas_object_image_pixels_import (<code>Evas_Object</code> * obj, <code>Evas_Pixel_Import_Source</code> * pixels)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References EVAS_PIXEL_FORMAT_ARGB32, and EVAS_PIXEL_FORMAT_YUV420P_601.</p>
<h3>EAPI void evas_object_image_reload (<code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_clip_set_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *clip) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_clip_set_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *clip) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_clip_unset_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_clip_unset_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_color_set_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, int r, int g, int b, int a) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_color_set_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, int r, int g, int b, int a) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_hide_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_hide_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_layer_set_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, int l) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_layer_set_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, int l) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_lower_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_lower_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_move_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_move_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_raise_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_raise_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_resize_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_resize_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_show_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_show_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_stack_above_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *above) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_stack_above_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *above) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_intercept_stack_below_callback_add (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *below) func, const void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void* evas_object_intercept_stack_below_callback_del (<code>Evas_Object</code> * obj, void(*)(void *data, <code>Evas_Object</code> *obj, <code>Evas_Object</code> *below) func)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI Evas_Bool evas_object_key_grab (<code>Evas_Object</code> * obj, const char * keyname, <code>Evas_Modifier_Mask</code> modifiers, <code>Evas_Modifier_Mask</code> not_modifiers, Evas_Bool exclusive)</h3>
<p>Requests keyname key events be directed to obj. </p>
<p> Key grabs allow an object to receive key events for specific key strokes even if another object has focus. If the grab is non-exclusive then all objects that have grabs on the key will get the event, however if the grab is exclusive, no other object can get a grab on the key and only that object will get the event. </p>
<p> keyname is a platform dependent symbolic name for the key pressed. It is sometimes possible to convert the string to an ASCII value of the key, but not always for example the enter key may be returned as the string &#8216;Enter&#8217;. </p>
<p> Typical platforms are Linux frame buffer (Ecore_FB) and X server (Ecore_X) when using Evas with Ecore and Ecore_Evas. </p>
<p> For a list of keynames for the Linux frame buffer, please refer to the Ecore_FB documentation. </p>
<p> modifiers and not_modifiers are bit masks of all the modifiers that are required and not required respectively for the new grab. Modifiers can be things such as shift and ctrl as well as user defigned types via evas_key_modifier_add. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_object_key_ungrab</code> </p>
<p> <code>evas_object_focus_set</code> </p>
<p> <code>evas_object_focus_get</code> </p>
<p> <code>evas_focus_get</code> </p>
<p> <code>evas_key_modifier_add</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the object to direct keyname events to.<br />
 <i>keyname</i> the key to request events for.<br />
 <i>modifiers</i> a mask of modifiers that should be present to trigger the event.<br />
 <i>not_modifiers</i> a mask of modifiers that should not be present to trigger the event.<br />
 <i>exclusive</i> request that the obj is the only object receiving the keyname events.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Boolean indicating whether the grab succeeded</dl>
<h3>EAPI void evas_object_key_ungrab (<code>Evas_Object</code> * obj, const char * keyname, <code>Evas_Modifier_Mask</code> modifiers, <code>Evas_Modifier_Mask</code> not_modifiers)</h3>
<p>Request that the grab on obj be removed. </p>
<p> Removes the grab on obj if keyname, modifiers, and not_modifiers match. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_object_key_grab</code> </p>
<p> <code>evas_object_focus_set</code> </p>
<p> <code>evas_object_focus_get</code> </p>
<p> <code>evas_focus_get</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the object that has an existing grab.<br />
 <i>keyname</i> the key the grab is for.<br />
 <i>modifiers</i> a mask of modifiers that should be present to trigger the event.<br />
 <i>not_modifiers</i> a mask of modifiers that should not be present to trigger the event.</dl>
<h3>EAPI void evas_object_lower (<code>Evas_Object</code> * obj)</h3>
<p>Lower obj to the bottom of its layer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the object to lower</dl>
<h3>EAPI Evas_Object_Pointer_Mode evas_object_pointer_mode_get (const <code>Evas_Object</code> * obj)</h3>
<p>Determine how pointer will behave. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer behavior.</dl>
<h3>EAPI void evas_object_pointer_mode_set (<code>Evas_Object</code> * obj, Evas_Object_Pointer_Mode setting)</h3>
<p>Set pointer behavior. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i><br />
 <i>setting</i> desired behavior.</dl>
<p> This function has direct effect on event callbacks related to mouse. </p>
<p> If setting is EVAS_OBJECT_POINTER_MODE_AUTOGRAB, then when mouse is down at this object, events will be restricted to it as source, mouse moves, for example, will be emitted even if outside this object area. </p>
<p> If setting is EVAS_OBJECT_POINTER_MODE_NOGRAB, then events will be emitted just when inside this object area. </p>
<p> The default value is EVAS_OBJECT_POINTER_MODE_AUTOGRAB.</p>
<h3>EAPI void evas_object_raise (<code>Evas_Object</code> * obj)</h3>
<p>Raise obj to the top of its layer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the object to raise</dl>
<h3>EAPI <code>Evas_Object</code>* evas_object_rectangle_add (<code>Evas</code> * e)</h3>
<p>Adds a rectangle to the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new rectangle object.</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Find a documentation group to put this under.</dl>
<h3>EAPI <code>Evas_List</code>* evas_object_smart_members_get (const <code>Evas_Object</code> * obj)</h3>
<p>Gets the list of the member objects of an Evas_Object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the Evas_Object you want to get the list of member objects</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns the list of the member objects of <i>obj</i>. The returned list should be freed with <code>evas_list_free()</code> when you no longer need it</dl>
<p> References evas_list_append().</p>
<h3>EAPI void evas_object_stack_above (<code>Evas_Object</code> * obj, <code>Evas_Object</code> * above)</h3>
<p>Stack obj immediately above above. </p>
<p> If obj is a member of a smart object, then above must also be a member of the same smart object. </p>
<p> Similarly, if obj is not a member of smart object, above may not either. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the object to stack<br />
 <i>above</i> the object above which to stack</dl>
<h3>EAPI void evas_object_stack_below (<code>Evas_Object</code> * obj, <code>Evas_Object</code> * below)</h3>
<p>Stack obj immediately below below. </p>
<p> If obj is a member of a smart object, then below must also be a member of the same smart object. </p>
<p> Similarly, if obj is not a member of smart object, below may not either. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the object to stack<br />
 <i>below</i> the object below which to stack</dl>
<h3>EAPI <code>Evas_Object</code>* evas_object_text_add (<code>Evas</code> * e)</h3>
<p>Creates a new text Evas_Object on the provided Evas canvas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The Evas canvas to create the text object upon.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_object_text_font_source_set</code> </p>
<p> <code>evas_object_text_font_set</code> </p>
<p> <code>evas_object_text_text_set</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on error, A pointer to a new Evas_Object on success.</dl>
<h3>EAPI Evas_Coord evas_object_text_ascent_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI int evas_object_text_char_coords_get (const <code>Evas_Object</code> * obj, Evas_Coord x, Evas_Coord y, Evas_Coord * cx, Evas_Coord * cy, Evas_Coord * cw, Evas_Coord * ch)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI int evas_object_text_char_pos_get (const <code>Evas_Object</code> * obj, int pos, Evas_Coord * cx, Evas_Coord * cy, Evas_Coord * cw, Evas_Coord * ch)</h3>
<p>Retrieve position and dimension information of a character within a text Evas_Object. </p>
<p> This function is used to obtain the X, Y, width and height of a the character located at pos within the Evas_Object obj. obj must be a text object as created with <code>evas_object_text_add()</code>. Any of the Evas_Coord parameters (cx, cy, cw, ch) may be NULL in which case no value will be assigned to that parameter. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The text object to retrieve position information for.<br />
 <i>pos</i> The character position to request co-ordinates for.<br />
 <i>cx</i> A pointer to an Evas_Coord to store the X value in (can be NULL).<br />
 <i>cy</i> A pointer to an Evas_Coord to store the Y value in (can be NULL).<br />
 <i>cw</i> A pointer to an Evas_Coord to store the Width value in (can be NULL).<br />
 <i>ch</i> A pointer to an Evas_Coord to store the Height value in (can be NULL).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on error, 1 on success.</dl>
<h3>EAPI Evas_Coord evas_object_text_descent_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_font_get (const <code>Evas_Object</code> * obj, const char ** font, Evas_Font_Size * size)</h3>
<p>Query evas for font information of a text Evas_Object. </p>
<p> This function allows the font name and size of a text Evas_Object as created with <code>evas_object_text_add()</code> to be queried. Be aware that the font name string is still owned by Evas and should NOT have free() called on it by the caller of the function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The evas text object to query for font information.<br />
 <i>font</i> A pointer to the location to store the font name in (may be NULL).<br />
 <i>size</i> A pointer to the location to store the font size in (may be NULL).</dl>
<h3>EAPI void evas_object_text_font_set (<code>Evas_Object</code> * obj, const char * font, Evas_Font_Size size)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI const char* evas_object_text_font_source_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_font_source_set (<code>Evas_Object</code> * obj, const char * font_source)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_glow2_color_get (const <code>Evas_Object</code> * obj, int * r, int * g, int * b, int * a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_glow2_color_set (<code>Evas_Object</code> * obj, int r, int g, int b, int a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_glow_color_get (const <code>Evas_Object</code> * obj, int * r, int * g, int * b, int * a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_glow_color_set (<code>Evas_Object</code> * obj, int r, int g, int b, int a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI Evas_Coord evas_object_text_horiz_advance_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI Evas_Coord evas_object_text_inset_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI Evas_Coord evas_object_text_max_ascent_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI Evas_Coord evas_object_text_max_descent_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_outline_color_get (const <code>Evas_Object</code> * obj, int * r, int * g, int * b, int * a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_outline_color_set (<code>Evas_Object</code> * obj, int r, int g, int b, int a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_shadow_color_get (const <code>Evas_Object</code> * obj, int * r, int * g, int * b, int * a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_shadow_color_set (<code>Evas_Object</code> * obj, int r, int g, int b, int a)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI Evas_Text_Style_Type evas_object_text_style_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_style_pad_get (const <code>Evas_Object</code> * obj, int * l, int * r, int * t, int * b)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_object_text_style_set (<code>Evas_Object</code> * obj, Evas_Text_Style_Type style)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI const char* evas_object_text_text_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the text currently being displayed by the given evas text object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas text object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The text currently being displayed. Do not free it.</dl>
<h3>EAPI void evas_object_text_text_set (<code>Evas_Object</code> * obj, const char * text)</h3>
<p>Sets the text to be displayed by the given evas text object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> Evas text object.<br />
 <i>text</i> Text to display.</dl>
<h3>EAPI Evas_Coord evas_object_text_vert_advance_get (const <code>Evas_Object</code> * obj)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI <code>Evas_Object</code>* evas_object_textblock_add (<code>Evas</code> * e)</h3>
<p>Adds a textblock to the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new textblock object.</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Find a documentation group to put this under.</dl>
<h3>EAPI const Evas_Textblock_Style* evas_object_textblock_style_get (const <code>Evas_Object</code> * obj)</h3>
<p>to be documented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> to be documented.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>to be documented.</dl>
<h3>EAPI void evas_object_textblock_style_set (<code>Evas_Object</code> * obj, Evas_Textblock_Style * ts)</h3>
<p>to be documented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> to be documented.<br />
 <i>ts</i> to be documented.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns no value.</dl>
<p> References evas_list_append(), and evas_list_remove().</p>
<h3>EAPI void evas_object_textblock_text_markup_set (<code>Evas_Object</code> * obj, const char * text)</h3>
<p>to be documented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ts</i> to be documented.<br />
 <i>text</i> to be documented.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return no value.</dl>
<p> References _Evas_List::data, and _Evas_List::next.</p>
<h3>EAPI <code>Evas_Object</code>* evas_object_top_get (const <code>Evas</code> * e)</h3>
<p>Get the highest evas object on the Evas e. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> an Evas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the highest object</dl>
<h3>EAPI void evas_obscured_clear (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References evas_list_remove().</p>
<h3>EAPI void evas_obscured_rectangle_add (<code>Evas</code> * e, int x, int y, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References evas_list_append(), _Evas_Rectangle::h, _Evas_Rectangle::w, _Evas_Rectangle::x, and _Evas_Rectangle::y.</p>
<h3>EAPI void evas_render (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_render_idle_flush (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI <code>Evas_List</code>* evas_render_updates (<code>Evas</code> * e)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_render_updates_free (<code>Evas_List</code> * updates)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References _Evas_List::data, and evas_list_remove().</p>
<h3>EAPI const <code>Evas_Smart_Class</code>* evas_smart_class_get (const <code>Evas_Smart</code> * s)</h3>
<p>Get the Evas_Smart_Class of an Evas_Smart. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>s</i> the Evas_Smart</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Evas_Smart_Class</dl>
<h3>EAPI <code>Evas_Smart</code>* evas_smart_class_new (const <code>Evas_Smart_Class</code> * sc)</h3>
<p>Creates an Evas_Smart from an Evas_Smart_Class. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>Evas_Smart_Class</i> the smart class definition</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>an Evas_Smart</dl>
<p> References _Evas_Smart_Class::version.</p>
<h3>EAPI void* evas_smart_data_get (const <code>Evas_Smart</code> * s)</h3>
<p>Get the data pointer set on an Evas_Smart. </p>
<p> This data pointer is set either as the final parameter to evas_smart_new or as the data field in the Evas_Smart_Class passed in to evas_smart_class_new </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>Evas_Smart</i></dl>
<h3>EAPI void evas_smart_free (<code>Evas_Smart</code> * s)</h3>
<p>Free an Evas_Smart. </p>
<p> If this smart was created using <code>evas_smart_class_new()</code>, the associated Evas_Smart_Class will not be freed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>s</i> the Evas_Smart to free</dl>
<h3>EAPI int evas_string_char_next_get (const char * str, int pos, int * decoded)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI int evas_string_char_prev_get (const char * str, int pos, int * decoded)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed.</p>
<h3>EAPI void evas_textblock_style_free (Evas_Textblock_Style * ts)</h3>
<p>Destroys a textblock style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>The</i> textblock style to free.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns no value.</dl>
<h3>EAPI const char* evas_textblock_style_get (const Evas_Textblock_Style * ts)</h3>
<p>to be documented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ts</i> to be documented.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>to be documented.</dl>
<h3>EAPI Evas_Textblock_Style* evas_textblock_style_new (void)</h3>
<p>Creates a new textblock style. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new textblock style.</dl>
<h3>EAPI void evas_textblock_style_set (Evas_Textblock_Style * ts, const char * text)</h3>
<p>to be documented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ts</i> to be documented.<br />
 <i>text</i> to be documented.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns no value.</dl>
<p> References _Evas_List::data, and _Evas_List::next.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
