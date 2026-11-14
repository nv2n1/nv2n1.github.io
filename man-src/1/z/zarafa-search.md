---
title: "zarafa-search(1)"
name: "zarafa-search"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-search/"
description: "zarafa-search – Zarafa Indexed Search Service."
---

<h2 class="name">NAME</h2>
<p> zarafa-search &#8211; Zarafa Indexed Search Service. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-search</code></dl>
<h2>DESCRIPTION</h2>
<dd>The zarafa-search daemon is used to index all messages for all users in the zarafa-server. Indexing messages greatly enhances the search performance of the zarafa-server. </p>
<p> After starting, the search daemon will continuesly update the store index files and will keep listening for connections on the configured TCP port and/or Unix socket for search requests from the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> The Zarafa search program takes the following configuration options: </p>
<p> <code>&#8211;config</code>, <code>-c</code> <i>file</i></p>
<dl>
<dt>
<dd> Specify the location of the configuration file. </p>
<p> Default: <i>/etc/zarafa/search.cfg</i></dl>
<p> <code>&#8211;foreground</code>, <code>-F</code></p>
<dl>
<dt>
<dd> Run in the foreground. Normally the zarafa-search process will daemonize and run in the background.</dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Print the version and exit.</dl>
<p> <code>&#8211;ignore-unknown-config-options</code></p>
<dl>
<dt>
<dd> When unknown options exists in the configuration file the search daemon will report an error and shutdown. Pass this option to ignore unknown options so zarafa-search will start.</dl>
<p> <code>&#8211;reindex</code> <i>username</i></p>
<dl>
<dt>
<dd> Remove the current index of the given user and start to make a new index immediately. </p>
<p> The zarafa-search daemon must already be running on the same machine.</dl>
<p> When invoked with no options, the zarafa-search daemon will search for a configuration file in /etc/zarafa/search.cfg. If no configuration file is found, default values are used. See <code><a href="/docs/linux/man/5-zarafa-search-cfg/">zarafa-search.cfg</a></code>(5) for all configuration options and their default values.</p>
<h2>USAGE</h2>
<p> Starting the zarafa-search daemon with an alternative configuration: </p>
<p> <code>zarafa-search</code><code>-c</code><i>/path/to/search.cfg</i> </p>
<p> You may also use the init.d scripts: </p>
<p> <code>/etc/init.d/zarafa-search</code> [<i>start</i>| <i>stop</i>| <i>restart</i>| <i>reload</i>]</p>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-search-cfg/">zarafa-search.cfg</a></code>(5) </p>
<h2>Index</h2>
