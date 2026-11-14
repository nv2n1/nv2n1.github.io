---
title: "flatpak-remote-info(1)"
name: "flatpak-remote-info"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-remote-info/"
description: "flatpak-remote-info – Show information about an application or runtime in a remote"
---

<h2 class="name">NAME</h2>
<p> flatpak-remote-info &#8211; Show information about an application or runtime in a remote </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak remote-info</code> [OPTION&#8230;] REMOTE REF</dl>
<h2>DESCRIPTION</h2>
<dd>Shows information about the runtime or application REF from the remote repository with the name REMOTE. You can find all configured remote repositories with flatpak remotes. </p>
<p> By default, the output is formatted in a friendly format. If you specify one of the <code>&#8211;show-&#8230;</code> options, the output is instead formatted in a machine-readable format. </p>
<p> Unless overridden with the <code>&#8211;system</code>, <code>&#8211;user</code>, or <code>&#8211;installation</code> options, this command uses either the default system-wide installation or the per-user one, depending on which has the specified REMOTE.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Use the per-user configuration.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Use the default system-wide configuration.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Use a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;cached</code></p>
<dl>
<dt>
<dd> Prefer to use locally cached information if possible, even though it may be out of date. This is faster, but risks returning stale information. Also, some information is not cached so will not be available.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Assume that REF is a runtime if not explicitly specified.</dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
<dd> Assume that REF is an app if not explicitly specified.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The default architecture to look for, if not given explicitly in the REF. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>&#8211;commit=COMMIT</code></p>
<dl>
<dt>
<dd> Show information about the specific commit, rather than the latest version.</dl>
<p> <code>&#8211;log</code></p>
<dl>
<dt>
<dd> Display a log of previous versions.</dl>
<p> <code>-r</code>, <code>&#8211;show-ref</code></p>
<dl>
<dt>
<dd> Show the matched ref.</dl>
<p> <code>-c</code>, <code>&#8211;show-commit</code></p>
<dl>
<dt>
<dd> Show the commit id.</dl>
<p> <code>-p</code>, <code>&#8211;show-parent</code></p>
<dl>
<dt>
<dd> Show the parent commit id.</dl>
<p> <code>-m</code>, <code>&#8211;show-metadata</code></p>
<dl>
<dt>
<dd> Show the metadata.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user remote-info flathub org.gnome.gedit</code> </p>
<dl>
<dt>
<dd>
<pre>
Ref: app/org.gnome.gedit/x86_64/stable
ID: org.gnome.gedit
Arch: x86_64
Branch: stable
Date: 2017-07-31 16:05:22 +0000
Subject: Build org.gnome.gedit at 3ec291fc1ce4d78220527fa79576f4cc1481ebe5
Commit: 3de7e9dde3bb8382aad9dfbbff20eccd9bf2100bc1887a3619ec0372e8066bf7
Parent: -
Download size: 3,4 MB
Installed size: 11,1 MB
Runtime: org.gnome.Platform/x86_64/3.24
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remotes/">flatpak-remotes</a></code>(1) <code><a href="/docs/linux/man/1-flatpak-remote-ls/">flatpak-remote-ls</a></code>(1) </p>
<h2>Index</h2>
