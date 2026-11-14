---
title: "edg-gridftp-rmdir(1)"
name: "edg-gridftp-rmdir"
section: "1"
letter: "e"
url: "/docs/linux/man/1-edg-gridftp-rmdir/"
description: "edg-gridftp-rmdir – Remove a directory on a GridFTP server."
---

<h2 class="name">NAME</h2>
<p> edg-gridftp-rmdir &#8211; Remove a directory on a GridFTP server. </p>
<h2>SYNOPSIS</h2>
<p> edg-gridftp-rmdir [<code>&#8211;proxy</code>=<i>proxy</i>] [<code>&#8211;timeout</code>=<i>timeout</i>] <i></i><font SIZE="-1"><i>URL</i></font><i></i> [<i></i><font SIZE="-1"><i>URL</i></font><i></i> &#8230;] </p>
<p> edg-gridftp-rmdir <code>&#8211;usage</code> </p>
<p> edg-gridftp-rmdir <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>edg-gridftp-rmdir</code> removes the directory from a GridFTP server. This command will return a status of 0 if the directory was successfully removed. In all other cases, it will return a non-zero value and print an error message to the standard error. </p>
<p> If more than one <font SIZE="-1">URL</font> is given, then a successful return will only occur if all of the URLs were successfully deleted. The processing will stop with the first failure.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;proxy</code>=<i>proxy</i></p>
<dd> Set the proxy to use for the GridFTP operation. If this is unset, then the underlying GridFTP library will try to find the proxy in the usual locations. This is useful if the proxy is in a non-standard location, or the caller is a daemon which must act on the behalf of a user.</p>
<dt><code>&#8211;timeout</code>=<i>timeout</i></p>
<dd> Set the overall time (in seconds) within which all the directory removals must complete. If no timeout is specified a default 120 second timeout will be used. A negative or zero timeout will report a timeout error before attempting to contact any of the <font SIZE="-1">FTP</font> servers. If a timeout error does happen then some of the directories may already have been removed.</p>
<dt><code>&#8211;usage</code></p>
<dd> Short description of the usage of this command is given.</p>
<dt><code>&#8211;help</code></p>
<dd> A description of the usage of this command and information on all of the options is given.</p>
<dt><i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> URLs of the following formats are accepted: </p>
<p> <a href="ftp://ftp.server.org//absolute/file/name">ftp://ftp.server.org//absolute/file/name</a> <a href="gsiftp://gridftp.server.org/~/home/relative/name.txt">gsiftp://gridftp.server.org/~/home/relative/name.txt</a> gridftp://grid<a href="ftp://ftp.server.org">ftp.server.org</a>/home/relative/name.txt </p>
<p> Note: for the URLs without a tilde, the server configuration determines whether the filename is absolute or relative. On servers which do not restrict users to their home areas, the tilde notation will not work.</dl>
<h2>AUTHOR</h2>
<p> Charles Loomis (charles.loomis [at] cern.ch). Later modifications by <font SIZE="-1">CERN IT-DM/SMD.</font></p>
<h2>LICENSE</h2>
<p> Copyright (c) 2002 by Charles A. Loomis, Jr. and Le Centre National de la Recherche Scientifique (<font SIZE="-1">CNRS</font>). All rights reserved. </p>
<p> The software was distributed with and is covered by the European DataGrid License. A copy of this license can be found in the included <font SIZE="-1">LICENSE</font> file. This license can also be obtained from <a rel="nofollow" href="http://www.eu-datagrid.org/license.">http://www.eu-datagrid.org/license.</a> </p>
<p> The underlying GridFTP library is part of the Globus Toolkit (<font SIZE="-1">TM</font>) and is covered by the Globus Toolkit Public License. See <a rel="nofollow" href="http://www.globus.org">http://www.globus.org</a> for more information. </p>
<h2>Index</h2>
