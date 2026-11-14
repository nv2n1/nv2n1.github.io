---
title: "globus_i_ftp_client_cache_entry_t(3)"
name: "globus_i_ftp_client_cache_entry_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_cache_entry_t/"
description: "globus_i_ftp_client_cache_entry_t –"
---

<h2 class="name">NAME</h2>
<p> globus_i_ftp_client_cache_entry_t &#8211; </p>
<p> URL caching support structure.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_i_ftp_client.h&gt;</p>
<h3>Data Fields</h3>
<p> globus_url_t <code>url</code> </p>
<p> <code>globus_i_ftp_client_target_t</code> * <code>target</code> </p>
<h2>Detailed Description</h2>
<p> URL caching support structure. </p>
<p> This structure is used to implement the cache of URLs. When a target is needed, the client library first checks the handle&#8217;s cache. If the target associated with the url is available, and it matches the security attributes of the operation being performed, it will be used for the operation. </p>
<p> The current implementation only allows for a URL to be cached only once per handle. </p>
<p> The cache manipulations are done by the API functions globus_ftp_client_cache_url_state() and globus_ftp_client_flush_url_state(), and the internal functions globus_i_ftp_client_target_find() and globus_i_ftp_client_target_release().</p>
<h2>Field Documentation</h2>
<h3><code>globus_i_ftp_client_target_t</code>* globus_i_ftp_client_cache_entry_t::target</h3>
<p> Target which matches that URL. If this is NULL, then the cache entry is empty.</p>
<h3>globus_url_t globus_i_ftp_client_cache_entry_t::url</h3>
<p> URL which the user has requested to be cached. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
