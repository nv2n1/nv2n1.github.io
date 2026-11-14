---
title: "globus_ftp_client_restart_plugin-h(3)"
name: "globus_ftp_client_restart_plugin-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_restart_plugin-h/"
description: "globus_ftp_client_restart_plugin.h –"
---

<p>globus_ftp_client_restart_plugin.h &#8211; </p>
<p> GridFTP Restart Plugin Implementation.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_ftp_client.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_FTP_CLIENT_RESTART_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_restart_plugin_module) </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_ftp_client_restart_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, int max_retries, globus_reltime_t *interval, globus_abstime_t *deadline) </p>
<p> globus_result_t <code>globus_ftp_client_restart_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<h2>Detailed Description</h2>
<p>GridFTP Restart Plugin Implementation. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_ftp_client from the source code.</p>
