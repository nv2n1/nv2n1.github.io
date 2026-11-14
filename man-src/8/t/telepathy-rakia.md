---
title: "telepathy-rakia(8)"
name: "telepathy-rakia"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telepathy-rakia/"
description: "telepathy-rakia – Telepathy connection manager for SIP"
---

<p>telepathy-rakia &#8211; Telepathy connection manager for SIP</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/telepathy-rakia</code></p>
<h2>Description</h2>
<p><code>telepathy-rakia</code> implements the Telepathy D-Bus specification for the Session Initiation Protocol, allowing Telepathy clients like <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) to connect to Voice over IP providers that implement SIP. </p>
<p> It is a D-Bus service which runs on the session bus, and should usually be started automatically by D-Bus activation. However, it might be useful to start it manually for debugging.</p>
<h2>Options</h2>
<p>There are no command-line options.</p>
<h2>Environment</h2>
<dl>
<dt><code>RAKIA_DEBUG</code>=<i>type</i></p>
<dd>May be set to &quot;all&quot; for full debug output, or various undocumented options (which may change from release to release) to filter the output.</p>
<dt><code>RAKIA_LOGFILE</code>=<i>filename</i></p>
<dd>May be set to the name of a file to overwrite with log messages. The filename may be prefixed with <code>+</code> to append messages to an existing file instead of overwriting it.</p>
<dt><code>RAKIA_PERSIST</code></p>
<dd>May be set to any value to avoid telepathy-rakia&#8217;s usual automatic exit when there have been no connections for a few seconds.</p>
<dt><code>TPORT_LOG</code></p>
<dd>May be set to any value to print all parsed SIP messages at the transport layer (this functionality is provided by the underlying Sofia-SIP library, which also offers various more specialized debugging options).</dl>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://telepathy.freedesktop.org/">http://telepathy.freedesktop.org/</a></i>, <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) </p>
