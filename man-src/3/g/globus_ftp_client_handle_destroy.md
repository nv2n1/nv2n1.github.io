---
title: "globus_ftp_client_handle_destroy(3)"
name: "globus_ftp_client_handle_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_handle_destroy/"
description: "Handle Management –"
---

<h2 class="name">NAME</h2>
<p> Handle Management &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_i_ftp_client_data_target_t</code><br />
 <i>Data connection caching information. </i><br />
 struct <code>globus_i_ftp_client_handle_t</code><br />
 <i>FTP Client handle implementation. </i></p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 <code>globus_i_ftp_client_handle_t</code> * <code>globus_ftp_client_handle_t</code>&quot;<br />
 <i>FTP Client Handle.</i> </p>
<p> An FTP client handle is used to associate state with a group of operations. Handles can have <code>attributes</code> associated with them. All FTP <code>operations </code> take a handle pointer as a parameter. &quot;<br />
 typedef struct<br />
 <code>globus_i_ftp_client_handle_t</code> <code>globus_i_ftp_client_handle_t</code>&quot;<br />
 <i>FTP Client handle implementation. </i></p>
<h3>Initialize</h3>
<p> globus_result_t <code>globus_ftp_client_handle_init</code> (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_handleattr_t</code> *attr) </p>
<h3>Destroy</h3>
<p> globus_result_t <code>globus_ftp_client_handle_destroy</code> (<code>globus_ftp_client_handle_t</code> *handle) </p>
<h3>URL Caching</h3>
<p> globus_result_t <code>globus_ftp_client_handle_cache_url_state</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url) </p>
<p> globus_result_t <code>globus_ftp_client_handle_flush_url_state</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url) </p>
<h3>User Pointer</h3>
<p> globus_result_t <code>globus_ftp_client_handle_set_user_pointer</code> (<code>globus_ftp_client_handle_t</code> *handle, void *user_pointer) </p>
<p> globus_result_t <code>globus_ftp_client_handle_get_user_pointer</code> (const <code>globus_ftp_client_handle_t</code> *handle, void **user_pointer) </p>
<h3>Plugins</h3>
<p> globus_result_t <code>globus_ftp_client_handle_add_plugin</code> (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_plugin_t</code> *plugin) </p>
<p> globus_result_t <code>globus_ftp_client_handle_remove_plugin</code> (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_plugin_t</code> *plugin) </p>
<h2>Detailed Description</h2>
<p> Create/Destroy/Modify an FTP Client Handle. </p>
<p> Within the Globus FTP Client Library, all FTP operations require a handle parameter. Currently, only one FTP operation may be in progress at once per FTP handle. FTP connections may be cached between FTP operations, for improved performance. </p>
<p> This section defines operations to create and destroy FTP Client handles, as well as to modify handles&#8217; connection caches.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>globus_i_ftp_client_handle_t</code>* <code>globus_ftp_client_handle_t</code></h3>
<p> FTP Client Handle. </p>
<p> An FTP client handle is used to associate state with a group of operations. Handles can have <code>attributes</code> associated with them. All FTP <code>operations </code> take a handle pointer as a parameter. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handle_init()</code>, <code>globus_ftp_client_handle_destroy()</code>, <code>globus_ftp_client_handleattr_t</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_handle_add_plugin (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Add a plugin to an FTP client handle. </p>
<p> This function adds a plugin to an FTP client handle after it has been created. Plugins may be added to an ftp client handle whenever an operation is not in progress. The plugin will be appended to the list of plugins present in the handle, and will be invoked during any subsequent operations processed with this handle. </p>
<p> Only one instance of a particular plugin may be added to a particular handle. </p>
<p> Plugins may be removed from a handle by calling globus_ftp_client_remove_plugin(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The FTP client handle to set or query.<br />
 <i>plugin</i> A pointer to the plugin structure to add to this handle.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_ftp_client_remove_plugin(), globus_ftp_clent_handleattr_add_plugin(), globus_ftp_clent_handleattr_remove_plugin()</dl>
<h3>globus_result_t globus_ftp_client_handle_cache_url_state (<code>globus_ftp_client_handle_t</code> *handle, const char *url)</h3>
<p> Cache connections to an FTP server. </p>
<p> Explicitly cache connections to URL server in an FTP handle. When an URL is cached, the client library will not close the connection to the URL server after a file transfer completes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Handle which will contain a cached connection to the URL server.<br />
 <i>url</i> The URL of the FTP or GSIFTP server to cache.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_ftp_client_flush_url_state()</dl>
<h3>globus_result_t globus_ftp_client_handle_destroy (<code>globus_ftp_client_handle_t</code> *handle)</h3>
<p> Destroy a client FTP handle. </p>
<p> A FTP client handle may not be destroyed if a get, put, or third-party transfer is in progress. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be destroyed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handle_init()</code></dl>
<h3>globus_result_t globus_ftp_client_handle_flush_url_state (<code>globus_ftp_client_handle_t</code> *handle, const char *url)</h3>
<p> Remove a cached connection from the FTP client handle. </p>
<p> Explicitly remove a cached connection to an FTP server from the FTP handle. If an idle connection to an FTP server exists, it will be closed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Handle which will contain a cached connection to the URL server.<br />
 <i>url</i> The URL of the FTP or GSIFTP server to cache.</dl>
<h3>globus_result_t globus_ftp_client_handle_init (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_handleattr_t</code> *attr)</h3>
<p> Initialize a client FTP handle. </p>
<p> Initialize an FTP handle which can be used in subsequent get, put, or transfer requests. A handle may have at most one get, put, or third-party transfer in progress. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be initialized.<br />
 <i>attr</i> Initial attributes to be used to create this handle.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handle_destroy()</code></dl>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h3>globus_result_t globus_ftp_client_handle_remove_plugin (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Remove a plugin to an FTP client handle. </p>
<p> This function removes a plugin from an FTP client handle after it has been created. Plugins may be removed from an ftp client handle whenever an operation is not in progress. The plugin will be removed from the list of plugins, and will not be used during any subsequent operations processed with this handle. </p>
<p> This function can remove plugins which were added at <code>handle initialization time</code> or by calling <code>globus_ftp_client_handle_add_plugin()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The FTP client handle to set or query.<br />
 <i>plugin</i> A pointer to the plugin structure to remove from this handle.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_ftp_client_add_plugin(), globus_ftp_clent_handleattr_add_plugin(), globus_ftp_clent_handleattr_remove_plugin()</dl>
<h3>globus_result_t globus_ftp_client_handle_set_user_pointer (<code>globus_ftp_client_handle_t</code> *handle, void *user_pointer)</h3>
<p> Set/Get the user pointer field from an ftp client handle. </p>
<p> The user pointer is provided to all the user of the FTP client library to assocate a pointer to any application-specific data to an FTP client handle. This pointer is never internally used by the client library. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The FTP client handle to set or query.<br />
 <i>user_pointer</i> The value of the user pointer field.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Access to the user_pointer are not synchronized, the user must take care to make sure that multiple threads are not modifying it&#8217;s value.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Function Documentation</a></p>
<dd>
<dt><a href="#lbAU">Author</a></p>
<dd></dl>
