---
title: "flatpak-info(1)"
name: "flatpak-info"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-info/"
description: "flatpak-info – Show information about an installed application or runtime"
---

<h2 class="name">NAME</h2>
<p> flatpak-info &#8211; Show information about an installed application or runtime </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak info</code> [OPTION&#8230;] NAME [BRANCH]</dl>
<h2>DESCRIPTION</h2>
<dd>Show info about an installed application or runtime. </p>
<p> By default, the output is formatted in a friendly format. If you specify any of the <code>&#8211;show-&#8230;</code> or <code>&#8211;file-access</code> options, the output is instead formatted in a machine-readable format. </p>
<p> By default, both per-user and system-wide installations are queried. Use the <code>&#8211;user</code>, <code>&#8211;system</code> or <code>&#8211;installation</code> options to change this.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Query per-user installations.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Query the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Query a system-wide installation by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> Query for this architecture. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>-r</code>, <code>&#8211;show-ref</code></p>
<dl>
<dt>
<dd> Show the installed ref.</dl>
<p> <code>-o</code>, <code>&#8211;show-origin</code></p>
<dl>
<dt>
<dd> Show the remote the ref is installed from.</dl>
<p> <code>-c</code>, <code>&#8211;show-commit</code></p>
<dl>
<dt>
<dd> Show the installed commit id.</dl>
<p> <code>-s</code>, <code>&#8211;show-size</code></p>
<dl>
<dt>
<dd> Show the installed size.</dl>
<p> <code>-m</code>, <code>&#8211;show-metadata</code></p>
<dl>
<dt>
<dd> Show the metadata.</dl>
<p> <code>&#8211;show-runtime</code></p>
<dl>
<dt>
<dd> Show the runtime.</dl>
<p> <code>&#8211;show-sdk</code></p>
<dl>
<dt>
<dd> Show the SDK.</dl>
<p> <code>-M</code>, <code>&#8211;show-permissions</code></p>
<dl>
<dt>
<dd> Show the permissions.</dl>
<p> <code>&#8211;file-access=PATH</code></p>
<dl>
<dt>
<dd> Show the level of access to the given path.</dl>
<p> <code>-e</code>, <code>&#8211;show-extensions</code></p>
<dl>
<dt>
<dd> Show the matching extensions.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak info org.gnome.Builder//master</code> </p>
<p> <code>$ tree `flatpak info -l org.gnome.Builder//master`/files</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-update/">flatpak-update</a></code>(1) </p>
<h2>Index</h2>
