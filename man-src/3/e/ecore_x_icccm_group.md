---
title: "ecore_x_icccm_group(3)"
name: "ecore_x_icccm_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_icccm_group/"
description: "ICCCM related functions. – Functions related to ICCCM."
---

<p>ICCCM related functions. &#8211; Functions related to ICCCM. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_icccm_state_set</code> (Ecore_X_Window window, Ecore_X_Window_State_Hint state)<br />
 <i>Sets the state of a window. </i><br />
 EAPI Ecore_X_Window_State_Hint <code>ecore_x_icccm_state_get</code> (Ecore_X_Window window __UNUSED__)<br />
 <i>Gets the state of a window. </i><br />
 EAPI void <code>ecore_x_icccm_delete_window_send</code> (Ecore_X_Window window, Ecore_X_Time time)<br />
 <i>Sends the ClientMessage event with the DeleteWindow property. </i><br />
 EAPI void <code>ecore_x_icccm_take_focus_send</code> (Ecore_X_Window window, Ecore_X_Time time)<br />
 <i>Sends the ClientMessage event with the TakeFocus property. </i><br />
 EAPI void <code>ecore_x_icccm_save_yourself_send</code> (Ecore_X_Window window, Ecore_X_Time time)<br />
 <i>Sends the ClientMessage event with the SaveYourself property. </i><br />
 EAPI void <code>ecore_x_icccm_move_resize_send</code> (Ecore_X_Window window, int x, int y, int width, int height)<br />
 <i>Sends the ConfigureNotify event with the StructureNotify property. </i><br />
 EAPI void <code>ecore_x_icccm_hints_set</code> (Ecore_X_Window window, int accepts_focus, Ecore_X_Window_State_Hint initial_state, Ecore_X_Pixmap icon_pixmap, Ecore_X_Pixmap icon_mask, Ecore_X_Window icon_window, Ecore_X_Window window_group, int is_urgent)<br />
 <i>Sets the hints of a window. </i><br />
 EAPI int <code>ecore_x_icccm_hints_get</code> (Ecore_X_Window window __UNUSED__, int *accepts_focus, Ecore_X_Window_State_Hint *initial_state, Ecore_X_Pixmap *icon_pixmap, Ecore_X_Pixmap *icon_mask, Ecore_X_Window *icon_window, Ecore_X_Window *window_group, int *is_urgent)<br />
 <i>Gets the hints of a window. </i><br />
 EAPI void <code>ecore_x_icccm_size_pos_hints_set</code> (Ecore_X_Window window, int request_pos, Ecore_X_Gravity gravity, int min_w, int min_h, int max_w, int max_h, int base_w, int base_h, int step_x, int step_y, double min_aspect, double max_aspect)<br />
 <i>Sets the hints of a window. </i><br />
 EAPI int <code>ecore_x_icccm_size_pos_hints_get</code> (Ecore_X_Window window __UNUSED__, int *request_pos, Ecore_X_Gravity *gravity, int *min_w, int *min_h, int *max_w, int *max_h, int *base_w, int *base_h, int *step_x, int *step_y, double *min_aspect, double *max_aspect)<br />
 <i>Gets the hints of a window. </i><br />
 EAPI void <code>ecore_x_icccm_title_set</code> (Ecore_X_Window window, const char *title)<br />
 <i>Set the title of a window. </i><br />
 EAPI char * <code>ecore_x_icccm_title_get</code> (Ecore_X_Window window __UNUSED__)<br />
 <i>Gets the title of a window. </i><br />
 EAPI void <code>ecore_x_icccm_protocol_set</code> (Ecore_X_Window window, Ecore_X_WM_Protocol protocol, int on)<br />
 <i>Set or unset a wm protocol property. </i><br />
 EAPI int <code>ecore_x_icccm_protocol_isset</code> (Ecore_X_Window window __UNUSED__, Ecore_X_WM_Protocol protocol)<br />
 <i>Determines whether a protocol is set for a window. </i><br />
 EAPI void <code>ecore_x_icccm_name_class_set</code> (Ecore_X_Window window, const char *name, const char *class)<br />
 <i>Set a window name &amp; class. </i><br />
 EAPI void <code>ecore_x_icccm_name_class_get</code> (Ecore_X_Window window __UNUSED__, char **name, char **class)<br />
 <i>Get a window name and class. </i><br />
 EAPI char * <code>ecore_x_icccm_client_machine_get</code> (Ecore_X_Window window)<br />
 <i>Get a window client machine string. </i><br />
 EAPI void <code>ecore_x_icccm_command_set</code> (Ecore_X_Window window, int argc, char **argv)<br />
 <i>Sets the WM_COMMAND property for win</i>.<br />
 EAPI void <code>ecore_x_icccm_command_get</code> (Ecore_X_Window window __UNUSED__, int *argc, char ***argv)<br />
 <i>Get the WM_COMMAND property for a window. </i><br />
 EAPI void <code>ecore_x_icccm_icon_name_set</code> (Ecore_X_Window window, const char *title)<br />
 <i>Set a window icon name. </i><br />
 EAPI char * <code>ecore_x_icccm_icon_name_get</code> (Ecore_X_Window window __UNUSED__)<br />
 <i>Get a window icon name. </i><br />
 EAPI void <code>ecore_x_icccm_colormap_window_set</code> (Ecore_X_Window window, Ecore_X_Window sub_window)<br />
 <i>Add a subwindow to the list of windows that need a different colormap installed. </i><br />
 EAPI void <code>ecore_x_icccm_colormap_window_unset</code> (Ecore_X_Window window, Ecore_X_Window sub_window)<br />
 <i>Remove a window from the list of colormap windows. </i><br />
 EAPI void <code>ecore_x_icccm_transient_for_set</code> (Ecore_X_Window window, Ecore_X_Window forwindow)<br />
 <i>Specify that a window is transient for another top-level window and should be handled accordingly. </i><br />
 EAPI void <code>ecore_x_icccm_transient_for_unset</code> (Ecore_X_Window window)<br />
 <i>Remove the transient_for setting from a window. </i><br />
 EAPI Ecore_X_Window <code>ecore_x_icccm_transient_for_get</code> (Ecore_X_Window window __UNUSED__)<br />
 <i>Get the window this window is transient for, if any. </i><br />
 EAPI void <code>ecore_x_icccm_window_role_set</code> (Ecore_X_Window window, const char *role)<br />
 <i>Set the window role hint. </i><br />
 EAPI void <code>ecore_x_icccm_window_role_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_icccm_window_role_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_icccm_window_role_get_prefetch()</code>.<br />
 EAPI char * <code>ecore_x_icccm_window_role_get</code> (Ecore_X_Window window)<br />
 <i>Get the window role. </i><br />
 EAPI void <code>ecore_x_icccm_client_leader_set</code> (Ecore_X_Window window, Ecore_X_Window leader)<br />
 <i>Set the window&#8217;s client leader. </i><br />
 EAPI void <code>ecore_x_icccm_client_leader_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_icccm_client_leader_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_icccm_client_leader_get_prefetch()</code>.<br />
 EAPI Ecore_X_Window <code>ecore_x_icccm_client_leader_get</code> (Ecore_X_Window window)<br />
 <i>Get the window&#8217;s client leader. </i><br />
 EAPI void <code>ecore_x_icccm_iconic_request_send</code> (Ecore_X_Window window, Ecore_X_Window root)<br />
 <i>Send the ClientMessage event with the ChangeState property. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to ICCCM.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_X_Window ecore_x_icccm_client_leader_get (Ecore_X_Window window)</h3>
<p>Get the window&#8217;s client leader. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window&#8217;s client leader window, or 0 if unset.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_icccm_client_leader_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_icccm_client_leader_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_icccm_client_leader_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.</dl>
<h3>EAPI void ecore_x_icccm_client_leader_set (Ecore_X_Window window, Ecore_X_Window leader)</h3>
<p>Set the window&#8217;s client leader. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>leader</i> The client leader window</dl>
<p> All non-transient top-level windows created by an app other than the main window must have this property set to the app&#8217;s main window.</p>
<h3>EAPI char* ecore_x_icccm_client_machine_get (Ecore_X_Window window)</h3>
<p>Get a window client machine string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The windows client machine string</dl>
<p> Return the client machine of a window. String must be free&#8217;d when done with. </p>
<p> To use this function, you must call before, and in order, ecore_x_icccm_client_machine_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_client_machine_get_fetch(), which gets the reply. </p>
<p> References ecore_x_window_prop_string_get().</p>
<h3>EAPI void ecore_x_icccm_colormap_window_set (Ecore_X_Window window, Ecore_X_Window sub_window)</h3>
<p>Add a subwindow to the list of windows that need a different colormap installed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The toplevel window<br />
 <i>sub_window</i> The subwindow to be added to the colormap windows list</dl>
<p> Add sub_window to the list of windows that need a different colormap installed. </p>
<p> To use this function, you must call before, and in order, ecore_x_icccm_colormap_window_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_colormap_window_get_fetch(), which gets the reply.</p>
<h3>EAPI void ecore_x_icccm_colormap_window_unset (Ecore_X_Window window, Ecore_X_Window sub_window)</h3>
<p>Remove a window from the list of colormap windows. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The toplevel window<br />
 <i>sub_window</i> The window to be removed from the colormap window list.</dl>
<p> Remove sub_window from the list of colormap windows. </p>
<p> To use this function, you must call before, and in order, ecore_x_icccm_colormap_window_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_colormap_window_get_fetch(), which gets the reply.</p>
<h3>EAPI void ecore_x_icccm_command_get (Ecore_X_Window window __UNUSED__, int * argc, char *** argv)</h3>
<p>Get the WM_COMMAND property for a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The window.<br />
 <i>argc</i> Number of arguments.<br />
 <i>argv</i> Arguments.</dl>
<p> Return the command of window and store it in argv. argc contains the number of arguments. String must be free&#8217;d when done with. </p>
<p> To use this function, you must call before, and in order, ecore_x_icccm_command_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_command_get_fetch(), which gets the reply. </p>
<p> References ecore_x_icccm_command_get().</p>
<h3>EAPI void ecore_x_icccm_command_set (Ecore_X_Window window, int argc, char ** argv)</h3>
<p>Sets the WM_COMMAND property for <i>win</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>argc</i> Number of arguments.<br />
 <i>argv</i> Arguments.</dl>
<h3>EAPI void ecore_x_icccm_delete_window_send (Ecore_X_Window window, Ecore_X_Time time)</h3>
<p>Sends the ClientMessage event with the DeleteWindow property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>time</i> The time.</dl>
<p> References ecore_x_client_message32_send().</p>
<h3>EAPI int ecore_x_icccm_hints_get (Ecore_X_Window window __UNUSED__, int * accepts_focus, Ecore_X_Window_State_Hint * initial_state, Ecore_X_Pixmap * icon_pixmap, Ecore_X_Pixmap * icon_mask, Ecore_X_Window * icon_window, Ecore_X_Window * window_group, int * is_urgent)</h3>
<p>Gets the hints of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>accepts_focus</i> AcceptFocus hint<br />
 <i>initial_state</i> Initial state flags.<br />
 <i>icon_pixmap</i> Icon pixmap.<br />
 <i>icon_mask</i> Icon mask.<br />
 <i>icon_window</i> Icon window.<br />
 <i>window_group</i> Group window.<br />
 <i>is_urgent</i> IsUrgent flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_hints_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_hints_get_fetch(), which gets the reply. </p>
<p> References ECORE_X_WINDOW_STATE_HINT_ICONIC, ECORE_X_WINDOW_STATE_HINT_NORMAL, and ECORE_X_WINDOW_STATE_HINT_WITHDRAWN.</p>
<h3>EAPI void ecore_x_icccm_hints_set (Ecore_X_Window window, int accepts_focus, Ecore_X_Window_State_Hint initial_state, Ecore_X_Pixmap icon_pixmap, Ecore_X_Pixmap icon_mask, Ecore_X_Window icon_window, Ecore_X_Window window_group, int is_urgent)</h3>
<p>Sets the hints of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>accepts_focus</i> AcceptFocus hint<br />
 <i>initial_state</i> Initial state flags.<br />
 <i>icon_pixmap</i> Icon pixmap.<br />
 <i>icon_mask</i> Icon mask.<br />
 <i>icon_window</i> Icon window.<br />
 <i>window_group</i> Group window.<br />
 <i>is_urgent</i> IsUrgent flag.</dl>
<p> References ECORE_X_WINDOW_STATE_HINT_ICONIC, ECORE_X_WINDOW_STATE_HINT_NORMAL, and ECORE_X_WINDOW_STATE_HINT_WITHDRAWN.</p>
<h3>EAPI char* ecore_x_icccm_icon_name_get (Ecore_X_Window window __UNUSED__)</h3>
<p>Get a window icon name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The windows icon name string.</dl>
<p> Return the icon name of window. String must be free&#8217;d when done with. </p>
<p> To use this function, you must call before, and in order, ecore_x_icccm_icon_name_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_icon_name_get_fetch(), which gets the reply. </p>
<p> References ecore_x_icccm_icon_name_get().</p>
<h3>EAPI void ecore_x_icccm_icon_name_set (Ecore_X_Window window, const char * title)</h3>
<p>Set a window icon name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>title</i> The icon name string.</dl>
<p> Set window icon name.</p>
<h3>EAPI void ecore_x_icccm_iconic_request_send (Ecore_X_Window window, Ecore_X_Window root)</h3>
<p>Send the ClientMessage event with the ChangeState property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>root</i> The root window.</dl>
<h3>EAPI void ecore_x_icccm_move_resize_send (Ecore_X_Window window, int x, int y, int width, int height)</h3>
<p>Sends the ConfigureNotify event with the StructureNotify property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>x</i> The X coordinate.<br />
 <i>y</i> The Y coordinate.<br />
 <i>width</i> The width.<br />
 <i>height</i> The height.</dl>
<h3>EAPI void ecore_x_icccm_name_class_get (Ecore_X_Window window __UNUSED__, char ** name, char ** class)</h3>
<p>Get a window name and class. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window (Unused).<br />
 <i>name</i> The name string.<br />
 <i>class</i> The class string.</dl>
<p> Store the name and class of window into respectively name and class. </p>
<p> To use this function, you must call before, and in order, ecore_x_icccm_name_class_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_name_class_get_fetch(), which gets the reply. </p>
<p> References ecore_x_icccm_name_class_get().</p>
<h3>EAPI void ecore_x_icccm_name_class_set (Ecore_X_Window window, const char * name, const char * class)</h3>
<p>Set a window name &amp; class. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>name</i> The name string<br />
 <i>class</i> The class string</dl>
<p> Set the name and class of window to respectively name and class.</p>
<h3>EAPI int ecore_x_icccm_protocol_isset (Ecore_X_Window window __UNUSED__, Ecore_X_WM_Protocol protocol)</h3>
<p>Determines whether a protocol is set for a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The Window (Unused).<br />
 <i>protocol</i> The protocol to query.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the protocol is set, else 0.</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_protocol_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_protocol_get_fetch(), which gets the reply. </p>
<p> References ecore_x_icccm_protocol_isset().</p>
<h3>EAPI void ecore_x_icccm_protocol_set (Ecore_X_Window window, Ecore_X_WM_Protocol protocol, int on)</h3>
<p>Set or unset a wm protocol property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The Window<br />
 <i>protocol</i> The protocol to enable/disable<br />
 <i>on</i> On/Off</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_protocol_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_protocol_get_fetch(), which gets the reply.</p>
<h3>EAPI void ecore_x_icccm_save_yourself_send (Ecore_X_Window window, Ecore_X_Time time)</h3>
<p>Sends the ClientMessage event with the SaveYourself property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>time</i> The time.</dl>
<p> References ecore_x_client_message32_send().</p>
<h3>EAPI int ecore_x_icccm_size_pos_hints_get (Ecore_X_Window window __UNUSED__, int * request_pos, Ecore_X_Gravity * gravity, int * min_w, int * min_h, int * max_w, int * max_h, int * base_w, int * base_h, int * step_x, int * step_y, double * min_aspect, double * max_aspect)</h3>
<p>Gets the hints of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>request_pos</i> Request position flag.<br />
 <i>gravity</i> Gravity.<br />
 <i>min_w</i> Minimum width.<br />
 <i>min_h</i> Minimum height.<br />
 <i>max_w</i> Maximum width.<br />
 <i>max_h</i> Maximum height.<br />
 <i>base_w</i> Base width<br />
 <i>base_h</i> Base height<br />
 <i>step_x</i> X step coordinate.<br />
 <i>step_y</i> Y step coordinate.<br />
 <i>min_aspect</i> Minimum aspect ratio.<br />
 <i>max_aspect</i> M</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_size_pos_hints_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_size_pos_hints_get_fetch(), which gets the reply.</p>
<h3>EAPI void ecore_x_icccm_size_pos_hints_set (Ecore_X_Window window, int request_pos, Ecore_X_Gravity gravity, int min_w, int min_h, int max_w, int max_h, int base_w, int base_h, int step_x, int step_y, double min_aspect, double max_aspect)</h3>
<p>Sets the hints of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>request_pos</i> Request position flag.<br />
 <i>gravity</i> Gravity.<br />
 <i>min_w</i> Minimum width.<br />
 <i>min_h</i> Minimum height.<br />
 <i>max_w</i> Maximum width.<br />
 <i>max_h</i> Maximum height.<br />
 <i>base_w</i> Base width<br />
 <i>base_h</i> Base height<br />
 <i>step_x</i> X step coordinate.<br />
 <i>step_y</i> Y step coordinate.<br />
 <i>min_aspect</i> Minimum aspect ratio.<br />
 <i>max_aspect</i> Maximum aspect ratio.</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_size_pos_hints_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_size_pos_hints_get_fetch(), which gets the reply.</p>
<h3>EAPI Ecore_X_Window_State_Hint ecore_x_icccm_state_get (Ecore_X_Window window __UNUSED__)</h3>
<p>Gets the state of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The state of the window</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_state_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_state_get_fetch(), which gets the reply. </p>
<p> References ECORE_X_WINDOW_STATE_HINT_ICONIC, ECORE_X_WINDOW_STATE_HINT_NONE, ECORE_X_WINDOW_STATE_HINT_NORMAL, and ECORE_X_WINDOW_STATE_HINT_WITHDRAWN.</p>
<h3>EAPI void ecore_x_icccm_state_set (Ecore_X_Window window, Ecore_X_Window_State_Hint state)</h3>
<p>Sets the state of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>state</i> The state.</dl>
<p> References ECORE_X_WINDOW_STATE_HINT_ICONIC, ECORE_X_WINDOW_STATE_HINT_NORMAL, and ECORE_X_WINDOW_STATE_HINT_WITHDRAWN.</p>
<h3>EAPI void ecore_x_icccm_take_focus_send (Ecore_X_Window window, Ecore_X_Time time)</h3>
<p>Sends the ClientMessage event with the TakeFocus property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>time</i> The time.</dl>
<p> References ecore_x_client_message32_send().</p>
<h3>EAPI char* ecore_x_icccm_title_get (Ecore_X_Window window __UNUSED__)</h3>
<p>Gets the title of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window (Unused).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The title of the window</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_title_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_title_get_fetch(), which gets the reply.</p>
<h3>EAPI void ecore_x_icccm_title_set (Ecore_X_Window window, const char * title)</h3>
<p>Set the title of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>title</i> The title.</dl>
<h3>EAPI Ecore_X_Window ecore_x_icccm_transient_for_get (Ecore_X_Window window __UNUSED__)</h3>
<p>Get the window this window is transient for, if any. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window to check (Unused).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window ID of the top-level window, or 0 if the property does not exist.</dl>
<p> To use this function, you must call before, and in order, ecore_x_icccm_transient_for_get_prefetch(), which sends the GetProperty request, then ecore_x_icccm_transient_for_get_fetch(), which gets the reply. </p>
<p> References ecore_x_icccm_transient_for_get().</p>
<h3>EAPI void ecore_x_icccm_transient_for_set (Ecore_X_Window window, Ecore_X_Window forwindow)</h3>
<p>Specify that a window is transient for another top-level window and should be handled accordingly. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The transient window<br />
 <i>forwindow</i> The toplevel window</dl>
<h3>EAPI void ecore_x_icccm_transient_for_unset (Ecore_X_Window window)</h3>
<p>Remove the transient_for setting from a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI char* ecore_x_icccm_window_role_get (Ecore_X_Window window)</h3>
<p>Get the window role. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The window&#8217;s role string.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_icccm_window_role_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_icccm_window_role_get_fetch()</code>, which gets the reply. </p>
<p> References ecore_x_window_prop_string_get().</p>
<h3>EAPI void ecore_x_icccm_window_role_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.</dl>
<h3>EAPI void ecore_x_icccm_window_role_set (Ecore_X_Window window, const char * role)</h3>
<p>Set the window role hint. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>role</i> The role string.</dl>
<p> References ecore_x_window_prop_string_set().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
