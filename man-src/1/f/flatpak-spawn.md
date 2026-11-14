---
title: "flatpak-spawn(1)"
name: "flatpak-spawn"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-spawn/"
description: "flatpak-spawn – Run commands in a sandbox"
---

<h2 class="name">NAME</h2>
<p> flatpak-spawn &#8211; Run commands in a sandbox </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak-spawn</code> [OPTION&#8230;] COMMAND [ARGUMENT&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Unlike other flatpak commands, <code>flatpak-spawn</code> is available to applications inside the sandbox. It runs COMMAND outside the sandbox, either in another sandbox, or on the host. </p>
<p> <code>flatpak-spawn</code> uses the Flatpak portal to create a copy the sandbox it was called from, optionally using tighter permissions and the latest version of the app and runtime.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information</dl>
<p> <code>&#8211;forward-fd=FD</code></p>
<dl>
<dt>
<dd> Forward a file descriptor</dl>
<p> <code>&#8211;clear-env</code></p>
<dl>
<dt>
<dd> Run with a clean environment</dl>
<p> <code>&#8211;watch-bus</code></p>
<dl>
<dt>
<dd> Make the spawned command exit if we do</dl>
<p> <code>&#8211;env=VAR=VALUE</code></p>
<dl>
<dt>
<dd> Set an environment variable</dl>
<p> <code>&#8211;latest-version</code></p>
<dl>
<dt>
<dd> Use the latest version of the refs that are used to set up the sandbox</dl>
<p> <code>&#8211;no-network</code></p>
<dl>
<dt>
<dd> Run without network access</dl>
<p> <code>&#8211;sandbox</code></p>
<dl>
<dt>
<dd> Run fully sandboxed. </p>
<p> See the <code>&#8211;sandbox-expose</code> and <code>&#8211;sandbox-expose-ro</code> options for selective file access.</dl>
<p> <code>&#8211;sandbox-expose=NAME</code></p>
<dl>
<dt>
<dd> Expose read-write access to a file in the sandbox. </p>
<p> Note that absolute paths or subdirectories are not allowed. The files must be in the sandbox subdirectory of the instance directory (i.e. ~/.var/app/$APP_ID/sandbox). </p>
<p> This option is useful in combination with <code>&#8211;sandbox</code> (otherwise the instance directory is accessible anyway).</dl>
<p> <code>&#8211;sandbox-expose-ro=NAME</code></p>
<dl>
<dt>
<dd> Expose readonly access to a file in the sandbox. </p>
<p> Note that absolute paths or subdirectories are not allowed. The files must be in the sandbox subdirectory of the instance directory (i.e. ~/.var/app/$APP_ID/sandbox). </p>
<p> This option is useful in combination with <code>&#8211;sandbox</code> (otherwise the instance directory is accessible anyway).</dl>
<p> <code>&#8211;host</code></p>
<dl>
<dt>
<dd> Run the command unsandboxed on the host. This requires access to the org.freedesktop.Flatpak D-Bus interface</dl>
<p> <code>&#8211;directory=DIR</code></p>
<dl>
<dt>
<dd> The working directory in which to run the command. </p>
<p> Note that the given directory must exist in the sandbox or, when used in conjunction with <code>&#8211;host</code>, on the host.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak-spawn ls /var/run</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1) </p>
<h2>Index</h2>
