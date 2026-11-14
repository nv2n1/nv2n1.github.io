---
title: "telepathy-salut(8)"
name: "telepathy-salut"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telepathy-salut/"
description: "telepathy-salut – Telepathy connection manager for link-local XMPP"
---

<p>telepathy-salut &#8211; Telepathy connection manager for link-local XMPP</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/telepathy-salut</code></p>
<h2>Description</h2>
<p>Salut implements the Telepathy D-Bus specification for link-local XMPP (XEP-0174, often called &quot;Bonjour&quot;), allowing Telepathy clients like <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) to communicate with other implementations of link-local XMPP, such as iChat. It also extends the protocol to support multicast-based chat rooms and collaboration. </p>
<p> It is a D-Bus service which runs on the session bus, and should usually be started automatically by D-Bus activation. However, it might be useful to start it manually for debugging.</p>
<h2>Options</h2>
<p>There are no command-line options.</p>
<h2>Environment</h2>
<dl>
<dt><code>SALUT_LOGFILE</code>=<i>filename</i></p>
<dd>If set, debug output will go to the given file rather than to stderr.</p>
<dt><code>SALUT_DEBUG</code>=<i>type</i></p>
<dd>May be set to &quot;all&quot; for full debug output, or various undocumented options (which may change from release to release) to filter the output. <code>GIBBER_DEBUG</code>=<i>type</i> May be set to &quot;all&quot; for full debug output from the Gibber XMPP library used by Salut, or various undocumented options (which may change from release to release) to filter the output.</dl>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://telepathy.freedesktop.org/">http://telepathy.freedesktop.org/</a></i>, <i><a rel="nofollow" href="http://telepathy.freedesktop.org/wiki/CategorySalut">http://telepathy.freedesktop.org/wiki/CategorySalut</a></i>, <i><a rel="nofollow" href="http://www.xmpp.org/extensions/xep-0174.html">http://www.xmpp.org/extensions/xep-0174.html</a></i>, <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) </p>
