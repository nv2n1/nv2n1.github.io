---
title: "ecore_x_netwm_group(3)"
name: "ecore_x_netwm_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_netwm_group/"
description: "Extended Window Manager Hint (EWMH) functions – Functions related to the Extended Window Manager Hint (EWMH)."
---

<p>Extended Window Manager Hint (EWMH) functions &#8211; Functions related to the Extended Window Manager Hint (EWMH). </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_netwm_wm_identify</code> (Ecore_X_Window root, Ecore_X_Window check, const char *wm_name)<br />
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
 EAPI void <code>ecore_x_netwm_desk_viewports_set</code> (Ecore_X_Window root, unsigned int *origins, unsigned int n_desks)<br />
 <i>Set the _NET_DESKTOP_VIEWPORT property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_layout_set</code> (Ecore_X_Window root, int orientation, int columns, int rows, int starting_corner)<br />
 <i>Set the _NET_DESKTOP_LAYOUT property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_workareas_set</code> (Ecore_X_Window root, unsigned int *areas, unsigned int n_desks)<br />
 <i>Set the _NET_WORKAREA property. </i><br />
 EAPI void <code>ecore_x_netwm_desk_current_set</code> (Ecore_X_Window root, unsigned int desk)<br />
 <i>Set the _NET_CURRENT_DESKTOP property. </i><br />
 EAPI void <code>ecore_x_netwm_showing_desktop_set</code> (Ecore_X_Window root, int on)<br />
 <i>Set the _NET_SHOWING_DESKTOP property. </i><br />
 EAPI void <code>ecore_x_netwm_client_list_set</code> (Ecore_X_Window root, Ecore_X_Window *p_clients, unsigned int n_clients)<br />
 <i>Set the _NET_CLIENT_LIST property. </i><br />
 EAPI void <code>ecore_x_netwm_client_list_stacking_set</code> (Ecore_X_Window root, Ecore_X_Window *p_clients, unsigned int n_clients)<br />
 <i>Set the _NET_CLIENT_LIST_STACKING property. </i><br />
 EAPI void <code>ecore_x_netwm_client_active_set</code> (Ecore_X_Window root, Ecore_X_Window window)<br />
 <i>Set the _NET_ACTIVE_WINDOW property. </i><br />
 EAPI void <code>ecore_x_netwm_name_set</code> (Ecore_X_Window window, const char *name)<br />
 <i>Set the _NET_WM_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_name_get</code> (Ecore_X_Window window, char **name)<br />
 <i>Get the title of a window. </i><br />
 EAPI void <code>ecore_x_netwm_startup_id_set</code> (Ecore_X_Window window, const char *id)<br />
 <i>Set the _NET_STARTUP_ID property. </i><br />
 EAPI void <code>ecore_x_netwm_startup_id_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_startup_id_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_startup_id_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_startup_id_get</code> (Ecore_X_Window window, char **id)<br />
 <i>Get the startup ID name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_visible_name_set</code> (Ecore_X_Window window, const char *name)<br />
 <i>Set the _NET_WM_VISIBLE_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_visible_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_visible_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_visible_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_visible_name_get</code> (Ecore_X_Window window, char **name)<br />
 <i>Get the visible title of a window. </i><br />
 EAPI void <code>ecore_x_netwm_icon_name_set</code> (Ecore_X_Window window, const char *name)<br />
 <i>Set the _NET_WM_ICON_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_icon_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_icon_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_icon_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_icon_name_get</code> (Ecore_X_Window window, char **name)<br />
 <i>Get the icon name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_visible_icon_name_set</code> (Ecore_X_Window window, const char *name)<br />
 <i>Set the _NET_WM_VISIBLE_ICON_NAME property. </i><br />
 EAPI void <code>ecore_x_netwm_visible_icon_name_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_visible_icon_name_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_visible_icon_name_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_visible_icon_name_get</code> (Ecore_X_Window window, char **name)<br />
 <i>Get the visible icon name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_set</code> (Ecore_X_Window window, unsigned int desk)<br />
 <i>Set the _NET_WM_DESKTOP property. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_desktop_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_desktop_get</code> (Ecore_X_Window window, unsigned int *desk)<br />
 <i>Get the visible icon name of a window. </i><br />
 EAPI void <code>ecore_x_netwm_strut_set</code> (Ecore_X_Window window, int left, int right, int top, int bottom)<br />
 <i>Set the _NET_WM_STRUT property. </i><br />
 EAPI void <code>ecore_x_netwm_strut_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_strut_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_strut_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_strut_get</code> (Ecore_X_Window window, int *left, int *right, int *top, int *bottom)<br />
 <i>Get the space at the edje of the screen. </i><br />
 EAPI void <code>ecore_x_netwm_strut_partial_set</code> (Ecore_X_Window window, int left, int right, int top, int bottom, int left_start_y, int left_end_y, int right_start_y, int right_end_y, int top_start_x, int top_end_x, int bottom_start_x, int bottom_end_x)<br />
 <i>Set the _NET_WM_STRUT_PARTIAL property. </i><br />
 EAPI void <code>ecore_x_netwm_strut_partial_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_strut_partial_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_strut_partial_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_strut_partial_get</code> (Ecore_X_Window window, int *left, int *right, int *top, int *bottom, int *left_start_y, int *left_end_y, int *right_start_y, int *right_end_y, int *top_start_x, int *top_end_x, int *bottom_start_x, int *bottom_end_x)<br />
 <i>Get the space at the edje of the screen of a window. </i><br />
 EAPI void <code>ecore_x_netwm_icons_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_icons_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_icons_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_icons_get</code> (Ecore_X_Window window, Ecore_X_Icon **icon, int *num)<br />
 <i>Retrieve hte possible icons of a window. </i><br />
 EAPI void <code>ecore_x_netwm_icon_geometry_set</code> (Ecore_X_Window window, int x, int y, int width, int height)<br />
 <i>Set the _NET_WM_ICON_GEOMETRY property. </i><br />
 EAPI void <code>ecore_x_netwm_icon_geometry_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_icon_geometry_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_icon_geometry_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_icon_geometry_get</code> (Ecore_X_Window window, int *x, int *y, int *width, int *height)<br />
 <i>Get the geometry of an icon. </i><br />
 EAPI void <code>ecore_x_netwm_pid_set</code> (Ecore_X_Window window, int pid)<br />
 <i>Set the _NET_WM_PID property. </i><br />
 EAPI void <code>ecore_x_netwm_pid_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_pid_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_pid_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_pid_get</code> (Ecore_X_Window window, int *pid)<br />
 <i>Get the process ID of a client window. </i><br />
 EAPI void <code>ecore_x_netwm_handled_icons_set</code> (Ecore_X_Window window)<br />
 <i>Set the _NET_WM_HANDLED_ICONS property. </i><br />
 EAPI void <code>ecore_x_netwm_handled_icons_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_handled_icons_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_handled_icons_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_handled_icons_get</code> (Ecore_X_Window window)<br />
 <i>Return wheter the Client handles icons or not. </i><br />
 EAPI void <code>ecore_x_netwm_user_time_set</code> (Ecore_X_Window window, unsigned int time)<br />
 <i>Set the _NET_WM_USER_TIME property. </i><br />
 EAPI void <code>ecore_x_netwm_user_time_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_user_time_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_user_time_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_user_time_get</code> (Ecore_X_Window window, unsigned int *time)<br />
 <i>Get the last user activity time in the window. </i><br />
 EAPI void <code>ecore_x_netwm_window_state_set</code> (Ecore_X_Window window, Ecore_X_Window_State *state, unsigned int num)<br />
 <i>Set the _NET_WM_STATE property. </i><br />
 EAPI void <code>ecore_x_netwm_window_state_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_window_state_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_window_state_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_window_state_get</code> (Ecore_X_Window window, Ecore_X_Window_State **state, unsigned int *num)<br />
 <i>Get the hints describing the window state. </i><br />
 EAPI void <code>ecore_x_netwm_window_type_set</code> (Ecore_X_Window window, Ecore_X_Window_Type type)<br />
 <i>Set the _NET_WM_WINDOW_TYPE property. </i><br />
 EAPI void <code>ecore_x_netwm_window_type_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_window_type_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_window_type_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_window_type_get</code> (Ecore_X_Window window, Ecore_X_Window_Type *type)<br />
 <i>Get the functional type of a window. </i><br />
 EAPI void <code>ecore_x_netwm_allowed_action_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_allowed_action_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by ecore_x_allowed_action_get_prefetch(). </i><br />
 EAPI int <code>ecore_x_netwm_allowed_action_isset</code> (Ecore_X_Window window, Ecore_X_Action action)<br />
 <i>Check whether an action is supported by a window. </i><br />
 EAPI void <code>ecore_x_netwm_allowed_action_set</code> (Ecore_X_Window window, Ecore_X_Action *action, unsigned int num)<br />
 <i>Set the _NET_WM_ALLOWED_ACTIONS property. </i><br />
 EAPI int <code>ecore_x_netwm_allowed_action_get</code> (Ecore_X_Window window, Ecore_X_Action **action, unsigned int *num)<br />
 <i>Get the allowed actions supported by a window. </i><br />
 EAPI void <code>ecore_x_netwm_opacity_set</code> (Ecore_X_Window window, unsigned int opacity)<br />
 <i>Set the _NET_WM_WINDOW_OPACITY property. </i><br />
 EAPI void <code>ecore_x_netwm_opacity_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_opacity_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_opacity_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_opacity_get</code> (Ecore_X_Window window, unsigned int *opacity)<br />
 <i>Get the opacity value of a window. </i><br />
 EAPI void <code>ecore_x_netwm_frame_size_set</code> (Ecore_X_Window window, int fl, int fr, int ft, int fb)<br />
 <i>Set the _NET_FRAME_EXTENTS property. </i><br />
 EAPI void <code>ecore_x_netwm_frame_size_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_frame_size_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_frame_size_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_frame_size_get</code> (Ecore_X_Window window, int *fl, int *fr, int *ft, int *fb)<br />
 <i>Get the frame extent of a window. </i><br />
 EAPI void <code>ecore_x_netwm_sync_counter_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_netwm_sync_counter_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_netwm_sync_counter_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_netwm_sync_counter_get</code> (Ecore_X_Window window, Ecore_X_Sync_Counter *counter)<br />
 <i>Get the X ID of a X Sync counter. </i><br />
 EAPI void <code>ecore_x_netwm_ping_send</code> (Ecore_X_Window window)<br />
 <i>Send a _NET_WM_PING property event. </i><br />
 EAPI void <code>ecore_x_netwm_sync_request_send</code> (Ecore_X_Window window, unsigned int serial)<br />
 <i>Send a _NET_WM_SYNC_REQUEST property event. </i><br />
 EAPI void <code>ecore_x_netwm_state_request_send</code> (Ecore_X_Window window, Ecore_X_Window root, Ecore_X_Window_State s1, Ecore_X_Window_State s2, int set)<br />
 <i>Send a _NET_WM_STATE property event. </i><br />
 EAPI void <code>ecore_x_netwm_desktop_request_send</code> (Ecore_X_Window window, Ecore_X_Window root, unsigned int desktop)<br />
 <i>Send a _NET_WM_DESKTOP property event. </i><br />
 EAPI int <code>ecore_x_screen_is_composited</code> (int screen)<br />
 <i>Check whether a screen is composited or not. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to the Extended Window Manager Hint (EWMH).</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_netwm_allowed_action_get (Ecore_X_Window window, Ecore_X_Action ** action, unsigned int * num)</h3>
<p>Get the allowed actions supported by a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>action</i> The returned array of the actions.<br />
 <i>num</i> The number of actions.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the user operations that the Window Manager supports for window and store them in action. The number of actions is stored in num. This function returns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_allowed_action_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_allowed_action_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_allowed_action_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI int ecore_x_netwm_allowed_action_isset (Ecore_X_Window window, Ecore_X_Action action)</h3>
<p>Check whether an action is supported by a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>action</i> The action</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if set, 0 otherwise.</dl>
<p> Return whether the user operation action is supported by the Window Manager for window. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_allowed_action_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_allowed_action_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_allowed_action_set (Ecore_X_Window window, Ecore_X_Action * action, unsigned int num)</h3>
<p>Set the _NET_WM_ALLOWED_ACTIONS property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>action</i> An array of allowed actions.<br />
 <i>num</i> The number of actions.</dl>
<p> Set the user operations that the Window Manager supports for window by sending the _NET_WM_ALLOWED_ACTIONS property to window. action stores num actions. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_allowed_action_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_allowed_action_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_client_active_set (Ecore_X_Window root, Ecore_X_Window window)</h3>
<p>Set the _NET_ACTIVE_WINDOW property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>window</i> The widow to activate.</dl>
<p> Activate window by sending the _NET_ACTIVE_WINDOW property to the root window. </p>
<p> If a Client wants to activate another window, it MUST call this function.</p>
<h3>EAPI void ecore_x_netwm_client_list_set (Ecore_X_Window root, Ecore_X_Window * p_clients, unsigned int n_clients)</h3>
<p>Set the _NET_CLIENT_LIST property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>p_clients</i> An array of windows.<br />
 <i>n_clients</i> The number of windows.</dl>
<p> Map all the X windows managed by the window manager from the oldest to the newest by sending the _NET_CLIENT_LIST property to the root window. The X windows are stored in p_clients and their number in n_clients. </p>
<p> This function SHOULD be called by the Window Manager.</p>
<h3>EAPI void ecore_x_netwm_client_list_stacking_set (Ecore_X_Window root, Ecore_X_Window * p_clients, unsigned int n_clients)</h3>
<p>Set the _NET_CLIENT_LIST_STACKING property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>p_clients</i> An array of windows.<br />
 <i>n_clients</i> The number of windows.</dl>
<p> Stack all the X windows managed by the window manager from bottom to top order by sending the _NET_CLIENT_LIST_STACKING property to the root window. The X windows are stored in p_clients and their number in n_clients. </p>
<p> This function SHOULD be called by the Window Manager.</p>
<h3>EAPI void ecore_x_netwm_desk_count_set (Ecore_X_Window root, unsigned int n_desks)</h3>
<p>Set the _NET_NUMBER_OF_DESKTOPS property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>n_desks</i> The number of desktops.</dl>
<p> Set the number of desktops n_desks of the Window Manager by sending the _NET_NUMBER_OF_DESKTOPS to the root window. </p>
<p> The Window Manager SHOULD set and update this property to indicate the number of virtual desktops. A Pager can request a change in the number of desktops by using that function.</p>
<h3>EAPI void ecore_x_netwm_desk_current_set (Ecore_X_Window root, unsigned int desk)</h3>
<p>Set the _NET_CURRENT_DESKTOP property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>desk</i> The index of the current desktop.</dl>
<p> Set the current desktop by sending the _NET_CURRENT_DESKTOP to the root window. deskmust be an integer number between 0 and the number of desks (set by <code>ecore_x_netwm_desk_count_set()</code>) -1. </p>
<p> This function MUST be called by the Window Manager. If a Pagerwants to switch to naother desktop, it MUST call that function.</p>
<h3>EAPI void ecore_x_netwm_desk_layout_set (Ecore_X_Window root, int orientation, int columns, int rows, int starting_corner)</h3>
<p>Set the _NET_DESKTOP_LAYOUT property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>orientation</i><br />
 <i>columns</i><br />
 <i>rows</i><br />
 <i>starting_corner</i> Set the layout of virtual desktops relative to each other by sending the _NET_DESKTOP_LAYOUT to the root window. orientation defines the orientation of the virtual desktop. 0 means horizontal layout, 1 means vertical layout. columns is the number of desktops in the X direction and rows is the number in the Y direction. starting_corner is the corner containing the first desktop. The values for starting_corner are 0 (top-left), 1 (top-right), 2 (bottom-right) and 3 (bottom-left).</dl>
<p> When the orientation is horizontal the desktops are laid out in rows, with the first desktop in the specified starting corner. So a layout with four columns and three rows starting in the top-left corner looks like this: </p>
<p> +&#8211;+&#8211;+&#8211;+&#8211;+ | 0| 1| 2| 3| +&#8211;+&#8211;+&#8211;+&#8211;+ | 4| 5| 6| 7| +&#8211;+&#8211;+&#8211;+&#8211;+ | 8| 9|10|11| +&#8211;+&#8211;+&#8211;+&#8211;+ </p>
<p> With starting_corner being bottom-right, it looks like this: </p>
<p> +&#8211;+&#8211;+&#8211;+&#8211;+ |11|10| 9| 8| +&#8211;+&#8211;+&#8211;+&#8211;+ | 7| 6| 5| 4| +&#8211;+&#8211;+&#8211;+&#8211;+ | 3| 2| 1| 0| +&#8211;+&#8211;+&#8211;+&#8211;+ </p>
<p> When the orientation is vertical the layout with four columns and three rows starting in the top-left corner looks like: </p>
<p> +&#8211;+&#8211;+&#8211;+&#8211;+ | 0| 3| 6| 9| +&#8211;+&#8211;+&#8211;+&#8211;+ | 1| 4| 7|10| +&#8211;+&#8211;+&#8211;+&#8211;+ | 2| 5| 8|11| +&#8211;+&#8211;+&#8211;+&#8211;+ </p>
<p> With starting_corner being top-right, it looks like: </p>
<p> +&#8211;+&#8211;+&#8211;+&#8211;+ | 9| 6| 3| 0| +&#8211;+&#8211;+&#8211;+&#8211;+ |10| 7| 4| 1| +&#8211;+&#8211;+&#8211;+&#8211;+ |11| 8| 5| 2| +&#8211;+&#8211;+&#8211;+&#8211;+ </p>
<p> This function MUST be used by a Pager and NOT by the Window Manager. When using this function, the Pager must own a manager selection.</p>
<h3>EAPI void ecore_x_netwm_desk_names_set (Ecore_X_Window root, const char ** names, unsigned int n_desks)</h3>
<p>Set the _NET_DESKTOP_NAMES property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>names</i> The names of the virtual desktops.<br />
 <i>n_desks</i> The number of virtual desktops.</dl>
<p> Set the name of each virtual desktop by sending the _NET_DESKTOP_NAMES to the root window. names are the names of the virtual desktops and n_desks is the number of virtual desktops. </p>
<p> A Pager MAY use that function. n_desks may be different from the one passed to <code>ecore_x_netwm_desk_count_set()</code>. If it less or equal, then the desktops with high numbers are unnamed. If it is larger, then the excess names are considered to be reserved in case the number of desktops is increased.</p>
<h3>EAPI void ecore_x_netwm_desk_roots_set (Ecore_X_Window root, Ecore_X_Window * vroots, unsigned int n_desks)</h3>
<p>Set the _NET_VIRTUAL_ROOTS property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>vroots</i> The virtual root windows.<br />
 <i>n_desks</i> The number of desks.</dl>
<p> Set the number of virtual desktops by sending the _NET_VIRTUAL_ROOTS property to the root window. vroots is an array of window and n_desks is the number of windows. </p>
<p> A Window Manager that implements virtual desktops by reparent client windows to a child of the root window MUST use that function.</p>
<h3>EAPI void ecore_x_netwm_desk_size_set (Ecore_X_Window root, unsigned int width, unsigned int height)</h3>
<p>Set the _NET_DESKTOP_GEOMETRY property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>width</i> The width of the desktop.<br />
 <i>height</i> The height of the desktop.</dl>
<p> Set the common width and height of all desktops by sending the _NET_DESKTOP_GEOMETRY to the root window. </p>
<p> This size is equal to the screen size if the Window Manager doesn&#8217;t support large desktops, otherwise it&#8217;s equal to the virtual size of the desktop. The Window Manager SHOULD set this property. A Pager can request a change in the desktop geometry by using this function.</p>
<h3>EAPI void ecore_x_netwm_desk_viewports_set (Ecore_X_Window root, unsigned int * origins, unsigned int n_desks)</h3>
<p>Set the _NET_DESKTOP_VIEWPORT property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>origins</i> An array of paris of coordiantes.<br />
 <i>n_desks</i> The number of virtual desktops.</dl>
<p> Set the top left corner of each desktop&#8217;s viewport by sending the _NET_DESKTOP_VIEWPORT property to the root window. origins contains each pair of X coordinate and Y coordinate of the top left corner of each desktop&#8217;s viewport. </p>
<p> If the Window Manager does not support large desktops, the coordinates MUST be (0,0). A Pager can request to change the viewport for the current desktop by using this function.</p>
<h3>EAPI void ecore_x_netwm_desk_workareas_set (Ecore_X_Window root, unsigned int * areas, unsigned int n_desks)</h3>
<p>Set the _NET_WORKAREA property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>areas</i> An array of areas.<br />
 <i>n_desks</i> The number of desks.</dl>
<p> Set the work area for each desktop by sending the _NET_WORKAREA property to the root window. An area contains the geometry (X and Y coordinates, width and height). These geometries are specified relative to the viewport on each desktop and specify an area that is completely contained within the viewport. areas stores these geometries. n_desks is the number of geometry to set. </p>
<p> This function MUST be set by the Window Manager. It is used by desktop applications to place desktop icons appropriately.</p>
<h3>EAPI int ecore_x_netwm_desktop_get (Ecore_X_Window window, unsigned int * desk)</h3>
<p>Get the visible icon name of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>desk</i> The desktop index.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the desktop index in which window is displayed and store it in desk. If desk value is 0xFFFFFFFF, the window appears on all desktops. The function returns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_desktop_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_desktop_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_desktop_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_desktop_request_send (Ecore_X_Window window, Ecore_X_Window root, unsigned int desktop)</h3>
<p>Send a _NET_WM_DESKTOP property event. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>root</i> The root window.<br />
 <i>desktop</i> The new desktop index.</dl>
<p> Send a ClientMessage event from window to the root window with the _NET_WM_DESKTOP property set. This change the state of a non-withdrawn window. desktop is the new desktop index to set.</p>
<h3>EAPI void ecore_x_netwm_desktop_set (Ecore_X_Window window, unsigned int desk)</h3>
<p>Set the _NET_WM_DESKTOP property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>desk</i> The desktop index.</dl>
<p> Set on which desktop the window is in by sending the _NET_WM_DESKTOP property to window. desk is the index of the desktop, starting from 0. To indicate that the window should appear on all desktops, desk must be equal to 0xFFFFFFFF. </p>
<p> A Client MAY choose not to set this property, in which case the Window Manager SHOULD place it as it wishes. </p>
<p> The Window Manager should honor _NET_WM_DESKTOP whenever a withdrawn window requests to be mapped. </p>
<p> A Client can request a change of desktop for a non-withdrawn window by sending a _NET_WM_DESKTOP client message to the root window.</p>
<h3>EAPI int ecore_x_netwm_frame_size_get (Ecore_X_Window window, int * fl, int * fr, int * ft, int * fb)</h3>
<p>Get the frame extent of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>fl</i> The number of pixels of the left border of the window.<br />
 <i>fr</i> The number of pixels of the right border of the window.<br />
 <i>ft</i> The number of pixels of the top border of the window.<br />
 <i>fb</i> The number of pixels of the bottom border of the window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the frame extents of window. The number of pixels of the left, right, top and bottom border of window are respectively stored in fl, fr, ft anfd fb. TYhis function retuirns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_frame_size_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_frame_size_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_frame_size_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_frame_size_set (Ecore_X_Window window, int fl, int fr, int ft, int fb)</h3>
<p>Set the _NET_FRAME_EXTENTS property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>fl</i> The number of pixels of the left border of the window.<br />
 <i>fr</i> The number of pixels of the right border of the window.<br />
 <i>ft</i> The number of pixels of the top border of the window.<br />
 <i>fb</i> The number of pixels of the bottom border of the window.</dl>
<p> Set the border witdh of window by sending the _NET_FRAME_EXTENTS property to window. fl, fr, ft and fb are respectively the number of pixels of the left, right, top and bottom border of window. </p>
<p> The Window Manager MUST set _NET_FRAME_EXTENTS to the extents of the window&#8217;s frame.</p>
<h3>EAPI int ecore_x_netwm_handled_icons_get (Ecore_X_Window window)</h3>
<p>Return wheter the Client handles icons or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if icons are handled, 0 otherwise.</dl>
<p> Return whether the client handles icons or not if window is iconified. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_handled_icons_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_handled_icons_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_handled_icons_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_handled_icons_set (Ecore_X_Window window)</h3>
<p>Set the _NET_WM_HANDLED_ICONS property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<p> Indicate to the Window Manager that it does not need to provide icons for the iconified window by sending the _NET_WM_HANDLED_ICONS property to window. </p>
<p> This function can be used by a Pager on one of its own toplevel windows (for example if the Client is a taskbar and provides buttons for iconified windows).</p>
<h3>EAPI int ecore_x_netwm_icon_geometry_get (Ecore_X_Window window, int * x, int * y, int * width, int * height)</h3>
<p>Get the geometry of an icon. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>x</i> x<br />
 <i>x</i> The X coordinate of the icon.<br />
 <i>y</i> The Y coordinate of the icon.<br />
 <i>width</i> The width of the icon.<br />
 <i>height</i> The height of the icon.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 othrwise.</dl>
<p> Retrieve the geometry of the icon of window. The geometry is stored in x, y, width and height. The function returns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_icon_geometry_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_icon_geometry_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_icon_geometry_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_icon_geometry_set (Ecore_X_Window window, int x, int y, int width, int height)</h3>
<p>Set the _NET_WM_ICON_GEOMETRY property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>x</i> The X coordinate of the icon.<br />
 <i>y</i> The Y coordinate of the icon.<br />
 <i>width</i> The width of the icon.<br />
 <i>height</i> The height of the icon.</dl>
<p> Set the geometry of the icon of window by sending the _NET_WM_ICON_GEOMETRY property to window. x, y, width and height specify respectively the X coordinate, the Y coordinate, the width and the height of the icon. </p>
<p> Stand alone tools like a taskbar or an iconbox MAY use this function. This functions makes possible for a Window Manager to display a nice animation like morphing the window into its icon.</p>
<h3>EAPI int ecore_x_netwm_icon_name_get (Ecore_X_Window window, char ** name)</h3>
<p>Get the icon name of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>name</i> The icon name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns always 1.</dl>
<p> Retrieve the icon name of window and store it in name. The function returns always 1. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_icon_name_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_icon_name_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_icon_name_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_icon_name_set (Ecore_X_Window window, const char * name)</h3>
<p>Set the _NET_WM_ICON_NAME property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The widow to activate.<br />
 <i>name</i> The icon name of the window.</dl>
<p> Set the icon name of window to name by sending the _NET_WM_ICON_NAME property to window. </p>
<p> The Client SHOULD set the title of window in UTF-8 encoding. If set, the Window Manager should use this in preference to WM_ICON_NAME.</p>
<h3>EAPI int ecore_x_netwm_icons_get (Ecore_X_Window window, Ecore_X_Icon ** icon, int * num)</h3>
<p>Retrieve hte possible icons of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>icon</i> An array of icons.<br />
 <i>num</i> The number of icons.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve an array of possible icons of window. The icons are stored in icon and their number in num. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_icons_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_icons_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_icons_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI int ecore_x_netwm_name_get (Ecore_X_Window window, char ** name)</h3>
<p>Get the title of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>name</i> The title name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns always 1.</dl>
<p> Retrieve the title name of window and store it in name. The function returns always 1. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_name_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_name_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_name_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_name_set (Ecore_X_Window window, const char * name)</h3>
<p>Set the _NET_WM_NAME property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The widow to activate.<br />
 <i>name</i> The title name of the window.</dl>
<p> Set the title name of window to name by sending the _NET_WM_NAME property to window. </p>
<p> The Client SHOULD set the title of window in UTF-8 encoding. If set, the Window Manager should use this in preference to WM_NAME.</p>
<h3>EAPI int ecore_x_netwm_opacity_get (Ecore_X_Window window, unsigned int * opacity)</h3>
<p>Get the opacity value of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>opacity</i> The returned opacity.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retriee the opacity value of window and store it in opacity. This function returns 1 on sucess, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_opacity_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_opacity_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_opacity_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_opacity_set (Ecore_X_Window window, unsigned int opacity)</h3>
<p>Set the _NET_WM_WINDOW_OPACITY property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>opacity</i> The opacity value.</dl>
<p> Set the desired opacity of window by sending the _NET_WM_WINDOW_OPACITY property to window. opacity is 0 for a transparent window and 0xffffffff for an opaque window. opacity must be multiplied with the original alpha value of window (which is 1 for visuals not including an alpha component) so that window content is modulated by the opacity value. </p>
<p> Window Managers acting as compositing managers MAY take this into account when displaying a window. Window Managers MUST forward the value of this property to any enclosing frame window. This property MAY change while the window is mapped and the Window Manager MUST respect changes while the window is mapped.</p>
<h3>EAPI int ecore_x_netwm_pid_get (Ecore_X_Window window, int * pid)</h3>
<p>Get the process ID of a client window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>pid</i> The process ID.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the process ID of window and store it in pid. This function returns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_pid_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_pid_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_pid_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_pid_set (Ecore_X_Window window, int pid)</h3>
<p>Set the _NET_WM_PID property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>pid</i> The process ID.</dl>
<p> Set the process ID of the client owning window by sending the _NET_WM_PID property to window. </p>
<p> This function MAY be used by the Window Manager to kill windows which do not respond to the _NET_WM_PING protocol. </p>
<p> If _NET_WM_PID is set, the ICCCM-specified property WM_CLIENT_MACHINE MUST also be set.</p>
<h3>EAPI void ecore_x_netwm_ping_send (Ecore_X_Window window)</h3>
<p>Send a _NET_WM_PING property event. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<p> Send a ClientMessage event from window with the _NET_WM_PING property set.</p>
<h3>EAPI void ecore_x_netwm_showing_desktop_set (Ecore_X_Window root, int on)</h3>
<p>Set the _NET_SHOWING_DESKTOP property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window<br />
 <i>on</i> 0 to hide the desktop, non 0 to show it.</dl>
<p> Set or unset the desktop in a &#8216;showing mode&#8217; by sending the _NET_SHOWING_DESKTOP property to the root window. If on is 0, the windows are hidden and the desktop background is displayed and focused. </p>
<p> If a Pager wants to enter or leave the mode, it MUST use this function.</p>
<h3>EAPI int ecore_x_netwm_startup_id_get (Ecore_X_Window window, char ** id)</h3>
<p>Get the startup ID name of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>id</i> The ID name</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return always 1.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_startup_id_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_startup_id_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_startup_id_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_startup_id_set (Ecore_X_Window window, const char * id)</h3>
<p>Set the _NET_STARTUP_ID property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>id</i> The ID name.</dl>
<p> Set the ID id used for the startup sequence by sending the property _NET_STARTUP_ID to window. The ID name should be encoded in UTF-8. </p>
<p> If a new value for the property is set, the Window Manager should update the window&#8217;s status accordingly (update its virtual desktop, etc.).</p>
<h3>EAPI void ecore_x_netwm_state_request_send (Ecore_X_Window window, Ecore_X_Window root, Ecore_X_Window_State s1, Ecore_X_Window_State s2, int set)</h3>
<p>Send a _NET_WM_STATE property event. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>root</i> The root window.<br />
 <i>s1</i> The first state to alter.<br />
 <i>s2</i> The second state to alter.<br />
 <i>set</i> 0 to unset the property, set it otherwise.</dl>
<p> Send a ClientMessage event from window to the root window with the _NET_WM_STATE property set. This change the state of a mapped window. s1 is the first state to alter. s2 is the second state to alter. If set value is 0, the property is removed (or unset), otherwise, the property is set.</p>
<h3>EAPI int ecore_x_netwm_strut_get (Ecore_X_Window window, int * left, int * right, int * top, int * bottom)</h3>
<p>Get the space at the edje of the screen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>left</i> The number of pixels at the left of the screen.<br />
 <i>right</i> The number of pixels at the right of the screen.<br />
 <i>top</i> The number of pixels at the top of the screen.<br />
 <i>bottom</i> The number of pixels at the bottom of the screen.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the space at the edje of the screen if window is to reserve such space. The number of pixels at the left, right, top and bottom of the screen are respectively stored in left, right, top and bottom. This function returns 1 on success, 0 otherwise. </p>
<p> This property is deprecated. See <code>ecore_x_netwm_strut_set()</code> for more informations. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_strut_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_strut_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_strut_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI int ecore_x_netwm_strut_partial_get (Ecore_X_Window window, int * left, int * right, int * top, int * bottom, int * left_start_y, int * left_end_y, int * right_start_y, int * right_end_y, int * top_start_x, int * top_end_x, int * bottom_start_x, int * bottom_end_x)</h3>
<p>Get the space at the edje of the screen of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>left</i> The number of pixels at the left of the screen.<br />
 <i>right</i> The number of pixels at the right of the screen.<br />
 <i>top</i> The number of pixels at the top of the screen.<br />
 <i>bottom</i> The number of pixels at the bottom of the screen.<br />
 <i>left_start_y</i> The number of pixels.<br />
 <i>left_end_y</i> The number of pixels.<br />
 <i>right_start_y</i> The number of pixels.<br />
 <i>right_end_y</i> The number of pixels.<br />
 <i>top_start_x</i> The number of pixels.<br />
 <i>top_end_x</i> The number of pixels.<br />
 <i>bottom_start_x</i> The number of pixels.<br />
 <i>bottom_end_x</i> The number of pixels.</dl>
<p> Retrieve the space at the edje of the screen if window is to reserve such space. The number of pixels at the left, right, top and bottom of the screen are respectively stored in left, right, top and bottom. This function returns 1 on success, 0 otherwise. </p>
<p> TODO: more description for that function. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_strut_partial_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_strut_partial_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_strut_partial_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_strut_partial_set (Ecore_X_Window window, int left, int right, int top, int bottom, int left_start_y, int left_end_y, int right_start_y, int right_end_y, int top_start_x, int top_end_x, int bottom_start_x, int bottom_end_x)</h3>
<p>Set the _NET_WM_STRUT_PARTIAL property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>left</i> The number of pixels at the left of the screen.<br />
 <i>right</i> The number of pixels at the right of the screen.<br />
 <i>top</i> The number of pixels at the top of the screen.<br />
 <i>bottom</i> The number of pixels at the bottom of the screen.<br />
 <i>left_start_y</i> The number of pixels.<br />
 <i>left_end_y</i> The number of pixels.<br />
 <i>right_start_y</i> The number of pixels.<br />
 <i>right_end_y</i> The number of pixels.<br />
 <i>top_start_x</i> The number of pixels.<br />
 <i>top_end_x</i> The number of pixels.<br />
 <i>bottom_start_x</i> The number of pixels.<br />
 <i>bottom_end_x</i> The number of pixels.</dl>
<p> Set space at the edje of the screen by sending the _NET_WM_STRUT_PARTIAL property to window if window is to reserve that space. left, right, top and bottom are respectively the number of pixels at the left, right, top and bottom of the screen. </p>
<p> TODO: more description for that function.</p>
<h3>EAPI void ecore_x_netwm_strut_set (Ecore_X_Window window, int left, int right, int top, int bottom)</h3>
<p>Set the _NET_WM_STRUT property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window<br />
 <i>left</i> The number of pixels at the left of the screen.<br />
 <i>right</i> The number of pixels at the right of the screen.<br />
 <i>top</i> The number of pixels at the top of the screen.<br />
 <i>bottom</i> The number of pixels at the bottom of the screen.</dl>
<p> Set space at the edje of the screen by sending the _NET_WM_STRUT property to window if window is to reserve that space. left, right, top and bottom are respectively the number of pixels at the left, right, top and bottom of the screen. </p>
<p> This property is deprecated and <code>ecore_x_netwm_strut_partial_set()</code> should be used instead. However, Clients MAY set this property in addition to _NET_WM_STRUT_PARTIAL to ensure backward compatibility with Window Managers supporting older versions of the Specification.</p>
<h3>EAPI int ecore_x_netwm_supported_get (Ecore_X_Window root, Ecore_X_Atom ** supported, int * num)</h3>
<p>Get the hints supported by the Window Manager. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>supported</i> The supported hints.<br />
 <i>num</i> The number of atoms.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Get the hints supported by the Window Manager. root is the root window. The hints are stored in supported. The number of hints is stored in num. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_supported_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_supported_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_supported_get_prefetch (Ecore_X_Window root)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window</dl>
<h3>EAPI void ecore_x_netwm_supported_set (Ecore_X_Window root, Ecore_X_Atom * supported, int num)</h3>
<p>Set the _NET_SUPPORTED property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>supported</i> The supported hints.<br />
 <i>num</i> The number of hints.</dl>
<p> Set the _NET_SUPPORTED property on the root window. The hints that the Window Manager supports are stored in supported. </p>
<p> The Window Manager MUST set this property to indicate which hints it supports.</p>
<h3>EAPI int ecore_x_netwm_sync_counter_get (Ecore_X_Window window, Ecore_X_Sync_Counter * counter)</h3>
<p>Get the X ID of a X Sync counter. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>counter</i> The X ID of the Sync counter.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the X ID of the X Sync counter of window and store it in counter. This function returns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_frame_size_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_frame_size_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_sync_counter_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_sync_request_send (Ecore_X_Window window, unsigned int serial)</h3>
<p>Send a _NET_WM_SYNC_REQUEST property event. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>serial</i> The update request number.</dl>
<p> Send a ClientMessage event from window with the _NET_WM_SYNC_REQUEST property set.</p>
<h3>EAPI int ecore_x_netwm_user_time_get (Ecore_X_Window window, unsigned int * time)</h3>
<p>Get the last user activity time in the window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>time</i> The returned time.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Return the XServer time at which last user activity in window took place. The time is stored in time. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_user_time_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_user_time_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_user_time_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_user_time_set (Ecore_X_Window window, unsigned int time)</h3>
<p>Set the _NET_WM_USER_TIME property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>time</i> The last user activity time in the window.</dl>
<p> Set the XServer time at which last user activity in window took place by sending the _NET_WM_USER_TIME property to window. time contains that XServer time in seconds. </p>
<p> This function allows a Window Manager to alter the focus, stacking, and/or placement behavior of windows when they are mapped depending on whether the new window was created by a user action or is a &#8216;pop-up&#8217; window activated by a timer or some other event.</p>
<h3>EAPI int ecore_x_netwm_visible_icon_name_get (Ecore_X_Window window, char ** name)</h3>
<p>Get the visible icon name of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>name</i> The icon name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns always 1.</dl>
<p> Retrieve the visible icon name of window and store it in name. The function returns always 1. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_visible_icon_name_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_visible_icon_name_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_visible_icon_name_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_visible_icon_name_set (Ecore_X_Window window, const char * name)</h3>
<p>Set the _NET_WM_VISIBLE_ICON_NAME property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The widow to activate.<br />
 <i>name</i> The title name of the window.</dl>
<p> Set the icon name of window to name by sending the _NET_WM_VISIBLE_ICON_NAME property to window, when the Window Manager displays a icon name other than by calling <code>ecore_x_netwm_icon_name_set()</code>. </p>
<p> The Client SHOULD set the icon name in UTF-8 encoding. The Window Manager MUST use this function is it display an icon name other than with <code>ecore_x_netwm_icon_name_set()</code>.</p>
<h3>EAPI int ecore_x_netwm_visible_name_get (Ecore_X_Window window, char ** name)</h3>
<p>Get the visible title of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>name</i> The title name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns always 1.</dl>
<p> Retrieve the visible title name of window and store it in name. The function returns always 1. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_visible_name_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_visible_name_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_visible_name_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_visible_name_set (Ecore_X_Window window, const char * name)</h3>
<p>Set the _NET_WM_VISIBLE_NAME property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The widow to activate.<br />
 <i>name</i> The title name of the window.</dl>
<p> Set the title name of window to name by sending the _NET_WM_VISIBLE_NAME property to window, when the Window Manager displays a window name other than by calling <code>ecore_x_netwm_name_set()</code>. </p>
<p> The Client SHOULD set the title of window in UTF-8 encoding. This function is used for displaying title windows like [xterm1], [xterm2], &#8230; thereby allowing Pagers to display the same title as the Window Manager.</p>
<h3>EAPI int ecore_x_netwm_window_state_get (Ecore_X_Window window, Ecore_X_Window_State ** state, unsigned int * num)</h3>
<p>Get the hints describing the window state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>state</i> The returned hins.<br />
 <i>num</i> The number of hints.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the hints describing window state. The state is returned in state. The nummber of hints is stored in num. This function returns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_window_state_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_window_state_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_window_state_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_window_state_set (Ecore_X_Window window, Ecore_X_Window_State * state, unsigned int num)</h3>
<p>Set the _NET_WM_STATE property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>state</i> An array of window hints.<br />
 <i>num</i> The number of hints.</dl>
<p> Set a list of hints describing window state by sending the _NET_WM_STATE property to window. The hints are stored in the array state. num must contain the number of hints. </p>
<p> The Window Manager SHOULD honor _NET_WM_STATE whenever a withdrawn window requests to be mapped. A Client wishing to change the state of a window MUST send a _NET_WM_STATE client message to the root window. The Window Manager MUST keep this property updated to reflect the current state of the window.</p>
<h3>EAPI int ecore_x_netwm_window_type_get (Ecore_X_Window window, Ecore_X_Window_Type * type)</h3>
<p>Get the functional type of a window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>type</i> The function type of the window.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Retrieve the functional type of window. The type is stored in type. This function returns 1 on success, 0 otherwise. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_netwm_window_type_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_netwm_window_type_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_netwm_window_type_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.</dl>
<h3>EAPI void ecore_x_netwm_window_type_set (Ecore_X_Window window, Ecore_X_Window_Type type)</h3>
<p>Set the _NET_WM_WINDOW_TYPE property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>type</i> The functional type of the window.</dl>
<p> Set the functional type of window by sending _NET_WM_WINDOW_TYPE property to window. </p>
<p> This property SHOULD be set by the Client before mapping. This property SHOULD be used by the window manager in determining the decoration, stacking position and other behavior of the window. The Client SHOULD specify window types in order of preference (the first being most preferable). </p>
<p> This hint is intended to replace the MOTIF hints.</p>
<h3>EAPI void ecore_x_netwm_wm_identify (Ecore_X_Window root, Ecore_X_Window check, const char * wm_name)</h3>
<p>Set the _NET_SUPPORTING_WM_CHECK property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>check</i> The child window.<br />
 <i>wm_name</i> The name of the Window Manager.</dl>
<p> Set the _NET_SUPPORTING_WM_CHECK property on the root window to be the ID of the child window check created by the Window Manager. check also have the _NET_WM_NAME property set to the name wm_name of the Window Manager. </p>
<p> The Window MUST call that function to indicate that a compliant window manager is active.</p>
<h3>EAPI int ecore_x_screen_is_composited (int screen)</h3>
<p>Check whether a screen is composited or not. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>screen</i> The screen index.</dl>
<p> Return 1 if screen is composited, 0 otherwise.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
