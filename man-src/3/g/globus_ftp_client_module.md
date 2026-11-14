---
title: "globus_ftp_client_module(3)"
name: "globus_ftp_client_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_module/"
description: "Activation –"
---

<p>Activation &#8211; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_FTP_CLIENT_MODULE</code> </p>
<h2>Detailed Description</h2>
<p>The Globus FTP Client library uses the standard module activation and deactivation API to initialize its state. Before any FTP functions are called, the module must be activated </p>
<pre>globus_module_activate(GLOBUS_FTP_CLIENT_MODULE);</pre>
<p>This function returns GLOBUS_SUCCESS if the FTP library was successfully initialized. This may be called multiple times. </p>
<p> To deactivate the FTP library, the following must be called </p>
<pre>globus_module_deactivate(GLOBUS_FTP_CLIENT_MODULE);</pre>
<p>&nbsp;<wbr></p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_FTP_CLIENT_MODULE</h3>
<p>Module descriptor </p>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_ftp_client from the source code.</p>
