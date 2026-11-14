---
title: "globus_ftp_client_debug_plugin_init(3)"
name: "globus_ftp_client_debug_plugin_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_debug_plugin_init/"
description: "Debugging Plugin –"
---

<h2 class="name">NAME</h2>
<p> Debugging Plugin &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_FTP_CLIENT_DEBUG_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_debug_plugin_module) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_debug_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, FILE *stream, const char *text) </p>
<p> globus_result_t <code>globus_ftp_client_debug_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<h2>Detailed Description</h2>
<p> The FTP Debugging plugin provides a way for the user to trace FTP protocol messages which occur while the GridFTP client library processes an FTP operation. This may be useful for debugging FTP configuration problems. </p>
<p> When this plugin is used for a GridFTP Client operation, information will be printed to the file stream associated with the plugin when a user begins an operation, for all data buffers which pass through while handling a data transfer, and for all protocol messages which are sent and received.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_FTP_CLIENT_DEBUG_PLUGIN_MODULE (&amp;globus_i_ftp_client_debug_plugin_module)</h3>
<p> Module descriptor </p>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_debug_plugin_destroy (<code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Destroy an instance of the GridFTP debugging plugin </p>
<p> This function will free all debugging plugin-specific instance data from this plugin, and will make the plugin unusable for further ftp handle creation. </p>
<p> Existing FTP client handles and handle attributes will not be affected by destroying a plugin associated with them, as a local copy of the plugin is made upon handle initialization. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> A pointer to a GridFTP debugging plugin, previously initialized by calling <code>globus_ftp_client_debug_plugin_init()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error if</p>
<dl>
<dt>&bull;</p>
<dd> plugin is null</p>
<dt>&bull;</p>
<dd> plugin is not a debugging plugin</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_debug_plugin_init()</code>, <code>globus_ftp_client_handleattr_add_plugin()</code>, globus_ftp_client_handleattr_remove_plugin(), <code>globus_ftp_client_handle_init()</code></dl>
<h3>globus_result_t globus_ftp_client_debug_plugin_init (<code>globus_ftp_client_plugin_t</code> *plugin, FILE *stream, const char *text)</h3>
<p> Initialize an instance of the GridFTP debugging plugin </p>
<p> This function will initialize the debugging plugin-specific instance data for this plugin, and will make the plugin usable for ftp client handle attribute and handle creation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> A pointer to an uninitialized plugin. The plugin will be configured as a debugging plugin, with the default of sending debugging messages to stderr.<br />
 <i>stream</i><br />
 <i>text</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error if</p>
<dl>
<dt>&bull;</p>
<dd> plugin is null</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_debug_plugin_destroy()</code>, <code>globus_ftp_client_handleattr_add_plugin()</code>, globus_ftp_client_handleattr_remove_plugin(), <code>globus_ftp_client_handle_init()</code></dl>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
