---
title: "edg-gridftp-mkdir(1)"
name: "edg-gridftp-mkdir"
section: "1"
letter: "e"
url: "/docs/linux/man/1-edg-gridftp-mkdir/"
description: "edg-gridftp-mkdir – Create a directory on a GridFTP server."
---

<h2 class="name">NAME</h2>
<p> edg-gridftp-mkdir &#8211; Create a directory on a GridFTP server. </p>
<h2>SYNOPSIS</h2>
<p> edg-gridftp-mkdir [<code>&#8211;proxy</code>=<i>proxy</i>] [<code>&#8211;timeout</code>=<i>timeout</i>] [<code>&#8211;parents</code>] <i></i><font SIZE="-1"><i>URL</i></font><i></i> [<i></i><font SIZE="-1"><i>URL</i></font><i></i> &#8230;] </p>
<p> edg-gridftp-mkdir <code>&#8211;usage</code> </p>
<p> edg-gridftp-mkdir <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>edg-gridftp-mkdir</code> creates a directory on a GridFTP server. This command will return a status of 0 if the directory was created successfully. In all other cases, it will return a non-zero value and print an error message to the standard error. </p>
<p> If the <code>&#8211;parents</code> option is given any parent directories of the given <font SIZE="-1">URL</font> will also be created. </p>
<p> If more than one <font SIZE="-1">URL</font> is given, then the URLs are processed sequentially. The processing will stop with the first failure. </p>
<p> <font SIZE="-1">NOTE:</font> The creation is only attempted if the <font SIZE="-1">URL</font> does not already exist. If the given file is a regular file, this command will return success.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;proxy</code>=<i>proxy</i></p>
<dd> Set the proxy to use for the GridFTP operation. If this is unset, then the underlying GridFTP library will try to find the proxy in the usual locations. This is useful if the proxy is in a non-standard location, or the caller is a daemon which must act on the behalf of a user.</p>
<dt><code>&#8211;timeout</code>=<i>timeout</i></p>
<dd> Set the overall time (in seconds) within which all the directory creations must complete. If no timeout is specified a default 120 second timeout will be used. A negative or zero timeout will report a timeout error before attempting to contact any of the <font SIZE="-1">FTP</font> servers. If an operation times out some directories may have already been created and will remain.</p>
<dt><code>&#8211;parents</code></p>
<dd> If this option is given, then any parent directories which do not already exist will also be created. Note that internally the <font SIZE="-1">URL</font> list is just expanded to include the parent URLs in the processing list. If an error occurs, it is possible that a partial path was created.</p>
<dt><code>&#8211;usage</code></p>
<dd> Short description of the usage of this command is given.</p>
<dt><code>&#8211;help</code></p>
<dd> A description of the usage of this command and information on all of the options is given.</p>
<dt><i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> URLs of the following formats are accepted: </p>
<p> <a href="ftp://ftp.server.org//absolute/file/name">ftp://ftp.server.org//absolute/file/name</a> <a href="gsiftp://gridftp.server.org/~/home/relative/dirname">gsiftp://gridftp.server.org/~/home/relative/dirname</a> gridftp://grid<a href="ftp://ftp.server.org">ftp.server.org</a>/home/relative/dirname </p>
<p> Note: for the URLs without a tilde, the server configuration determines whether the filename is absolute or relative. On servers which do not restrict users to their home areas, the tilde notation will not work.</dl>
<h2>AUTHOR</h2>
<p> Charles Loomis (charles.loomis [at] cern.ch). Later modifications by <font SIZE="-1">CERN IT-DM/SMD.</font></p>
<h2>LICENSE</h2>
<p> Copyright (c) 2002 by Charles A. Loomis, Jr. and Le Centre National de la Recherche Scientifique (<font SIZE="-1">CNRS</font>). All rights reserved. </p>
<p> The software was distributed with and is covered by the European DataGrid License. A copy of this license can be found in the included <font SIZE="-1">LICENSE</font> file. This license can also be obtained from <a rel="nofollow" href="http://www.eu-datagrid.org/license.">http://www.eu-datagrid.org/license.</a> </p>
<p> The underlying GridFTP library is part of the Globus Toolkit (<font SIZE="-1">TM</font>) and is covered by the Globus Toolkit Public License. See <a rel="nofollow" href="http://www.globus.org">http://www.globus.org</a> for more information. </p>
<h2>Index</h2>
