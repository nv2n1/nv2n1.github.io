---
title: "globus_i_ftp_client_data_target_t(3)"
name: "globus_i_ftp_client_data_target_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_data_target_t/"
description: "globus_i_ftp_client_data_target_t –"
---

<h2 class="name">NAME</h2>
<p> globus_i_ftp_client_data_target_t &#8211; </p>
<p> Data connection caching information.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_i_ftp_client.h&gt;</p>
<h3>Data Fields</h3>
<p> struct<br />
 <code>globus_i_ftp_client_target_s</code> * <code>source</code>&quot; </p>
<p> struct<br />
 <code>globus_i_ftp_client_target_s</code> * <code>dest</code>&quot; </p>
<p> globus_i_ftp_client_operation_t <code>operation</code> </p>
<h2>Detailed Description</h2>
<p> Data connection caching information.</p>
<h2>Field Documentation</h2>
<h3>struct <code>globus_i_ftp_client_target_s</code>* globus_i_ftp_client_data_target_t::dest</h3>
<p> A pointer to the source of whatever FTP operation this data channel was last used on.</p>
<h3>globus_i_ftp_client_operation_t globus_i_ftp_client_data_target_t::operation</h3>
<p> The type of operation which this data channel was used for.</p>
<h3>struct <code>globus_i_ftp_client_target_s</code>* globus_i_ftp_client_data_target_t::source</h3>
<p> A pointer to the source of whatever FTP operation this data channel was last used on. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
