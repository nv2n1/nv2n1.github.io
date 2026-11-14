---
title: "globus_ftp_client_restart_marker_plugin_init(3)"
name: "globus_ftp_client_restart_marker_plugin_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_restart_marker_plugin_init/"
description: "Restart Marker Plugin –"
---

<h2 class="name">NAME</h2>
<p> Restart Marker Plugin &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_FTP_CLIENT_RESTART_MARKER_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_restart_marker_plugin_module) </p>
<h3>Typedefs</h3>
<p> typedef globus_bool_t(* <code>globus_ftp_client_restart_marker_plugin_begin_cb_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, <code>globus_ftp_client_restart_marker_t</code> *user_saved_marker)<br />
 <i>Transfer begin callback. </i><br />
 typedef void(* <code>globus_ftp_client_restart_marker_plugin_marker_cb_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_restart_marker_t</code> *marker) </p>
<p> typedef void(* <code>globus_ftp_client_restart_marker_plugin_complete_cb_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, const char *error_url) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_restart_marker_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_restart_marker_plugin_begin_cb_t</code> begin_cb, <code>globus_ftp_client_restart_marker_plugin_marker_cb_t</code> marker_cb, <code>globus_ftp_client_restart_marker_plugin_complete_cb_t</code> complete_cb, void *user_arg) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<h2>Detailed Description</h2>
<p> This plugin is intended to allow users to make restart markers persistent. During a transfer, every marker received will result in the user&#8217;s &#8216;marker&#8217; callback being called with the new restart marker that can be stored. If the application were to prematurely terminate (while transferring), the user (after restarting the application) could pass this stored marker back to the plugin via the &#8216;begin&#8217; callback to force the transfer to be restarted from the last marked point.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_FTP_CLIENT_RESTART_MARKER_PLUGIN_MODULE (&amp;globus_i_ftp_client_restart_marker_plugin_module)</h3>
<p> Module descriptor</p>
<h2>Typedef Documentation</h2>
<h3>typedef globus_bool_t(* globus_ftp_client_restart_marker_plugin_begin_cb_t)(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, <code>globus_ftp_client_restart_marker_t</code> *user_saved_marker)</h3>
<p> Transfer begin callback. This callback is called when a get, put, or third party transfer is started. </p>
<p> The intended use for this callback is for the user to use the transfer urls to locate a restart marker in some persistent storage. If one is found, it should be copied into &#8216;user_saved_marker&#8217; and the callback should return GLOBUS_TRUE. This will cause the transfer to be restarted using that restart marker. If one is not found, return GLOBUS_FALSE to indicate that the transfer should proceed from the beginning. </p>
<p> In any case, this is also an opportunity for the user to set up any storage in anticipation of restart markers for this transfer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> this the client handle that this transfer will be occurring on<br />
 <i>user_arg</i> this is the user_arg passed to the init func<br />
 <i>source_url</i> source of the transfer (GLOBUS_NULL if &#8216;put&#8217;)<br />
 <i>dest_url</i> dest of the transfer (GLOBUS_NULL if &#8216;get&#8217;)<br />
 <i>user_saved_marker</i> pointer to an unitialized restart marker</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_TRUE to indicate that the plugin should use &#8216;user_saved_marker&#8217; to restart the transfer (and subsequently, destroy the marker)</p>
<dt>&bull;</p>
<dd> GLOBUS_FALSE to indicate that &#8216;user_saved_marker&#8217; has not been modified, and that the transfer should proceed normally</dl>
</dl>
<h3>typedef void(* globus_ftp_client_restart_marker_plugin_complete_cb_t)(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, const char *error_url)</h3>
<p> Transfer complete callback </p>
<p> This callback will be called upon transfer completion (successful or otherwise) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> this the client handle that this transfer was occurring on<br />
 <i>user_arg</i> this is the user_arg passed to the init func<br />
 <i>error</i> the error object indicating what went wrong (GLOBUS_NULL on success)<br />
 <i>error_url</i> the url which is the source of the above error (GLOBUS_NULL on success)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h3>typedef void(* globus_ftp_client_restart_marker_plugin_marker_cb_t)(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_restart_marker_t</code> *marker)</h3>
<p> Restart marker received callback </p>
<p> This callback will be called every time a restart marker is available. </p>
<p> To receive restart markers in a &#8216;put&#8217; or &#8216;third_party_transfer&#8217;, the transfer must be in Extended Block mode. &#8216;get&#8217; transfers will have their markers generated internally. Markers generated internally will be &#8216;sent&#8217; at most, once per second. </p>
<p> The intended use for this callback is to allow the user to store this marker (most likely in place of any previous marker) in a format that the &#8216;begin_cb&#8217; can parse and pass back. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> this the client handle that this transfer is occurring on<br />
 <i>user_arg</i> this is the user_arg passed to the init func<br />
 <i>marker</i> the restart marker that has been received. Thsi marker is owned by the caller. The user must use the copy method to keep it. Note: this restart marker currently contains all ranges received as of yet. Should I instead only pass a marker with the ranges just made available? If so, the user may need a way to combine restart markers (globus_ftp_client_restart_marker_combine)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_restart_marker_plugin_destroy (<code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Destroy restart marker plugin </p>
<p> Frees up memory associated with plugin </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> plugin previously initialized with init (above)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</p>
<dt>&bull;</p>
<dd> Error on NULL plugin</dl>
</dl>
<h3>globus_result_t globus_ftp_client_restart_marker_plugin_init (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_restart_marker_plugin_begin_cb_t</code>begin_cb, <code>globus_ftp_client_restart_marker_plugin_marker_cb_t</code>marker_cb, <code>globus_ftp_client_restart_marker_plugin_complete_cb_t</code>complete_cb, void *user_arg)</h3>
<p> Initialize a restart marker plugin </p>
<p> This function initializes a restart marker plugin. Any params except for the plugin may be GLOBUS_NULL </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> a pointer to a plugin type to be initialized<br />
 <i>user_arg</i> a pointer to some user specific data that will be provided to all callbacks<br />
 <i>begin_cb</i> the callback to be called upon the start of a transfer<br />
 <i>marker_cb</i> the callback to be called with every restart marker received<br />
 <i>complete_cb</i> the callback to be called to indicate transfer completion</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</p>
<dt>&bull;</p>
<dd> Error on NULL plugin</p>
<dt>&bull;</p>
<dd> Error on init internal plugin</dl>
</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Function Documentation</a></p>
<dd>
<dt><a href="#lbAP">Author</a></p>
<dd></dl>
