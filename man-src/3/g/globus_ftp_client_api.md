---
title: "globus_ftp_client_api(3)"
name: "globus_ftp_client_api"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_api/"
description: "Globus FTP Client API –"
---

<h2 class="name">NAME</h2>
<p> Globus FTP Client API &#8211; </p>
<h3>Modules</h3>
<p> <code>Activation</code> </p>
<p> <code>Restart Markers</code> </p>
<p> <code>Handle Management</code> </p>
<p> <code>Handle Attributes</code> </p>
<p> <code>FTP Operations</code> </p>
<p> <code>FTP Operation Attributes</code> </p>
<p> <code>Reading and Writing Data</code> </p>
<p> <code>Plugins</code><br />
 <i>Plugin API. </i></p>
<h2>Detailed Description</h2>
<p> The Globus FTP Client library provides a convenient way of accessing files on remote FTP servers. In addition to supporting the basic FTP protocol, the FTP Client library supports several security and performance extensions to make FTP more suitable for Grid applications. These extensions are described in the Grid FTP Protocol document. </p>
<p> In addition to protocol support for grid applications, the FTP Client library provides a <code>plugin architecture </code> for installing application or grid-specific fault recovery and performance tuning algorithms within the library. Application writers may then target their code toward the FTP Client library, and by simply enabling the appropriate plugins, easily tune their application to run it on a different grid. </p>
<p> All applications which use the Globus FTP Client API must include the header file <code>globus_ftp_client.h</code> and activate the GLOBUS_FTP_CLIENT_MODULE </p>
<p> To use the Globus FTP Client API, one must create an <code>FTP Client handle </code>. This structure contains context information about FTP operations which are being executed, a cache of FTP control and data connections, and information about plugins which are being used. The specifics of the connection caching and plugins are found in the <code>Handle Attributes</code> section of this manual. </p>
<p> Once the handle is created, one may begin transferring files or doing other FTP operations by calling the functions in the <code>FTP Operations</code> section of this manual. In addition to whole-file transfers, the API supports partial file transfers, restarting transfers from a known point, and various FTP directory management commands. All FTP operations may have a set of attributes, defined in the <code>FTP Operation Attributes</code> section, associated with them to tune various FTP parameters. The data structures and functions needed to restart a file transfer are described in the <code>Restart Markers</code> section of this manual. For operations which require the user to send to or receive data from an FTP server the must call the functions in the <code>Reading and Writing Data</code> section of the manual.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
