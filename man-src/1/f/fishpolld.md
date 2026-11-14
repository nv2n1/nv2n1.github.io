---
title: "fishpolld(1)"
name: "fishpolld"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fishpolld/"
description: "fishpolld – daemon that allows remote script’s execution when triggered from the network"
---

<h2>NAME</h2>
<p> fishpolld &#8211; daemon that allows remote script&#8217;s execution when triggered from the network</p>
<h2>SYNOPSIS</h2>
<pre>
<code>fishpolld [OPTIONS]</code>
</pre>
<h2>DESCRIPTION</h2>
<p> Fishpoll is meant to deal with a common situation. You have a data source (a version control repository, a database, etc). You have something built from that data source (a web site, say). When the data source changes, you want them to rebuild against the latest commits. </p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code> Shows this help message.</p>
<dl>
<dt><code>-d, &#8211;debug</code></p>
<dd> Do not daemonize and log to stdout.</p>
<dt><code>&#8211;pid-file=PID_FILE</code></p>
<dd> Location to write PID of daemon.</p>
<dt><code>&#8211;handler-dir=HANDLER_DIR</code></p>
<dd> Directory to look for handlers in.</p>
<dt><code>&#8211;listen=HOST[:PORT] </code></p>
<dd> Address to listen on. </p>
</dl>
<h2>AUTHORS</h2>
<p> This manual page was written by Andrea Veri &lt;and [at] debian.org&gt; for the Debian GNU/Linux distribution. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<h2>Index</h2>
