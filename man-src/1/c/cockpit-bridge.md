---
title: "cockpit-bridge(1)"
name: "cockpit-bridge"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cockpit-bridge/"
description: "cockpit-bridge – Cockpit Host Bridge"
---

<h2 class="name">NAME</h2>
<p> cockpit-bridge &#8211; Cockpit Host Bridge </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cockpit-bridge</code> [<code>&#8211;help</code>] [<code>&#8211;packages</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cockpit-bridge</code> program is used by Cockpit to relay messages and commands from the Web front end to the server. Among other things it relays DBus, and spawns processes on behalf of the Web user interface. </p>
<p> This program is not routinely run by users or administrators. It is in the $PATH so that Cockpit can find it when connecting between hosts. However there are some diagnostics available when running from the command line.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options.</dl>
<p> <code>&#8211;interact=boundary</code></p>
<dl>
<dt>
<dd> Interact with the raw cockpit1 protocol. Useful for debugging and testing. Specify a <code>boundary</code> which should be on an empty line between messages.</dl>
<p> <code>&#8211;packages</code></p>
<dl>
<dt>
<dd> List all available Cockpit packages and exit. Note this includes packages available to the user running this command.</dl>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the m[blue]<code>upstream bug tracker</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>AUTHOR</h2>
<p> Cockpit has been written by many m[blue]<code>contributors</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-cockpit-ws/">cockpit-ws</a></code>(8)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> upstream bug tracker</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/cockpit-project/cockpit/issues/new">https://github.com/cockpit-project/cockpit/issues/new</a></dl>
<dt> 2.</p>
<dd> contributors</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/cockpit-project/cockpit/">https://github.com/cockpit-project/cockpit/</a></dl>
</dl>
<h2>Index</h2>
