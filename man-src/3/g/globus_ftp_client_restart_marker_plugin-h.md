---
title: "globus_ftp_client_restart_marker_plugin-h(3)"
name: "globus_ftp_client_restart_marker_plugin-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_restart_marker_plugin-h/"
description: "globus_ftp_client_restart_marker_plugin.h –"
---

<p>globus_ftp_client_restart_marker_plugin.h &#8211; </p>
<p> GridFTP Restart Marker Plugin Implementation.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_ftp_client.h&#8217;<br />
 #include &#8216;globus_ftp_client_plugin.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_FTP_CLIENT_RESTART_MARKER_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_restart_marker_plugin_module) </p>
<h3>Typedefs</h3>
<p>typedef globus_bool_t(* <code>globus_ftp_client_restart_marker_plugin_begin_cb_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, <code>globus_ftp_client_restart_marker_t</code> *user_saved_marker)<br />
 <i>Transfer begin callback. </i><br />
 typedef void(* <code>globus_ftp_client_restart_marker_plugin_marker_cb_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_restart_marker_t</code> *marker) </p>
<p> typedef void(* <code>globus_ftp_client_restart_marker_plugin_complete_cb_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, const char *error_url) </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_ftp_client_restart_marker_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_restart_marker_plugin_begin_cb_t</code> begin_cb, <code>globus_ftp_client_restart_marker_plugin_marker_cb_t</code> marker_cb, <code>globus_ftp_client_restart_marker_plugin_complete_cb_t</code> complete_cb, void *user_arg) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<h2>Detailed Description</h2>
<p>GridFTP Restart Marker Plugin Implementation. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_ftp_client from the source code.</p>
