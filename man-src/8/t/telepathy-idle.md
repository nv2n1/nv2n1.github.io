---
title: "telepathy-idle(8)"
name: "telepathy-idle"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telepathy-idle/"
description: "telepathy-idle – Telepathy connection manager for IRC"
---

<p>telepathy-idle &#8211; Telepathy connection manager for IRC</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/telepathy-idle</code></p>
<h2>Description</h2>
<p>Idle implements the Telepathy D-Bus specification for Internet Relay Chat, allowing Telepathy clients like <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) to connect to IRC servers. </p>
<p> It is a D-Bus service which runs on the session bus, and should usually be started automatically by D-Bus activation. However, it might be useful to start it manually for debugging.</p>
<h2>Options</h2>
<p>There are no command-line options.</p>
<h2>Environment</h2>
<dl>
<dt><code>IDLE_LOGFILE</code>=<i>filename</i></p>
<dd>If set, debug output will go to the given file rather than to stderr. If <code>+</code> is prepended to the <i>filename</i> (e.g. <code>IDLE_LOGFILE=+idle.log</code>), debug output will be appended to the file; otherwise, any existing file will be replaced.</p>
<dt>
<dt><code>IDLE_DEBUG</code>=<i>type</i></p>
<dd>
<dd>May be set to &quot;all&quot; for full debug output, or various undocumented options (which may change from release to release) to filter the output.</dl>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://telepathy.freedesktop.org/">http://telepathy.freedesktop.org/</a></i>, <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) </p>
