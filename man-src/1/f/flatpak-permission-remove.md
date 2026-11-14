---
title: "flatpak-permission-remove(1)"
name: "flatpak-permission-remove"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-permission-remove/"
description: "flatpak-permission-remove – Remove permissions"
---

<h2 class="name">NAME</h2>
<p> flatpak-permission-remove &#8211; Remove permissions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak permission-remove</code> [OPTION&#8230;] TABLE ID [APP_ID]</dl>
<h2>DESCRIPTION</h2>
<dd>Removes an entry for the object with id ID to the permission store table TABLE. The ID must be in a suitable format for the table. If APP_ID is specified, only the entry for that application is removed. </p>
<p> The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.</p>
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
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permissions/">flatpak-permissions</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-show/">flatpak-permission-show</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-reset/">flatpak-permission-reset</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-set/">flatpak-permission-set</a></code>(1) </p>
<h2>Index</h2>
