---
title: "ecore_x_randr_group(3)"
name: "ecore_x_randr_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_randr_group/"
description: "X RandR Extension Functions – Functions related to the X RandR extension."
---

<p>X RandR Extension Functions &#8211; Functions related to the X RandR extension. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_randr_query</code> (void)<br />
 <i>Return whether the X server supports the RandR Extension. </i><br />
 EAPI int <code>ecore_x_randr_events_select</code> (Ecore_X_Window window, int on)<br />
 <i>Select if the ScreenChangeNotify events will be sent. </i><br />
 EAPI void <code>ecore_x_randr_get_screen_info_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetScreenInfo request. </i><br />
 EAPI void <code>ecore_x_randr_get_screen_info_fetch</code> (void)<br />
 <i>Gets the reply of the GetScreenInfo request sent by </i><code>ecore_x_randr_get_screen_info_prefetch()</code>.<br />
 EAPI Ecore_X_Randr_Rotation <code>ecore_x_randr_screen_rotations_get</code> (Ecore_X_Window root __UNUSED__)<br />
 <i>Get the set of rotations and reflections. </i><br />
 EAPI Ecore_X_Randr_Rotation <code>ecore_x_randr_screen_rotation_get</code> (Ecore_X_Window root __UNUSED__)<br />
 <i>Get the rotation. </i><br />
 EAPI Ecore_X_Screen_Size * <code>ecore_x_randr_screen_sizes_get</code> (Ecore_X_Window root __UNUSED__, int *num)<br />
 <i>Get the frame buffer sizes. </i><br />
 EAPI Ecore_X_Screen_Size <code>ecore_x_randr_current_screen_size_get</code> (Ecore_X_Window root __UNUSED__)<br />
 <i>Get the current frame buffer size. </i><br />
 EAPI Ecore_X_Screen_Refresh_Rate <code>ecore_x_randr_current_screen_refresh_rate_get</code> (Ecore_X_Window root __UNUSED__)<br />
 <i>Get the current refresh rate. </i><br />
 EAPI Ecore_X_Screen_Refresh_Rate * <code>ecore_x_randr_screen_refresh_rates_get</code> (Ecore_X_Window root __UNUSED__, int size_id __UNUSED__, int *num)<br />
 <i>Get the refresh rates. </i><br />
 EAPI void <code>ecore_x_randr_screen_rotation_set</code> (Ecore_X_Window root, Ecore_X_Randr_Rotation rot)<br />
 <i>Set the screen rotation. </i><br />
 EAPI int <code>ecore_x_randr_screen_size_set</code> (Ecore_X_Window root, Ecore_X_Screen_Size size)<br />
 <i>Set the screen size. </i><br />
 EAPI int <code>ecore_x_randr_screen_refresh_rate_set</code> (Ecore_X_Window root, Ecore_X_Screen_Size size, Ecore_X_Screen_Refresh_Rate rate)<br />
 <i>Set the screen refresh rate. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to the X RandR extension.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_X_Screen_Refresh_Rate ecore_x_randr_current_screen_refresh_rate_get (Ecore_X_Window root __UNUSED__)</h3>
<p>Get the current refresh rate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The window (Unused).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current refresh rate.</dl>
<p> Get the current refresh rate supported by the screen associated to window (passed to <code>ecore_x_randr_get_screen_info_prefetch()</code>). </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_randr_get_screen_info_prefetch()</code>, which sends the GetScreenInfo request, then <code>ecore_x_randr_get_screen_info_fetch()</code>, which gets the reply.</p>
<h3>EAPI Ecore_X_Screen_Size ecore_x_randr_current_screen_size_get (Ecore_X_Window root __UNUSED__)</h3>
<p>Get the current frame buffer size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The window (Unused).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The active size.</dl>
<p> Get the active frame buffer size supported by the screen associated to window (passed to <code>ecore_x_randr_get_screen_info_prefetch()</code>). </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_randr_get_screen_info_prefetch()</code>, which sends the GetScreenInfo request, then <code>ecore_x_randr_get_screen_info_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_randr_events_select (Ecore_X_Window window, int on)</h3>
<p>Select if the ScreenChangeNotify events will be sent. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>on</i> 1 to enable, 0 to disable.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> If on value is 1, ScreenChangeNotify events will be sent when the screen configuration changes, either from this protocol extension, or due to detected external screen configuration changes. ScreenChangeNotify may also be sent when this request executes if the screen configuration has changed since the client connected, to avoid race conditions.</p>
<h3>EAPI void ecore_x_randr_get_screen_info_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetScreenInfo request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose properties are requested.</dl>
<h3>EAPI int ecore_x_randr_query (void)</h3>
<p>Return whether the X server supports the RandR Extension. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X RandR Extension is available, 0 otherwise.</dl>
<p> Return 1 if the X server supports the RandR Extension version 1.1, 0 otherwise.</p>
<h3>EAPI int ecore_x_randr_screen_refresh_rate_set (Ecore_X_Window root, Ecore_X_Screen_Size size, Ecore_X_Screen_Refresh_Rate rate)</h3>
<p>Set the screen refresh rate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>size</i> The size.<br />
 <i>rate</i> The refresh rate.</dl>
<p> Set the size and the refresh rate of the screen associated to root. </p>
<p> Note that that function is blocking.</p>
<h3>EAPI Ecore_X_Screen_Refresh_Rate* ecore_x_randr_screen_refresh_rates_get (Ecore_X_Window root __UNUSED__, int size_id __UNUSED__, int * num)</h3>
<p>Get the refresh rates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The window (Unused).<br />
 <i>num</i> The number of refresh rates.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The refresh rates.</dl>
<p> Get the list of refresh rates for each size supported by the screen associated to window (passed to <code>ecore_x_randr_get_screen_info_prefetch()</code>). Each element of &#8216;sizes&#8217; has a corresponding element in &#8216;refresh&#8217;. An empty list indicates no known rates, or a device for which refresh is not relevant. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_randr_get_screen_info_prefetch()</code>, which sends the GetScreenInfo request, then <code>ecore_x_randr_get_screen_info_fetch()</code>, which gets the reply.</p>
<h3>EAPI Ecore_X_Randr_Rotation ecore_x_randr_screen_rotation_get (Ecore_X_Window root __UNUSED__)</h3>
<p>Get the rotation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The window (Unused).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The rotation.</dl>
<p> Get the rotation supported by the screen associated to window (passed to <code>ecore_x_randr_get_screen_info_prefetch()</code>). </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_randr_get_screen_info_prefetch()</code>, which sends the GetScreenInfo request, then <code>ecore_x_randr_get_screen_info_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_randr_screen_rotation_set (Ecore_X_Window root, Ecore_X_Randr_Rotation rot)</h3>
<p>Set the screen rotation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>rot</i> The rotation.</dl>
<p> Set the rotation of the screen associated to root. </p>
<p> Note that that function is blocking.</p>
<h3>EAPI Ecore_X_Randr_Rotation ecore_x_randr_screen_rotations_get (Ecore_X_Window root __UNUSED__)</h3>
<p>Get the set of rotations and reflections. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The window (Unused).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The set of rotations and reflections.</dl>
<p> Get the set of rotations and reflections supported by the screen associated to window (passed to <code>ecore_x_randr_get_screen_info_prefetch()</code>). </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_randr_get_screen_info_prefetch()</code>, which sends the GetScreenInfo request, then <code>ecore_x_randr_get_screen_info_fetch()</code>, which gets the reply.</p>
<h3>EAPI int ecore_x_randr_screen_size_set (Ecore_X_Window root, Ecore_X_Screen_Size size)</h3>
<p>Set the screen size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The root window.<br />
 <i>size</i> The size.</dl>
<p> Set the size of the screen associated to root. </p>
<p> Note that that function is blocking.</p>
<h3>EAPI Ecore_X_Screen_Size* ecore_x_randr_screen_sizes_get (Ecore_X_Window root __UNUSED__, int * num)</h3>
<p>Get the frame buffer sizes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>root</i> The window (Unused).<br />
 <i>num</i> The number of sizes.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The sizes.</dl>
<p> Get the list of possible frame buffer sizes (at the normal orientation supported by the screen associated to window (passed to <code>ecore_x_randr_get_screen_info_prefetch()</code>). Each size indicates both the linear physical size of the screen and the pixel size. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_randr_get_screen_info_prefetch()</code>, which sends the GetScreenInfo request, then <code>ecore_x_randr_get_screen_info_fetch()</code>, which gets the reply.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
