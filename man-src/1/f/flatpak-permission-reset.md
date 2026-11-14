---
title: "flatpak-permission-reset(1)"
name: "flatpak-permission-reset"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-permission-reset/"
description: "flatpak-permission-reset – Reset permissions"
---

<h2 class="name">NAME</h2>
<p> flatpak-permission-reset &#8211; Reset permissions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak permission-reset</code> [OPTION&#8230;] APP_ID</p>
<dt> <code>flatpak permission-reset</code> [OPTION&#8230;] &#8211;all</dl>
<h2>DESCRIPTION</h2>
<dd>Removes all permissions for the given app from the Flatpak permission store. </p>
<p> The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Remove permissions for all applications.</dl>
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
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permissions/">flatpak-permissions</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-show/">flatpak-permission-show</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-remove/">flatpak-permission-remove</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-set/">flatpak-permission-set</a></code>(1) </p>
<h2>Index</h2>
