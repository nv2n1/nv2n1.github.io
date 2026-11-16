---
title: "diffindex-download(1)"
name: "diffindex-download"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diffindex-download/"
description: "diffindex-download – Download utility for Debian Contents files"
---

<h2 class="name">NAME</h2>
<p> diffindex-download &#8211; Download utility for Debian Contents files </p>
<h2>SYNOPSIS</h2>
<p> <code>diffindex-download</code> [ <code>options</code> ] <code>URL</code> <code>filename</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>diffindex-download</code> is a command line tool for downloading Contents files. It uses APT&#8217;s diff/Index format patches when available to avoid downloading the full file. <code>diffindex-download</code> is used by <code>apt-file</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code> -n number </code></dt>
<dd> If more than number patches would be necessary, download the whole file. Specifying 0 to always download the whole file is possible.</dd>
<dt><code> -k </code></dt>
<dd> Don&#8217;t verify the peer certificate when using https.</dd>
<dt><code> -c cacert </code></dt>
<dd> If cacert is a directory: Use cacert as CA certificate path. Otherwise use cacert as CA certificate bundle. See the &#8211;capath and &#8211;cacert options in the <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1) man page.</dd>
<dt><code> -i </code></dt>
<dd> Don&#8217;t exit with errror if the URL does not exist. This is useful as some archives don&#8217;t provide Contents files.</dd>
<dt><code> -q </code></dt>
<dd> Be quiet (opposite of -v). The default if stdout is not a terminal.</dd>
<dt><code> -v </code></dt>
<dd> Be verbose (opposite of -q). The default if stdout is a terminal.</dd>
<dt><code> -d </code></dt>
<dd> Print additional debug info.</dd>
<dt><code> -h </code></dt>
<dd> Display a short help screen.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apt-file/">apt-file</a></code>(1), <code><a href="/docs/linux/man/1-diffindex-rred/">diffindex-rred</a></code>(1), <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>diffindex-download</code> was written by Stefan Fritsch &lt;sf [at] debian.org&gt;. </p>
<h2>Index</h2>
