---
title: "flatpak-remote-list(1)"
name: "flatpak-remote-list"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-remote-list/"
description: "flatpak-remote-list – List remote repositories"
---

<h2 class="name">NAME</h2>
<p> flatpak-remote-list &#8211; List remote repositories </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak remote-list</code> [OPTION&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Lists the known remote repositories, in priority order. </p>
<p> By default, both per-user and system-wide installations are shown. Use the &#8211;user, &#8211;system or &#8211;installation options to change this.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Show the per-user configuration.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Show the default system-wide configuration.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Show a system-wide installation by NAME among those defined in /etc/flatpak/installations.d. Using &#8211;installation=default is equivalent to using &#8211;system.</dl>
<p> <code>-d</code>, <code>&#8211;show-details</code></p>
<dl>
<dt>
<dd> Show more information each repository in addition to the name.</dl>
<p> <code>&#8211;show-disabled</code></p>
<dl>
<dt>
<dd> Show disabled repos.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak remote-list &#8211;user &#8211;show-details</code> </p>
<dl>
<dt>
<dd>
<pre>
testrepo        Test Repository  <a rel="nofollow" href="http://209.132.179.91/repo/">http://209.132.179.91/repo/</a> no-gpg-verify
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-add-remote/">flatpak-add-remote</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-delete-remote/">flatpak-delete-remote</a></code>(1) </p>
<h2>Index</h2>
