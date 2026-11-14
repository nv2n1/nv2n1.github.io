---
title: "globus_gass_copy_get_url_mode(3)"
name: "globus_gass_copy_get_url_mode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_copy_get_url_mode/"
description: "GASS Copy –"
---

<h2 class="name">NAME</h2>
<p> GASS Copy &#8211; </p>
<p> Protocol-Independent File Transfer.</p>
<h3>Data Structures</h3>
<p> struct <code>globus_gass_copy_attr_s</code><br />
 <i>Attributes. </i><br />
 struct <code>globus_gass_copy_handleattr_s</code><br />
 <i>Handle Attributes. </i><br />
 struct <code>globus_gass_copy_glob_stat_t</code><br />
 <i>Glob expanded entry information. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GASS_COPY_MODULE</code> (&amp;globus_i_gass_copy_module)<br />
 <i>Module Descriptor. </i></p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_gass_copy_performance_cb_t</code> )(void *user_arg, <code>globus_gass_copy_handle_t</code> *handle, globus_off_t total_bytes, float instantaneous_throughput, float avg_throughput)<br />
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
<p> enum <code>globus_gass_copy_status_t</code><br />
 <i>Status States. </i><br />
 enum <code>globus_gass_copy_url_mode_t</code><br />
 <i>URL Modes. </i><br />
 enum <code>globus_gass_copy_glob_entry_t</code> </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gass_copy_handle_init</code> (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_handleattr_t</code> *attr)<br />
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
 globus_result_t <code>globus_gass_copy_set_allocate</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_t send_allo)<br />
 <i>Set allo on or off. </i><br />
 globus_result_t <code>globus_gass_copy_set_stat_on_expand</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_t always_stat)<br />
 <i>Make globus_gass_copy_expand_url() always send stat info. </i><br />
 globus_result_t <code>globus_gass_copy_set_partial_offsets</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_off_t offset, globus_off_t end_offset)<br />
 <i>Set partial file offsets. </i><br />
 globus_result_t <code>globus_gass_copy_get_partial_offsets</code> (<code>globus_gass_copy_handle_t</code> *handle, globus_off_t *offset, globus_off_t *end_offset)<br />
 <i>Get partial transfer offsets. </i><br />
 globus_result_t <code>globus_gass_copy_attr_init</code> (<code>globus_gass_copy_attr_t</code> *attr)<br />
 <i>Initialize an attribute structure. </i><br />
 globus_result_t <code>globus_gass_copy_attr_set_ftp</code> (<code>globus_gass_copy_attr_t</code> *attr, globus_ftp_client_operationattr_t *ftp_attr)<br />
 <i>Set the attributes for ftp/gsiftp transfers. </i><br />
 globus_result_t <code>globus_gass_copy_attr_set_io</code> (<code>globus_gass_copy_attr_t</code> *attr, globus_io_attr_t *io_attr)<br />
 <i>Set file transfers attributes. </i><br />
 globus_result_t <code>globus_gass_copy_attr_set_gass</code> (<code>globus_gass_copy_attr_t</code> *attr, globus_gass_transfer_requestattr_t *gass_attr)<br />
 <i>Set the http/https attributes. </i><br />
 globus_result_t <code>globus_gass_copy_get_url_mode</code> (char *url, <code>globus_gass_copy_url_mode_t</code> *mode)<br />
 <i>Get URL scheme. </i><br />
 globus_result_t <code>globus_gass_copy_register_performance_cb</code> (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_performance_cb_t</code> callback, void *user_arg)<br />
 <i>Register a performance information callback. </i><br />
 globus_result_t <code>globus_gass_copy_get_status</code> (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_status_t</code> *status)<br />
 <i>Get the status code of a transfer. </i><br />
 const char * <code>globus_gass_copy_get_status_string</code> (<code>globus_gass_copy_handle_t</code> *handle)<br />
 <i>Get the status string of a transfer. </i><br />
 globus_result_t <code>globus_gass_copy_glob_expand_url</code> (<code>globus_gass_copy_handle_t</code> *handle, const char *url, <code>globus_gass_copy_attr_t</code> *attr, <code>globus_gass_copy_glob_entry_cb_t</code> entry_cb, void *user_arg)<br />
 <i>Expand globbed url. </i><br />
 globus_result_t <code>globus_gass_copy_mkdir</code> (<code>globus_gass_copy_handle_t</code> *handle, char *url, <code>globus_gass_copy_attr_t</code> *attr)<br />
 <i>Make directory. </i></p>
<h2>Detailed Description</h2>
<p> Protocol-Independent File Transfer. </p>
<p> The Globus GASS Copy library is motivated by the desire to provide a uniform interface to transfer files specified by different protocols. </p>
<p> The goals in doing this are to: </p>
<dl>
<dt>&bull;</p>
<dd> Provide a robust way to describe and apply file transfer properties for a variety of protocols. These include the standard HTTP, FTP and GSIFTP options. Some of the new file transfer capabilities in GSIFTP are parallel, striping, authentication and TCP buffer sizing.</p>
<dt>&bull;</p>
<dd> Provide a service to support nonblocking file transfer and handle asynchronous file and network events.</p>
<dt>&bull;</p>
<dd> Provide a simple and portable way to implement file transfers.</dl>
<p> Any program that uses Globus GASS Copy functions must include &#8216;globus_gass_copy.h&#8217;. </p>
<p> Globus GASS Copy uses standard Globus module activation and deactivation. Before any Globus GASS Copy functions are called, the following function must be called: </p>
<pre>
globus_module_activate(GLOBUS_GASS_COPY_MODULE)
</pre>
<p> This function returns GLOBUS_SUCCESS if Globus GASS Copy was successfully initialized, and you are therefore allowed to subsequently call Globus GASS Copy functions. Otherwise, an error code is returned, and Globus GASS Copy functions should not be subsequently called. This function may be called multiple times. </p>
<p> To deactivate Globus GASS Copy, the following function must be called: </p>
<pre>
globus_module_deactivate(GLOBUS_GASS_COPY_MODULE)
</pre>
<p> This function should be called once for each time Globus GASS Copy was activated.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>globus_gass_copy_attr_s</code> <code>globus_gass_copy_attr_t</code></h3>
<p> Attributes. Contains any/all attributes that are required to perform the supported transfer methods (ftp, gass, io).</p>
<h3>typedef void(* globus_gass_copy_callback_t)(void *callback_arg, <code>globus_gass_copy_handle_t</code> *handle, globus_object_t *error)</h3>
<p> Copy Callback. Signature of a callback from globus_gass_copy_register_*() functions. (nonblocking transfer functions)</p>
<h3>typedef void(* globus_gass_copy_glob_entry_cb_t)(const char *url, const <code>globus_gass_copy_glob_stat_t</code> *info_stat, void *user_arg)</h3>
<p> Gass copy glob entry callback. This callback is passed as a parameter to <code>globus_gass_copy_glob_expand_url()</code>. It is called once for each entry that the original expands to. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> The full url to the expanded entry. A directory entry will end in a forward slash &#8216;/&#8217;.<br />
 <i>stat</i> A pointer to a <code>globus_gass_copy_glob_stat_t</code> containing information about the entry.<br />
 <i>user_arg</i> The user_arg passed to globus_gass_copy_glob_expand()</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_glob_stat_t</code>, <code>globus_gass_copy_glob_expand_url</code></dl>
<h3>typedef struct <code>globus_gass_copy_handleattr_s</code> <code>globus_gass_copy_handleattr_t</code></h3>
<p> Handle Attributes. Contains any/all attributes that are required to create lower-level handles (ftp, gass, io).</p>
<h3>typedef void(* globus_gass_copy_performance_cb_t)(void *user_arg, <code>globus_gass_copy_handle_t</code> *handle, globus_off_t total_bytes, float instantaneous_throughput, float avg_throughput)</h3>
<p> Performance Callback. This callback is registered with &#8216;globus_gass_copy_register_performance_cb&#8217; It will be called during a transfer to supply performance information on current transfer. Its frequency will be at most one per second, but it is possible to receive no callbacks. This is possible in very short transfers and in ftp transfers in which the server does not provide performance information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the gass copy handle this transfer is occurring on<br />
 <i>user_arg</i> a user pointer registered with &#8216;globus_gass_copy_register_performance_cb&#8217;<br />
 <i>total_bytes</i> the total number of bytes transfer so far<br />
 <i>instantaneous_throughput</i> instantaneous rate of transfer (since last callback or start) (bytes / sec)<br />
 <i>avg_throughput</i> the avg thoughput calculated since the start of the transfer (bytes / sec)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> n/a</dl>
</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gass_copy_glob_entry_t</code></h3>
<p> globbed entry types</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gass_copy_attr_init (<code>globus_gass_copy_attr_t</code> *attr)</h3>
<p> Initialize an attribute structure. The globus_gass_copy_attr_t can be used to pass the globus_gass_copy library information about how a transfer should be performed. It must first be initialized by calling this function. Then any or all of the following functions may be called to set attributes associated with a particular protocol: <code>globus_gass_copy_attr_set_ftp()</code>, <code>globus_gass_copy_attr_set_gass()</code>, <code>globus_gass_copy_attr_set_io()</code>. Any function which takes a globus_gass_copy_attr_t as an argument will also accept GLOBUS_NULL, in which case the appropriate set of default attributes will be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute structure to be initialized</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_attr_set_ftp()</code>, <code>globus_gass_copy_attr_set_gass()</code>, <code>globus_gass_copy_attr_set_io()</code>, <code>globus_gass_copy_get_url_mode()</code>.</dl>
<h3>globus_result_t globus_gass_copy_attr_set_ftp (<code>globus_gass_copy_attr_t</code> *attr, globus_ftp_client_operationattr_t *ftp_attr)</h3>
<p> Set the attributes for ftp/gsiftp transfers. In order to specify attributes for ftp/gsiftp transfers, a globus_ftp_client_operationattr_t should be initialized and its values set using the appropriate globus_ftp_client_operationattr_* functions. The globus_ftp_client_operationattr_t * can then be passed to the globus_gass_copy_attr_t via this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A globus_gass_copy attribute structure<br />
 <i>ftp_attr</i> The ftp/gsiftp attributes to be used</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_attr_init()</code>, <code>globus_gass_copy_attr_set_gass()</code>, <code>globus_gass_copy_attr_set_io()</code>, <code>globus_gass_copy_get_url_mode()</code>, globus_ftp_client_operationattr_*</dl>
<h3>globus_result_t globus_gass_copy_attr_set_gass (<code>globus_gass_copy_attr_t</code> *attr, globus_gass_transfer_requestattr_t *gass_attr)</h3>
<p> Set the http/https attributes. In order to specify attributes for http/https transfers, a globus_gass_transfer_requestattr_t should be initialized and its values set using the appropriate globus_gass_transfer_requestattr_* functions. The globus_gass_transfer_requestattr_t can then be passed to the globus_gass_copy_attr_t via this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A globus_gass_copy attribute structure<br />
 <i>gass_attr</i> The http/https attributes to be used</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_attr_init()</code>, <code>globus_gass_copy_attr_set_io()</code>, <code>globus_gass_copy_attr_set_ftp()</code>, <code>globus_gass_copy_get_url_mode()</code>, globus_gass_transfer_requestattr_*</dl>
<h3>globus_result_t globus_gass_copy_attr_set_io (<code>globus_gass_copy_attr_t</code> *attr, globus_io_attr_t *io_attr)</h3>
<p> Set file transfers attributes. In order to specify attributes for file transfers, a globus_io_attr_t should be initialized and its values set using the appropriate globus_io_attr_* functions. The globus_io_attr_t can then be passed to the globus_gass_copy_attr_t via this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A globus_gass_copy attribute structure<br />
 <i>io_attr</i> The file attributes to be used</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_attr_init()</code>, <code>globus_gass_copy_attr_set_gass()</code>, <code>globus_gass_copy_attr_set_ftp()</code>, <code>globus_gass_copy_get_url_mode()</code>, globus_io_attr_*</dl>
<h3>globus_result_t globus_gass_copy_get_buffer_length (<code>globus_gass_copy_handle_t</code> *handle, int *length)</h3>
<p> Get the size of the transfer buffer. This function allows the user to get the size of the buffer that is being used for doing transfers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Get the buffer length for transfers associated with this handle.<br />
 <i>length</i> The length, in bytes, of the buffer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>globus_result_t globus_gass_copy_get_no_third_party_transfers (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_t *no_third_party_transfers)</h3>
<p> Query third-party transfer status. This function allows the user to see if third-party transfers are turned on or off for ftp to ftp transfers associated with a particular handle. This is often desired if one of the servers involved in the transfer does not allow third-party transfers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> See if third-party transfers are turned on or off for transfers associated with this handle. They are on by default.<br />
 <i>no_third_party_transfers</i> GLOBUS_FALSE if third-party transfers should be used. GLOBUS_TRUE if third-party transfers should not be used.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>globus_result_t globus_gass_copy_get_partial_offsets (<code>globus_gass_copy_handle_t</code> *handle, globus_off_t *offset, globus_off_t *end_offset)</h3>
<p> Get partial transfer offsets. This function allows the user to get the offsets that are being used for doing partial transfers. An offset of -1 means partial transfers are disabled. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Get the offsets for partial transfers associated with this handle.<br />
 <i>offset</i> The starting offset for the partial transfer.<br />
 <i>end_offset</i> The ending offset for the partial transfer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>globus_result_t globus_gass_copy_get_status (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_status_t</code> *status)</h3>
<p> Get the status code of a transfer. Get the status of the last transfer to be initiated using the given handle. Only one transfer can be active on a handle at a given time, therefore new transfers may only be initiated when the current status is one of the following: GLOBUS_GASS_COPY_STATUS_NONE, GLOBUS_GASS_COPY_STATUS_DONE_SUCCESS, GLOBUS_GASS_COPY_STATUS_DONE_FAILURE, GLOBUS_GASS_COPY_STATUS_DONE_CANCELLED </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A globus_gass_copy_handle<br />
 <i>status</i> Will be one of the following: GLOBUS_GASS_COPY_STATUS_NONE (No transfers have been initiated using this handle.) GLOBUS_GASS_COPY_STATUS_PENDING (A transfer is currently being set up.) GLOBUS_GASS_COPY_STATUS_TRANSFER_IN_PROGRESS (There is currently a transfer in progress.) GLOBUS_GASS_COPY_STATUS_CANCEL (The last transfer initiated using this handle has been cancelled by the user before completing, and is in the process of being cleaned up.) GLOBUS_GASS_COPY_STATUS_FAILURE (The last transfer initiated using this handle failed, and is in the process of being cleaned up.) GLOBUS_GASS_COPY_STATUS_DONE_SUCCESS (The last transfer initiated using this handle has completed successfully.) GLOBUS_GASS_COPY_STATUS_DONE_FAILURE (The last transfer initiated using this handle failed and has finished cleaning up.) GLOBUS_GASS_COPY_STATUS_DONE_CANCELLED (The last transfer initiated using this handle was cancelled and has finished cleaning up.)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>const char* globus_gass_copy_get_status_string (<code>globus_gass_copy_handle_t</code> *handle)</h3>
<p> Get the status string of a transfer. Get the status of the last transfer to be initiated using the given handle. Only one transfer can be active on a handle at a given time, therefore new transfers may only be initiated when the current status is one of the following: GLOBUS_GASS_COPY_STATUS_NONE, GLOBUS_GASS_COPY_STATUS_DONE_SUCCESS, GLOBUS_GASS_COPY_STATUS_DONE_FAILURE, GLOBUS_GASS_COPY_STATUS_DONE_CANCELLED </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A globus_gass_copy_handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns a pointer to a character string describing the current status</dl>
<h3>globus_result_t globus_gass_copy_get_url_mode (char *url, <code>globus_gass_copy_url_mode_t</code> *mode)</h3>
<p> Get URL scheme. This function enables the user to determine what protocol will be used to transfer data to/from a particular url. This information can then be used to specify the appropriate attributes when initiating a transfer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> The URL for schema checking<br />
 <i>mode</i> the filled in schema type of the URL param</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_attr_init()</code>, <code>globus_gass_copy_attr_set_io()</code>, <code>globus_gass_copy_attr_set_ftp()</code>, globus_gass_copy_set_gass()</dl>
<h3>globus_result_t globus_gass_copy_glob_expand_url (<code>globus_gass_copy_handle_t</code> *handle, const char *url, <code>globus_gass_copy_attr_t</code> *attr, <code>globus_gass_copy_glob_entry_cb_t</code>entry_cb, void *user_arg)</h3>
<p> Expand globbed url. This function expands wildcards in a globbed url, and calls entry_cb() on each one. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A gass copy handle to use for the operation.<br />
 <i>url</i> The URL to expand. The URL may be an ftp, gsiftp or file URL. Wildcard characters supported are &#8216;?&#8217; &#8216;*&#8217; &#8216;[ ]&#8217; in the filename portion of the url.<br />
 <i>attr</i> Gass copy attributes for this operation.<br />
 <i>entry_cb</i> Function to call with information about each entry<br />
 <i>user_arg</i> An argument to pass to entry_cb()</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp, gsiftp or file url</dl>
</dl>
<h3>globus_result_t globus_gass_copy_handle_destroy (<code>globus_gass_copy_handle_t</code> *handle)</h3>
<p> Destroy a GASS Copy handle. Destroy a gass_copy_handle, which was initialized using <code>globus_gass_copy_handle_init()</code>, that will no longer be used for doing transfers. Once the handle is detroyed, no further transfers should be associated with it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be destroyed</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_handle_init()</code>, globus_ftp_client_handle_destroy()</dl>
<h3>globus_result_t globus_gass_copy_handle_init (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_handleattr_t</code> *attr)</h3>
<p> Initialize a GASS Copy handle. A globus_gass_copy_handle must be initialized before any transfers may be associated with it. This function initializes a globus_gass_copy_handle to be used for doing transfers, this includes initializing a globus_ftp_client_handle which will be used for doing any ftp/gsiftp transfers. The same handle may be used to perform multiple, consecutive transfers. However, there can only be one transfer associated with a particular handle at any given time. After all transfers to be associated with this handle have completed, the handle should be destroyed by calling <code>globus_gass_copy_handle_destroy()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be initialized<br />
 <i>attr</i> The handle attributes used to use with this handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_handle_destroy()</code> , globus_gass_copy_handleattr_init(), globus_ftp_client_hande_init()</dl>
<h3>globus_result_t globus_gass_copy_mkdir (<code>globus_gass_copy_handle_t</code> *handle, char *url, <code>globus_gass_copy_attr_t</code> *attr)</h3>
<p> Make directory. This function creates a directory given a ftp or file url. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A gass copy handle to use for the mkdir operation.<br />
 <i>url</i> The URL for the directory to create. The URL may be an ftp, gsiftp or file URL.<br />
 <i>attr</i> Gass copy attributes for this operation.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp, gsiftp or file url</p>
<dt>&bull;</p>
<dd> the directory could not be created</dl>
</dl>
<h3>globus_result_t globus_gass_copy_register_performance_cb (<code>globus_gass_copy_handle_t</code> *handle, <code>globus_gass_copy_performance_cb_t</code>callback, void *user_arg)</h3>
<p> Register a performance information callback. Use this to register a performance information callback. You change or set to GLOBUS_NULL the callback any time a transfer is not occurring. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> an initialized gass copy handle for which you would like to see performance info<br />
 <i>callback</i> the performance callback<br />
 <i>user_arg</i> a user pointer that will be passed to all callbacks for a given handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</p>
<dt>&bull;</p>
<dd> error on a NULL or busy handle</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_copy_performance_cb_t</code></dl>
<h3>globus_result_t globus_gass_copy_set_buffer_length (<code>globus_gass_copy_handle_t</code> *handle, intlength)</h3>
<p> Set the size of the buffer to be used for doing transfers. This function allows the user to set the size of the buffer that will be used for doing transfers, if this function is not called the buffer size will default to 1M. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Set the buffer length for transfers associated with this handle.<br />
 <i>length</i> The length, in bytes, to make the buffer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>globus_result_t globus_gass_copy_set_no_third_party_transfers (<code>globus_gass_copy_handle_t</code> *handle, globus_bool_tno_third_party_transfers)</h3>
<p> Enable/Disable third-party transfers. This function allows the user to turn third-party transfers on or off for ftp to ftp transfers associated with a particular handle. This is often desired if one of the servers involved in the transfer does not allow third-party transfers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Turn third-party transfers on or off for transfers associated with this handle. They are on by default.<br />
 <i>no_third_party_transfers</i> GLOBUS_FALSE if third-party transfers should be used. GLOBUS_TRUE if third-party transfers should not be used.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h3>globus_result_t globus_gass_copy_set_partial_offsets (<code>globus_gass_copy_handle_t</code> *handle, globus_off_toffset, globus_off_tend_offset)</h3>
<p> Set partial file offsets. This function allows the user to set the offsets that will be used for doing partial transfers. An offset of -1 will disable partial transfers. An end_offset of -1 means EOF. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Set the offsets for partial transfers associated with this handle.<br />
 <i>offset</i> The starting offset for the partial transfer.<br />
 <i>end_offset</i> The ending offset for the partial transfer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS if successful, or a globus_result_t indicating the error that occurred.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_copy from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAQ">Function Documentation</a></p>
<dd>
<dt><a href="#lbBJ">Author</a></p>
<dd></dl>
