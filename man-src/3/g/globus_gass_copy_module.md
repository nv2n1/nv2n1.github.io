---
title: "globus_gass_copy_module(3)"
name: "globus_gass_copy_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_copy_module/"
description: "globus_gass_copy.h – GASS Copy Library."
---

<p>globus_gass_copy.h &#8211; GASS Copy Library.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_gass_transfer.h&#8217;<br />
 #include &#8216;globus_ftp_client.h&#8217;<br />
 #include &#8216;globus_io.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_gass_copy_handle_s</code><br />
 <i>Copy Handle. </i><br />
 struct <code>globus_gass_copy_attr_s</code><br />
 <i>Attributes. </i><br />
 struct <code>globus_gass_copy_handleattr_s</code><br />
 <i>Handle Attributes. </i><br />
 struct <code>globus_gass_copy_glob_stat_t</code><br />
 <i>Glob expanded entry information. </i></p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GASS_COPY_MODULE</code> (&amp;globus_i_gass_copy_module)<br />
 <i>Module Descriptor. </i></p>
<h3>Typedefs</h3>
<p>typedef void(* <code>globus_gass_copy_performance_cb_t</code> )(void *user_arg, <code>globus_gass_copy_handle_t</code> *handle, globus_off_t total_bytes, float instantaneous_throughput, float avg_throughput)<br />
 <i>Performance Callback. </i><br />
 typedef void(* <code>globus_gass_copy_callback_t</code> )(void *callback_arg, <code>globus_gass_copy_handle_t</code> *handle, globus_object_t *error)<br />
 <i>Copy Callback. </i><br />
 typedef struct<br />
 <code>globus_gass_copy_attr_s</code> <code>globus_gass_copy_attr_t</code>&quot;<br />
 <i>Attributes. </i><br />
 typedef struct<br />
 <code>globus_gass_copy_handleattr_s</code> <code>globus_gass_copy_handleattr_t</code>&quot;<br />
 <i>Handle Attributes. </i><br />
 typedef void(* <code>globus_gass_copy_glob_entry_cb_t</code> )(const char *url, const <code>globus_gass_copy_glob_stat_t</code> *info_stat, void *user_arg)<br />
 <i>Gass copy glob entry callback. </i></p>
<h3>Enumerations</h3>
<p>enum <code>globus_gass_copy_status_t</code><br />
 <i>Status States. </i><br />
 enum <code>globus_gass_copy_url_mode_t</code><br />
 <i>URL Modes. </i><br />
 enum <code>globus_gass_copy_glob_entry_t</code> </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_gass_copy_handle_init</code> (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_handleattr_t</code> *handle_attr)<br />
 <i>Initialize a GASS Copy handle. </i><br />
 globus_result_t <code>globus_gass_copy_handle_destroy</code> (<code>globus_gass_copy_handle_t</code> *handle)<br />
 <i>Destroy a GASS Copy handle. </i><br />
 globus_result_t <code>globus_gass_copy_set_buffer_length</code> (<code>globus_gass_copy_handle_t</code> *handle, int length)<br />
 <i>Set the size of the buffer to be used for doing transfers. </i><br />
 globus_result_t <code>globus_gass_copy_get_buffer_length</code> (<code>globus_gass_copy_handle_t</code> *handle, int *length)<br />
 <i>Get the size of the transfer buffer. </i><br />
 globus_result_t <code>globus_gass_copy_set_no_third_party_transfers</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_t no_third_party_transfers)<br />
 <i>Enable/Disable third-party transfers. </i><br />
 globus_result_t <code>globus_gass_copy_get_no_third_party_transfers</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_t *no_third_party_transfers)<br />
 <i>Query third-party transfer status. </i><br />
 globus_result_t <code>globus_gass_copy_get_partial_offsets</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_off_t *offset, globus_off_t *end_offset)<br />
 <i>Get partial transfer offsets. </i><br />
 globus_result_t <code>globus_gass_copy_set_partial_offsets</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_off_t offset, globus_off_t end_offset)<br />
 <i>Set partial file offsets. </i><br />
 globus_result_t <code>globus_gass_copy_set_allocate</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_t send_allo)<br />
 <i>Set allo on or off. </i><br />
 globus_result_t <code>globus_gass_copy_set_stat_on_expand</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_t always_stat)<br />
 <i>Make globus_gass_copy_expand_url() always send stat info. </i><br />
 globus_result_t <code>globus_gass_copy_get_url_mode</code> (char *url, <code>globus_gass_copy_url_mode_t</code> *mode)<br />
 <i>Get URL scheme. </i><br />
 globus_result_t <code>globus_gass_copy_attr_init</code> (<code>globus_gass_copy_attr_t</code> *attr)<br />
 <i>Initialize an attribute structure. </i><br />
 globus_result_t <code>globus_gass_copy_attr_set_ftp</code> (<code>globus_gass_copy_attr_t</code> *attr, globus_ftp_client_operationattr_t *ftp_attr)<br />
 <i>Set the attributes for ftp/gsiftp transfers. </i><br />
 globus_result_t <code>globus_gass_copy_attr_set_io</code> (<code>globus_gass_copy_attr_t</code> *attr, globus_io_attr_t *io_attr)<br />
 <i>Set file transfers attributes. </i><br />
 globus_result_t <code>globus_gass_copy_attr_set_gass</code> (<code>globus_gass_copy_attr_t</code> *attr, globus_gass_transfer_requestattr_t *gass_attr)<br />
 <i>Set the http/https attributes. </i><br />
 globus_result_t <code>globus_gass_copy_url_to_url</code> (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *source_attr, char *dest_url, <code>globus_gass_copy_attr_t</code> *dest_attr)<br />
 <i>Blocking Transfer between URLs. </i><br />
 globus_result_t <code>globus_gass_copy_url_to_handle</code> (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *source_attr, globus_io_handle_t *dest_handle)<br />
 <i>Blocking Transfer from an URL to an IO handle. </i><br />
 globus_result_t <code>globus_gass_copy_handle_to_url</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_io_handle_t *source_handle, char *dest_url, <code>globus_gass_copy_attr_t</code> *dest_attr)<br />
 <i>Blocking transfer from an IO handle to an URL. </i><br />
 globus_result_t <code>globus_gass_copy_register_url_to_url</code> (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *dest_attr, char *dest_url, <code>globus_gass_copy_attr_t</code> *source_attr, <code>globus_gass_copy_callback_t</code> callback_func, void *callback_arg) </p>
<p> globus_result_t <code>globus_gass_copy_register_url_to_handle</code> (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *source_attr, globus_io_handle_t *dest_handle, <code>globus_gass_copy_callback_t</code> callback_func, void *callback_arg)<br />
 <i>Nonblocking transfer from an URL to an IO handle. </i><br />
 globus_result_t <code>globus_gass_copy_register_handle_to_url</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_io_handle_t *source_handle, char *dest_url, <code>globus_gass_copy_attr_t</code> *dest_attr, <code>globus_gass_copy_callback_t</code> callback_func, void *callback_arg) </p>
<p> globus_result_t <code>globus_gass_copy_get_status</code> (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_status_t</code> *status)<br />
 <i>Get the status code of a transfer. </i><br />
 const char * <code>globus_gass_copy_get_status_string</code> (<code>globus_gass_copy_handle_t</code> *handle)<br />
 <i>Get the status string of a transfer. </i><br />
 globus_result_t <code>globus_gass_copy_cancel</code> (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_callback_t</code> cancel_callback, void *cancel_callback_arg)<br />
 <i>Cancel a transfer. </i><br />
 globus_result_t <code>globus_gass_copy_cache_url_state</code> (<code>globus_gass_copy_handle_t</code> *handle, char *url)<br />
 <i>Cache connections to an FTP or GridFTP server. </i><br />
 globus_result_t <code>globus_gass_copy_flush_url_state</code> (<code>globus_gass_copy_handle_t</code> *handle, char *url)<br />
 <i>Remove an FTP or GridFTP cached connection. </i><br />
 globus_result_t <code>globus_gass_copy_set_user_pointer</code> (<code>globus_gass_copy_handle_t</code> *handle, void *user_data)<br />
 <i>Set the user pointer in a handle. </i><br />
 globus_result_t <code>globus_gass_copy_get_user_pointer</code> (<code>globus_gass_copy_handle_t</code> *handle, void **user_data)<br />
 <i>Get the user pointer in a handle. </i><br />
 globus_result_t <code>globus_gass_copy_register_performance_cb</code> (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_performance_cb_t</code> callback, void *user_arg)<br />
 <i>Register a performance information callback. </i><br />
 globus_result_t <code>globus_gass_copy_glob_expand_url</code> (<code>globus_gass_copy_handle_t</code> *handle, const char *url, <code>globus_gass_copy_attr_t</code> *attr, <code>globus_gass_copy_glob_entry_cb_t</code> entry_cb, void *user_arg)<br />
 <i>Expand globbed url. </i><br />
 globus_result_t <code>globus_gass_copy_mkdir</code> (<code>globus_gass_copy_handle_t</code> *handle, char *url, <code>globus_gass_copy_attr_t</code> *attr)<br />
 <i>Make directory. </i></p>
<h2>Detailed Description</h2>
<p>GASS Copy Library. </p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gass_copy_cache_url_state (<code>globus_gass_copy_handle_t</code> *handle, char *url)</h3>
<p>Cache connections to an FTP or GridFTP server. Explicitly cache connections to URL server. When an URL is cached, the connection to the URL server will not be closed after a file transfer completes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> Handle which will contain a cached connection to the URL server.<br />
 <i>url</i> The URL of the FTP or GSIFTP server to cache.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>globus_result_t globus_gass_copy_flush_url_state (<code>globus_gass_copy_handle_t</code> *handle, char *url)</h3>
<p>Remove an FTP or GridFTP cached connection. Explicitly remove a cached connection to an FTP or GSIFTP server. If an idle connection to an FTP server exists, it will be closed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> Handle which contains a cached connection to the URL server.<br />
 <i>url</i> The URL of the FTP or GSIFTP server to remove.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>globus_result_t globus_gass_copy_handle_to_url (<code>globus_gass_copy_handle_t</code> *handle, globus_io_handle_t *source_handle, char *dest_url, <code>globus_gass_copy_attr_t</code> *dest_attr)</h3>
<p>Blocking transfer from an IO handle to an URL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> The handle to perform the copy operation<br />
 <i>source_handle</i> transfer data from this IO handle<br />
 <i>dest_url</i> transfer data to this URL<br />
 <i>dest_attr</i> Attributes describing how the transfer to the destination should be done</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if the transfer was completed successfully, or a result pointing to an object of one of the the following error types:</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>GLOBUS_GASS_COPY_ERROR_TYPE_NULL_PARAMETER</i> The handle was equal to GLOBUS_NULL, so the transfer could not processed.<br />
 <i>GLOBUS_GASS_COPY_ERROR_TYPE_next_error</i> next error description</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_gass_copy_url_to_url()</code> <code>globus_gass_copy_url_to_handle()</code></dl>
<h3>globus_result_t globus_gass_copy_register_handle_to_url (<code>globus_gass_copy_handle_t</code> *handle, globus_io_handle_t *source_handle, char *dest_url, <code>globus_gass_copy_attr_t</code> *dest_attr, <code>globus_gass_copy_callback_t</code>callback_func, void *callback_arg)</h3>
<p>Nonblocking Transfer From an IO handle to an URL </p>
<p> This functions initiates a transfer from an IO handle to destination URL, then returns immediately. </p>
<p> When the transfer is completed or if the transfer is aborted, the callback_func will be invoked with the final status of the transfer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> The handle to perform the copy operation<br />
 <i>source_handle</i> transfer data from this IO handle<br />
 <i>dest_url</i> transfer data to this URL<br />
 <i>dest_attr</i> Attributes describing how the transfer to the destination should be done<br />
 <i>callback_func</i> Callback to be invoked once the transfer is completed.<br />
 <i>callback_arg</i> Argument to be passed to the callback_func.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if the transfer was initiated successfully, or a result pointing to an object of one of the the following error types:</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>GLOBUS_GASS_COPY_ERROR_TYPE_NULL_PARAMETER</i> The handle was equal to GLOBUS_NULL, so the transfer could not processed.<br />
 <i>GLOBUS_GASS_COPY_ERROR_TYPE_next_error</i> next error description</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_gass_copy_register_url_to_url()</code>, <code>globus_gass_copy_register_url_to_handle()</code></dl>
<h3>globus_result_t globus_gass_copy_register_url_to_handle (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *source_attr, globus_io_handle_t *dest_handle, <code>globus_gass_copy_callback_t</code>callback_func, void *callback_arg)</h3>
<p>Nonblocking transfer from an URL to an IO handle. This functions initiates a transfer from source URL to an IO handle, then returns immediately. </p>
<p> When the transfer is completed or if the transfer is aborted, the callback_func will be invoked with the final status of the transfer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> The handle to perform the copy operation<br />
 <i>source_url</i> transfer data from this URL<br />
 <i>source_attr</i> Attributes describing how the transfer form the source should be done<br />
 <i>dest_handle</i> transfer data to this IO handle<br />
 <i>callback_func</i> Callback to be invoked once the transfer is completed.<br />
 <i>callback_arg</i> Argument to be passed to the callback_func.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if the transfer was initiated successfully, or a result pointing to an object of one of the the following error types:</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>GLOBUS_GASS_COPY_ERROR_TYPE_NULL_PARAMETER</i> The handle was equal to GLOBUS_NULL, so the transfer could not processed.<br />
 <i>GLOBUS_GASS_COPY_ERROR_TYPE_next_error</i> next error description</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_gass_copy_register_url_to_url()</code>, <code>globus_gass_copy_register_handle_to_url()</code></dl>
<h3>globus_result_t globus_gass_copy_register_url_to_url (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *source_attr, char *dest_url, <code>globus_gass_copy_attr_t</code> *dest_attr, <code>globus_gass_copy_callback_t</code>callback_func, void *callback_arg)</h3>
<p>Nonblocking Transfer between URLs </p>
<p> This functions initiates a transfer from source URL to destination URL, then returns immediately. </p>
<p> When the transfer is completed or if the transfer is aborted, the callback_func will be invoked with the final status of the transfer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> The handle to perform the copy operation<br />
 <i>source_url</i> transfer data from this URL<br />
 <i>source_attr</i> Attributes describing how the transfer form the source should be done<br />
 <i>dest_url</i> transfer data to this URL<br />
 <i>dest_attr</i> Attributes describing how the transfer to the destination should be done<br />
 <i>callback_func</i> Callback to be invoked once the transfer is completed.<br />
 <i>callback_arg</i> Argument to be passed to the callback_func.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if the transfer was initiated successfully, or a result pointing to an object of one of the the following error types:</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>GLOBUS_GASS_COPY_ERROR_TYPE_NULL_PARAMETER</i> The handle was equal to GLOBUS_NULL, so the transfer could not processed.<br />
 <i>GLOBUS_GASS_COPY_ERROR_TYPE_next_error</i> next error description</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_gass_copy_register_url_to_handle()</code>, <code>globus_gass_copy_register_handle_to_url()</code></dl>
<h3>globus_result_t globus_gass_copy_url_to_handle (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *source_attr, globus_io_handle_t *dest_handle)</h3>
<p>Blocking Transfer from an URL to an IO handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> The handle to perform the copy operation<br />
 <i>source_url</i> transfer data from this URL<br />
 <i>source_attr</i> Attributes describing how the transfer form the source should be done<br />
 <i>dest_handle</i> transfer data to this IO handle</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if the transfer was completed successfully, or a result pointing to an object of one of the the following error types:</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>GLOBUS_GASS_COPY_ERROR_TYPE_NULL_PARAMETER</i> The handle was equal to GLOBUS_NULL, so the transfer could not processed.<br />
 <i>GLOBUS_GASS_COPY_ERROR_TYPE_next_error</i> next error description</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_gass_copy_url_to_url()</code> <code>globus_gass_copy_handle_to_url()</code></dl>
<h3>globus_result_t globus_gass_copy_url_to_url (<code>globus_gass_copy_handle_t</code> *handle, char *source_url, <code>globus_gass_copy_attr_t</code> *source_attr, char *dest_url, <code>globus_gass_copy_attr_t</code> *dest_attr)</h3>
<p>Blocking Transfer between URLs. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>handle</i> The handle to perform the copy operation<br />
 <i>source_url</i> transfer data from this URL<br />
 <i>source_attr</i> Attributes describing how the transfer form the source should be done<br />
 <i>dest_url</i> transfer data to this URL<br />
 <i>dest_attr</i> Attributes describing how the transfer to the destination should be done</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This function returns GLOBUS_SUCCESS if the transfer was completed successfully, or a result pointing to an object of one of the the following error types:</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>GLOBUS_GASS_COPY_ERROR_TYPE_NULL_PARAMETER</i> The handle was equal to GLOBUS_NULL, so the transfer could not processed.<br />
 <i>GLOBUS_GASS_COPY_ERROR_TYPE_next_error</i> next error description</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_gass_copy_url_to_handle()</code> <code>globus_gass_copy_handle_to_url()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gass_copy from the source code.</p>
