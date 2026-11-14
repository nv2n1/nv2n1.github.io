---
title: "xapian-tcpsrv(1)"
name: "xapian-tcpsrv"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xapian-tcpsrv/"
description: "xapian-tcpsrv – TCP daemon for use with Xapian’s remote backend"
---

<h2>NAME</h2>
<p> xapian-tcpsrv &#8211; TCP daemon for use with Xapian&#8217;s remote backend</p>
<h2>SYNOPSIS</h2>
<p> <code>xapian-tcpsrv</code> [<i>OPTIONS</i>] <i>DATABASE_DIRECTORY</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> xapian-tcpsrv &#8211; TCP daemon for use with Xapian&#8217;s remote backend</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;port</code> PORTNUM</p>
<dd> listen on port PORTNUM for connections (no default)</p>
<dt><code>&#8211;interface</code> ADDRESS</p>
<dd> listen on the interface associated with name or address ADDRESS (default is all interfaces)</p>
<dt><code>&#8211;idle-timeout</code> MSECS</p>
<dd> set timeout for idle connections (default MSECS_IDLE_TIMEOUT_DEFAULTms)</p>
<dt><code>&#8211;active-timeout</code> MSECS</p>
<dd> set timeout for active connections (default MSECS_ACTIVE_TIMEOUT_DEFAULTms)</p>
<dt><code>&#8211;timeout</code> MSECS</p>
<dd> set both timeout values</p>
<dt><code>&#8211;one-shot</code></p>
<dd> serve a single connection and exit</p>
<dt><code>&#8211;quiet</code></p>
<dd> disable information messages to stdout</p>
<dt><code>&#8211;writable</code></p>
<dd> allow updates (only one database directory allowed)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit </p>
</dl>
<h2>Index</h2>
