---
title: "flatpak-enter(1)"
name: "flatpak-enter"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-enter/"
description: "flatpak-enter – Enter an application or runtime’s sandbox"
---

<h2 class="name">NAME</h2>
<p> flatpak-enter &#8211; Enter an application or runtime&#8217;s sandbox </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak enter</code> [OPTION&#8230;] INSTANCE COMMAND [ARG&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Enter a running sandbox. </p>
<p> INSTANCE must be either the pid of a process running in a flatpak sandbox, or the ID of a running application, or the instance ID of a running sandbox. You can use <code>flatpak ps</code> to find the instance IDs of running flatpaks. </p>
<p> COMMAND is the command to run in the sandbox. Extra arguments are passed on to the command. </p>
<p> This creates a new process within the running sandbox, with the same environment. This is useful when you want to debug a problem with a running application. </p>
<p> This command works as a regular user if the system support unprivileged user namespace. If that is not available you need to run run it like: <code>sudo -E flatpak enter</code>.</p>
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
<p> <code>$ flatpak enter 15345 sh</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1) <code><a href="/docs/linux/man/1-flatpak-ps/">flatpak-ps</a></code>(1) </p>
<h2>Index</h2>
