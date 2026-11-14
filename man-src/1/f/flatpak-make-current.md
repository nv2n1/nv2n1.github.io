---
title: "flatpak-make-current(1)"
name: "flatpak-make-current"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-make-current/"
description: "flatpak-make-current – Make a specific version of an app current"
---

<h2 class="name">NAME</h2>
<p> flatpak-make-current &#8211; Make a specific version of an app current </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak make-current</code> [OPTION&#8230;] APP BRANCH</dl>
<h2>DESCRIPTION</h2>
<dd>Makes a particular branch of an application current. Only the current branch of an app has its exported files (such as desktop files and icons) made visible to the host. </p>
<p> When a new branch is installed it will automatically be made current, so this command is often not needed. </p>
<p> Unless overridden with the <code>&#8211;user</code> or <code>&#8211;installation</code> options, this command changes the default system-wide installation.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Update a per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Update the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Updates a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The architecture to make current for. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user make-current org.gnome.gedit 3.14</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-list/">flatpak-list</a></code>(1) </p>
<h2>Index</h2>
