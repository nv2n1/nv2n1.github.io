---
title: "globus_ftp_client_throughput_nl_plugin-h(3)"
name: "globus_ftp_client_throughput_nl_plugin-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_throughput_nl_plugin-h/"
description: "globus_ftp_client_throughput_nl_plugin.h –"
---

<p>globus_ftp_client_throughput_nl_plugin.h &#8211; </p>
<p> GridFTP Netlogger Throughput Plugin.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_ftp_client.h&#8217;<br />
 #include &#8216;globus_ftp_client_plugin.h&#8217;<br />
 #include &#8216;globus_ftp_client_throughput_plugin.h&#8217;<br />
 #include &#8216;NetLogger.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_FTP_CLIENT_THROUGHPUT_NL_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_throughput_nl_plugin_module) </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_ftp_client_throughput_nl_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, const char *nl_url, const char *prog_name, const char *opaque_string) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_nl_plugin_init_with_handle</code> (<code>globus_ftp_client_plugin_t</code> *plugin, NLhandle *nl_handle, const char *opaque_string) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_nl_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_nl_plugin_set_callbacks</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_begin_cb_t</code> begin_cb, <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code> per_stripe_cb, <code>globus_ftp_client_throughput_plugin_total_cb_t</code> total_cb, <code>globus_ftp_client_throughput_plugin_complete_cb_t</code> complete_cb, void *user_specific) </p>
<h2>Detailed Description</h2>
<p>GridFTP Netlogger Throughput Plugin. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_ftp_client from the source code.</p>
