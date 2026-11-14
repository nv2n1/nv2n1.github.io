---
title: "globus_ftp_client_perf_plugin(3)"
name: "globus_ftp_client_perf_plugin"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_perf_plugin/"
description: "Performance Marker Plugin –"
---

<h2 class="name">NAME</h2>
<p> Performance Marker Plugin &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_FTP_CLIENT_PERF_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_perf_plugin_module) </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_ftp_client_perf_plugin_begin_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_perf_plugin_marker_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, long time_stamp_int, char time_stamp_tength, int stripe_ndx, int num_stripes, globus_off_t nbytes) </p>
<p> typedef void(* <code>globus_ftp_client_perf_plugin_complete_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_bool_t success) </p>
<p> typedef void *(* <code>globus_ftp_client_perf_plugin_user_copy_cb_t</code> )(void *user_specific) </p>
<p> typedef void(* <code>globus_ftp_client_perf_plugin_user_destroy_cb_t</code> )(void *user_specific) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_perf_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_perf_plugin_begin_cb_t</code> begin_cb, <code>globus_ftp_client_perf_plugin_marker_cb_t</code> marker_cb, <code>globus_ftp_client_perf_plugin_complete_cb_t</code> complete_cb, void *user_specific) </p>
<p> globus_result_t <code>globus_ftp_client_perf_plugin_set_copy_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_perf_plugin_user_copy_cb_t</code> copy_cb, <code>globus_ftp_client_perf_plugin_user_destroy_cb_t</code> destroy_cb) </p>
<p> globus_result_t <code>globus_ftp_client_perf_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<p> globus_result_t <code>globus_ftp_client_perf_plugin_get_user_specific</code> (<code>globus_ftp_client_plugin_t</code> *plugin, void **user_specific) </p>
<h2>Detailed Description</h2>
<p> The FTP Performance Marker plugin allows the user to obtain performance markers for all types of transfers except a third party transfer in which Extended Block mode is not enabled. </p>
<p> These markers may be generated internally, or they may be received from a server (&#8216;put&#8217; or third_party_transfer&#8217; only). </p>
<p> Copy constructor and destructor callbacks are also provided to allow one to more easily layer other plugins on top of this one.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_FTP_CLIENT_PERF_PLUGIN_MODULE (&amp;globus_i_ftp_client_perf_plugin_module)</h3>
<p> Module descriptor</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_ftp_client_perf_plugin_begin_cb_t)(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, globus_bool_t restart)</h3>
<p> Transfer begin callback </p>
<p> This callback is called when a get, put, or third party transfer is started. Note that it is possible for this callback to be made multiple times before ever receiving the complete callback&#8230; this would be the case if a transfer was restarted. The &#8216;restart&#8217; will indicate whether or not we have been restarted. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> this the client handle that this transfer will be occurring on<br />
 <i>user_specific</i> this is user specific data either created by the copy method, or, if a copy method was not specified, the value passed to init<br />
 <i>source_url</i> source of the transfer (GLOBUS_NULL if &#8216;put&#8217;)<br />
 <i>dest_url</i> dest of the transfer (GLOBUS_NULL if &#8216;get&#8217;)<br />
 <i>restart</i> boolean indicating whether this callback is result of a restart</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h3>typedef void(* globus_ftp_client_perf_plugin_complete_cb_t)(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_bool_t success)</h3>
<p> Transfer complete callback </p>
<p> This callback will be called upon transfer completion (successful or otherwise) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> this the client handle that this transfer was occurring on<br />
 <i>user_specific</i> this is user specific data either created by the copy method, or, if a copy method was not specified, the value passed to init<br />
 <i>success</i> indicates whether this transfer completed successfully or was interrupted (by error or abort)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h3>typedef void(* globus_ftp_client_perf_plugin_marker_cb_t)(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, long time_stamp_int, char time_stamp_tength, int stripe_ndx, int num_stripes, globus_off_t nbytes)</h3>
<p> Performance marker received callback </p>
<p> This callback is called for all types of transfers except a third party in which extended block mode is not used (because 112 perf markers wont be sent in that case). For extended mode &#8216;put&#8217; and &#8216;3pt&#8217;, actual 112 perf markers will be used and the frequency of this callback is dependent upon the frequency those messages are received. For &#8216;put&#8217; in which extended block mode is not enabled and &#8216;get&#8217; transfers, the information in this callback will be determined locally and the frequency of this callback will be at a maximum of one per second. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> this the client handle that this transfer is occurring on<br />
 <i>user_specific</i> this is user specific data either created by the copy method, or, if a copy method was not specified, the value passed to init<br />
 <i>time_stamp</i> the timestamp at which the number of bytes is valid<br />
 <i>stripe_ndx</i> the stripe index this data refers to<br />
 <i>num_stripes</i> total number of stripes involved in this transfer<br />
 <i>nbytes</i> the total bytes transferred on this stripe</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h3>typedef void*(* globus_ftp_client_perf_plugin_user_copy_cb_t)(void *user_specific)</h3>
<p> Copy constructor </p>
<p> This callback will be called when a copy of this plugin is made, it is intended to allow initialization of a new user_specific data </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_specific</i> this is user specific data either created by this copy method, or the value passed to init</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> a pointer to a user specific piece of data</p>
<dt>&bull;</p>
<dd> GLOBUS_NULL (does not indicate error)</dl>
</dl>
<h3>typedef void(* globus_ftp_client_perf_plugin_user_destroy_cb_t)(void *user_specific)</h3>
<p> Destructor </p>
<p> This callback will be called when a copy of this plugin is destroyed, it is intended to allow the user to free up any memory associated with the user specific data </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_specific</i> this is user specific data created by the copy method</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_perf_plugin_destroy (<code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Destroy performance marker plugin </p>
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
<h3>globus_result_t globus_ftp_client_perf_plugin_get_user_specific (<code>globus_ftp_client_plugin_t</code> *plugin, void **user_specific)</h3>
<p> Retrieve user specific pointer </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> plugin previously initialized with init (above)<br />
 <i>user_specific</i> pointer to storage for user_specific pointer</dl>
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
<dd> Error on NULL user_specific</dl>
</dl>
<h3>globus_result_t globus_ftp_client_perf_plugin_init (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_perf_plugin_begin_cb_t</code>begin_cb, <code>globus_ftp_client_perf_plugin_marker_cb_t</code>marker_cb, <code>globus_ftp_client_perf_plugin_complete_cb_t</code>complete_cb, void *user_specific)</h3>
<p> Initialize a perf plugin </p>
<p> This function initializes a performance marker plugin. Any params except for the plugin may be GLOBUS_NULL </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> a pointer to a plugin type to be initialized<br />
 <i>user_specific</i> a pointer to some user specific data that will be provided to all callbacks<br />
 <i>begin_cb</i> the callback to be called upon the start of a transfer<br />
 <i>marker_cb</i> the callback to be called with every performance marker received<br />
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
<h3>globus_result_t globus_ftp_client_perf_plugin_set_copy_destroy (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_perf_plugin_user_copy_cb_t</code>copy_cb, <code>globus_ftp_client_perf_plugin_user_destroy_cb_t</code>destroy_cb)</h3>
<p> Set user copy and destroy callbacks </p>
<p> Use this to have the plugin make callbacks any time a copy of this plugin is being made. This will allow the user to keep state for different handles. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> plugin previously initialized with init (above)<br />
 <i>copy_cb</i> func to be called when a copy is needed<br />
 <i>destroy_cb</i> func to be called when a copy is to be destroyed</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error on NULL arguments</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Function Documentation</a></p>
<dd>
<dt><a href="#lbAT">Author</a></p>
<dd></dl>
