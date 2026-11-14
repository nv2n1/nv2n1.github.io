---
title: "globus_i_ftp_client_range_t(3)"
name: "globus_i_ftp_client_range_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_range_t/"
description: "globus_i_ftp_client_range_t –"
---

<h2 class="name">NAME</h2>
<p> globus_i_ftp_client_range_t &#8211; </p>
<p> Byte range report. </p>
<p> This structure contains information about a single extent of data stored on an FTP server. A report structure is generated from each part of an extended-block mode restart marker message from an FTP server.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_i_ftp_client.h&gt;</p>
<h3>Data Fields</h3>
<p> globus_off_t <code>offset</code> </p>
<p> globus_off_t <code>end_offset</code> </p>
<h2>Detailed Description</h2>
<p> Byte range report. </p>
<p> This structure contains information about a single extent of data stored on an FTP server. A report structure is generated from each part of an extended-block mode restart marker message from an FTP server.</p>
<h2>Field Documentation</h2>
<h3>globus_off_t globus_i_ftp_client_range_t::end_offset</h3>
<p> Maximum value of this range.</p>
<h3>globus_off_t globus_i_ftp_client_range_t::offset</h3>
<p> Minimum value of this range. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
