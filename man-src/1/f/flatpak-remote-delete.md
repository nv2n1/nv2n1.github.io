---
title: "flatpak-remote-delete(1)"
name: "flatpak-remote-delete"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-remote-delete/"
description: "flatpak-remote-delete – Delete a remote repository"
---

<h2 class="name">NAME</h2>
<p> flatpak-remote-delete &#8211; Delete a remote repository </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak remote-delete</code> [OPTION&#8230;] NAME</dl>
<h2>DESCRIPTION</h2>
<dd>Removes a remote repository from the flatpak repository configuration. NAME is the name of an existing remote. </p>
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
<dd> Modify the per-user configuration.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Modify the default system-wide configuration.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Modify a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Remove remote even if its in use by installed apps or runtimes.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user remote-delete dried-raisins</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-add/">flatpak-remote-add</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-modify/">flatpak-remote-modify</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remotes/">flatpak-remotes</a></code>(1) </p>
<h2>Index</h2>
