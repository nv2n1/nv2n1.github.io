---
title: "flatpak-permission-set(1)"
name: "flatpak-permission-set"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-permission-set/"
description: "flatpak-permission-set – Set permissions"
---

<h2 class="name">NAME</h2>
<p> flatpak-permission-set &#8211; Set permissions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak permission-set</code> [OPTION&#8230;] TABLE ID APP_ID [PERMISSION&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Set the permissions for an application in an entry in the permission store. The entry is identified by TABLE and ID, the application is identified by APP_ID. The PERMISSION strings must be in a format suitable for the table. </p>
<p> The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;data=DATA</code></p>
<dl>
<dt>
<dd> Associate DATA with the entry. The data must be a serialized GVariant.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak permission-set &#8211;data &quot;{&#8216;always-ask&#8217;:&lt;true&gt;}&quot; desktop-used-apps text/plain org.mozilla.Firefox org.gnome.gedit 0 3</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permissions/">flatpak-permissions</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-remove/">flatpak-permission-remove</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-reset/">flatpak-permission-reset</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-permission-show/">flatpak-permission-show</a></code>(1) </p>
<h2>Index</h2>
