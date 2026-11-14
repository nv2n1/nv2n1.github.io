---
title: "globus_ftp_client_throughput_plugin_get_user_specific(3)"
name: "globus_ftp_client_throughput_plugin_get_user_specific"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_throughput_plugin_get_user_specific/"
description: "Throughput Performance Plugin –"
---

<h2 class="name">NAME</h2>
<p> Throughput Performance Plugin &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_FTP_CLIENT_THROUGHPUT_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_throughput_plugin_module) </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_begin_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, int stripe_ndx, globus_off_t bytes, float instantaneous_throughput, float avg_throughput) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_total_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_off_t bytes, float instantaneous_throughput, float avg_throughput) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_complete_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_bool_t success) </p>
<p> typedef void *(* <code>globus_ftp_client_throughput_plugin_user_copy_cb_t</code> )(void *user_specific) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_user_destroy_cb_t</code> )(void *user_specific) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_throughput_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_begin_cb_t</code> begin_cb, <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code> per_stripe_cb, <code>globus_ftp_client_throughput_plugin_total_cb_t</code> total_cb, <code>globus_ftp_client_throughput_plugin_complete_cb_t</code> complete_cb, void *user_specific) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_plugin_set_copy_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_user_copy_cb_t</code> copy_cb, <code>globus_ftp_client_throughput_plugin_user_destroy_cb_t</code> destroy_cb) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_plugin_get_user_specific</code> (<code>globus_ftp_client_plugin_t</code> *plugin, void **user_specific) </p>
<h2>Detailed Description</h2>
<p> The FTP Throughput Performance plugin allows the user to obtain calculated performance information for all types of transfers except a third party transfer in which Extended Block mode is not enabled. </p>
<p> Note: Since this plugin is built on top of the Performance Marker Plugin, it is not possible to associate both plugins with a handle</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_FTP_CLIENT_THROUGHPUT_PLUGIN_MODULE (&amp;globus_i_ftp_client_throughput_plugin_module)</h3>
<p> Module descriptor</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_ftp_client_throughput_plugin_begin_cb_t)(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url)</h3>
<p> Transfer begin callback </p>
<p> This callback will be called when a transfer begins </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The client handle associated with this transfer<br />
 <i>user_specific</i> User argument passed to globus_ftp_client_throughput_plugin_init<br />
 <i>source_url</i> source of the transfer (GLOBUS_NULL if &#8216;put&#8217;)<br />
 <i>dest_url</i> dest of the transfer (GLOBUS_NULL if &#8216;get&#8217;)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h3>typedef void(* globus_ftp_client_throughput_plugin_complete_cb_t)(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_bool_t success)</h3>
<p> Transfer complete callback </p>
<p> This callback will be called upon transfer completion (successful or otherwise) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The client handle associated with this transfer<br />
 <i>user_specific</i> User argument passed to globus_ftp_client_throughput_plugin_init<br />
 <i>success</i> indicates whether this transfer completed successfully or was interrupted (by error or abort)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h3>typedef void(* globus_ftp_client_throughput_plugin_stripe_cb_t)(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, int stripe_ndx, globus_off_t bytes, float instantaneous_throughput, float avg_throughput)</h3>
<p> Stripe performace throughput callback </p>
<p> This callback will be called with every performance callback that is received by the perf plugin. The first callback for each stripe_ndx will have an instantaneous_throughput based from the time the command was sent. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The client handle associated with this transfer<br />
 <i>user_specific</i> User argument passed to globus_ftp_client_throughput_plugin_init<br />
 <i>bytes</i> The total number of bytes received on this stripe<br />
 <i>instantaneous_throughput</i> Instanteous throughput on this stripe (bytes / sec)<br />
 <i>avg_throughput</i> Average throughput on this stripe (bytes / sec)<br />
 <i>stripe_ndx</i> This stripe&#8217;s index</dl>
<h3>typedef void(* globus_ftp_client_throughput_plugin_total_cb_t)(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_off_t bytes, float instantaneous_throughput, float avg_throughput)</h3>
<p> Total performace throughput callback </p>
<p> This callback will be called with every performance callback that is received by the perf plugin. The first callback for will have an instantaneous_throughput based from the time the command was sent. This callback will be called after the per_stripe_cb </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The client handle associated with this transfer<br />
 <i>user_specific</i> User argument passed to globus_ftp_client_throughput_plugin_init<br />
 <i>bytes</i> The total number of bytes received on all stripes<br />
 <i>instantaneous_throughput</i> Total instanteous throughput on all stripes (bytes / sec)<br />
 <i>avg_throughput</i> Average total throughput on all stripes (bytes / sec)</dl>
<h3>typedef void*(* globus_ftp_client_throughput_plugin_user_copy_cb_t)(void *user_specific)</h3>
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
<h3>typedef void(* globus_ftp_client_throughput_plugin_user_destroy_cb_t)(void *user_specific)</h3>
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
<h3>globus_result_t globus_ftp_client_throughput_plugin_destroy (<code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Destroy throughput plugin </p>
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
<h3>globus_result_t globus_ftp_client_throughput_plugin_get_user_specific (<code>globus_ftp_client_plugin_t</code> *plugin, void **user_specific)</h3>
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
<h3>globus_result_t globus_ftp_client_throughput_plugin_init (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_begin_cb_t</code>begin_cb, <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code>per_stripe_cb, <code>globus_ftp_client_throughput_plugin_total_cb_t</code>total_cb, <code>globus_ftp_client_throughput_plugin_complete_cb_t</code>complete_cb, void *user_specific)</h3>
<p> Throughput plugin init </p>
<p> Use this function to initialize a throughput plugin. The throughput plugin sits on top of the perf_plugin. The only required param is &#8216;plugin&#8217;, all others may be GLOBUS_NULL </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> a pointer to a plugin type to be initialized<br />
 <i>begin_cb</i> the callback to be called upon the start of a transfer<br />
 <i>per_stripe_cb</i> the callback to be called every time updated throughput info is available for a given stripe<br />
 <i>total_cb</i> the callback to be called every time updated throughput info is available for any stripe<br />
 <i>complete_cb</i> the callback to be called to indicate transfer completion<br />
 <i>user_specific</i> a pointer to some user specific data that will be provided to all callbacks</dl>
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
<dd> Error on init perf plugin</dl>
</dl>
<h3>globus_result_t globus_ftp_client_throughput_plugin_set_copy_destroy (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_user_copy_cb_t</code>copy_cb, <code>globus_ftp_client_throughput_plugin_user_destroy_cb_t</code>destroy_cb)</h3>
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
<dt><a href="#lbAP">Function Documentation</a></p>
<dd>
<dt><a href="#lbAU">Author</a></p>
<dd></dl>
