---
title: "globus_ftp_client_throughput_plugin-h(3)"
name: "globus_ftp_client_throughput_plugin-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_throughput_plugin-h/"
description: "globus_ftp_client_throughput_plugin.h –"
---

<p>globus_ftp_client_throughput_plugin.h &#8211; </p>
<p> GridFTP Throughput Performance Plugin Implementation.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_ftp_client.h&#8217;<br />
 #include &#8216;globus_ftp_client_plugin.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_FTP_CLIENT_THROUGHPUT_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_throughput_plugin_module) </p>
<h3>Typedefs</h3>
<p>typedef void(* <code>globus_ftp_client_throughput_plugin_begin_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, int stripe_ndx, globus_off_t bytes, float instantaneous_throughput, float avg_throughput) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_total_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_off_t bytes, float instantaneous_throughput, float avg_throughput) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_complete_cb_t</code> )(void *user_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_bool_t success) </p>
<p> typedef void *(* <code>globus_ftp_client_throughput_plugin_user_copy_cb_t</code> )(void *user_specific) </p>
<p> typedef void(* <code>globus_ftp_client_throughput_plugin_user_destroy_cb_t</code> )(void *user_specific) </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_ftp_client_throughput_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_begin_cb_t</code> begin_cb, <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code> per_stripe_cb, <code>globus_ftp_client_throughput_plugin_total_cb_t</code> total_cb, <code>globus_ftp_client_throughput_plugin_complete_cb_t</code> complete_cb, void *user_specific) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_plugin_set_copy_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_user_copy_cb_t</code> copy_cb, <code>globus_ftp_client_throughput_plugin_user_destroy_cb_t</code> destroy_cb) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_plugin_get_user_specific</code> (<code>globus_ftp_client_plugin_t</code> *plugin, void **user_specific) </p>
<h2>Detailed Description</h2>
<p>GridFTP Throughput Performance Plugin Implementation. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_ftp_client from the source code.</p>
