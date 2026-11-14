---
title: "globus_ftp_client_handleattr_set_rfc1738_url(3)"
name: "globus_ftp_client_handleattr_set_rfc1738_url"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_handleattr_set_rfc1738_url/"
description: "Handle Attributes –"
---

<h2 class="name">NAME</h2>
<p> Handle Attributes &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_i_ftp_client_handleattr_t</code><br />
 <i>Handle attributes. </i></p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 <code>globus_i_ftp_client_handleattr_t</code> * <code>globus_ftp_client_handleattr_t</code>&quot;<br />
 <i>Handle Attributes.</i> </p>
<p> Handle attributes are used to control the caching behavior of the ftp client handle, and to implement the plugin features for reliability and performance tuning. &quot;<br />
 typedef struct<br />
 <code>globus_i_ftp_client_handleattr_t</code> <code>globus_i_ftp_client_handleattr_t</code>&quot;<br />
 <i>Handle attributes. </i></p>
<h3>Initialize</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_init</code> (<code>globus_ftp_client_handleattr_t</code> *attr) </p>
<h3>Destroy</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_destroy</code> (<code>globus_ftp_client_handleattr_t</code> *attr) </p>
<h3>Copy</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_copy</code> (<code>globus_ftp_client_handleattr_t</code> *dest, <code>globus_ftp_client_handleattr_t</code> *src) </p>
<h3>Connection Caching</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_set_cache_all</code> (<code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_t cache_all) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_get_cache_all</code> (const <code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_t *cache_all) </p>
<h3>Non-root relative URLs</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_set_rfc1738_url</code> (<code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_t rfc1738_url) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_get_rfc1738_url</code> (const <code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_t *rfc1738_url) </p>
<h3>Client Info</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_set_clientinfo</code> (<code>globus_ftp_client_handleattr_t</code> *attr, const char *app_name, const char *app_version, const char *other) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_get_clientinfo</code> (<code>globus_ftp_client_handleattr_t</code> *attr, char **app_name, char **app_version, char **other) </p>
<h3>GridFTP2 support</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_set_gridftp2</code> (<code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_t gridftp2) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_get_gridftp2</code> (const <code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_t *gridftp2) </p>
<h3>Command Pipelining</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_set_pipeline</code> (<code>globus_ftp_client_handleattr_t</code> *attr, globus_size_t outstanding_commands, globus_ftp_client_pipeline_callback_t pipeline_callback, void *pipeline_arg) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_get_pipeline</code> (const <code>globus_ftp_client_handleattr_t</code> *attr, globus_size_t *outstanding_commands, globus_ftp_client_pipeline_callback_t *pipeline_callback, void **pipeline_arg) </p>
<h3>URL Caching</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_add_cached_url</code> (<code>globus_ftp_client_handleattr_t</code> *attr, const char *url) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_remove_cached_url</code> (<code>globus_ftp_client_handleattr_t</code> *attr, const char *url) </p>
<h3>Netlogger management</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_set_netlogger</code> (<code>globus_ftp_client_handleattr_t</code> *attr, globus_netlogger_handle_t *nl_handle) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_set_netlogger_ftp_io</code> (<code>globus_ftp_client_handleattr_t</code> *attr, globus_netlogger_handle_t *nl_handle, globus_bool_t ftp, globus_bool_t io) </p>
<h3>Plugin Management</h3>
<p> globus_result_t <code>globus_ftp_client_handleattr_add_plugin</code> (<code>globus_ftp_client_handleattr_t</code> *attr, <code>globus_ftp_client_plugin_t</code> *plugin) </p>
<p> globus_result_t <code>globus_ftp_client_handleattr_remove_plugin</code> (<code>globus_ftp_client_handleattr_t</code> *attr, <code>globus_ftp_client_plugin_t</code> *plugin) </p>
<h2>Detailed Description</h2>
<p> Handle attributes are used to control additional features of the FTP Client handle. These features are operation independent. </p>
<p> The attribute which can currently set on a handle concern the connection caching behavior of the handle, and the associations of plugins with a handle. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handle_t</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>globus_i_ftp_client_handleattr_t</code>* <code>globus_ftp_client_handleattr_t</code></h3>
<p> Handle Attributes. </p>
<p> Handle attributes are used to control the caching behavior of the ftp client handle, and to implement the plugin features for reliability and performance tuning. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handle_t</code>, <code>Handle Attributes</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_handleattr_add_cached_url (<code>globus_ftp_client_handleattr_t</code> *attr, const char *url)</h3>
<p> Enable/Disable caching for a specific URL. </p>
<p> This function adds/removes the specified URL into the default cache for a handle attribute. Handles initialized with this attr will keep connections to FTP servers associated with the URLs in its cache open between <code>operations </code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute to modify<br />
 <i>url</i> URL string to cache</dl>
<h3>globus_result_t globus_ftp_client_handleattr_add_plugin (<code>globus_ftp_client_handleattr_t</code> *attr, <code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Add/Remove a plugin to a handle attribute set. </p>
<p> Each handle attribute set contains a list of plugins associated with it. When a handle is created with a particular attribute set, it will be associated with a copy of those plugins. </p>
<p> Only one instance of a specific plugin may be added to an attribute set. Each plugin must have a different name. </p>
<p> A copy of the plugin is created via the plugins &#8216;copy&#8217; method when it is added to an attribute set. Thus, any changes to a particular plugin must be done before the plugin is added to an attribute set, and before the attribute set is used to create handles. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to modify.<br />
 <i>plugin</i> The plugin to add or remove from the list.</dl>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h3>globus_result_t globus_ftp_client_handleattr_copy (<code>globus_ftp_client_handleattr_t</code> *dest, <code>globus_ftp_client_handleattr_t</code> *src)</h3>
<p> Create a duplicate of a handle attribute set. </p>
<p> The duplicated attribute set has a deep copy of all data in the attribute set, so the original may be destroyed while the copy is still valid. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dest</i> The attribute set to be initialized to the same values as src.<br />
 <i>src</i> The original attribute set to duplicate.</dl>
<h3>globus_result_t globus_ftp_client_handleattr_destroy (<code>globus_ftp_client_handleattr_t</code> *attr)</h3>
<p> Destroy an FTP client handle attribute set. </p>
<p> This function destroys an ftp client handle attribute set. All attributes on this set will be lost. The user must call <code>globus_ftp_client_handleattr_init()</code> again on this attribute set before calling any other handle attribute functions on it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to destroy.</dl>
<h3>globus_result_t globus_ftp_client_handleattr_init (<code>globus_ftp_client_handleattr_t</code> *attr)</h3>
<p> Initialize an FTP client handle attribute set. </p>
<p> This function creates an empty FTP Client handle attribute set. This function must be called on each attribute set before any of the other functions in this section may be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The new handle attribute.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handleattr_destroy()</code></dl>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h3>globus_result_t globus_ftp_client_handleattr_set_cache_all (<code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_tcache_all)</h3>
<p> Set/Get the cache all connections attribute for an ftp client handle attribute set. </p>
<p> This attribute allows the user to cause all control connections to be cached between ftp operations. When this is enabled, the user skips the authentication handshake and connection establishment overhead for multiple subsequent ftp operations to the same server. </p>
<p> Memory and network connections associated with the caching will be used until the handle is destroyed. If fine grained caching is needed, then the user should disable this attribute and explicitly cache specific URLs. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute to query or modify.<br />
 <i>cache_all</i> Value of the cache_all attribute.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handleattr_add_cached_url()</code>, globus_ftp_client_handleattr_remove_cached_url(), <code>globus_ftp_client_handle_cache_url_state()</code> <code>globus_ftp_client_handle_flush_url_state()</code></dl>
<h3>globus_result_t globus_ftp_client_handleattr_set_clientinfo (<code>globus_ftp_client_handleattr_t</code> *attr, const char *app_name, const char *app_version, const char *other)</h3>
<p> Set/Get client info reported to server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute to modify<br />
 <i>app_name</i> Name of client application.<br />
 <i>app_version</i> Client application specific version string.<br />
 <i>other</i> Additional client info to be reported to the server. This may be used to pass custom info to a custom server module. The format of the string must be: key1=&#8217;value1&#8242;;key2=&#8217;value2&#8242;;[keyn=&#8217;valuen&#8217;;]</dl>
<p> Any parameter may be NULL. By default, generic library info will be reported to the server &#8212; set all NULL to disable this.</p>
<h3>globus_result_t globus_ftp_client_handleattr_set_gridftp2 (<code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_tgridftp2)</h3>
<p> Enable/Disable GridFTP2 [GFD.41] support for servers supporting it. This currently only applies to the GET/PUT command. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute to modify<br />
 <i>gridftp2</i> Set to GLOBUS_FALSE to disable GridFTP2 support. GridFTP2 support is enabled by default for servers that support it.</dl>
<h3>globus_result_t globus_ftp_client_handleattr_set_netlogger (<code>globus_ftp_client_handleattr_t</code> *attr, globus_netlogger_handle_t *nl_handle)</h3>
<p> Set the netlogger handle used with this transfer. </p>
<p> Each handle can have a netlogger handle associated with it for logging its data. </p>
<p> Only 1 netlogger handle can be associated with a client handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to modify.<br />
 <i>nl_handle</i> The open netlogger handle to be associated with this attribute set.</dl>
<h3>globus_result_t globus_ftp_client_handleattr_set_pipeline (<code>globus_ftp_client_handleattr_t</code> *attr, globus_size_toutstanding_commands, globus_ftp_client_pipeline_callback_tpipeline_callback, void *pipeline_arg)</h3>
<p> Enable/Disable command queueing for pipelined transfers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute to modify<br />
 <i>outstanding_commands</i> Set to the number of commands to have sent without receiving a reply. Use 0 for the library default.<br />
 <i>pipeline_callback</i> Set to a function of type globus_ftp_client_pipeline_callback_t to enable command pipelining. This function will be called during a transfer operation to request the next urls to be transferred.<br />
 <i>pipeline_arg</i> User data that will be passed in the pipeline_callback.</dl>
<h3>globus_result_t globus_ftp_client_handleattr_set_rfc1738_url (<code>globus_ftp_client_handleattr_t</code> *attr, globus_bool_trfc1738_url)</h3>
<p> Enable/Disable rfc1738 support for non-root relative URLs. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute to modify<br />
 <i>rfc1738_url</i> Set to GLOBUS_TRUE to enable non-root relative URLs. Default of GLOBUS_FALSE specifies root-relative URLs.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAS">Function Documentation</a></p>
<dd>
<dt><a href="#lbBE">Author</a></p>
<dd></dl>
