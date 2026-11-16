---
title: "do-release-upgrade(8)"
name: "do-release-upgrade"
section: "8"
letter: "d"
url: "/docs/linux/man/8-do-release-upgrade/"
description: "do-release-upgrade – upgrade operating system to latest release"
---

<p>do-release-upgrade &#8211; upgrade operating system to latest release</p>
<h2>Synopsis</h2>
<p><code>do-release-upgrade</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>Upgrade the operating system to the latest release from the command-line. This is the preferred command if the machine has no graphic environment or if the machine is to be upgraded over a remote connection.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>show help message and exit</dd>
<dt><code>-d</code>, <code>&#8211;devel-release</code></dt>
<dd>If using the latest supported release, upgrade to the development release</dd>
<dt><code>-p</code>, <code>&#8211;proposed</code></dt>
<dd>Try upgrading to the latest release using the upgrader from Ubuntu-proposed</dd>
<dt><code>-m</code> MODE, <code>&#8211;mode</code>=<i>MODE</i></dt>
<dd>Run in a special upgrade mode. Currently &quot;desktop&quot; for regular upgrades of a desktop system and &quot;server&quot; for server systems are supported.</dd>
<dt><code>-f</code> FRONTEND, <code>&#8211;frontend</code>=<i>FRONTEND</i></dt>
<dd>Run the specified frontend</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-update-manager/">update-manager</a></code>(8), <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) </p>
