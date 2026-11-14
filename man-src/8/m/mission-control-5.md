---
title: "mission-control-5(8)"
name: "mission-control-5"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mission-control-5/"
description: "mission-control-5 – Telepathy account manager/chanel dispatcher"
---

<p>mission-control-5 &#8211; Telepathy account manager/chanel dispatcher</p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/mission-control-5</code></p>
<h2>Description</h2>
<p>Mission Control 5 implements the AccountManager and ChannelDispatcher services described in the Telepathy D-Bus specification, allowing clients like <code><a href="/docs/linux/man/1-empathy/">empathy</a></code>(1) to store account details, connect to accounts, request communication channels, and have channels dispatched to them. </p>
<p> It is a D-Bus service which runs on the session bus, and should usually be started automatically by D-Bus activation. However, it might be useful to start it manually for debugging.</p>
<h2>Options</h2>
<p>There are no command-line options.</p>
<h2>Environment</h2>
<dl>
<dt><code>MC_DEBUG=all</code> or <code>MC_DEBUG=</code><i>category</i>[<code>,</code><i>category</i>&#8230;]</p>
<dd>May be set to &quot;all&quot; for full debug output from Mission Control and telepathy-glib, or various undocumented category names (which may change from release to release) to filter the output. See Mission Control and telepathy-glib source code for the available categories.</p>
<dt><code>MC_DEBUG=</code><i>level</i></p>
<dd>Set a numeric debug level for Mission Control itself (but not telepathy-glib). Level 0 logs nothing, level 1 logs most messages, and level 2 logs all messages.</p>
<dt><code>MC_TP_DEBUG</code>=<i>type</i></p>
<dd>May be set to &quot;all&quot; for full debug output from telepathy-glib, or various undocumented options (which may change from telepathy-glib release to release) to filter the output. See telepathy-glib source code for the available options.</dl>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://telepathy.freedesktop.org/">http://telepathy.freedesktop.org/</a></i> </p>
