---
title: "globus_ftp_client_restart_plugin_init(3)"
name: "globus_ftp_client_restart_plugin_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_restart_plugin_init/"
description: "Restart Plugin –"
---

<h2 class="name">NAME</h2>
<p> Restart Plugin &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_FTP_CLIENT_RESTART_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_restart_plugin_module) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_restart_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, int max_retries, globus_reltime_t *interval, globus_abstime_t *deadline) </p>
<p> globus_result_t <code>globus_ftp_client_restart_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<h2>Detailed Description</h2>
<p> The restart plugin implements one scheme for providing reliability functionality for the FTP Client library. Other plugins may be developed to provide other methods of reliability. </p>
<p> The specific functionality of this plugin is to restart any FTP operation when a fault occurs. The plugin&#8217;s operation is parameterized to control how often and when to attempt to restart the operation. </p>
<p> This restart plugin will restart an FTP operation if a noticeable fault has occurred&#8212;a connection timing out, a failure by the server to process a command, a protocol error, an authentication error. </p>
<p> This plugin has three user-configurable parameters; these are the maximum number of retries to attempt, the interval to wait between retries, and the deadline after which no further retries will be attempted. These are set by initializing a restart plugin instance with the function <code>globus_ftp_client_restart_plugin_init()</code>.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_FTP_CLIENT_RESTART_PLUGIN_MODULE (&amp;globus_i_ftp_client_restart_plugin_module)</h3>
<p> Module descriptor </p>
<p> <code>Examples: </code> <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_restart_plugin_destroy (<code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Destroy an instance of the GridFTP restart plugin </p>
<p> This function will free all restart plugin-specific instance data from this plugin, and will make the plugin unusable for further ftp handle creation. </p>
<p> Existing FTP client handles and handle attributes will not be affected by destroying a plugin associated with them, as a local copy of the plugin is made upon handle initialization. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> A pointer to a GridFTP restart plugin, previously initialized by calling <code>globus_ftp_client_restart_plugin_init()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error if</p>
<dl>
<dt>&bull;</p>
<dd> plugin is null</p>
<dt>&bull;</p>
<dd> plugin is not a restart plugin</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_restart_plugin_init()</code>, <code>globus_ftp_client_handleattr_add_plugin()</code>, globus_ftp_client_handleattr_remove_plugin(), <code>globus_ftp_client_handle_init()</code></dl>
<h3>globus_result_t globus_ftp_client_restart_plugin_init (<code>globus_ftp_client_plugin_t</code> *plugin, intmax_retries, globus_reltime_t *interval, globus_abstime_t *deadline)</h3>
<p> Initialize an instance of the GridFTP restart plugin </p>
<p> This function will initialize the plugin-specific instance data for this plugin, and will make the plugin usable for ftp client handle attribute and handle creation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> A pointer to an uninitialized plugin. The plugin will be configured as a restart plugin.<br />
 <i>max_retries</i> The maximum number of times to retry the operation before giving up on the transfer. If this value is less than or equal to 0, then the restart plugin will keep trying to restart the operation until it completes or the deadline is reached with an unsuccessful operation.<br />
 <i>interval</i> The interval to wait after a failures before retrying the transfer. If the interval is 0 seconds or GLOBUS_NULL, then an exponential backoff will be used.<br />
 <i>deadline</i> An absolute timeout. If the deadline is GLOBUS_NULL then the retry will never timeout.</dl>
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
<dd> <code>globus_ftp_client_restart_plugin_destroy()</code>, <code>globus_ftp_client_handleattr_add_plugin()</code>, globus_ftp_client_handleattr_remove_plugin(), <code>globus_ftp_client_handle_init()</code></dl>
<p> <code>Examples: </code> <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
