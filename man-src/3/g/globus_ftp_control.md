---
title: "globus_ftp_control(3)"
name: "globus_ftp_control"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_control/"
description: "GridFTP Control API –"
---

<h2 class="name">NAME</h2>
<p> GridFTP Control API &#8211; </p>
<p> GridFTP Control API.</p>
<h3>Modules</h3>
<p> <code>GridFTP Constants</code><br />
 <i>Constants. </i><br />
 <code>GridFTP Server Control</code><br />
 <i>Manage GridFTP Server Control Connections. </i><br />
 <code>GridFTP Control Client</code><br />
 <i>Control Client. </i><br />
 <code>GridFTP Data Connections</code><br />
 <i>Data Connections. </i></p>
<h2>Detailed Description</h2>
<p> GridFTP Control API. </p>
<p> The globus_ftp_control library provides low-level services needed to implement FTP client and servers. The API provided is protocol specific. See the GASS Transfer library for a protocol-independent transfer interface. </p>
<p> This data transfer portion of this API provides support for the standard data methods described in the <code>FTP Specification</code> as well as <code>extensions</code> for parallel, striped, and partial data transfer. </p>
<p> Any program that uses the GridFTP Control Library must include the <code>globus_ftp_control.h</code> header. </p>
<p> The API documentation is organized into several sections</p>
<dl>
<dt>&bull;</p>
<dd> <code>GridFTP Server Control</code></p>
<dt>&bull;</p>
<dd> <code>GridFTP Control Client</code></p>
<dt>&bull;</p>
<dd> <code>GridFTP Data Connections</code></p>
<dt>&bull;</p>
<dd> <code>GridFTP Constants</code></dl>
<p> The Globus FTP Control library uses the standard module activation and deactivation API to initialize it&#8217;s state. Before any GridFTP functions are called, the module must be activated </p>
<pre>
globus_module_activate(GLOBUS_FTP_CONTROL_MODULE);
</pre>
<p> This function returns GLOBUS_SUCCESS if the GridFTP library was successfully initialized. This may be called multiple times. </p>
<p> To deactivate the GridFTP library, the following must be called </p>
<pre>
globus_module_deactivate(GLOBUS_FTP_CONTROL_MODULE);
</pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_control from the source code. </p>
<h2>Index</h2>
