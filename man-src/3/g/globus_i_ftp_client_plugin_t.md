---
title: "globus_i_ftp_client_plugin_t(3)"
name: "globus_i_ftp_client_plugin_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_plugin_t/"
description: "globus_i_ftp_client_plugin_t –"
---

<h2 class="name">NAME</h2>
<p> globus_i_ftp_client_plugin_t &#8211; </p>
<p> FTP Client Plugin. </p>
<p> Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_i_ftp_client.h&gt;</p>
<h3>Data Fields</h3>
<p> char * <code>plugin_name</code> </p>
<p> <code>globus_ftp_client_plugin_t</code> * <code>plugin</code> </p>
<p> <code>globus_ftp_client_plugin_copy_t</code> <code>copy_func</code> </p>
<p> <code>globus_ftp_client_plugin_destroy_t</code> <code>destroy_func</code> </p>
<p> <code>globus_ftp_client_plugin_command_mask_t</code> <code>command_mask</code> </p>
<p> void * <code>plugin_specific</code> </p>
<h2>Detailed Description</h2>
<p> FTP Client Plugin. </p>
<p> Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes. </p>
<p> Each plugin function may be either GLOBUS_NULL, or a valid function pointer. If the function is GLOBUS_NULL, then the plugin will not be notified when the corresponding event happens. </p>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h2>Field Documentation</h2>
<h3><code>globus_ftp_client_plugin_command_mask_t</code> globus_i_ftp_client_plugin_t::command_mask</h3>
<p> Command Mask </p>
<p> The bits set in this mask determine which command responses the plugin is interested in. The command_mask should be a bitwise-or of the values in the globus_ftp_client_plugin_command_mask_t enumeration.</p>
<h3><code>globus_ftp_client_plugin_copy_t</code> globus_i_ftp_client_plugin_t::copy_func</h3>
<p> Plugin function pointers.</p>
<h3><code>globus_ftp_client_plugin_destroy_t</code> globus_i_ftp_client_plugin_t::destroy_func</h3>
<p> Plugin function pointers.</p>
<h3><code>globus_ftp_client_plugin_t</code>* globus_i_ftp_client_plugin_t::plugin</h3>
<p> The value the user/plugin implementation passed into the plugin handling parts of the API.</p>
<h3>char* globus_i_ftp_client_plugin_t::plugin_name</h3>
<p> Plugin name. </p>
<p> The plugin name is used by the FTP Client library to detect multiple instances of the same plugin being associated with a <code>globus_ftp_client_handleattr_t</code> or <code>globus_ftp_client_handle_t</code>. </p>
<p> Each plugin type should have a unique plugin name, which must be a NULL-terminated string of arbitrary length.</p>
<h3>void* globus_i_ftp_client_plugin_t::plugin_specific</h3>
<p> This pointer is reserved for plugin-specific data </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
