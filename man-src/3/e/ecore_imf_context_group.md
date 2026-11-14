---
title: "ecore_imf_context_group(3)"
name: "ecore_imf_context_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_imf_context_group/"
description: "Ecore Input Method Context Functions – Functions that operate on Ecore Input Method Context objects."
---

<p>Ecore Input Method Context Functions &#8211; Functions that operate on Ecore Input Method Context objects. </p>
<h3>Functions</h3>
<p>EAPI Ecore_List * <code>ecore_imf_context_available_ids_get</code> (void)<br />
 <i>Get the list of the available Input Method Context ids. </i><br />
 EAPI const char * <code>ecore_imf_context_default_id_get</code> (void)<br />
 <i>Get the id of the default Input Method Context. </i><br />
 EAPI const Ecore_IMF_Context_Info * <code>ecore_imf_context_info_by_id_get</code> (const char *id)<br />
 <i>Retrieve the info for the Input Method Context with </i>id.<br />
 EAPI Ecore_IMF_Context * <code>ecore_imf_context_add</code> (const char *id)<br />
 <i>Create a new Input Method Context defined by the given id. </i><br />
 EAPI const Ecore_IMF_Context_Info * <code>ecore_imf_context_info_get</code> (Ecore_IMF_Context *ctx)<br />
 <i>Retrieve the info for the given Input Method Context. </i><br />
 EAPI void <code>ecore_imf_context_del</code> (Ecore_IMF_Context *ctx)<br />
 <i>Delete the given Input Method Context and free its memory. </i><br />
 EAPI void <code>ecore_imf_context_client_window_set</code> (Ecore_IMF_Context *ctx, void *window)<br />
 <i>Set the client window for the Input Method Context; this is the Ecore_X_Window when using X11, Ecore_Win32_Window when using Win32, etc. </i><br />
 EAPI void <code>ecore_imf_context_client_canvas_set</code> (Ecore_IMF_Context *ctx, void *canvas)<br />
 <i>Set the client canvas for the Input Method Context; this is the canvas in which the input appears. </i><br />
 EAPI void <code>ecore_imf_context_show</code> (Ecore_IMF_Context *ctx)<br />
 <i>Ask the Input Method Context to show itself. </i><br />
 EAPI void <code>ecore_imf_context_hide</code> (Ecore_IMF_Context *ctx)<br />
 <i>Ask the Input Method Context to hide itself. </i><br />
 EAPI void <code>ecore_imf_context_focus_in</code> (Ecore_IMF_Context *ctx)<br />
 <i>Notify the Input Method Context that the widget to which its correspond has gained focus. </i><br />
 EAPI void <code>ecore_imf_context_focus_out</code> (Ecore_IMF_Context *ctx)<br />
 <i>Notify the Input Method Context that the widget to which its correspond has lost focus. </i><br />
 EAPI void <code>ecore_imf_context_reset</code> (Ecore_IMF_Context *ctx)<br />
 <i>Notify the Input Method Context that a change such as a change in cursor position has been made. </i><br />
 EAPI void <code>ecore_imf_context_cursor_position_set</code> (Ecore_IMF_Context *ctx, int cursor_pos)<br />
 <i>Notify the Input Method Context that a change in the cursor position has been made. </i><br />
 EAPI void <code>ecore_imf_context_use_preedit_set</code> (Ecore_IMF_Context *ctx, int use_preedit)<br />
 <i>Set whether the IM context should use the preedit string to display feedback. </i><br />
 EAPI void <code>ecore_imf_context_retrieve_surrounding_callback_set</code> (Ecore_IMF_Context *ctx, int(*func)(void *data, Ecore_IMF_Context *ctx, char **text, int *cursor_pos), const void *data)<br />
 <i>Set the callback to be used on get_surrounding request. </i><br />
 EAPI void <code>ecore_imf_context_input_mode_set</code> (Ecore_IMF_Context *ctx, Ecore_IMF_Input_Mode input_mode)<br />
 <i>Set the input mode used by the Ecore Input Context. </i><br />
 EAPI Ecore_IMF_Input_Mode <code>ecore_imf_context_input_mode_get</code> (Ecore_IMF_Context *ctx)<br />
 <i>Get the input mode being used by the Ecore Input Context. </i><br />
 EAPI int <code>ecore_imf_context_filter_event</code> (Ecore_IMF_Context *ctx, Ecore_IMF_Event_Type type, Ecore_IMF_Event *event)<br />
 <i>Allow an Ecore Input Context to internally handle an event. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on Ecore Input Method Context objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_IMF_Context* ecore_imf_context_add (const char * id)</h3>
<p>Create a new Input Method Context defined by the given id. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>id</i> The Input Method Context id.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated Input Method Context; on failure it returns NULL.</dl>
<p> References ecore_imf_context_input_mode_set(), and ecore_imf_context_use_preedit_set().</p>
<h3>EAPI Ecore_List* ecore_imf_context_available_ids_get (void)</h3>
<p>Get the list of the available Input Method Context ids. </p>
<p> Note that the caller is responsible for freeing the Ecore_List when finished with it. There is no need to finish the list strings. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return an Ecore_List of strings; on failure it returns NULL.</dl>
<h3>EAPI void ecore_imf_context_client_canvas_set (Ecore_IMF_Context * ctx, void * canvas)</h3>
<p>Set the client canvas for the Input Method Context; this is the canvas in which the input appears. </p>
<p> The canvas type can be determined by using the context canvas type. Actually only canvas with type &#8216;evas&#8217; (Evas *) is supported. This canvas may be used in order to correctly position status windows, and may also be used for purposes internal to the Input Method Context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>canas</i> The client canvas. This may be NULL to indicate that the previous client canvas no longer exists.</dl>
<h3>EAPI void ecore_imf_context_client_window_set (Ecore_IMF_Context * ctx, void * window)</h3>
<p>Set the client window for the Input Method Context; this is the Ecore_X_Window when using X11, Ecore_Win32_Window when using Win32, etc. </p>
<p> This window is used in order to correctly position status windows, and may also be used for purposes internal to the Input Method Context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>window</i> The client window. This may be NULL to indicate that the previous client window no longer exists.</dl>
<h3>EAPI void ecore_imf_context_cursor_position_set (Ecore_IMF_Context * ctx, int cursor_pos)</h3>
<p>Notify the Input Method Context that a change in the cursor position has been made. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>cursor_pos</i> New cursor position in characters.</dl>
<h3>EAPI const char* ecore_imf_context_default_id_get (void)</h3>
<p>Get the id of the default Input Method Context. </p>
<p> The id may to used to create a new instance of an Input Method Context object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return a string containing the id of the default Input Method Context; on failure it returns NULL.</dl>
<h3>EAPI void ecore_imf_context_del (Ecore_IMF_Context * ctx)</h3>
<p>Delete the given Input Method Context and free its memory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<h3>EAPI int ecore_imf_context_filter_event (Ecore_IMF_Context * ctx, Ecore_IMF_Event_Type type, Ecore_IMF_Event * event)</h3>
<p>Allow an Ecore Input Context to internally handle an event. </p>
<p> If this function returns 1, then no further processing should be done for this event. </p>
<p> Input methods must be able to accept all types of events (simply returning 0 if the event was not handled), but there is no obligation of any events to be submitted to this function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>type</i> The type of event defined by Ecore_IMF_Event_Type.<br />
 <i>event</i> The event itself.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the event was handled; otherwise 0.</dl>
<h3>EAPI void ecore_imf_context_focus_in (Ecore_IMF_Context * ctx)</h3>
<p>Notify the Input Method Context that the widget to which its correspond has gained focus. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<h3>EAPI void ecore_imf_context_focus_out (Ecore_IMF_Context * ctx)</h3>
<p>Notify the Input Method Context that the widget to which its correspond has lost focus. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<h3>EAPI void ecore_imf_context_hide (Ecore_IMF_Context * ctx)</h3>
<p>Ask the Input Method Context to hide itself. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<h3>EAPI const Ecore_IMF_Context_Info* ecore_imf_context_info_by_id_get (const char * id)</h3>
<p>Retrieve the info for the Input Method Context with id. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>id</i> The Input Method Context id to query for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return a Ecore_IMF_Context_Info for the Input Method Context with id; on failure it returns NULL.</dl>
<h3>EAPI const Ecore_IMF_Context_Info* ecore_imf_context_info_get (Ecore_IMF_Context * ctx)</h3>
<p>Retrieve the info for the given Input Method Context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Return a Ecore_IMF_Context_Info for the given Input Method Context; on failure it returns NULL.</dl>
<h3>EAPI Ecore_IMF_Input_Mode ecore_imf_context_input_mode_get (Ecore_IMF_Context * ctx)</h3>
<p>Get the input mode being used by the Ecore Input Context. </p>
<p> See <code>ecore_imf_context_input_mode_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The input mode being used by ctx.</dl>
<h3>EAPI void ecore_imf_context_input_mode_set (Ecore_IMF_Context * ctx, Ecore_IMF_Input_Mode input_mode)</h3>
<p>Set the input mode used by the Ecore Input Context. </p>
<p> The input mode can be one of the input modes defined in Ecore_IMF_Input_Mode. The default input mode is ECORE_IMF_INPUT_MODE_FULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>input_mode</i> The input mode to be used by ctx.</dl>
<p> Referenced by ecore_imf_context_add().</p>
<h3>EAPI void ecore_imf_context_reset (Ecore_IMF_Context * ctx)</h3>
<p>Notify the Input Method Context that a change such as a change in cursor position has been made. </p>
<p> This will typically cause the Input Method Context to clear the preedit state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<h3>EAPI void ecore_imf_context_retrieve_surrounding_callback_set (Ecore_IMF_Context * ctx, int(*)(void *data, Ecore_IMF_Context *ctx, char **text, int *cursor_pos) func, const void * data)</h3>
<p>Set the callback to be used on get_surrounding request. </p>
<p> This callback will be called when the Input Method Context module requests the surrounding context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>func</i> The callback to be called.<br />
 <i>data</i> The data pointer to be passed to func</dl>
<h3>EAPI void ecore_imf_context_show (Ecore_IMF_Context * ctx)</h3>
<p>Ask the Input Method Context to show itself. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<h3>EAPI void ecore_imf_context_use_preedit_set (Ecore_IMF_Context * ctx, int use_preedit)</h3>
<p>Set whether the IM context should use the preedit string to display feedback. </p>
<p> If is 0 (default is 1), then the IM context may use some other method to display feedback, such as displaying it in a child of the root window. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>use_preedit</i> Whether the IM context should use the preedit string.</dl>
<p> Referenced by ecore_imf_context_add().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
