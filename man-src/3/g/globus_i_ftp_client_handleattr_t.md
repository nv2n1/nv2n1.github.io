---
title: "globus_i_ftp_client_handleattr_t(3)"
name: "globus_i_ftp_client_handleattr_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_handleattr_t/"
description: "globus_i_ftp_client_handleattr_t –"
---

<h2 class="name">NAME</h2>
<p> globus_i_ftp_client_handleattr_t &#8211; </p>
<p> Handle attributes.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_i_ftp_client.h&gt;</p>
<h3>Data Fields</h3>
<p> globus_bool_t <code>cache_all</code> </p>
<p> globus_bool_t <code>rfc1738_url</code> </p>
<p> globus_bool_t <code>gridftp2</code> </p>
<p> globus_list_t * <code>url_cache</code> </p>
<p> globus_list_t * <code>plugins</code> </p>
<h2>Detailed Description</h2>
<p> Handle attributes. </p>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h2>Field Documentation</h2>
<h3>globus_bool_t globus_i_ftp_client_handleattr_t::cache_all</h3>
<p> Cache all connections. </p>
<p> This attribute is used to cause the ftp client library to keep all control (and where possible) data connections open between ftp operations.</p>
<h3>globus_bool_t globus_i_ftp_client_handleattr_t::gridftp2</h3>
<p> Use GRIDFTP2 if supported by the server</p>
<h3>globus_list_t* globus_i_ftp_client_handleattr_t::plugins</h3>
<p> List of plugin structures. </p>
<p> This list contains all plugins which can be associated with an ftp client handle. These plugins will be notified when operations are done using a handle associated with them.</p>
<h3>globus_bool_t globus_i_ftp_client_handleattr_t::rfc1738_url</h3>
<p> parse all URLs for caching with RFC1738 compliant parser</p>
<h3>globus_list_t* globus_i_ftp_client_handleattr_t::url_cache</h3>
<p> List of cached URLs. </p>
<p> This list is used to manage the URL cache which is manipulated by the user calling <code>globus_ftp_client_handle_cache_url_state()</code> and <code>globus_ftp_client_handle_flush_url_state()</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
