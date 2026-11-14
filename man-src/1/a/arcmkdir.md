---
title: "arcmkdir(1)"
name: "arcmkdir"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcmkdir/"
description: "arcmkdir – create directories"
---

<h2 class="name">NAME</h2>
<p> arcmkdir &#8211; create directories</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcmkdir</code> command creates directories on grid storage elements and indexing services. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcmkdir [options] url</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;parents</code></p>
<dd> make parent directories as needed</p>
<dt><code>-P</code>, <code>&#8211;listplugins</code></p>
<dd> list the available plugins (protocols supported)</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> timeout in seconds (default 20)</p>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></p>
<dd> configuration file (default ~/.arc/client.conf)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> print help </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>url</code></p>
<dd> the directory to create</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arcmkdir</code> command creates directories on grid storage elements and indexing services. If the parent directory does not exist and <code>-p</code> is not specified, then arcmkdir will probably fail, but it depends on the protocol. The permissions on the new directory are the default of the server, or if the protocol requires them to be specified then the directory is only readable/writable/searchable by the user (the equivalent of 700 on a file system). </p>
<p> If <code>url</code> starts from &#8216;@&#8217;, the remaining argument is assumed to be a path to a local file containing a list of URLs, one per line. In this case <code>arcmkdir</code> performs like it were called multiple times &#8211; once for every URL. </p>
<p> Depending on the installed libraries (check with <code>-P</code> ), the following protocols may be used: file (file:// prefix may be omitted), http, https, httpg, ftp, gsiftp, srm, root. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></p>
<dd> The location of the user&#8217;s Grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. </p>
<dt><code>ARC_LOCATION</code></p>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </p>
<dt><code>ARC_PLUGIN_PATH</code></p>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </p>
</dl>
<h2>EXAMPLE</h2>
<p> arcmkdir <a href="gsiftp://example.com/grid/newdir">gsiftp://example.com/grid/newdir</a> </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcrename/">arcrename</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), </p>
<h2>Index</h2>
