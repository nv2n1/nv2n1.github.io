---
title: "flatpak-kill(1)"
name: "flatpak-kill"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-kill/"
description: "flatpak-kill – Stop a running application"
---

<h2 class="name">NAME</h2>
<p> flatpak-kill &#8211; Stop a running application </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak kill</code> INSTANCE</dl>
<h2>DESCRIPTION</h2>
<dd>Stop a running Flatpak instance. </p>
<p> INSTANCE can be either the numeric instance ID or the application ID of a running Flatpak. You can use <code>flatpak ps</code> to find the instance IDs of running flatpaks.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak kill org.gnome.Todo</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-ps/">flatpak-ps</a></code>(1) </p>
<h2>Index</h2>
