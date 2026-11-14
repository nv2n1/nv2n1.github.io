---
title: "ecore_x(3)"
name: "ecore_x"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x/"
description: "Ecore_X.h – Ecore functions for dealing with the X Windows System."
---

<p>Ecore_X.h &#8211; Ecore functions for dealing with the X Windows System. </p>
<h2>Synopsis</h2>
<h3>Enumerations</h3>
<p>enum <code>_Ecore_X_Window_State</code> { <code>ECORE_X_WINDOW_STATE_ICONIFIED</code>, <code>ECORE_X_WINDOW_STATE_MODAL</code>, <code>ECORE_X_WINDOW_STATE_STICKY</code>, <code>ECORE_X_WINDOW_STATE_MAXIMIZED_VERT</code>, <code>ECORE_X_WINDOW_STATE_MAXIMIZED_HORZ</code>, <code>ECORE_X_WINDOW_STATE_SHADED</code>, <code>ECORE_X_WINDOW_STATE_SKIP_TASKBAR</code>, <code>ECORE_X_WINDOW_STATE_SKIP_PAGER</code>, <code>ECORE_X_WINDOW_STATE_HIDDEN</code>, <code>ECORE_X_WINDOW_STATE_FULLSCREEN</code> } </p>
<p> enum <code>_Ecore_X_WM_Protocol</code> { <code>ECORE_X_WM_PROTOCOL_DELETE_REQUEST</code>, <code>ECORE_X_WM_PROTOCOL_TAKE_FOCUS</code>, <code>ECORE_X_NET_WM_PROTOCOL_PING</code>, <code>ECORE_X_NET_WM_PROTOCOL_SYNC_REQUEST</code> } </p>
<p> enum <code>_Ecore_X_Window_Input_Mode</code> { <code>ECORE_X_WINDOW_INPUT_MODE_NONE</code>, <code>ECORE_X_WINDOW_INPUT_MODE_PASSIVE</code>, <code>ECORE_X_WINDOW_INPUT_MODE_ACTIVE_LOCAL</code>, <code>ECORE_X_WINDOW_INPUT_MODE_ACTIVE_GLOBAL</code> } </p>
<p> enum <code>_Ecore_X_Window_State_Hint</code> { <code>ECORE_X_WINDOW_STATE_HINT_NONE</code> = -1, <code>ECORE_X_WINDOW_STATE_HINT_WITHDRAWN</code>, <code>ECORE_X_WINDOW_STATE_HINT_NORMAL</code>, <code>ECORE_X_WINDOW_STATE_HINT_ICONIC</code> } </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_init</code> (const char *name)<br />
 <i>Initialize the X display connection to the given display. </i><br />
 EAPI int <code>ecore_x_shutdown</code> (void)<br />
 <i>Shuts down the Ecore X library. </i><br />
 EAPI int <code>ecore_x_disconnect</code> (void)<br />
 <i>Shuts down the Ecore X library. </i><br />
 EAPI Ecore_X_Display * <code>ecore_x_display_get</code> (void)<br />
 <i>Retrieves the Ecore_X_Display handle used for the current X connection. </i><br />
 EAPI Ecore_X_Connection * <code>ecore_x_connection_get</code> (void)<br />
 <i>Retrieves the Ecore_X_Connection handle used for the current X connection. </i><br />
 EAPI int <code>ecore_x_fd_get</code> (void)<br />
 <i>Retrieves the X display file descriptor. </i><br />
 EAPI Ecore_X_Screen * <code>ecore_x_default_screen_get</code> (void)<br />
 <i>Retrieves the Ecore_X_Screen handle used for the current X connection. </i><br />
 EAPI void <code>ecore_x_double_click_time_set</code> (double t)<br />
 <i>Sets the timeout for a double and triple clicks to be flagged. </i><br />
 EAPI double <code>ecore_x_double_click_time_get</code> (void)<br />
 <i>Retrieves the double and triple click flag timeout. </i><br />
 EAPI void <code>ecore_x_flush</code> (void)<br />
 <i>Sends all X commands in the X Display buffer. </i><br />
 EAPI void <code>ecore_x_sync</code> (void)<br />
 <i>Flushes the command buffer and waits until all requests have been processed by the server. </i><br />
 EAPI void <code>ecore_x_killall</code> (Ecore_X_Window root)<br />
 <i>Kill all clients with subwindows under a given window. </i><br />
 EAPI void <code>ecore_x_kill</code> (Ecore_X_Window win)<br />
 <i>Kill a specific client. </i><br />
 EAPI int <code>ecore_x_dpi_get</code> (void)<br />
 <i>Return the screen DPI. </i><br />
 EAPI Ecore_X_Time <code>ecore_x_current_time_get</code> (void)<br />
 <i>Return the last event time. </i><br />
 EAPI void <code>ecore_x_error_handler_set</code> (void(*func)(void *data), const void *data)<br />
 <i>Set the error handler. </i><br />
 EAPI void <code>ecore_x_io_error_handler_set</code> (void(*func)(void *data), const void *data)<br />
 <i>Set the I/O error handler. </i><br />
 EAPI int <code>ecore_x_error_request_get</code> (void)<br />
 <i>Get the request code that caused the error. </i><br />
 EAPI int <code>ecore_x_error_code_get</code> (void)<br />
 <i>Get the error code from the error. </i><br />
 EAPI void <code>ecore_x_selection_primary_prefetch</code> (void)<br />
 <i>Sends the GetSelectionOwner request. </i><br />
 EAPI void <code>ecore_x_selection_primary_fetch</code> (void)<br />
 <i>Gets the reply of the GetSelectionOwner request sent by </i><code>ecore_x_selection_primary_prefetch()</code>.<br />
 EAPI int <code>ecore_x_selection_primary_set</code> (Ecore_X_Window w, const void *data, int size)<br />
 <i>Claim ownership of the PRIMARY selection and set its data. </i><br />
 EAPI int <code>ecore_x_selection_primary_clear</code> (void)<br />
 <i>Release ownership of the primary selection. </i><br />
 EAPI void <code>ecore_x_selection_secondary_prefetch</code> (void)<br />
 <i>Sends the GetSelectionOwner request. </i><br />
 EAPI void <code>ecore_x_selection_secondary_fetch</code> (void)<br />
 <i>Gets the reply of the GetSelectionOwner request sent by </i><code>ecore_x_selection_secondary_prefetch()</code>.<br />
 EAPI int <code>ecore_x_selection_secondary_set</code> (Ecore_X_Window w, const void *data, int size)<br />
 <i>Claim ownership of the SECONDARY selection and set its data. </i><br />
 EAPI int <code>ecore_x_selection_secondary_clear</code> (void)<br />
 <i>Release ownership of the secondary selection. </i><br />
 EAPI void <code>ecore_x_selection_xdnd_prefetch</code> (void)<br />
 <i>Sends the GetSelectionOwner request. </i><br />
 EAPI void <code>ecore_x_selection_xdnd_fetch</code> (void)<br />
 <i>Gets the reply of the GetSelectionOwner request sent by </i><code>ecore_x_selection_xdnd_prefetch()</code>.<br />
 EAPI int <code>ecore_x_selection_xdnd_set</code> (Ecore_X_Window w, const void *data, int size)<br />
 <i>Claim ownership of the XDND selection and set its data. </i><br />
 EAPI int <code>ecore_x_selection_xdnd_clear</code> (void)<br />
 <i>Release ownership of the XDND selection. </i><br />
 EAPI void <code>ecore_x_selection_clipboard_prefetch</code> (void)<br />
 <i>Sends the GetSelectionOwner request. </i><br />
 EAPI void <code>ecore_x_selection_clipboard_fetch</code> (void)<br />
 <i>Gets the reply of the GetSelectionOwner request sent by </i><code>ecore_x_selection_clipboard_prefetch()</code>.<br />
 EAPI int <code>ecore_x_selection_clipboard_set</code> (Ecore_X_Window w, const void *data, int size)<br />
 <i>Claim ownership of the CLIPBOARD selection and set its data. </i><br />
 EAPI int <code>ecore_x_selection_clipboard_clear</code> (void)<br />
 <i>Release ownership of the clipboard selection. </i><br />
 EAPI void <code>ecore_x_dnd_version_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_dnd_version_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_dnd_version_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_dnd_version_get</code> (Ecore_X_Window win)<br />
 <i>Get the DnD version. </i><br />
 EAPI void <code>ecore_x_dnd_type_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_dnd_type_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_dnd_type_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_dnd_type_isset</code> (Ecore_X_Window win, const char *type)<br />
 <i>Check if the type is set. </i><br />
 EAPI void <code>ecore_x_dnd_type_set</code> (Ecore_X_Window win, const char *type, int on)<br />
 <i>Set the type. </i><br />
 EAPI void <code>ecore_x_dnd_types_set</code> (Ecore_X_Window win, char **types, unsigned int num_types)<br />
 <i>Set the types. </i><br />
 EAPI void <code>ecore_x_dnd_begin_prefetch</code> (Ecore_X_Window source)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_dnd_begin_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_dnd_begin_prefetch()</code>.<br />
 EAPI int <code>ecore_x_dnd_begin</code> (Ecore_X_Window source, unsigned char *data, int size)<br />
 <i>Begins the DnD. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_new</code> (Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>Creates a new window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_override_new</code> (Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>Creates a window with the override redirect attribute set to </i>True.<br />
 EAPI Ecore_X_Window <code>ecore_x_window_manager_argb_new</code> (Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>Creates a new window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_argb_new</code> (Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>Creates a new window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_override_argb_new</code> (Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>Creates a window with the override redirect attribute set to </i>True.<br />
 EAPI Ecore_X_Window <code>ecore_x_window_input_new</code> (Ecore_X_Window parent, int x, int y, int w, int h)<br />
 <i>Creates a new input window. </i><br />
 EAPI void <code>ecore_x_window_configure</code> (Ecore_X_Window win, Ecore_X_Window_Configure_Mask mask, int x, int y, int w, int h, int border_width, Ecore_X_Window sibling, int stack_mode)<br />
 <i>Configures the given window with the given mask. </i><br />
 EAPI void <code>ecore_x_window_cursor_set</code> (Ecore_X_Window win, Ecore_X_Cursor c)<br />
 <i>Sets the cursor of the given window. </i><br />
 EAPI void <code>ecore_x_window_del</code> (Ecore_X_Window win)<br />
 <i>Deletes the given window. </i><br />
 EAPI void <code>ecore_x_window_ignore_set</code> (Ecore_X_Window win, int ignore)<br />
 <i>Set if a window should be ignored. </i><br />
 EAPI Ecore_X_Window * <code>ecore_x_window_ignore_list</code> (int *num)<br />
 <i>Get the ignore list. </i><br />
 EAPI void <code>ecore_x_window_delete_request_send</code> (Ecore_X_Window win)<br />
 <i>Sends a delete request to the given window. </i><br />
 EAPI void <code>ecore_x_window_show</code> (Ecore_X_Window win)<br />
 <i>Shows a window. </i><br />
 EAPI void <code>ecore_x_window_hide</code> (Ecore_X_Window win)<br />
 <i>Hides a window. </i><br />
 EAPI void <code>ecore_x_window_move</code> (Ecore_X_Window win, int x, int y)<br />
 <i>Moves a window to the position </i>x, y.<br />
 EAPI void <code>ecore_x_window_resize</code> (Ecore_X_Window win, int w, int h)<br />
 <i>Resizes a window. </i><br />
 EAPI void <code>ecore_x_window_move_resize</code> (Ecore_X_Window win, int x, int y, int w, int h)<br />
 <i>Moves and resizes a window. </i><br />
 EAPI void <code>ecore_x_window_focus</code> (Ecore_X_Window win)<br />
 <i>Sets the focus to the window </i>window.<br />
 EAPI void <code>ecore_x_window_focus_at_time</code> (Ecore_X_Window win, Ecore_X_Time t)<br />
 <i>Sets the focus to the given window at a specific time. </i><br />
 EAPI void <code>ecore_x_get_input_focus_prefetch</code> (void)<br />
 <i>Sends the GetInputFocus request. </i><br />
 EAPI void <code>ecore_x_get_input_focus_fetch</code> (void)<br />
 <i>Gets the reply of the GetInputFocus request sent by </i><code>ecore_x_get_input_focus_prefetch()</code>.<br />
 EAPI Ecore_X_Window <code>ecore_x_window_focus_get</code> (void)<br />
 <i>Gets the window that has focus. </i><br />
 EAPI void <code>ecore_x_window_raise</code> (Ecore_X_Window win)<br />
 <i>Raises the given window. </i><br />
 EAPI void <code>ecore_x_window_lower</code> (Ecore_X_Window win)<br />
 <i>Lowers the given window. </i><br />
 EAPI void <code>ecore_x_window_reparent</code> (Ecore_X_Window win, Ecore_X_Window new_parent, int x, int y)<br />
 <i>Moves a window to within another window at a given position. </i><br />
 EAPI void <code>ecore_x_window_size_get</code> (Ecore_X_Window win, int *w, int *h)<br />
 <i>Retrieves the size of the given window. </i><br />
 EAPI void <code>ecore_x_window_geometry_get</code> (Ecore_X_Window win, int *x, int *y, int *w, int *h)<br />
 <i>Retrieves the geometry of the given window. </i><br />
 EAPI int <code>ecore_x_window_border_width_get</code> (Ecore_X_Window win)<br />
 <i>Retrieves the width of the border of the given window. </i><br />
 EAPI void <code>ecore_x_window_border_width_set</code> (Ecore_X_Window win, int width)<br />
 <i>Sets the width of the border of the given window. </i><br />
 EAPI int <code>ecore_x_window_depth_get</code> (Ecore_X_Window win)<br />
 <i>Retrieves the depth of the given window. </i><br />
 EAPI void <code>ecore_x_window_cursor_show</code> (Ecore_X_Window win, int show)<br />
 <i>Shows the cursor of the given window. </i><br />
 EAPI void <code>ecore_x_window_defaults_set</code> (Ecore_X_Window win)<br />
 <i>Sets the default properties for the given window. </i><br />
 EAPI int <code>ecore_x_window_visible_get</code> (Ecore_X_Window win)<br />
 <i>Finds out whether the given window is currently visible. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_shadow_tree_at_xy_with_skip_get</code> (Ecore_X_Window base, int x, int y, Ecore_X_Window *skip, int skip_num)<br />
 <i>Retrieves the top, visible window at the given location, but skips the windows in the list. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_shadow_parent_get</code> (Ecore_X_Window root, Ecore_X_Window win)<br />
 <i>Retrieves the parent window a given window has. </i><br />
 EAPI void <code>ecore_x_window_shadow_tree_flush</code> (void)<br />
 <i>Flushes the window shadow tree so nothing is stored. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_root_get</code> (Ecore_X_Window win)<br />
 <i>Retrieves the root window a given window is on. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_at_xy_get</code> (int x, int y)<br />
 <i>Retrieves the top, visible window at the given location. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_at_xy_with_skip_get</code> (int x, int y, Ecore_X_Window *skip, int skip_num)<br />
 <i>Retrieves the top, visible window at the given location, but skips the windows in the list. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_window_at_xy_begin_get</code> (Ecore_X_Window begin, int x, int y)<br />
 <i>Retrieves the top, visible window at the given location, but begins at the </i>begin window instead of the root one.<br />
 EAPI void <code>ecore_x_query_tree_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the QueryTree request. </i><br />
 EAPI void <code>ecore_x_query_tree_fetch</code> (void)<br />
 <i>Gets the reply of the QueryTree request sent by </i><code>ecore_x_query_tree_prefetch()</code>.<br />
 EAPI Ecore_X_Window <code>ecore_x_window_parent_get</code> (Ecore_X_Window win)<br />
 <i>Retrieves the parent window of the given window. </i><br />
 EAPI void <code>ecore_x_window_background_color_set</code> (Ecore_X_Window win, unsigned short r, unsigned short g, unsigned short b)<br />
 <i>Sets the background color of the given window. </i><br />
 EAPI void <code>ecore_x_window_gravity_set</code> (Ecore_X_Window win, Ecore_X_Gravity grav)<br />
 <i>Sets the gravity of the given window. </i><br />
 EAPI void <code>ecore_x_window_pixel_gravity_set</code> (Ecore_X_Window win, Ecore_X_Gravity grav)<br />
 <i>Sets the bit gravity of the given window. </i><br />
 EAPI void <code>ecore_x_window_pixmap_set</code> (Ecore_X_Window win, Ecore_X_Pixmap pmap)<br />
 <i>Sets the background pixmap of the given window. </i><br />
 EAPI void <code>ecore_x_window_area_clear</code> (Ecore_X_Window win, int x, int y, int w, int h)<br />
 <i>Clears an area of the given window. </i><br />
 EAPI void <code>ecore_x_window_area_expose</code> (Ecore_X_Window win, int x, int y, int w, int h)<br />
 <i>Exposes an area of the given window. </i><br />
 EAPI void <code>ecore_x_window_override_set</code> (Ecore_X_Window win, int override)<br />
 <i>Sets the override attribute of the given window. </i><br />
 EAPI void <code>ecore_x_window_prop_card32_get_prefetch</code> (Ecore_X_Window window, Ecore_X_Atom atom)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_window_prop_card32_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_window_prop_card32_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_window_prop_xid_get_prefetch</code> (Ecore_X_Window window, Ecore_X_Atom atom, Ecore_X_Atom type)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_window_prop_xid_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_window_prop_xid_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_window_prop_atom_get_prefetch</code> (Ecore_X_Window window, Ecore_X_Atom atom)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_window_prop_atom_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_window_prop_atom_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_window_prop_window_get_prefetch</code> (Ecore_X_Window window, Ecore_X_Atom atom)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_window_prop_window_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_window_prop_window_get_prefetch()</code>.<br />
 EAPI Ecore_X_Atom <code>ecore_x_window_prop_any_type</code> (void)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_x_window_prop_property_set</code> (Ecore_X_Window win, Ecore_X_Atom type, Ecore_X_Atom format, int size, void *data, int number)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_x_window_prop_property_get_prefetch</code> (Ecore_X_Window window, Ecore_X_Atom property, Ecore_X_Atom type)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_window_prop_property_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_window_prop_property_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_window_prop_property_get</code> (Ecore_X_Window win, Ecore_X_Atom property, Ecore_X_Atom type, int size, unsigned char **data, int *num)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_x_window_prop_list_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the ListProperties request. </i><br />
 EAPI void <code>ecore_x_window_prop_list_fetch</code> (void)<br />
 <i>Gets the reply of the ListProperties request sent by </i><code>ecore_x_window_prop_list_prefetch()</code>.<br />
 EAPI void <code>ecore_x_window_prop_string_set</code> (Ecore_X_Window win, Ecore_X_Atom type, const char *str)<br />
 <i>Set a window string property. </i><br />
 EAPI void <code>ecore_x_window_prop_string_get_prefetch</code> (Ecore_X_Window window, Ecore_X_Atom type)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_window_prop_string_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_window_prop_string_get_prefetch()</code>.<br />
 EAPI char * <code>ecore_x_window_prop_string_get</code> (Ecore_X_Window win, Ecore_X_Atom type)<br />
 <i>Get a window string property. </i><br />
 EAPI Ecore_X_WM_Protocol * <code>ecore_x_window_prop_protocol_list_get</code> (Ecore_X_Window win, int *num_ret)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_x_window_shape_mask_set</code> (Ecore_X_Window win, Ecore_X_Pixmap mask)<br />
 <i>Sets the shape of the given window to the given pixmap. </i><br />
 EAPI void <code>ecore_x_window_shape_rectangle_set</code> (Ecore_X_Window win, int x, int y, int w, int h)<br />
 <i>Sets the shape of the given window to a rectangle. </i><br />
 EAPI void <code>ecore_x_window_shape_rectangles_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the ShapeGetRectangles request. </i><br />
 EAPI void <code>ecore_x_window_shape_rectangles_get_fetch</code> (void)<br />
 <i>Gets the reply of the ShapeGetRectangles request sent by </i><code>ecore_x_window_shape_rectangles_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_window_shape_input_mask_set</code> (Ecore_X_Window win, Ecore_X_Pixmap mask)<br />
 <i>Sets the input shape of the given window to that given by the pixmap </i>mask.<br />
 EAPI Ecore_X_Pixmap <code>ecore_x_pixmap_new</code> (Ecore_X_Window win, int w, int h, int dep)<br />
 <i>Creates a new pixmap. </i><br />
 EAPI void <code>ecore_x_pixmap_del</code> (Ecore_X_Pixmap pmap)<br />
 <i>Deletes the reference to the given pixmap. </i><br />
 EAPI void <code>ecore_x_pixmap_paste</code> (Ecore_X_Pixmap pmap, Ecore_X_Drawable dest, Ecore_X_GC gc, int sx, int sy, int w, int h, int dx, int dy)<br />
 <i>Pastes a rectangular area of the given pixmap onto the given drawable. </i><br />
 EAPI void <code>ecore_x_pixmap_geometry_get</code> (Ecore_X_Pixmap pmap, int *x, int *y, int *w, int *h)<br />
 <i>Retrieves the size of the given pixmap. </i><br />
 EAPI int <code>ecore_x_pixmap_depth_get</code> (Ecore_X_Pixmap pmap)<br />
 <i>Retrieves the depth of the given pixmap. </i><br />
 EAPI Ecore_X_GC <code>ecore_x_gc_new</code> (Ecore_X_Drawable draw)<br />
 <i>Creates a new default graphics context associated with the given drawable. </i><br />
 EAPI void <code>ecore_x_gc_del</code> (Ecore_X_GC gc)<br />
 <i>Deletes and frees the given graphics context. </i><br />
 EAPI int <code>ecore_x_client_message32_send</code> (Ecore_X_Window win, Ecore_X_Atom type, Ecore_X_Event_Mask mask, long d0, long d1, long d2, long d3, long d4)<br />
 <i>Send client message with given type and format 32. </i><br />
 EAPI int <code>ecore_x_client_message8_send</code> (Ecore_X_Window win, Ecore_X_Atom type, const void *data, int len)<br />
 <i>Send client message with given type and format 8. </i><br />
 EAPI void <code>ecore_x_drawable_geometry_get_prefetch</code> (Ecore_X_Drawable drawable)<br />
 <i>Sends the GetGeometry request. </i><br />
 EAPI void <code>ecore_x_drawable_geometry_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetGeometry request sent by </i><code>ecore_x_atom_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_drawable_geometry_get</code> (Ecore_X_Drawable d, int *x, int *y, int *w, int *h)<br />
 <i>Retrieves the geometry of the given drawable. </i><br />
 EAPI int <code>ecore_x_drawable_border_width_get</code> (Ecore_X_Drawable d)<br />
 <i>Retrieves the width of the border of the given drawable. </i><br />
 EAPI int <code>ecore_x_drawable_depth_get</code> (Ecore_X_Drawable d)<br />
 <i>Retrieves the depth of the given drawable. </i><br />
 EAPI Ecore_X_Window * <code>ecore_x_window_root_list</code> (int *num_ret)<br />
 <i>Get a list of all the root windows on the server. </i><br />
 EAPI void <code>ecore_x_window_container_manage</code> (Ecore_X_Window win)<br />
 <i>Todo. </i><br />
 EAPI void <code>ecore_x_window_client_manage</code> (Ecore_X_Window win)<br />
 <i>Todo. </i><br />
 EAPI void <code>ecore_x_window_sniff</code> (Ecore_X_Window win)<br />
 <i>Todo. </i><br />
 EAPI void <code>ecore_x_window_client_sniff</code> (Ecore_X_Window win)<br />
 <i>Todo. </i><br />
 EAPI void <code>ecore_x_atom_get_prefetch</code> (const char *name)<br />
 <i>Sends the InternAtom request. </i><br />
 EAPI void <code>ecore_x_atom_get_fetch</code> (void)<br />
 <i>Gets the reply of the InternAtom request sent by </i><code>ecore_x_atom_get_prefetch()</code>.<br />
 EAPI Ecore_X_Atom <code>ecore_x_atom_get</code> (const char *name)<br />
 <i>Retrieves the atom value associated with the given name. </i><br />
 EAPI void <code>ecore_x_icccm_state_set</code> (Ecore_X_Window win, Ecore_X_Window_State_Hint state)<br />
 <i>Sets the state of a window. </i><br />
 EAPI void <code>ecore_x_icccm_delete_window_send</code> (Ecore_X_Window win, Ecore_X_Time t)<br />
 <i>Sends the ClientMessage event with the DeleteWindow property. </i><br />
 EAPI void <code>ecore_x_icccm_take_focus_send</code> (Ecore_X_Window win, Ecore_X_Time t)<br />
 <i>Sends the ClientMessage event with the TakeFocus property. </i><br />
 EAPI void <code>ecore_x_icccm_save_yourself_send</code> (Ecore_X_Window win, Ecore_X_Time t)<br />
 <i>Sends the ClientMessage event with the SaveYourself property. </i><br />
 EAPI void <code>ecore_x_icccm_move_resize_send</code> (Ecore_X_Window win, int x, int y, int w, int h)<br />
 <i>Sends the ConfigureNotify event with the StructureNotify property. </i><br />
 EAPI void <code>ecore_x_icccm_hints_set</code> (Ecore_X_Window win, int accepts_focus, Ecore_X_Window_State_Hint initial_state, Ecore_X_Pixmap icon_pixmap, Ecore_X_Pixmap icon_mask, Ecore_X_Window icon_window, Ecore_X_Window window_group, int is_urgent)<br />
 <i>Sets the hints of a window. </i><br />
 EAPI void <code>ecore_x_icccm_size_pos_hints_set</code> (Ecore_X_Window win, int request_pos, Ecore_X_Gravity gravity, int min_w, int min_h, int max_w, int max_h, int base_w, int base_h, int step_x, int step_y, double min_aspect, double max_aspect)<br />
 <i>Sets the hints of a window. </i><br />
 EAPI void <code>ecore_x_icccm_title_set</code> (Ecore_X_Window win, const char *t)<br />
 <i>Set the title of a window. </i><br />
 EAPI void <code>ecore_x_icccm_protocol_set</code> (Ecore_X_Window win, Ecore_X_WM_Protocol protocol, int on)<br />
 <i>Set or unset a wm protocol property. </i><br />
 EAPI int <code>ecore_x_icccm_protocol_isset</code> (Ecore_X_Window win, Ecore_X_WM_Protocol protocol)<br />
 <i>Determines whether a protocol is set for a window. </i><br />
 EAPI void <code>ecore_x_icccm_name_class_set</code> (Ecore_X_Window win, const char *n, const char *c)<br />
 <i>Set a window name &amp; class. </i><br />
 EAPI void <code>ecore_x_icccm_name_class_get</code> (Ecore_X_Window win, char **n, char **c)<br />
 <i>Get a window name &amp; class. </i><br />
 EAPI char * <code>ecore_x_icccm_client_machine_get</code> (Ecore_X_Window win)<br />
 <i>Get a window client machine string. </i><br />
 EAPI void <code>ecore_x_icccm_command_set</code> (Ecore_X_Window win, int argc, char **argv)<br />
 <i>Sets the WM_COMMAND property for win</i>.<br />
 EAPI void <code>ecore_x_icccm_command_get</code> (Ecore_X_Window win, int *argc, char ***argv)<br />
 <i>Get the WM_COMMAND property for win</i>.<br />
 EAPI char * <code>ecore_x_icccm_icon_name_get</code> (Ecore_X_Window win)<br />
 <i>Get a window icon name. </i><br />
 EAPI void <code>ecore_x_icccm_icon_name_set</code> (Ecore_X_Window win, const char *t)<br />
 <i>Set a window icon name. </i><br />
 EAPI void <code>ecore_x_icccm_colormap_window_set</code> (Ecore_X_Window win, Ecore_X_Window subwin)<br />
 <i>Add a subwindow to the list of windows that need a different colormap installed. </i><br />
 EAPI void <code>ecore_x_icccm_colormap_window_unset</code> (Ecore_X_Window win, Ecore_X_Window subwin)<br />
 <i>Remove a window from the list of colormap windows. </i><br />
 EAPI void <code>ecore_x_icccm_transient_for_set</code> (Ecore_X_Window win, Ecore_X_Window forwin)<br />
 <i>Specify that a window is transient for another top-level window and should be handled accordingly. </i><br />
 EAPI void <code>ecore_x_icccm_transient_for_unset</code> (Ecore_X_Window win)<br />
 <i>Remove the transient_for setting from a window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_icccm_transient_for_get</code> (Ecore_X_Window win)<br />
 <i>Get the window this window is transient for, if any. </i><br />
 EAPI void <code>ecore_x_icccm_window_role_set</code> (Ecore_X_Window win, const char *role)<br />
 <i>Set the window role hint. </i><br />
 EAPI char * <code>ecore_x_icccm_window_role_get</code> (Ecore_X_Window win)<br />
 <i>Get the window role. </i><br />
 EAPI void <code>ecore_x_icccm_client_leader_set</code> (Ecore_X_Window win, Ecore_X_Window l)<br />
 <i>Set the window&#8217;s client leader. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_icccm_client_leader_get</code> (Ecore_X_Window win)<br />
 <i>Get the window&#8217;s client leader. </i><br />
 EAPI void <code>ecore_x_icccm_iconic_request_send</code> (Ecore_X_Window win, Ecore_X_Window root)<br />
 <i>Send the ClientMessage event with the ChangeState property. </i><br />
 EAPI void <code>ecore_x_mwm_hints_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_mwm_hints_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_mwm_hints_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_mwm_borderless_set</code> (Ecore_X_Window win, int borderless)<br />
 <i>Sets the borderless flag of a window using MWM. </i><br />
 EAPI void <code>ecore_x_netwm_init</code> (void)<br />
 <i>Initialize the NetWM module. </i><br />
 EAPI void <code>ecore_x_netwm_shutdown</code> (void)<br />
 <i>Shutdown the NetWM module. </i><br />
 EAPI void <code>ecore_x_netwm_wm_identify</code> (Ecore_X_Window root, Ecore_X_Window check, const char *wm_name)<br />
 <i>Set the _NET_SUPPORTING_WM_CHECK property. </i><br />
 EAPI void <code>ecore_x_netwm_supported_set</code> (Ecore_X_Window root, Ecore_X_Atom *supported, int num)<br />
 <i>Set the _NET_SUPPORTED property. </i><br />
 EAPI void <code>ecore_x_netwm_supported_get_prefetch</code> (Ecore_X_Window root)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_supported_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_supported_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_supported_get</code> (Ecore_X_Window root, Ecore_X_Atom **supported, int *num)<br />
 <i>Get the hints supported by the Window Manager. </i><br />
 EAPI void <code>ecore_x_netwm_desk_count_set</code> (Ecore_X_Window root, unsigned int n_desks)<br />
 <i>Set the _NET_NUMBER_OF_DESKTOPS property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_roots_set</code> (Ecore_X_Window root, Ecore_X_Window *vroots, unsigned int n_desks)<br />
 <i>Set the _NET_VIRTUAL_ROOTS property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_names_set</code> (Ecore_X_Window root, const char **names, unsigned int n_desks)<br />
 <i>Set the _NET_DESKTOP_NAMES property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_size_set</code> (Ecore_X_Window root, unsigned int width, unsigned int height)<br />
 <i>Set the _NET_DESKTOP_GEOMETRY property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_workareas_set</code> (Ecore_X_Window root, unsigned int *areas, unsigned int n_desks)<br />
 <i>Set the _NET_WORKAREA property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_current_set</code> (Ecore_X_Window root, unsigned int desk)<br />
 <i>Set the _NET_CURRENT_DESKTOP property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_viewports_set</code> (Ecore_X_Window root, unsigned int *origins, unsigned int n_desks)<br />
 <i>Set the _NET_DESKTOP_VIEWPORT property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_layout_set</code> (Ecore_X_Window root, int orientation, int columns, int rows, int starting_corner)<br />
 <i>Set the _NET_DESKTOP_LAYOUT property. </i><br />
 EAPI void <code>ecore_x_netwm_showing_desktop_set</code> (Ecore_X_Window root, int on)<br />
 <i>Set the _NET_SHOWING_DESKTOP property. </i><br />
 EAPI void <code>ecore_x_netwm_client_list_set</code> (Ecore_X_Window root, Ecore_X_Window *p_clients, unsigned int n_clients)<br />
 <i>Set the _NET_CLIENT_LIST property. </i><br />
 EAPI void <code>ecore_x_netwm_client_list_stacking_set</code> (Ecore_X_Window root, Ecore_X_Window *p_clients, unsigned int n_clients)<br />
 <i>Set the _NET_CLIENT_LIST_STACKING property. </i><br />
 EAPI void <code>ecore_x_netwm_client_active_set</code> (Ecore_X_Window root, Ecore_X_Window win)<br />
 <i>Set the _NET_ACTIVE_WINDOW property. </i><br />
 EAPI void <code>ecore_x_netwm_name_set</code> (Ecore_X_Window win, const char *name)<br />
 <i>Set the _NET_WM_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_name_get</code> (Ecore_X_Window win, char **name)<br />
 <i>Get the title of a window. </i><br />
 EAPI void <code>ecore_x_netwm_startup_id_set</code> (Ecore_X_Window win, const char *id)<br />
 <i>Set the _NET_STARTUP_ID property. </i><br />
 EAPI void <code>ecore_x_netwm_startup_id_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_startup_id_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_startup_id_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_startup_id_get</code> (Ecore_X_Window win, char **id)<br />
 <i>Get the startup ID name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_visible_name_set</code> (Ecore_X_Window win, const char *name)<br />
 <i>Set the _NET_WM_VISIBLE_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_visible_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_visible_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_visible_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_visible_name_get</code> (Ecore_X_Window win, char **name)<br />
 <i>Get the visible title of a window. </i><br />
 EAPI void <code>ecore_x_netwm_icon_name_set</code> (Ecore_X_Window win, const char *name)<br />
 <i>Set the _NET_WM_ICON_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_icon_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_icon_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_icon_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_icon_name_get</code> (Ecore_X_Window win, char **name)<br />
 <i>Get the icon name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_visible_icon_name_set</code> (Ecore_X_Window win, const char *name)<br />
 <i>Set the _NET_WM_VISIBLE_ICON_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_visible_icon_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_visible_icon_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_visible_icon_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_visible_icon_name_get</code> (Ecore_X_Window win, char **name)<br />
 <i>Get the visible icon name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_set</code> (Ecore_X_Window win, unsigned int desk)<br />
 <i>Set the _NET_WM_DESKTOP property. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_desktop_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_desktop_get</code> (Ecore_X_Window win, unsigned int *desk)<br />
 <i>Get the visible icon name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_strut_set</code> (Ecore_X_Window win, int left, int right, int top, int bottom)<br />
 <i>Set the _NET_WM_STRUT property. </i><br />
 EAPI void <code>ecore_x_netwm_strut_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_strut_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_strut_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_strut_get</code> (Ecore_X_Window win, int *left, int *right, int *top, int *bottom)<br />
 <i>Get the space at the edje of the screen. </i><br />
 EAPI void <code>ecore_x_netwm_strut_partial_set</code> (Ecore_X_Window win, int left, int right, int top, int bottom, int left_start_y, int left_end_y, int right_start_y, int right_end_y, int top_start_x, int top_end_x, int bottom_start_x, int bottom_end_x)<br />
 <i>Set the _NET_WM_STRUT_PARTIAL property. </i><br />
 EAPI void <code>ecore_x_netwm_strut_partial_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_strut_partial_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_strut_partial_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_strut_partial_get</code> (Ecore_X_Window win, int *left, int *right, int *top, int *bottom, int *left_start_y, int *left_end_y, int *right_start_y, int *right_end_y, int *top_start_x, int *top_end_x, int *bottom_start_x, int *bottom_end_x)<br />
 <i>Get the space at the edje of the screen of a window. </i><br />
 EAPI void <code>ecore_x_netwm_icons_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_icons_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_icons_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_icons_get</code> (Ecore_X_Window win, Ecore_X_Icon **icon, int *num)<br />
 <i>Retrieve hte possible icons of a window. </i><br />
 EAPI void <code>ecore_x_netwm_icon_geometry_set</code> (Ecore_X_Window win, int x, int y, int width, int height)<br />
 <i>Set the _NET_WM_ICON_GEOMETRY property. </i><br />
 EAPI void <code>ecore_x_netwm_icon_geometry_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_icon_geometry_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_icon_geometry_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_icon_geometry_get</code> (Ecore_X_Window win, int *x, int *y, int *width, int *height)<br />
 <i>Get the geometry of an icon. </i><br />
 EAPI void <code>ecore_x_netwm_pid_set</code> (Ecore_X_Window win, int pid)<br />
 <i>Set the _NET_WM_PID property. </i><br />
 EAPI void <code>ecore_x_netwm_pid_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_pid_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_pid_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_pid_get</code> (Ecore_X_Window win, int *pid)<br />
 <i>Get the process ID of a client window. </i><br />
 EAPI void <code>ecore_x_netwm_handled_icons_set</code> (Ecore_X_Window win)<br />
 <i>Set the _NET_WM_HANDLED_ICONS property. </i><br />
 EAPI void <code>ecore_x_netwm_handled_icons_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_handled_icons_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_handled_icons_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_handled_icons_get</code> (Ecore_X_Window win)<br />
 <i>Return wheter the Client handles icons or not. </i><br />
 EAPI void <code>ecore_x_netwm_user_time_set</code> (Ecore_X_Window win, unsigned int time)<br />
 <i>Set the _NET_WM_USER_TIME property. </i><br />
 EAPI void <code>ecore_x_netwm_user_time_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_user_time_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_user_time_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_user_time_get</code> (Ecore_X_Window win, unsigned int *time)<br />
 <i>Get the last user activity time in the window. </i><br />
 EAPI void <code>ecore_x_netwm_window_state_set</code> (Ecore_X_Window win, Ecore_X_Window_State *state, unsigned int num)<br />
 <i>Set the _NET_WM_STATE property. </i><br />
 EAPI void <code>ecore_x_netwm_window_state_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_window_state_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_window_state_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_window_state_get</code> (Ecore_X_Window win, Ecore_X_Window_State **state, unsigned int *num)<br />
 <i>Get the hints describing the window state. </i><br />
 EAPI void <code>ecore_x_netwm_window_type_set</code> (Ecore_X_Window win, Ecore_X_Window_Type type)<br />
 <i>Set the _NET_WM_WINDOW_TYPE property. </i><br />
 EAPI void <code>ecore_x_netwm_window_type_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_window_type_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_window_type_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_window_type_get</code> (Ecore_X_Window win, Ecore_X_Window_Type *type)<br />
 <i>Get the functional type of a window. </i><br />
 EAPI int <code>ecore_x_netwm_allowed_action_isset</code> (Ecore_X_Window win, Ecore_X_Action action)<br />
 <i>Check whether an action is supported by a window. </i><br />
 EAPI void <code>ecore_x_netwm_allowed_action_set</code> (Ecore_X_Window win, Ecore_X_Action *action, unsigned int num)<br />
 <i>Set the _NET_WM_ALLOWED_ACTIONS property. </i><br />
 EAPI void <code>ecore_x_netwm_allowed_action_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_allowed_action_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_allowed_action_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_allowed_action_get</code> (Ecore_X_Window win, Ecore_X_Action **action, unsigned int *num)<br />
 <i>Get the allowed actions supported by a window. </i><br />
 EAPI void <code>ecore_x_netwm_opacity_set</code> (Ecore_X_Window win, unsigned int opacity)<br />
 <i>Set the _NET_WM_WINDOW_OPACITY property. </i><br />
 EAPI void <code>ecore_x_netwm_opacity_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_opacity_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_opacity_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_opacity_get</code> (Ecore_X_Window win, unsigned int *opacity)<br />
 <i>Get the opacity value of a window. </i><br />
 EAPI void <code>ecore_x_netwm_frame_size_set</code> (Ecore_X_Window win, int fl, int fr, int ft, int fb)<br />
 <i>Set the _NET_FRAME_EXTENTS property. </i><br />
 EAPI void <code>ecore_x_netwm_frame_size_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_frame_size_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_frame_size_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_frame_size_get</code> (Ecore_X_Window win, int *fl, int *fr, int *ft, int *fb)<br />
 <i>Get the frame extent of a window. </i><br />
 EAPI void <code>ecore_x_netwm_sync_counter_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_sync_counter_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_sync_counter_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_sync_counter_get</code> (Ecore_X_Window win, Ecore_X_Sync_Counter *counter)<br />
 <i>Get the X ID of a X Sync counter. </i><br />
 EAPI void <code>ecore_x_netwm_ping_send</code> (Ecore_X_Window win)<br />
 <i>Send a _NET_WM_PING property event. </i><br />
 EAPI void <code>ecore_x_netwm_sync_request_send</code> (Ecore_X_Window win, unsigned int serial)<br />
 <i>Send a _NET_WM_SYNC_REQUEST property event. </i><br />
 EAPI void <code>ecore_x_netwm_state_request_send</code> (Ecore_X_Window win, Ecore_X_Window root, Ecore_X_Window_State s1, Ecore_X_Window_State s2, int set)<br />
 <i>Send a _NET_WM_STATE property event. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_request_send</code> (Ecore_X_Window win, Ecore_X_Window root, unsigned int desktop)<br />
 <i>Send a _NET_WM_DESKTOP property event. </i><br />
 EAPI void <code>ecore_x_xinerama_query_screens_prefetch</code> (void)<br />
 <i>Sends the XineramaQueryScreens request. </i><br />
 EAPI void <code>ecore_x_xinerama_query_screens_fetch</code> (void)<br />
 <i>Gets the reply of the XineramaQueryScreens request sent by </i><code>ecore_x_xinerama_query_screens_prefetch()</code>.<br />
 EAPI int <code>ecore_x_xinerama_screen_count_get</code> (void)<br />
 <i>Return the number of screens. </i><br />
 EAPI int <code>ecore_x_xinerama_screen_geometry_get</code> (int screen, int *x, int *y, int *w, int *h)<br />
 <i>Get the geometry of the screen. </i><br />
 EAPI int <code>ecore_x_screensaver_event_available_get</code> (void)<br />
 <i>Return whether the X server supports the ScrenSaver Extension. </i><br />
 EAPI void <code>ecore_x_screensaver_idle_time_prefetch</code> (void)<br />
 <i>Sends the QueryInfo request. </i><br />
 EAPI void <code>ecore_x_screensaver_idle_time_fetch</code> (void)<br />
 <i>Gets the reply of the QueryInfo request sent by </i><code>ecore_x_get_screensaver_prefetch()</code>.<br />
 EAPI int <code>ecore_x_screensaver_idle_time_get</code> (void)<br />
 <i>Get the number of seconds since the last input was received. </i><br />
 EAPI void <code>ecore_x_get_screensaver_prefetch</code> (void)<br />
 <i>Sends the GetScreenSaver request. </i><br />
 EAPI void <code>ecore_x_get_screensaver_fetch</code> (void)<br />
 <i>Gets the reply of the GetScreenSaver request sent by </i><code>ecore_x_get_screensaver_prefetch()</code>.<br />
 EAPI void <code>ecore_x_screensaver_set</code> (int timeout, int interval, int prefer_blanking, int allow_exposures)<br />
 <i>Set the parameters of the screen saver. </i><br />
 EAPI void <code>ecore_x_screensaver_timeout_set</code> (int timeout)<br />
 <i>Set the timeout of the screen saver. </i><br />
 EAPI int <code>ecore_x_screensaver_timeout_get</code> (void)<br />
 <i>Get the timeout of the screen saver. </i><br />
 EAPI void <code>ecore_x_screensaver_blank_set</code> (int timeout)<br />
 <i>Set the screen blanking. </i><br />
 EAPI int <code>ecore_x_screensaver_blank_get</code> (void)<br />
 <i>Get the screen blanking. </i><br />
 EAPI void <code>ecore_x_screensaver_expose_set</code> (int timeout)<br />
 <i>Set the screen save control values. </i><br />
 EAPI int <code>ecore_x_screensaver_expose_get</code> (void)<br />
 <i>Get the screen save control values. </i><br />
 EAPI void <code>ecore_x_screensaver_interval_set</code> (int timeout)<br />
 <i>Set the interval of the screen saver. </i><br />
 EAPI int <code>ecore_x_screensaver_interval_get</code> (void)<br />
 <i>Get the interval of the screen saver. </i><br />
 EAPI void <code>ecore_x_screensaver_event_listen_set</code> (int on)<br />
 <i>Specifies if the Screen Saver NotifyMask event should be generated. </i><br />
 EAPI void <code>ecore_x_get_window_attributes_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetWindowAttributes request. </i><br />
 EAPI void <code>ecore_x_get_window_attributes_fetch</code> (void)<br />
 <i>Gets the reply of the GetWindowAttributes request sent by </i><code>ecore_x_get_window_attributes_prefetch()</code>.<br />
 EAPI void <code>ecore_x_window_save_set_add</code> (Ecore_X_Window win)<br />
 <i>Inserts the window in the client&#8217;s save-set. </i><br />
 EAPI void <code>ecore_x_window_save_set_del</code> (Ecore_X_Window win)<br />
 <i>Deletes the window from the client&#8217;s save-set. </i><br />
 EAPI void <code>ecore_x_pointer_xy_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the QueryPointer request. </i><br />
 EAPI void <code>ecore_x_pointer_xy_get_fetch</code> (void)<br />
 <i>Gets the reply of the QueryPointer request sent by ecore_x_query_pointer_prefetch(). </i><br />
 EAPI Ecore_X_Sync_Alarm <code>ecore_x_sync_alarm_new</code> (Ecore_X_Sync_Counter counter)<br />
 <i>Create a new alarm. </i><br />
 EAPI int <code>ecore_x_sync_alarm_free</code> (Ecore_X_Sync_Alarm alarm)<br />
 <i>Delete an alarm. </i><br />
 EAPI int <code>ecore_x_randr_query</code> ()<br />
 <i>Return whether the X server supports the RandR Extension. </i><br />
 EAPI int <code>ecore_x_randr_events_select</code> (Ecore_X_Window win, int on)<br />
 <i>Select if the ScreenChangeNotify events will be sent. </i><br />
 EAPI void <code>ecore_x_randr_get_screen_info_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetScreenInfo request. </i><br />
 EAPI void <code>ecore_x_randr_get_screen_info_fetch</code> (void)<br />
 <i>Gets the reply of the GetScreenInfo request sent by </i><code>ecore_x_randr_get_screen_info_prefetch()</code>.<br />
 EAPI Ecore_X_Randr_Rotation <code>ecore_x_randr_screen_rotations_get</code> (Ecore_X_Window root)<br />
 <i>Get the set of rotations and reflections. </i><br />
 EAPI Ecore_X_Randr_Rotation <code>ecore_x_randr_screen_rotation_get</code> (Ecore_X_Window root)<br />
 <i>Get the rotation. </i><br />
 EAPI void <code>ecore_x_randr_screen_rotation_set</code> (Ecore_X_Window root, Ecore_X_Randr_Rotation rot)<br />
 <i>Set the screen rotation. </i><br />
 EAPI Ecore_X_Screen_Size * <code>ecore_x_randr_screen_sizes_get</code> (Ecore_X_Window root, int *num)<br />
 <i>Get the frame buffer sizes. </i><br />
 EAPI Ecore_X_Screen_Size <code>ecore_x_randr_current_screen_size_get</code> (Ecore_X_Window root)<br />
 <i>Get the current frame buffer size. </i><br />
 EAPI int <code>ecore_x_randr_screen_size_set</code> (Ecore_X_Window root, Ecore_X_Screen_Size size)<br />
 <i>Set the screen size. </i><br />
 EAPI Ecore_X_Screen_Refresh_Rate * <code>ecore_x_randr_screen_refresh_rates_get</code> (Ecore_X_Window root, int size_id, int *num)<br />
 <i>Get the refresh rates. </i><br />
 EAPI Ecore_X_Screen_Refresh_Rate <code>ecore_x_randr_current_screen_refresh_rate_get</code> (Ecore_X_Window root)<br />
 <i>Get the current refresh rate. </i><br />
 EAPI int <code>ecore_x_randr_screen_refresh_rate_set</code> (Ecore_X_Window root, Ecore_X_Screen_Size size, Ecore_X_Screen_Refresh_Rate rate)<br />
 <i>Set the screen refresh rate. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new</code> (Ecore_X_Rectangle *rects, int num)<br />
 <i>Create a region from rectangles. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new_from_bitmap</code> (Ecore_X_Pixmap bitmap)<br />
 <i>Create a region from a pixmap. </i><br />
 EAPI Ecore_X_Region <code>ecore_x_region_new_from_window</code> (Ecore_X_Window win, Ecore_X_Region_Type type)<br />
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
 EAPI Ecore_X_Rectangle * <code>ecore_x_region_fetch</code> (Ecore_X_Region region, int *num, Ecore_X_Rectangle *bounds)<br />
 <i>Return the rectangles that compose a region. </i><br />
 EAPI void <code>ecore_x_region_expand</code> (Ecore_X_Region dest, Ecore_X_Region source, unsigned int left, unsigned int right, unsigned int top, unsigned int bottom)<br />
 <i>Expand a region. </i><br />
 EAPI void <code>ecore_x_region_gc_clip_set</code> (Ecore_X_Region region, Ecore_X_GC gc, int x_origin, int y_origin)<br />
 <i>Change clip-mask in a graphic context to the specified region. </i><br />
 EAPI void <code>ecore_x_region_window_shape_set</code> (Ecore_X_Region region, Ecore_X_Window win, Ecore_X_Shape_Type type, int x_offset, int y_offset)<br />
 <i>Change the shape extension of a window. </i><br />
 EAPI void <code>ecore_x_region_picture_clip_set</code> (Ecore_X_Region region, Ecore_X_Picture picture, int x_origin, int y_origin)<br />
 <i>Change clip-mask in picture to the specified region. </i><br />
 EAPI int <code>ecore_x_composite_query</code> (void)<br />
 <i>Return whether the Composite Extension is available. </i><br />
 EAPI int <code>ecore_x_damage_query</code> (void)<br />
 <i>Return whether the Damage Extension is available. </i><br />
 EAPI Ecore_X_Damage <code>ecore_x_damage_new</code> (Ecore_X_Drawable d, Ecore_X_Damage_Report_Level level)<br />
 <i>Creates a damage object. </i><br />
 EAPI void <code>ecore_x_damage_del</code> (Ecore_X_Damage damage)<br />
 <i>Destroys a damage object. </i><br />
 EAPI void <code>ecore_x_damage_subtract</code> (Ecore_X_Damage damage, Ecore_X_Region repair, Ecore_X_Region parts)<br />
 <i>Synchronously modifies the region. </i><br />
 EAPI int <code>ecore_x_screen_is_composited</code> (int screen)<br />
 <i>Check whether a screen is composited or not. </i><br />
 EAPI int <code>ecore_x_dpms_query</code> (void)<br />
 <i>Checks if the X DPMS extension is available on the server. </i><br />
 EAPI void <code>ecore_x_dpms_capable_get_prefetch</code> (void)<br />
 <i>Sends the DPMSCapable request. </i><br />
 EAPI void <code>ecore_x_dpms_capable_get_fetch</code> (void)<br />
 <i>Gets the reply of the DPMSCapable request sent by </i><code>ecore_x_dpms_capable_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_dpms_capable_get</code> (void)<br />
 <i>Checks if the X server is capable of DPMS. </i><br />
 EAPI void <code>ecore_x_dpms_enable_get_prefetch</code> (void)<br />
 <i>Sends the DPMSInfo request. </i><br />
 EAPI void <code>ecore_x_dpms_enable_get_fetch</code> (void)<br />
 <i>Gets the reply of the DPMSInfo request sent by </i><code>ecore_x_dpms_enable_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_dpms_enabled_get</code> (void)<br />
 <i>Checks the DPMS state of the display. </i><br />
 EAPI void <code>ecore_x_dpms_enabled_set</code> (int enabled)<br />
 <i>Sets the DPMS state of the display. </i><br />
 EAPI void <code>ecore_x_dpms_timeouts_get_prefetch</code> (void)<br />
 <i>Sends the DPMSGetTimeouts request. </i><br />
 EAPI void <code>ecore_x_dpms_timeouts_get_fetch</code> (void)<br />
 <i>Gets the reply of the DPMSGetTimeouts request sent by </i><code>ecore_x_dpms_timeouts_get_prefetch()</code>.<br />
 EAPI void <code>ecore_x_dpms_timeouts_get</code> (unsigned int *standby, unsigned int *suspend, unsigned int *off)<br />
 <i>Gets the timeouts. </i><br />
 EAPI int <code>ecore_x_dpms_timeouts_set</code> (unsigned int standby, unsigned int suspend, unsigned int off)<br />
 <i>Sets the timeouts. </i><br />
 EAPI unsigned int <code>ecore_x_dpms_timeout_standby_get</code> (void)<br />
 <i>Returns the amount of time of inactivity before standby mode is invoked. </i><br />
 EAPI unsigned int <code>ecore_x_dpms_timeout_suspend_get</code> (void)<br />
 <i>Returns the amount of time of inactivity before the second level of power saving is invoked. </i><br />
 EAPI unsigned int <code>ecore_x_dpms_timeout_off_get</code> (void)<br />
 <i>Returns the amount of time of inactivity before the third and final level of power saving is invoked. </i><br />
 EAPI void <code>ecore_x_dpms_timeout_standby_set</code> (unsigned int new_timeout)<br />
 <i>Sets the standby timeout (in unit of seconds). </i><br />
 EAPI void <code>ecore_x_dpms_timeout_suspend_set</code> (unsigned int new_timeout)<br />
 <i>Sets the suspend timeout (in unit of seconds). </i><br />
 EAPI void <code>ecore_x_dpms_timeout_off_set</code> (unsigned int new_timeout)<br />
 <i>Sets the off timeout (in unit of seconds). </i></p>
<h2>Detailed Description</h2>
<p>Ecore functions for dealing with the X Windows System. </p>
<p> Ecore_X provides a wrapper and convenience functions for using the X Windows System. Function groups for this part of the library include the following: </p>
<dl COMPACT>
<dt>*</p>
<dd><code>X Library Init and Shutdown Functions</code></p>
<dt>*</p>
<dd><code>X Display Attributes</code></p>
<dt>*</p>
<dd><code>X Synchronization Functions</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>_Ecore_X_Window_Input_Mode</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_INPUT_MODE_NONE </i></p>
<dd>The window can never be focused.</p>
<dt><i>ECORE_X_WINDOW_INPUT_MODE_PASSIVE </i></p>
<dd>The window can be focused by the WM but doesn&#8217;t focus itself.</p>
<dt><i>ECORE_X_WINDOW_INPUT_MODE_ACTIVE_LOCAL </i></p>
<dd>The window sets the focus itself if one of its sub-windows already is focused.</p>
<dt><i>ECORE_X_WINDOW_INPUT_MODE_ACTIVE_GLOBAL </i></p>
<dd>The window sets the focus itself even if another window is currently focused.</dl>
<h3>enum <code>_Ecore_X_Window_State</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_ICONIFIED </i></p>
<dd>The window is iconified.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_MODAL </i></p>
<dd>The window is a modal dialog box.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_STICKY </i></p>
<dd>The window manager should keep the window&#8217;s position fixed even if the virtual desktop scrolls.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_MAXIMIZED_VERT </i></p>
<dd>The window has the maximum vertical size.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_MAXIMIZED_HORZ </i></p>
<dd>The window has the maximum horizontal size.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_SHADED </i></p>
<dd>The window is shaded.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_SKIP_TASKBAR </i></p>
<dd>The window should not be included in the taskbar.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_SKIP_PAGER </i></p>
<dd>The window should not be included in the pager.</dl>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_HIDDEN </i></p>
<dd>The window is invisible (i.e.</dl>
<p> minimized/iconified)</p>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_FULLSCREEN </i></p>
<dd>The window should fill the entire screen and have no window border/decorations.</dl>
<h3>enum <code>_Ecore_X_Window_State_Hint</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_X_WINDOW_STATE_HINT_NONE </i></p>
<dd>Do not provide any state hint to the window manager.</p>
<dt><i>ECORE_X_WINDOW_STATE_HINT_WITHDRAWN </i></p>
<dd>The window wants to remain hidden and NOT iconified.</p>
<dt><i>ECORE_X_WINDOW_STATE_HINT_NORMAL </i></p>
<dd>The window wants to be mapped normally.</p>
<dt><i>ECORE_X_WINDOW_STATE_HINT_ICONIC </i></p>
<dd>The window wants to start in an iconified state.</dl>
<h3>enum <code>_Ecore_X_WM_Protocol</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_X_WM_PROTOCOL_DELETE_REQUEST </i></p>
<dd>If enabled the window manager will be asked to send a delete message instead of just closing (destroying) the window.</p>
<dt><i>ECORE_X_WM_PROTOCOL_TAKE_FOCUS </i></p>
<dd>If enabled the window manager will be told that the window explicitly sets input focus.</p>
<dt><i>ECORE_X_NET_WM_PROTOCOL_PING </i></p>
<dd>If enabled the window manager can ping the window to check if it is alive.</p>
<dt><i>ECORE_X_NET_WM_PROTOCOL_SYNC_REQUEST </i></p>
<dd>If enabled the window manager can sync updating with the window (?).</dl>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_X_Atom ecore_x_atom_get (const char * name)</h3>
<p>Retrieves the atom value associated with the given name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The given name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Associated atom value.</dl>
<p> References ecore_x_atom_get(). </p>
<p> Referenced by ecore_x_atom_get(), and ecore_x_dnd_type_set().</p>
<h3>EAPI int ecore_x_client_message32_send (Ecore_X_Window win, Ecore_X_Atom type, Ecore_X_Event_Mask mask, long d0, long d1, long d2, long d3, long d4)</h3>
<p>Send client message with given type and format 32. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window the message is sent to.<br />
 <i>type</i> The client message type.<br />
 <i>mask</i> The client message mask.<br />
 <i>d0</i> The client message data item 1<br />
 <i>d1</i> The client message data item 2<br />
 <i>d2</i> The client message data item 3<br />
 <i>d3</i> The client message data item 4<br />
 <i>d4</i> The client message data item 5</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>!0 on success.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window the message is sent to.<br />
 <i>type</i> The client message type.<br />
 <i>d0</i> The client message data item 1<br />
 <i>d1</i> The client message data item 2<br />
 <i>d2</i> The client message data item 3<br />
 <i>d3</i> The client message data item 4<br />
 <i>d4</i> The client message data item 5</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>!0 on success.</dl>
<p> References ecore_x_client_message32_send(). </p>
<p> Referenced by ecore_x_client_message32_send(), ecore_x_icccm_delete_window_send(), ecore_x_icccm_save_yourself_send(), and ecore_x_icccm_take_focus_send().</p>
<h3>EAPI int ecore_x_client_message8_send (Ecore_X_Window win, Ecore_X_Atom type, const void * data, int len)</h3>
<p>Send client message with given type and format 8. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window the message is sent to.<br />
 <i>type</i> The client message type.<br />
 <i>data</i> Data to be sent.<br />
 <i>len</i> Number of data bytes, max 20.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>!0 on success.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window the message is sent to.<br />
 <i>type</i> The client message type.<br />
 <i>data</i> Data to be sent.<br />
 <i>len</i> Number of data bytes, max 20.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>!0 on success.</dl>
<p> References ecore_x_client_message8_send(). </p>
<p> Referenced by ecore_x_client_message8_send().</p>
<h3>EAPI int ecore_x_dnd_begin (Ecore_X_Window source, unsigned char * data, int size)</h3>
<p>Begins the DnD. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>source</i> Unused.<br />
 <i>data</i> The data.<br />
 <i>size</i> The size of the data.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on failure, 1 otherwise.</dl>
<p> Begins the DnD. Returns 0 on failure, 1 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_dnd_begin_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_dnd_begin_fetch()</code>, which gets the reply. </p>
<p> References ecore_x_dnd_begin(), ecore_x_dnd_version_get(), ecore_x_selection_xdnd_fetch(), ecore_x_selection_xdnd_prefetch(), ecore_x_selection_xdnd_set(), and ecore_x_window_ignore_set(). </p>
<p> Referenced by ecore_x_dnd_begin().</p>
<h3>EAPI void ecore_x_dnd_begin_prefetch (Ecore_X_Window source)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>source</i> Window whose properties are requested.</dl>
<p> References ecore_x_dnd_begin_prefetch(). </p>
<p> Referenced by ecore_x_dnd_begin_prefetch().</p>
<h3>EAPI void ecore_x_dnd_type_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.</dl>
<p> References ecore_x_dnd_type_get_prefetch(). </p>
<p> Referenced by ecore_x_dnd_type_get_prefetch().</p>
<h3>EAPI int ecore_x_dnd_type_isset (Ecore_X_Window window, const char * type)</h3>
<p>Check if the type is set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.<br />
 <i>type</i> The type to check</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on failure, 1 otherwise.</dl>
<p> Check if the type is set. 0 on failure, 1 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_dnd_type_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_dnd_type_get_fetch()</code>, which gets the reply. </p>
<p> References ecore_x_dnd_type_isset(), and ecore_x_window_prop_property_get(). </p>
<p> Referenced by ecore_x_dnd_type_isset(), and ecore_x_dnd_type_set().</p>
<h3>EAPI void ecore_x_dnd_type_set (Ecore_X_Window window, const char * type, int on)</h3>
<p>Set the type. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.<br />
 <i>type</i> The type to set<br />
 <i>on</i> 0 or non 0&#8230;</dl>
<p> Set the type. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_dnd_type_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_dnd_type_get_fetch()</code>, which gets the reply. </p>
<p> References ecore_x_atom_get(), ecore_x_dnd_type_isset(), ecore_x_dnd_type_set(), ecore_x_window_prop_property_get(), and ecore_x_window_prop_property_set(). </p>
<p> Referenced by ecore_x_dnd_type_set().</p>
<h3>EAPI void ecore_x_dnd_types_set (Ecore_X_Window window, char ** types, unsigned int num_types)</h3>
<p>Set the types. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.<br />
 <i>types</i> The types to set<br />
 <i>num_types</i> The number of types</dl>
<p> Set the types. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_dnd_type_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_dnd_type_get_fetch()</code>, which gets the reply. </p>
<p> References ecore_x_dnd_types_set(), and ecore_x_window_prop_property_set(). </p>
<p> Referenced by ecore_x_dnd_types_set().</p>
<h3>EAPI int ecore_x_dnd_version_get (Ecore_X_Window window)</h3>
<p>Get the DnD version. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on failure, the version otherwise.</dl>
<p> Get the DnD version. Returns 0 on failure, the version otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_dnd_version_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_dnd_version_get_fetch()</code>, which gets the reply. </p>
<p> References ecore_x_dnd_version_get(), and ecore_x_window_prop_property_get(). </p>
<p> Referenced by ecore_x_dnd_begin(), and ecore_x_dnd_version_get().</p>
<h3>EAPI void ecore_x_dnd_version_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.</dl>
<p> References ecore_x_dnd_version_get_prefetch(). </p>
<p> Referenced by ecore_x_dnd_version_get_prefetch().</p>
<h3>EAPI int ecore_x_dpi_get (void)</h3>
<p>Return the screen DPI. </p>
<p> This is a simplistic call to get DPI. It does not account for differing DPI in the x amd y axes nor does it accoutn for multihead or xinerama and xrander where different parts of the screen may have differen DPI etc. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the general screen DPI (dots/pixels per inch).</dl>
<p> References ecore_x_dpi_get(). </p>
<p> Referenced by ecore_x_dpi_get().</p>
<h3>EAPI int ecore_x_error_code_get (void)</h3>
<p>Get the error code from the error. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The error code from the X error</dl>
<p> Return the error code from the last X error </p>
<p> References ecore_x_error_code_get(). </p>
<p> Referenced by ecore_x_error_code_get().</p>
<h3>EAPI void ecore_x_error_handler_set (void(*)(void *data) func, const void * data)</h3>
<p>Set the error handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The error handler function<br />
 <i>data</i> The data to be passed to the handler function</dl>
<p> Set the X error handler function </p>
<p> References ecore_x_error_handler_set(). </p>
<p> Referenced by ecore_x_error_handler_set().</p>
<h3>EAPI int ecore_x_error_request_get (void)</h3>
<p>Get the request code that caused the error. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The request code causing the X error</dl>
<p> Return the X request code that caused the last X error </p>
<p> References ecore_x_error_request_get(). </p>
<p> Referenced by ecore_x_error_request_get().</p>
<h3>EAPI void ecore_x_gc_del (Ecore_X_GC gc)</h3>
<p>Deletes and frees the given graphics context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>gc</i> The given graphics context.</dl>
<p> Destroyes the graphic context gc as well as the associated storage. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>gc</i> The given graphics context.</dl>
<p> References ecore_x_gc_del(). </p>
<p> Referenced by ecore_x_gc_del().</p>
<h3>EAPI Ecore_X_GC ecore_x_gc_new (Ecore_X_Drawable draw)</h3>
<p>Creates a new default graphics context associated with the given drawable. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>drawable</i> Drawable to create graphics context with. If 0 is given instead, the default root window is used.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new default graphics context.</dl>
<p> Creates a new default graphics context associated with drawable. The graphic context can be used with any destination drawable having the same root and depth as drawable. Use with other drawables results in a BadMatch error. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>draw</i> Drawable to create graphics context with. If 0 is given instead, the default root window is used.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new default graphics context.</dl>
<p> References ecore_x_gc_new(). </p>
<p> Referenced by ecore_x_gc_new().</p>
<h3>EAPI void ecore_x_icccm_command_get (Ecore_X_Window win, int * argc, char *** argv)</h3>
<p>Get the WM_COMMAND property for <i>win</i>. </p>
<p> Return the command of a window. String must be free&#8217;d when done with. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window.<br />
 <i>argc</i> Number of arguments.<br />
 <i>argv</i> Arguments.</dl>
<p> References ecore_x_icccm_command_get(). </p>
<p> Referenced by ecore_x_icccm_command_get().</p>
<h3>EAPI char* ecore_x_icccm_icon_name_get (Ecore_X_Window win)</h3>
<p>Get a window icon name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The windows icon name string</dl>
<p> Return the icon name of a window. String must be free&#8217;d when done with. </p>
<p> References ecore_x_icccm_icon_name_get(). </p>
<p> Referenced by ecore_x_icccm_icon_name_get().</p>
<h3>EAPI void ecore_x_icccm_name_class_get (Ecore_X_Window win, char ** n, char ** c)</h3>
<p>Get a window name &amp; class. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window<br />
 <i>n</i> The name string<br />
 <i>c</i> The class string</dl>
<p> Get a window name * class </p>
<p> References ecore_x_icccm_name_class_get(). </p>
<p> Referenced by ecore_x_icccm_name_class_get().</p>
<h3>EAPI int ecore_x_icccm_protocol_isset (Ecore_X_Window win, Ecore_X_WM_Protocol protocol)</h3>
<p>Determines whether a protocol is set for a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The Window<br />
 <i>protocol</i> The protocol to query</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the protocol is set, else 0.</dl>
<p> References ecore_x_icccm_protocol_isset(). </p>
<p> Referenced by ecore_x_icccm_protocol_isset().</p>
<h3>EAPI Ecore_X_Window ecore_x_icccm_transient_for_get (Ecore_X_Window win)</h3>
<p>Get the window this window is transient for, if any. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window to check</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window ID of the top-level window, or 0 if the property does not exist.</dl>
<p> References ecore_x_icccm_transient_for_get(). </p>
<p> Referenced by ecore_x_icccm_transient_for_get().</p>
<h3>EAPI void ecore_x_io_error_handler_set (void(*)(void *data) func, const void * data)</h3>
<p>Set the I/O error handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The I/O error handler function<br />
 <i>data</i> The data to be passed to the handler function</dl>
<p> Set the X I/O error handler function </p>
<p> References ecore_x_io_error_handler_set(). </p>
<p> Referenced by ecore_x_io_error_handler_set().</p>
<h3>EAPI void ecore_x_kill (Ecore_X_Window win)</h3>
<p>Kill a specific client. </p>
<p> You can kill a specific client woning window window </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window of the client to be killed</dl>
<p> You can kill a specific client owning window win </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> Window of the client to be killed</dl>
<p> References ecore_x_kill(). </p>
<p> Referenced by ecore_x_kill().</p>
<h3>EAPI void ecore_x_killall (Ecore_X_Window root)</h3>
<p>Kill all clients with subwindows under a given window. </p>
<p> You can kill all clients connected to the X server by using <code>ecore_x_window_root_list</code> to get a list of root windows, and then passing each root window to this function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The window whose children will be killed.</dl>
<p> References ecore_x_killall(). </p>
<p> Referenced by ecore_x_killall().</p>
<h3>EAPI int ecore_x_selection_clipboard_clear (void)</h3>
<p>Release ownership of the clipboard selection. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_clipboard_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_clipboard_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> References ecore_x_selection_clipboard_clear(). </p>
<p> Referenced by ecore_x_selection_clipboard_clear().</p>
<h3>EAPI int ecore_x_selection_clipboard_set (Ecore_X_Window w, const void * data, int size)</h3>
<p>Claim ownership of the CLIPBOARD selection and set its data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> Get the converted data from a previous CLIPBOARD selection request. The buffer must be freed when done with. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_clipboard_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_clipboard_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>w</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> Get the converted data from a previous CLIPBOARD selection request. The buffer must be freed when done with. </p>
<p> References ecore_x_selection_clipboard_set(). </p>
<p> Referenced by ecore_x_selection_clipboard_set().</p>
<h3>EAPI int ecore_x_selection_primary_clear (void)</h3>
<p>Release ownership of the primary selection. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_primary_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_primary_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> References ecore_x_selection_primary_clear(). </p>
<p> Referenced by ecore_x_selection_primary_clear().</p>
<h3>EAPI int ecore_x_selection_primary_set (Ecore_X_Window w, const void * data, int size)</h3>
<p>Claim ownership of the PRIMARY selection and set its data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_primary_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_primary_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>w</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> References ecore_x_selection_primary_set(). </p>
<p> Referenced by ecore_x_selection_primary_set().</p>
<h3>EAPI int ecore_x_selection_secondary_clear (void)</h3>
<p>Release ownership of the secondary selection. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_secondary_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_secondary_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> References ecore_x_selection_secondary_clear(). </p>
<p> Referenced by ecore_x_selection_secondary_clear().</p>
<h3>EAPI int ecore_x_selection_secondary_set (Ecore_X_Window w, const void * data, int size)</h3>
<p>Claim ownership of the SECONDARY selection and set its data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_secondary_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_secondary_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>w</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> References ecore_x_selection_secondary_set(). </p>
<p> Referenced by ecore_x_selection_secondary_set().</p>
<h3>EAPI int ecore_x_selection_xdnd_clear (void)</h3>
<p>Release ownership of the XDND selection. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_xdnd_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_xdnd_fetch()</code>, which gets the reply. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the selection was successfully cleared, or 0 if unsuccessful.</dl>
<p> References ecore_x_selection_xdnd_clear(). </p>
<p> Referenced by ecore_x_selection_xdnd_clear().</p>
<h3>EAPI int ecore_x_selection_xdnd_set (Ecore_X_Window w, const void * data, int size)</h3>
<p>Claim ownership of the XDND selection and set its data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_selection_xdnd_prefetch()</code>, which sends the GetSelectionOwner request, then <code>ecore_x_selection_xdnd_fetch()</code>, which gets the reply. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>w</i> The window to which this selection belongs<br />
 <i>data</i> The data associated with the selection<br />
 <i>size</i> The size of the data buffer in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns 1 if the ownership of the selection was successfully claimed, or 0 if unsuccessful.</dl>
<p> References ecore_x_selection_xdnd_set(). </p>
<p> Referenced by ecore_x_dnd_begin(), and ecore_x_selection_xdnd_set().</p>
<h3>EAPI void ecore_x_window_area_clear (Ecore_X_Window window, int x, int y, int width, int height)</h3>
<p>Clears an area of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>x</i> The X coordinate of the area.<br />
 <i>y</i> The Y coordinate of the area.<br />
 <i>width</i> The width of the area.<br />
 <i>height</i> The height of the area.</dl>
<p> References ecore_x_window_area_clear(). </p>
<p> Referenced by ecore_x_window_area_clear().</p>
<h3>EAPI void ecore_x_window_area_expose (Ecore_X_Window window, int x, int y, int width, int height)</h3>
<p>Exposes an area of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>x</i> The X coordinate of the area.<br />
 <i>y</i> The Y coordinate of the area.<br />
 <i>width</i> The width of the area.<br />
 <i>height</i> The height of the area.</dl>
<p> References ecore_x_window_area_expose(). </p>
<p> Referenced by ecore_x_window_area_expose().</p>
<h3>EAPI void ecore_x_window_defaults_set (Ecore_X_Window win)</h3>
<p>Sets the default properties for the given window. </p>
<p> The default properties set for the window are WM_CLIENT_MACHINE and _NET_WM_PID. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.</dl>
<p> The default properties set for the window are WM_CLIENT_MACHINE and _NET_WM_PID. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.</dl>
<p> References ecore_app_args_get(), ecore_x_icccm_command_set(), ecore_x_netwm_pid_set(), ecore_x_netwm_window_type_set(), and ecore_x_window_defaults_set(). </p>
<p> Referenced by ecore_x_window_defaults_set(), and ecore_x_window_new().</p>
<h3>EAPI int ecore_x_window_depth_get (Ecore_X_Window win)</h3>
<p>Retrieves the depth of the given window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Depth of the window.</dl>
<p> References ecore_x_drawable_depth_get(), and ecore_x_window_depth_get(). </p>
<p> Referenced by ecore_x_window_depth_get().</p>
<h3>EAPI Ecore_X_Window* ecore_x_window_ignore_list (int * num)</h3>
<p>Get the ignore list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>num</i> number of windows in the list</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>list of windows to ignore</dl>
<p> References ecore_x_window_ignore_list(). </p>
<p> Referenced by ecore_x_window_ignore_list().</p>
<h3>EAPI void ecore_x_window_ignore_set (Ecore_X_Window win, int ignore)</h3>
<p>Set if a window should be ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The given window.<br />
 <i>ignore</i> if to ignore<br />
 <i>win</i> The given window.<br />
 <i>ignore</i> if to ignore</dl>
<p> References ecore_x_window_ignore_set(). </p>
<p> Referenced by ecore_x_dnd_begin(), and ecore_x_window_ignore_set().</p>
<h3>EAPI Ecore_X_Atom ecore_x_window_prop_any_type (void)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_x_window_prop_any_type(). </p>
<p> Referenced by ecore_x_window_prop_any_type().</p>
<h3>EAPI void ecore_x_window_prop_atom_get_prefetch (Ecore_X_Window window, Ecore_X_Atom atom)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.<br />
 <i>atom</i> Property atom.</dl>
<p> References ecore_x_window_prop_atom_get_prefetch(). </p>
<p> Referenced by ecore_x_window_prop_atom_get_prefetch().</p>
<h3>EAPI void ecore_x_window_prop_card32_get_prefetch (Ecore_X_Window window, Ecore_X_Atom atom)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.<br />
 <i>atom</i> The atom.</dl>
<p> References ecore_x_window_prop_card32_get_prefetch(). </p>
<p> Referenced by ecore_x_window_prop_card32_get_prefetch().</p>
<h3>EAPI void ecore_x_window_prop_list_prefetch (Ecore_X_Window window)</h3>
<p>Sends the ListProperties request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.</dl>
<p> References ecore_x_window_prop_list_prefetch(). </p>
<p> Referenced by ecore_x_window_prop_list_prefetch().</p>
<h3>EAPI int ecore_x_window_prop_property_get (Ecore_X_Window win, Ecore_X_Atom property, Ecore_X_Atom type, int size __UNUSED__, unsigned char ** data, int * num)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_x_window_prop_property_get(). </p>
<p> Referenced by ecore_x_dnd_type_isset(), ecore_x_dnd_type_set(), ecore_x_dnd_version_get(), ecore_x_icccm_colormap_window_set(), ecore_x_icccm_colormap_window_unset(), and ecore_x_window_prop_property_get().</p>
<h3>EAPI void ecore_x_window_prop_property_get_prefetch (Ecore_X_Window window, Ecore_X_Atom property, Ecore_X_Atom type)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.<br />
 <i>property</i> Property atom.<br />
 <i>type</i> Type atom.</dl>
<p> References ecore_x_window_prop_property_get_prefetch(). </p>
<p> Referenced by ecore_x_window_prop_property_get_prefetch().</p>
<h3>EAPI void ecore_x_window_prop_property_set (Ecore_X_Window win, Ecore_X_Atom property, Ecore_X_Atom type, int size, void * data, int number)</h3>
<p>To be documented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>property</i> The property atom.<br />
 <i>type</i> The type atom.<br />
 <i>size</i> The size.<br />
 <i>data</i> The data.<br />
 <i>number</i> The size of the data.</dl>
<p> FIXME: To be fixed. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_x_window_prop_property_set(). </p>
<p> Referenced by ecore_x_dnd_type_set(), ecore_x_dnd_types_set(), ecore_x_icccm_colormap_window_set(), ecore_x_icccm_colormap_window_unset(), ecore_x_mwm_borderless_set(), and ecore_x_window_prop_property_set().</p>
<h3>EAPI Ecore_X_WM_Protocol* ecore_x_window_prop_protocol_list_get (Ecore_X_Window win, int * num_ret)</h3>
<p>To be documented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>num_ret</i> The number of WM protocols.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The returned WM protocols.</dl>
<p> FIXME: To be fixed. </p>
<p> FIXME: To be fixed. </p>
<p> References ecore_x_window_prop_protocol_list_get(). </p>
<p> Referenced by ecore_x_window_prop_protocol_list_get().</p>
<h3>EAPI char* ecore_x_window_prop_string_get (Ecore_X_Window win, Ecore_X_Atom type)</h3>
<p>Get a window string property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window<br />
 <i>type</i> The property</dl>
<p> Return window string property of a window. String must be free&#8217;d when done. </p>
<p> References ecore_x_window_prop_string_get(). </p>
<p> Referenced by ecore_x_icccm_client_machine_get(), ecore_x_icccm_window_role_get(), and ecore_x_window_prop_string_get().</p>
<h3>EAPI void ecore_x_window_prop_string_get_prefetch (Ecore_X_Window window, Ecore_X_Atom type)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.<br />
 <i>type</i> The atom.</dl>
<p> References ecore_x_window_prop_string_get_prefetch(). </p>
<p> Referenced by ecore_x_window_prop_string_get_prefetch().</p>
<h3>EAPI void ecore_x_window_prop_string_set (Ecore_X_Window win, Ecore_X_Atom type, const char * str)</h3>
<p>Set a window string property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window<br />
 <i>type</i> The property<br />
 <i>str</i> The string</dl>
<p> Set a window string property </p>
<p> References ecore_x_window_prop_string_set(). </p>
<p> Referenced by ecore_x_icccm_window_role_set(), and ecore_x_window_prop_string_set().</p>
<h3>EAPI void ecore_x_window_prop_window_get_prefetch (Ecore_X_Window window, Ecore_X_Atom atom)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.<br />
 <i>atom</i> The atom.</dl>
<p> References ecore_x_window_prop_window_get_prefetch(). </p>
<p> Referenced by ecore_x_window_prop_window_get_prefetch().</p>
<h3>EAPI void ecore_x_window_prop_xid_get_prefetch (Ecore_X_Window window, Ecore_X_Atom atom, Ecore_X_Atom type)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.<br />
 <i>atom</i> The atom.<br />
 <i>type</i> The atom type.</dl>
<p> References ecore_x_window_prop_xid_get_prefetch(). </p>
<p> Referenced by ecore_x_window_prop_xid_get_prefetch().</p>
<h3>EAPI Ecore_X_Window* ecore_x_window_root_list (int * num_ret)</h3>
<p>Get a list of all the root windows on the server. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The returned array will need to be freed after use.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>num_ret</i> Pointer to integer to put number of windows returned in.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An array of all the root windows. NULL is returned if memory could not be allocated for the list, or if num_ret is NULL.</dl>
<p> References ecore_x_window_root_list(). </p>
<p> Referenced by ecore_evas_software_x11_16_new(), ecore_evas_software_x11_new(), ecore_evas_xrender_x11_new(), and ecore_x_window_root_list().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
