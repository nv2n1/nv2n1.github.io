---
title: "flatpak-permissions(1)"
name: "flatpak-permissions"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-permissions/"
description: "flatpak-permissions – List permissions"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak permissions</code> [OPTION&#8230;] [TABLE] [ID]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>Lists dynamic permissions which are stored in the Flatpak permission store. </dd>
<p> When called without arguments, lists all the entries in all permission store tables. When called with one argument, lists all the entries in the named table. When called with two arguments, lists the entry in the named table for the given object ID. </p>
<p> The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help options and exit.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Print debug information during command processing.</dd></dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
</dt><dd> Print OSTree debug information during command processing.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-show/">flatpak-permission-show</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-remove/">flatpak-permission-remove</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-reset/">flatpak-permission-reset</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-set/">flatpak-permission-set</a></code>(1) </p>
