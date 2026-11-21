---

title: "xapian-tcpsrv(1)"
name: "xapian-tcpsrv"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xapian-tcpsrv/"
description: "xapian-tcpsrv – TCP daemon for use with Xapian’s remote backend"
---

<p> xapian-tcpsrv &#8211; TCP daemon for use with Xapian&#8217;s remote backend</p>
<h2>SYNOPSIS</h2>
<p> <code>xapian-tcpsrv</code> [<i>OPTIONS</i>] <i>DATABASE_DIRECTORY</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> xapian-tcpsrv &#8211; TCP daemon for use with Xapian&#8217;s remote backend</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;port</code> PORTNUM</dt>
<dd> listen on port PORTNUM for connections (no default)</dd>
<dt><code>&#8211;interface</code> ADDRESS</dt>
<dd> listen on the interface associated with name or address ADDRESS (default is all interfaces)</dd>
<dt><code>&#8211;idle-timeout</code> MSECS</dt>
<dd> set timeout for idle connections (default MSECS_IDLE_TIMEOUT_DEFAULTms)</dd>
<dt><code>&#8211;active-timeout</code> MSECS</dt>
<dd> set timeout for active connections (default MSECS_ACTIVE_TIMEOUT_DEFAULTms)</dd>
<dt><code>&#8211;timeout</code> MSECS</dt>
<dd> set both timeout values</dd>
<dt><code>&#8211;one-shot</code></dt>
<dd> serve a single connection and exit</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> disable information messages to stdout</dd>
<dt><code>&#8211;writable</code></dt>
<dd> allow updates (only one database directory allowed)</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit </dd>
</dl>
