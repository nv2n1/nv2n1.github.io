---
title: "grid-proxy-destroy(1)"
name: "grid-proxy-destroy"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-proxy-destroy/"
description: "grid-proxy-destroy – Destroy the default proxy certificate"
---

<h2 class="name">NAME</h2>
<p> grid-proxy-destroy &#8211; Destroy the default proxy certificate </p>
<h2>SYNOPSIS</h2>
<p> grid-proxy-destroy -help | -usage | -version </p>
<p> grid-proxy-destroy [-debug] [-dryrun] [-default] [&#8211; FILENAME &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The grid-proxy-destroy program removes X.509 proxy files from the local filesystem. It overwrites the data in the files and removes the files from the filesystem. By default, it removes the current user&#8217;s default proxy (either /tmp/x509up_u&#8217;UID&#8217; where <i>UID</i> is the current POSIX user id, or the file pointed to by the X509_USER_PROXY environment variable) unless a list of proxy file paths are included as part of the command line. </p>
<p> Use the <code>&#8212;</code> command-line option to separate a list of proxy paths from command line options if the proxy file begins with the <code>&#8211;</code> character.</p>
<h2>OPTIONS</h2>
<p> The full list of command-line options to <code>grid-proxy-destroy</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display the command-line options to <code>grid-proxy-destroy</code>.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the version number of the <code>grid-proxy-destroy</code> command.</dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Display verbose error messages.</dl>
<p> <code>-dryrun</code></p>
<dl>
<dt>
<dd> Do not remove the proxy, but display the path of the files that would have been removed, or the directory where they would have been removed from if the <i>-all</i> command-line option is used.</dl>
<p> <code>-default</code></p>
<dl>
<dt>
<dd> Remove the default proxy in addition to the files included on the command-line. Only needed if other paths are included on the command-line.</dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> Remove the default proxy and all delegated proxies in the temporary file directory.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of grid-proxy-destroy: </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
<dd> Path to the default user proxy.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grid-proxy-init/">grid-proxy-init</a>(1), <a href="/docs/linux/man/1-grid-proxy-info/">grid-proxy-info</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
