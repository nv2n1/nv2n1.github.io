---
title: "telepathy-haze(8)"
name: "telepathy-haze"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telepathy-haze/"
description: "telepathy-haze – Telepathy connection manager using libpurple"
---

<p>telepathy-haze &#8211; Telepathy connection manager using libpurple</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/telepathy-haze</code></p>
<h2>Description</h2>
<p>Haze implements the Telepathy D-Bus specification using libpurple, allowing Telepathy clients like <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) to connect to any protocol supported by <code><a href="/docs/linux/man/1-pidgin/">pidgin</a></code>(1). </p>
<p> It is a D-Bus service which runs on the session bus, and should usually be started automatically by D-Bus activation. However, it might be useful to start it manually for debugging.</p>
<h2>Options</h2>
<p>There are no command-line options.</p>
<h2>Environment</h2>
<dl>
<dt><code>HAZE_DEBUG</code>=<i>type</i></p>
<dd>May be set to &quot;all&quot; for full debug output, or various undocumented options (which may change from release to release) to filter the output.</p>
<dt><code>HAZE_PERSIST</code>=1</p>
<dd>If set, Haze will not automatically close itself after five seconds without any connections.</p>
<dt><code>HAZE_LOGFILE</code>=<i>filename</i></p>
<dd>If set, all debugging output will be written to <i>filename</i> rather than to the terminal.</dl>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://telepathy.freedesktop.org/">http://telepathy.freedesktop.org/</a></i>, <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1), <code><a href="/docs/linux/man/1-pidgin/">pidgin</a></code>(1) </p>
