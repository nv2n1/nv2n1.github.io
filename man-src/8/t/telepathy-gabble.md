---
title: "telepathy-gabble(8)"
name: "telepathy-gabble"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telepathy-gabble/"
description: "telepathy-gabble – Telepathy connection manager for XMPP (Jabber)"
---

<p>telepathy-gabble &#8211; Telepathy connection manager for XMPP (Jabber)</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/telepathy-gabble</code></p>
<h2>Description</h2>
<p>Gabble implements the Telepathy D-Bus specification for XMPP (Jabber), allowing Telepathy clients like <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) to connect to XMPP accounts, including Google Talk. </p>
<p> It is a D-Bus service which runs on the session bus, and should usually be started automatically by D-Bus activation. However, it might be useful to start it manually for debugging.</p>
<h2>Options</h2>
<p>There are no command-line options.</p>
<h2>Environment</h2>
<dl>
<dt><code>GABBLE_LOGFILE</code>=<i>filename</i></p>
<dd>If set, debug output will go to the given file rather than to stderr. If <code>+</code> is prepended to the <i>filename</i> (e.g. <code>GABBLE_LOGFILE=+gabble.log</code>), debug output will be appended to the file; otherwise, any existing file will be replaced.</p>
<dt><code>GABBLE_DEBUG</code>=<i>type</i></p>
<dd>May be set to &quot;all&quot; for full debug output, or various undocumented options (which may change from release to release) to filter the output.</p>
<dt><code>WOCKY_DEBUG</code>=<i>type</i></p>
<dd>May be set to &quot;all&quot; for full debug output from the Wocky XMPP library used by Gabble, or various undocumented options (which may change from release to release) to filter the output. For general Gabble debugging, &quot;net&quot; is recommended.</p>
<dt><code>GABBLE_PERSIST</code>=<i>1</i></p>
<dd>If set (to any value), Gabble will continue running until killed, rather than timing out if it has no open connections for a few seconds.</p>
<dt><code>GABBLE_PLUGIN_DIR</code>=<i>directory</i></p>
<dd>If set, and Gabble was compiled with plugin support, plugins will be loaded from <i>directory</i> rather than from the default directory.</dl>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://telepathy.freedesktop.org/">http://telepathy.freedesktop.org/</a></i>, <i><a rel="nofollow" href="http://telepathy.freedesktop.org/wiki/CategoryGabble">http://telepathy.freedesktop.org/wiki/CategoryGabble</a></i>, <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) </p>
