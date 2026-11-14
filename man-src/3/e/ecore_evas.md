---
title: "ecore_evas(3)"
name: "ecore_evas"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_evas/"
description: "Ecore_Evas.h – Evas wrapper functions."
---

<p>Ecore_Evas.h &#8211; Evas wrapper functions. </p>
<h2>Synopsis</h2>
<h3>Functions</h3>
<p>EAPI int <code>ecore_evas_engine_type_supported_get</code> (Ecore_Evas_Engine_Type engine)<br />
 <i>Query if a particular renginering engine target has support. </i><br />
 EAPI int <code>ecore_evas_init</code> (void)<br />
 <i>Init the Evas system. </i><br />
 EAPI int <code>ecore_evas_shutdown</code> (void)<br />
 <i>Shut down the Evas system. </i><br />
 EAPI Evas_List * <code>ecore_evas_engines_get</code> (void)<br />
 <i>Returns a list of supported engines names. </i><br />
 EAPI void <code>ecore_evas_engines_free</code> (Evas_List *engines)<br />
 <i>Free list returned by </i><code>ecore_evas_engines_get()</code>.<br />
 EAPI Ecore_Evas * <code>ecore_evas_new</code> (const char *engine_name, int x, int y, int w, int h, const char *extra_options)<br />
 <i>Creates a new Ecore_Evas based on engine name and common parameters. </i><br />
 EAPI Ecore_Evas * <code>ecore_evas_software_x11_new</code> (const char *disp_name, Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_software_x11_window_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_software_x11_subwindow_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_software_x11_direct_resize_set</code> (Ecore_Evas *ee, int on)<br />
 <i>To be documented. </i><br />
 EAPI int <code>ecore_evas_software_x11_direct_resize_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_software_x11_extra_event_window_add</code> (Ecore_Evas *ee, Ecore_X_Window win)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_Evas * <code>ecore_evas_gl_x11_new</code> (const char *disp_name, Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_gl_x11_window_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_gl_x11_subwindow_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_gl_x11_direct_resize_set</code> (Ecore_Evas *ee, int on)<br />
 <i>To be documented. </i><br />
 EAPI int <code>ecore_evas_gl_x11_direct_resize_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_gl_x11_extra_event_window_add</code> (Ecore_Evas *ee, Ecore_X_Window win)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_Evas * <code>ecore_evas_xrender_x11_new</code> (const char *disp_name, Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_xrender_x11_window_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_xrender_x11_subwindow_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_xrender_x11_direct_resize_set</code> (Ecore_Evas *ee, int on)<br />
 <i>To be documented. </i><br />
 EAPI int <code>ecore_evas_xrender_x11_direct_resize_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_xrender_x11_extra_event_window_add</code> (Ecore_Evas *ee, Ecore_X_Window win)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_Evas * <code>ecore_evas_software_x11_16_new</code> (const char *disp_name, Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_software_x11_16_window_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_X_Window <code>ecore_evas_software_x11_16_subwindow_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_software_x11_16_direct_resize_set</code> (Ecore_Evas *ee, int on)<br />
 <i>To be documented. </i><br />
 EAPI int <code>ecore_evas_software_x11_16_direct_resize_get</code> (Ecore_Evas *ee)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_evas_software_x11_16_extra_event_window_add</code> (Ecore_Evas *ee, Ecore_X_Window win)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_Evas * <code>ecore_evas_fb_new</code> (char *disp_name, int rotation, int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_Evas * <code>ecore_evas_buffer_new</code> (int w, int h)<br />
 <i>To be documented. </i><br />
 EAPI Ecore_Evas * <code>ecore_evas_ecore_evas_get</code> (Evas *e)<br />
 <i>Return the Ecore_Evas for this Evas. </i><br />
 EAPI void <code>ecore_evas_free</code> (Ecore_Evas *ee)<br />
 <i>Free an Ecore_Evas. </i><br />
 EAPI void * <code>ecore_evas_data_get</code> (Ecore_Evas *ee, const char *key)<br />
 <i>Retrieve user data associated with an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_data_set</code> (Ecore_Evas *ee, const char *key, const void *data)<br />
 <i>Store user data in an Ecore_Evas structure. </i><br />
 EAPI void <code>ecore_evas_callback_resize_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas resize events. </i><br />
 EAPI void <code>ecore_evas_callback_move_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas move events. </i><br />
 EAPI void <code>ecore_evas_callback_show_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas show events. </i><br />
 EAPI void <code>ecore_evas_callback_hide_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas hide events. </i><br />
 EAPI void <code>ecore_evas_callback_delete_request_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas delete request events. </i><br />
 EAPI void <code>ecore_evas_callback_destroy_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas destroy events. </i><br />
 EAPI void <code>ecore_evas_callback_focus_in_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas focus in events. </i><br />
 EAPI void <code>ecore_evas_callback_focus_out_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas focus out events. </i><br />
 EAPI void <code>ecore_evas_callback_sticky_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas sticky events. </i><br />
 EAPI void <code>ecore_evas_callback_unsticky_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas un-sticky events. </i><br />
 EAPI void <code>ecore_evas_callback_mouse_in_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas mouse in events. </i><br />
 EAPI void <code>ecore_evas_callback_mouse_out_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas mouse out events. </i><br />
 EAPI void <code>ecore_evas_callback_pre_render_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas mouse pre render events. </i><br />
 EAPI void <code>ecore_evas_callback_post_render_set</code> (Ecore_Evas *ee, void(*func)(Ecore_Evas *ee))<br />
 <i>Set a callback for Ecore_Evas mouse post render events. </i><br />
 EAPI Evas * <code>ecore_evas_get</code> (Ecore_Evas *ee)<br />
 <i>Get an Ecore_Evas&#8217;s Evas. </i><br />
 EAPI void <code>ecore_evas_move</code> (Ecore_Evas *ee, int x, int y)<br />
 <i>Move an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_managed_move</code> (Ecore_Evas *ee, int x, int y)<br />
 <i>Provide Managed move co-ordinates for an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_resize</code> (Ecore_Evas *ee, int w, int h)<br />
 <i>Resize an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_move_resize</code> (Ecore_Evas *ee, int x, int y, int w, int h)<br />
 <i>Resize an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_geometry_get</code> (Ecore_Evas *ee, int *x, int *y, int *w, int *h)<br />
 <i>Get the geometry of an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_rotation_set</code> (Ecore_Evas *ee, int rot)<br />
 <i>Set the rotation of an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_rotation_get</code> (Ecore_Evas *ee)<br />
 <i>Set the rotation of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_shaped_set</code> (Ecore_Evas *ee, int shaped)<br />
 <i>Set whether an Ecore_Evas is shaped or not. </i><br />
 EAPI int <code>ecore_evas_shaped_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas is shaped or not. </i><br />
 EAPI void <code>ecore_evas_alpha_set</code> (Ecore_Evas *ee, int alpha)<br />
 <i>Set whether an Ecore_Evas has an alpha channel or not. </i><br />
 EAPI int <code>ecore_evas_alpha_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas has an alpha channel. </i><br />
 EAPI void <code>ecore_evas_show</code> (Ecore_Evas *ee)<br />
 <i>Show an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_hide</code> (Ecore_Evas *ee)<br />
 <i>Hide an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_visibility_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window is visible or not. </i><br />
 EAPI void <code>ecore_evas_raise</code> (Ecore_Evas *ee)<br />
 <i>Raise and Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_lower</code> (Ecore_Evas *ee)<br />
 <i>Lower an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_activate</code> (Ecore_Evas *ee)<br />
 <i>Activate (set focus to, via the window manager) an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_title_set</code> (Ecore_Evas *ee, const char *t)<br />
 <i>Set the title of an Ecore_Evas&#8217; window. </i><br />
 EAPI const char * <code>ecore_evas_title_get</code> (Ecore_Evas *ee)<br />
 <i>Get the title of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_name_class_set</code> (Ecore_Evas *ee, const char *n, const char *c)<br />
 <i>Set the name and class of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_name_class_get</code> (Ecore_Evas *ee, const char **n, const char **c)<br />
 <i>Get the name and class of an Ecore_Evas&#8217; window </i>ee The Ecore_Evas to query n A pointer to a string to place the name in.<br />
 EAPI void <code>ecore_evas_size_min_set</code> (Ecore_Evas *ee, int w, int h)<br />
 <i>Set the min size of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_size_min_get</code> (Ecore_Evas *ee, int *w, int *h)<br />
 <i>Get the min size of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_size_max_set</code> (Ecore_Evas *ee, int w, int h)<br />
 <i>Set the max size of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_size_max_get</code> (Ecore_Evas *ee, int *w, int *h)<br />
 <i>Get the max size of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_size_base_set</code> (Ecore_Evas *ee, int w, int h)<br />
 <i>Set the base size of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_size_base_get</code> (Ecore_Evas *ee, int *w, int *h)<br />
 <i>Get the base size of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_size_step_set</code> (Ecore_Evas *ee, int w, int h)<br />
 <i>Set the step size of an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_size_step_get</code> (Ecore_Evas *ee, int *w, int *h)<br />
 <i>Get the step size of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_cursor_set</code> (Ecore_Evas *ee, const char *file, int layer, int hot_x, int hot_y)<br />
 <i>Set the cursor of an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_object_cursor_set</code> (Ecore_Evas *ee, Evas_Object *obj, int layer, int hot_x, int hot_y)<br />
 <i>Set the cursor of an Ecore_Evas. </i><br />
 EAPI void <code>ecore_evas_cursor_get</code> (Ecore_Evas *ee, Evas_Object **obj, int *layer, int *hot_x, int *hot_y)<br />
 <i>Get information about an Ecore_Evas&#8217; cursor. </i><br />
 EAPI void <code>ecore_evas_layer_set</code> (Ecore_Evas *ee, int layer)<br />
 <i>Set the layer of an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_layer_get</code> (Ecore_Evas *ee)<br />
 <i>Get the layer of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_focus_set</code> (Ecore_Evas *ee, int on)<br />
 <i>Set the focus of an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_focus_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window is focused or not. </i><br />
 EAPI void <code>ecore_evas_iconified_set</code> (Ecore_Evas *ee, int on)<br />
 <i>Iconify or uniconify an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_iconified_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window is iconified or not. </i><br />
 EAPI void <code>ecore_evas_borderless_set</code> (Ecore_Evas *ee, int on)<br />
 <i>Set whether an Ecore_Evas&#8217; window is borderless or not. </i><br />
 EAPI int <code>ecore_evas_borderless_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window is borderless or not. </i><br />
 EAPI void <code>ecore_evas_override_set</code> (Ecore_Evas *ee, int on)<br />
 <i>Tell the WM whether or not to ignore an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_override_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window is overridden or not. </i><br />
 EAPI void <code>ecore_evas_maximized_set</code> (Ecore_Evas *ee, int on)<br />
 <i>Maximize (or unmaximize) an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_maximized_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window is maximized or not. </i><br />
 EAPI void <code>ecore_evas_fullscreen_set</code> (Ecore_Evas *ee, int on)<br />
 <i>Set whether or not an Ecore_Evas&#8217; window is fullscreen. </i><br />
 EAPI int <code>ecore_evas_fullscreen_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window is fullscreen or not. </i><br />
 EAPI void <code>ecore_evas_avoid_damage_set</code> (Ecore_Evas *ee, Ecore_Evas_Avoid_Damage_Type on)<br />
 <i>Set whether or not an Ecore_Evas&#8217; window should avoid damage. </i><br />
 EAPI Ecore_Evas_Avoid_Damage_Type <code>ecore_evas_avoid_damage_get</code> (Ecore_Evas *ee)<br />
 <i>Query whether an Ecore_Evas&#8217; window avoids damage or not. </i><br />
 EAPI void <code>ecore_evas_withdrawn_set</code> (Ecore_Evas *ee, int withdrawn)<br />
 <i>Set the withdrawn state of an Ecore_Evas&#8217; window. </i><br />
 EAPI int <code>ecore_evas_withdrawn_get</code> (Ecore_Evas *ee)<br />
 <i>Returns the withdrawn state of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_sticky_set</code> (Ecore_Evas *ee, int sticky)<br />
 <i>Set the sticky state of an Ecore_Evas window. </i><br />
 EAPI int <code>ecore_evas_sticky_get</code> (Ecore_Evas *ee)<br />
 <i>Returns the sticky state of an Ecore_Evas&#8217; window. </i><br />
 EAPI void <code>ecore_evas_ignore_events_set</code> (Ecore_Evas *ee, int ignore)<br />
 <i>Set if this evas should ignore events. </i><br />
 EAPI int <code>ecore_evas_ignore_events_get</code> (Ecore_Evas *ee)<br />
 <i>Returns the ignore state of an Ecore_Evas&#8217; window. </i></p>
<h2>Detailed Description</h2>
<p>Evas wrapper functions. </p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_evas_activate (Ecore_Evas * ee)</h3>
<p>Activate (set focus to, via the window manager) an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to activate.</dl>
<p> This functions activates the Ecore_Evas.</p>
<h3>EAPI int ecore_evas_alpha_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas has an alpha channel. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to query.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee has an alpha channel, 0 if it does not.</dl>
<p> This function returns 1 if ee has an alpha channel, and 0 if it does not.</p>
<h3>EAPI void ecore_evas_alpha_set (Ecore_Evas * ee, int alpha)</h3>
<p>Set whether an Ecore_Evas has an alpha channel or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to shape<br />
 <i>alpha</i> 1 to enable the alpha channel, 0 to disable it</dl>
<p> This function allows you to make an Ecore_Evas translucent using an alpha channel. See <code>ecore_evas_shaped_set()</code> for details. The difference between a shaped window and a window with an alpha channel is that an alpha channel supports multiple levels of transpararency, as opposed to the 1 bit transparency of a shaped window (a pixel is either opaque, or it&#8217;s transparent).</p>
<h3>EAPI Ecore_Evas_Avoid_Damage_Type ecore_evas_avoid_damage_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window avoids damage or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee avoids damage, 0 if not.</dl>
<h3>EAPI void ecore_evas_avoid_damage_set (Ecore_Evas * ee, Ecore_Evas_Avoid_Damage_Type on)</h3>
<p>Set whether or not an Ecore_Evas&#8217; window should avoid damage. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>on</i> 1 to avoid damage, 0 to not</dl>
<p> This function causes ee to be drawn to a pixmap to avoid recalculations. On expose events it will copy from the pixmap to the window.</p>
<h3>EAPI int ecore_evas_borderless_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window is borderless or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee is borderless, 0 if not.</dl>
<h3>EAPI void ecore_evas_borderless_set (Ecore_Evas * ee, int on)</h3>
<p>Set whether an Ecore_Evas&#8217; window is borderless or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>on</i> 1 for borderless, 0 for bordered.</dl>
<p> This function makes ee borderless if on is 1, or bordered if on is 0.</p>
<h3>EAPI Ecore_Evas* ecore_evas_buffer_new (int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_buffer_new(). </p>
<p> Referenced by ecore_evas_buffer_new().</p>
<h3>EAPI void ecore_evas_callback_delete_request_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas delete request events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee gets a delete request.</p>
<h3>EAPI void ecore_evas_callback_destroy_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas destroy events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee is destroyed.</p>
<h3>EAPI void ecore_evas_callback_focus_in_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas focus in events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee gets focus.</p>
<h3>EAPI void ecore_evas_callback_focus_out_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas focus out events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee loses focus.</p>
<h3>EAPI void ecore_evas_callback_hide_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas hide events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee is hidden.</p>
<h3>EAPI void ecore_evas_callback_mouse_in_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas mouse in events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever the mouse enters ee.</p>
<h3>EAPI void ecore_evas_callback_mouse_out_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas mouse out events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever the mouse leaves ee.</p>
<h3>EAPI void ecore_evas_callback_move_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas move events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee is moved.</p>
<h3>EAPI void ecore_evas_callback_post_render_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas mouse post render events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called just after the evas in ee is rendered.</p>
<h3>EAPI void ecore_evas_callback_pre_render_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas mouse pre render events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called just before the evas in ee is rendered.</p>
<h3>EAPI void ecore_evas_callback_resize_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas resize events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee is resized.</p>
<h3>EAPI void ecore_evas_callback_show_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas show events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee is shown.</p>
<h3>EAPI void ecore_evas_callback_sticky_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas sticky events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee becomes sticky.</p>
<h3>EAPI void ecore_evas_callback_unsticky_set (Ecore_Evas * ee, void(*)(Ecore_Evas *ee) func)</h3>
<p>Set a callback for Ecore_Evas un-sticky events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set callbacks on<br />
 <i>func</i> The function to call</dl>
<p> A call to this function will set a callback on an Ecore_Evas, causing func to be called whenever ee becomes un-sticky.</p>
<h3>EAPI void ecore_evas_cursor_get (Ecore_Evas * ee, Evas_Object ** obj, int * layer, int * hot_x, int * hot_y)</h3>
<p>Get information about an Ecore_Evas&#8217; cursor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>obj</i> A pointer to an Evas_Object to place the cursor Evas_Object.<br />
 <i>layer</i> A pointer to an int to place the cursor&#8217;s layer in..<br />
 <i>hot_x</i> A pointer to an int to place the cursor&#8217;s hot_x coordinate in.<br />
 <i>hot_y</i> A pointer to an int to place the cursor&#8217;s hot_y coordinate in.</dl>
<p> This function queries information about an Ecore_Evas&#8217; cursor.</p>
<h3>EAPI void ecore_evas_cursor_set (Ecore_Evas * ee, const char * file, int layer, int hot_x, int hot_y)</h3>
<p>Set the cursor of an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>file</i> The path to an image file for the cursor<br />
 <i>layer</i><br />
 <i>hot_x</i> The x coordinate of the cursor&#8217;s hot spot<br />
 <i>hot_y</i> The y coordinate of the cursor&#8217;s hot spot</dl>
<p> This function makes the mouse cursor over ee be the image specified by file. The actual point within the image that the mouse is at is specified by hot_x and hot_y, which are coordinates with respect to the top left corner of the cursor image.</p>
<h3>EAPI void* ecore_evas_data_get (Ecore_Evas * ee, const char * key)</h3>
<p>Retrieve user data associated with an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to retrieve the user data from.<br />
 <i>key</i> The key which the user data to be retrieved is associated with.</dl>
<p> This function retrieves user specific data that has been stored within an Ecore_Evas structure with <code>ecore_evas_data_set()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on error or no data found, A pointer to the user data on success.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>ecore_evas_data_set</code></dl>
<h3>EAPI void ecore_evas_data_set (Ecore_Evas * ee, const char * key, const void * data)</h3>
<p>Store user data in an Ecore_Evas structure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>eeThe</i> Ecore_Evas to store the user data in.<br />
 <i>keyA</i> unique string to associate the user data against. Cannot be NULL.<br />
 <i>dataA</i> pointer to the user data to store.</dl>
<p> This function associates the data with a key which is stored by the Ecore_Evas ee. Be aware that a call to <code>ecore_evas_free()</code> will not free any memory for the associated user data, this is the responsibility of the caller. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>ecore_evas_free</code></dl>
<h3>EAPI Ecore_Evas* ecore_evas_ecore_evas_get (Evas * e)</h3>
<p>Return the Ecore_Evas for this Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The Evas to get the Ecore_Evas from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Ecore_Evas that holds this Evas</dl>
<h3>EAPI int ecore_evas_engine_type_supported_get (Ecore_Evas_Engine_Type engine)</h3>
<p>Query if a particular renginering engine target has support. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>engine</i> The engine to check support for</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the particualr engine is supported, 0 if it is not</dl>
<p> Query if engine </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>engine</i> is supported by ecore_evas. 1 is returned if it is, and 0 is returned if it is not supported.</dl>
<h3>EAPI Evas_List* ecore_evas_engines_get (void)</h3>
<p>Returns a list of supported engines names. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>newly allocated list with engines names. Engines names strings are internal and should be considered constants, do not free them, to avoid problems use <code>ecore_evas_engines_free()</code></dl>
<h3>EAPI Ecore_Evas* ecore_evas_fb_new (char * disp_name, int rotation, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_fb_new(), ecore_fb_callback_gain_set(), ecore_fb_callback_lose_set(), ecore_fb_init(), and ecore_time_get(). </p>
<p> Referenced by ecore_evas_fb_new().</p>
<h3>EAPI int ecore_evas_focus_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window is focused or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee if focused, 0 if not.</dl>
<h3>EAPI void ecore_evas_focus_set (Ecore_Evas * ee, int on)</h3>
<p>Set the focus of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>on</i> 1 for focus, 0 to defocus.</dl>
<p> This function focuses ee if on is 1, or defocuses ee if on is 0.</p>
<h3>EAPI void ecore_evas_free (Ecore_Evas * ee)</h3>
<p>Free an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to free</dl>
<p> This frees up any memory used by the Ecore_Evas.</p>
<h3>EAPI int ecore_evas_fullscreen_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window is fullscreen or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee is fullscreen, 0 if not.</dl>
<h3>EAPI void ecore_evas_fullscreen_set (Ecore_Evas * ee, int on)</h3>
<p>Set whether or not an Ecore_Evas&#8217; window is fullscreen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>on</i> 1 fullscreen, 0 not.</dl>
<p> This function causes ee to be fullscreen if on is 1, or not if on is 0.</p>
<h3>EAPI void ecore_evas_geometry_get (Ecore_Evas * ee, int * x, int * y, int * w, int * h)</h3>
<p>Get the geometry of an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose geometry y<br />
 <i>x</i> A pointer to an int to place the x coordinate in<br />
 <i>y</i> A pointer to an int to place the y coordinate in<br />
 <i>w</i> A pointer to an int to place the w size in<br />
 <i>h</i> A pointer to an int to place the h size in</dl>
<p> This function takes four pointers to (already allocated) ints, and places the geometry of ee in them. </p>
<pre> int x, y, w, h;
 ecore_evas_geometry_get(ee, &amp;x, &amp;y, &amp;w, &amp;h);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI Evas* ecore_evas_get (Ecore_Evas * ee)</h3>
<p>Get an Ecore_Evas&#8217;s Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose Evas you wish to get</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Evas wrapped by ee</dl>
<p> This function returns the Evas contained within ee.</p>
<h3>EAPI int ecore_evas_gl_x11_direct_resize_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_gl_x11_direct_resize_get(). </p>
<p> Referenced by ecore_evas_gl_x11_direct_resize_get().</p>
<h3>EAPI void ecore_evas_gl_x11_direct_resize_set (Ecore_Evas * ee, int on)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_gl_x11_direct_resize_set(). </p>
<p> Referenced by ecore_evas_gl_x11_direct_resize_set().</p>
<h3>EAPI void ecore_evas_gl_x11_extra_event_window_add (Ecore_Evas * ee, Ecore_X_Window win)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_gl_x11_extra_event_window_add(), and ecore_evas_software_x11_extra_event_window_add(). </p>
<p> Referenced by ecore_evas_gl_x11_extra_event_window_add().</p>
<h3>EAPI Ecore_Evas* ecore_evas_gl_x11_new (const char * disp_name, Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_gl_x11_new(), ecore_x_display_get(), ecore_x_init(), and ecore_x_netwm_startup_id_set(). </p>
<p> Referenced by ecore_evas_gl_x11_new().</p>
<h3>EAPI Ecore_X_Window ecore_evas_gl_x11_subwindow_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_gl_x11_subwindow_get(). </p>
<p> Referenced by ecore_evas_gl_x11_subwindow_get().</p>
<h3>EAPI Ecore_X_Window ecore_evas_gl_x11_window_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_gl_x11_window_get(). </p>
<p> Referenced by ecore_evas_gl_x11_window_get().</p>
<h3>EAPI void ecore_evas_hide (Ecore_Evas * ee)</h3>
<p>Hide an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to show.</dl>
<p> This function makes ee hidden.</p>
<h3>EAPI int ecore_evas_iconified_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window is iconified or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee is iconified, 0 if not.</dl>
<h3>EAPI void ecore_evas_iconified_set (Ecore_Evas * ee, int on)</h3>
<p>Iconify or uniconify an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>on</i> 1 to iconify, 0 to uniconify.</dl>
<p> This function iconifies ee if on is 1, or uniconifies ee if on is 0.</p>
<h3>EAPI int ecore_evas_ignore_events_get (Ecore_Evas * ee)</h3>
<p>Returns the ignore state of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose window&#8217;s ignore events state is returned.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Ecore_Evas window&#8217;s ignore state.</dl>
<h3>EAPI void ecore_evas_ignore_events_set (Ecore_Evas * ee, int ignore)</h3>
<p>Set if this evas should ignore events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose window&#8217;s to ignore events<br />
 <i>sticky</i> The Ecore_Evas new ignore state</dl>
<h3>EAPI int ecore_evas_init (void)</h3>
<p>Init the Evas system. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>greater than 0 on success, 0 on failure</dl>
<p> Set up the Evas wrapper system. </p>
<p> References ECORE_FD_READ, and ecore_main_fd_handler_add().</p>
<h3>EAPI int ecore_evas_layer_get (Ecore_Evas * ee)</h3>
<p>Get the layer of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the layer ee&#8217;s window is on.</dl>
<h3>EAPI void ecore_evas_layer_set (Ecore_Evas * ee, int layer)</h3>
<p>Set the layer of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>layer</i> The layer to put ee on.</dl>
<p> This function moves ee to the layer layer.</p>
<h3>EAPI void ecore_evas_lower (Ecore_Evas * ee)</h3>
<p>Lower an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to raise.</dl>
<p> This functions lowers the Ecore_Evas to the back.</p>
<h3>EAPI void ecore_evas_managed_move (Ecore_Evas * ee, int x, int y)</h3>
<p>Provide Managed move co-ordinates for an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to move<br />
 <i>x</i> The x coordinate to set as the managed location<br />
 <i>y</i> The y coordinate to set as the managed location</dl>
<p> This sets the managed geometry position of the ee to (x, y)</p>
<h3>EAPI int ecore_evas_maximized_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window is maximized or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee is maximized, 0 if not.</dl>
<h3>EAPI void ecore_evas_maximized_set (Ecore_Evas * ee, int on)</h3>
<p>Maximize (or unmaximize) an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>on</i> 1 to maximize, 0 to unmaximize.</dl>
<p> This function maximizes ee if on is 1, or unmaximizes ee if on is 0.</p>
<h3>EAPI void ecore_evas_move (Ecore_Evas * ee, int x, int y)</h3>
<p>Move an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to move<br />
 <i>x</i> The x coordinate to move to<br />
 <i>y</i> The y coordinate to move to</dl>
<p> This moves ee to the screen coordinates (x, y)</p>
<h3>EAPI void ecore_evas_move_resize (Ecore_Evas * ee, int x, int y, int w, int h)</h3>
<p>Resize an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to move<br />
 <i>x</i> The x coordinate to move to<br />
 <i>y</i> The y coordinate to move to<br />
 <i>w</i> The w coordinate to resize to<br />
 <i>h</i> The h coordinate to resize to</dl>
<p> This moves ee to the screen coordinates (x, y) and resizes it to w x h.</p>
<h3>EAPI void ecore_evas_name_class_get (Ecore_Evas * ee, const char ** n, const char ** c)</h3>
<p>Get the name and class of an Ecore_Evas&#8217; window ee The Ecore_Evas to query n A pointer to a string to place the name in. </p>
<p> c A pointer to a string to place the class in. </p>
<p> This function gets puts the name of ee into n, and its class into c.</p>
<h3>EAPI void ecore_evas_name_class_set (Ecore_Evas * ee, const char * n, const char * c)</h3>
<p>Set the name and class of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> the Ecore_Evas<br />
 <i>n</i> the name<br />
 <i>c</i> the class</dl>
<p> This function sets the name of ee to n, and its class to c.</p>
<h3>EAPI Ecore_Evas* ecore_evas_new (const char * engine_name, int x, int y, int w, int h, const char * extra_options)</h3>
<p>Creates a new Ecore_Evas based on engine name and common parameters. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>engine_name</i> engine name as returned by <code>ecore_evas_engines_get()</code> or NULL to use environment variable ECORE_EVAS_ENGINE, that can be undefined and in this case this call will try to find the first working engine.<br />
 <i>x</i> horizontal position of window (not supported in all engines)<br />
 <i>y</i> vertical position of window (not supported in all engines)<br />
 <i>w</i> width of window<br />
 <i>h</i> height of window<br />
 <i>extra_options</i> string with extra parameter, dependent on engines or NULL. String is usually in the form: &#8216;key1=value1;key2=value2&#8217;. Pay attention that when getting that from shell commands, most consider &#8216;;&#8217; as the command terminator, so you need to escape it or use quotes.<br />
 <i>Ecore_Evas</i> instance or NULL if creation failed.</dl>
<h3>EAPI void ecore_evas_object_cursor_set (Ecore_Evas * ee, Evas_Object * obj, int layer, int hot_x, int hot_y)</h3>
<p>Set the cursor of an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>obj</i> The Evas_Object for the cursor<br />
 <i>layer</i><br />
 <i>hot_x</i> The x coordinate of the cursor&#8217;s hot spot<br />
 <i>hot_y</i> The y coordinate of the cursor&#8217;s hot spot</dl>
<p> This function makes the mouse cursor over ee be the image specified by file. The actual point within the image that the mouse is at is specified by hot_x and hot_y, which are coordinates with respect to the top left corner of the cursor image.</p>
<h3>EAPI int ecore_evas_override_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window is overridden or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if ee is overridden, 0 if not.</dl>
<h3>EAPI void ecore_evas_override_set (Ecore_Evas * ee, int on)</h3>
<p>Tell the WM whether or not to ignore an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>on</i> 1 to ignore, 0 to not.</dl>
<p> This function causes the window manager to ignore ee if on is 1, or not ignore ee if on is 0.</p>
<h3>EAPI void ecore_evas_raise (Ecore_Evas * ee)</h3>
<p>Raise and Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to raise.</dl>
<p> This functions raises the Ecore_Evas to the front.</p>
<h3>EAPI void ecore_evas_resize (Ecore_Evas * ee, int w, int h)</h3>
<p>Resize an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to move<br />
 <i>w</i> The w coordinate to resize to<br />
 <i>h</i> The h coordinate to resize to</dl>
<p> This resizes ee to w x h</p>
<h3>EAPI int ecore_evas_rotation_get (Ecore_Evas * ee)</h3>
<p>Set the rotation of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the angle (in degrees) of rotation.</dl>
<h3>EAPI void ecore_evas_rotation_set (Ecore_Evas * ee, int rot)</h3>
<p>Set the rotation of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas<br />
 <i>rot</i> the angle (in degrees) of rotation.</dl>
<p> The allowed values of rot depend on the engine being used. Most only allow multiples of 90.</p>
<h3>EAPI int ecore_evas_shaped_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas is shaped or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to query.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if shaped, 0 if not.</dl>
<p> This function returns 1 if ee is shaped, and 0 if not.</p>
<h3>EAPI void ecore_evas_shaped_set (Ecore_Evas * ee, int shaped)</h3>
<p>Set whether an Ecore_Evas is shaped or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to shape<br />
 <i>shaped</i> 1 to shape, 0 to not</dl>
<p> This function allows one to make an Ecore_Evas shaped to the contents of the evas. If shaped is 1, ee will be transparent in parts of the evas that contain no objects. If shaped is 0, then ee will be rectangular, and and parts with no data will show random framebuffer artifacting. For non-shaped Ecore_Evases, it is recommend to cover the entire evas with a background object.</p>
<h3>EAPI void ecore_evas_show (Ecore_Evas * ee)</h3>
<p>Show an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to show.</dl>
<p> This function makes ee visible.</p>
<h3>EAPI int ecore_evas_shutdown (void)</h3>
<p>Shut down the Evas system. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 if ecore evas is fully shut down, or &gt; 0 if it still needs to be shut down</dl>
<p> This closes the Evas system down. </p>
<p> References ecore_main_fd_handler_del().</p>
<h3>EAPI void ecore_evas_size_base_get (Ecore_Evas * ee, int * w, int * h)</h3>
<p>Get the base size of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> A pointer to an int to place the base width in.<br />
 <i>h</i> A pointer to an int to place the base height in.</dl>
<p> This function puts the base size of ee into w and h.</p>
<h3>EAPI void ecore_evas_size_base_set (Ecore_Evas * ee, int w, int h)</h3>
<p>Set the base size of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> The base width<br />
 <i>h</i> The base height</dl>
<p> This function sets the base size of ee to w x h.</p>
<h3>EAPI void ecore_evas_size_max_get (Ecore_Evas * ee, int * w, int * h)</h3>
<p>Get the max size of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> A pointer to an int to place the max width in.<br />
 <i>h</i> A pointer to an int to place the max height in.</dl>
<p> This function puts the maximum size of ee into w and h.</p>
<h3>EAPI void ecore_evas_size_max_set (Ecore_Evas * ee, int w, int h)</h3>
<p>Set the max size of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> The maximum width<br />
 <i>h</i> The maximum height</dl>
<p> This function sets the maximum size of ee to w x h.</p>
<h3>EAPI void ecore_evas_size_min_get (Ecore_Evas * ee, int * w, int * h)</h3>
<p>Get the min size of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> A pointer to an int to place the min width in.<br />
 <i>h</i> A pointer to an int to place the min height in.</dl>
<p> This function puts the minimum size of ee into w and h.</p>
<h3>EAPI void ecore_evas_size_min_set (Ecore_Evas * ee, int w, int h)</h3>
<p>Set the min size of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> The minimum width<br />
 <i>h</i> The minimum height</dl>
<p> This function sets the minimum size of ee to w x h.</p>
<h3>EAPI void ecore_evas_size_step_get (Ecore_Evas * ee, int * w, int * h)</h3>
<p>Get the step size of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> A pointer to an int to place the step width in.<br />
 <i>h</i> A pointer to an int to place the step height in.</dl>
<p> This function puts the step size of ee into w and h.</p>
<h3>EAPI void ecore_evas_size_step_set (Ecore_Evas * ee, int w, int h)</h3>
<p>Set the step size of an Ecore_Evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to set<br />
 <i>w</i> The step width<br />
 <i>h</i> The step height</dl>
<p> This function sets the step size of ee to w x h. This limits the size of an Ecore_Evas to always being an integer multiple of the step size.</p>
<h3>EAPI int ecore_evas_software_x11_16_direct_resize_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_16_direct_resize_get(). </p>
<p> Referenced by ecore_evas_software_x11_16_direct_resize_get().</p>
<h3>EAPI void ecore_evas_software_x11_16_direct_resize_set (Ecore_Evas * ee, int on)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_16_direct_resize_set(). </p>
<p> Referenced by ecore_evas_software_x11_16_direct_resize_set().</p>
<h3>EAPI void ecore_evas_software_x11_16_extra_event_window_add (Ecore_Evas * ee, Ecore_X_Window win)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_16_extra_event_window_add(). </p>
<p> Referenced by ecore_evas_software_x11_16_extra_event_window_add().</p>
<h3>EAPI Ecore_Evas* ecore_evas_software_x11_16_new (const char * disp_name, Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_16_new(), ecore_x_display_get(), ecore_x_init(), ecore_x_netwm_startup_id_set(), ecore_x_window_argb_new(), ecore_x_window_new(), and ecore_x_window_root_list(). </p>
<p> Referenced by ecore_evas_software_x11_16_new().</p>
<h3>EAPI Ecore_X_Window ecore_evas_software_x11_16_subwindow_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_16_subwindow_get(). </p>
<p> Referenced by ecore_evas_software_x11_16_subwindow_get().</p>
<h3>EAPI Ecore_X_Window ecore_evas_software_x11_16_window_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_16_window_get(). </p>
<p> Referenced by ecore_evas_software_x11_16_window_get().</p>
<h3>EAPI int ecore_evas_software_x11_direct_resize_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_direct_resize_get(). </p>
<p> Referenced by ecore_evas_software_x11_direct_resize_get().</p>
<h3>EAPI void ecore_evas_software_x11_direct_resize_set (Ecore_Evas * ee, int on)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_direct_resize_set(). </p>
<p> Referenced by ecore_evas_software_x11_direct_resize_set().</p>
<h3>EAPI void ecore_evas_software_x11_extra_event_window_add (Ecore_Evas * ee, Ecore_X_Window win)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_extra_event_window_add(). </p>
<p> Referenced by ecore_evas_gl_x11_extra_event_window_add(), ecore_evas_software_x11_extra_event_window_add(), and ecore_evas_xrender_x11_extra_event_window_add().</p>
<h3>EAPI Ecore_Evas* ecore_evas_software_x11_new (const char * disp_name, Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_new(), ecore_x_connection_get(), ecore_x_default_screen_get(), ecore_x_display_get(), ecore_x_init(), ecore_x_netwm_startup_id_set(), ecore_x_window_argb_new(), ecore_x_window_new(), and ecore_x_window_root_list(). </p>
<p> Referenced by ecore_evas_software_x11_new().</p>
<h3>EAPI Ecore_X_Window ecore_evas_software_x11_subwindow_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_subwindow_get(). </p>
<p> Referenced by ecore_evas_software_x11_subwindow_get().</p>
<h3>EAPI Ecore_X_Window ecore_evas_software_x11_window_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_window_get(). </p>
<p> Referenced by ecore_evas_software_x11_window_get().</p>
<h3>EAPI int ecore_evas_sticky_get (Ecore_Evas * ee)</h3>
<p>Returns the sticky state of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose window&#8217;s sticky state is returned.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Ecore_Evas window&#8217;s sticky state.</dl>
<h3>EAPI void ecore_evas_sticky_set (Ecore_Evas * ee, int sticky)</h3>
<p>Set the sticky state of an Ecore_Evas window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose window&#8217;s sticky state is set.<br />
 <i>sticky</i> The Ecore_Evas window&#8217;s new sticky state.</dl>
<h3>EAPI const char* ecore_evas_title_get (Ecore_Evas * ee)</h3>
<p>Get the title of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose title you wish to get.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The title of ee.</dl>
<p> This function returns the title of ee.</p>
<h3>EAPI void ecore_evas_title_set (Ecore_Evas * ee, const char * t)</h3>
<p>Set the title of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose title you wish to set.<br />
 <i>t</i> The title</dl>
<p> This function sets the title of ee to t.</p>
<h3>EAPI int ecore_evas_visibility_get (Ecore_Evas * ee)</h3>
<p>Query whether an Ecore_Evas&#8217; window is visible or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas to query.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if visible, 0 if not.</dl>
<p> This function queries ee and returns 1 if it is visible, and 0 if not.</p>
<h3>EAPI int ecore_evas_withdrawn_get (Ecore_Evas * ee)</h3>
<p>Returns the withdrawn state of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose window&#8217;s withdrawn state is returned.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Ecore_Evas window&#8217;s withdrawn state.</dl>
<h3>EAPI void ecore_evas_withdrawn_set (Ecore_Evas * ee, int withdrawn)</h3>
<p>Set the withdrawn state of an Ecore_Evas&#8217; window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ee</i> The Ecore_Evas whose window&#8217;s withdrawn state is set.<br />
 <i>withdrawn</i> The Ecore_Evas window&#8217;s new withdrawn state.</dl>
<h3>EAPI int ecore_evas_xrender_x11_direct_resize_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_xrender_x11_direct_resize_get(). </p>
<p> Referenced by ecore_evas_xrender_x11_direct_resize_get().</p>
<h3>EAPI void ecore_evas_xrender_x11_direct_resize_set (Ecore_Evas * ee, int on)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_xrender_x11_direct_resize_set(). </p>
<p> Referenced by ecore_evas_xrender_x11_direct_resize_set().</p>
<h3>EAPI void ecore_evas_xrender_x11_extra_event_window_add (Ecore_Evas * ee, Ecore_X_Window win)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_software_x11_extra_event_window_add(), and ecore_evas_xrender_x11_extra_event_window_add(). </p>
<p> Referenced by ecore_evas_xrender_x11_extra_event_window_add().</p>
<h3>EAPI Ecore_Evas* ecore_evas_xrender_x11_new (const char * disp_name, Ecore_X_Window parent, int x, int y, int w, int h)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_xrender_x11_new(), ecore_x_connection_get(), ecore_x_default_screen_get(), ecore_x_display_get(), ecore_x_init(), ecore_x_netwm_startup_id_set(), ecore_x_window_new(), and ecore_x_window_root_list(). </p>
<p> Referenced by ecore_evas_xrender_x11_new().</p>
<h3>EAPI Ecore_X_Window ecore_evas_xrender_x11_subwindow_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_xrender_x11_subwindow_get(). </p>
<p> Referenced by ecore_evas_xrender_x11_subwindow_get().</p>
<h3>EAPI Ecore_X_Window ecore_evas_xrender_x11_window_get (Ecore_Evas * ee)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_evas_xrender_x11_window_get(). </p>
<p> Referenced by ecore_evas_xrender_x11_window_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
