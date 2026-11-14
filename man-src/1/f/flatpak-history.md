---
title: "flatpak-history(1)"
name: "flatpak-history"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-history/"
description: "flatpak-history – Show history"
---

<h2 class="name">NAME</h2>
<p> flatpak-history &#8211; Show history </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak history</code> [OPTION&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Shows changes to the flatpak installations on the system. This includes installs, updates and removals of applications and runtimes. </p>
<p> By default, both per-user and system-wide installations are shown. Use the <code>&#8211;user</code>, <code>&#8211;installation</code> or <code>&#8211;system</code> options to change this. </p>
<p> The information for the history command is taken from the systemd journal, and can also be accessed using e.g. the journalctl command.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Show changes to the user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Show changes to the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Show changes to the installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;since=TIME</code></p>
<dl>
<dt>
<dd> Only show changes that are newer than the time specified by TIME. </p>
<p> TIME can be either an absolute time in a format like YYYY-MM-DD HH:MM:SS, or a relative time like &quot;2h&quot;, &quot;7days&quot;, &quot;4days 2hours&quot;.</dl>
<p> <code>&#8211;until=TIME</code></p>
<dl>
<dt>
<dd> Only show changes that are older than the time specified by TIME.</dl>
<p> <code>&#8211;reverse</code></p>
<dl>
<dt>
<dd> Show newest entries first.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<p> <code>&#8211;columns=FIELD,&#8230;</code></p>
<dl>
<dt>
<dd> Specify what information to show about each ref. You can list multiple fields, or use this option multiple times. </p>
<p> Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names to change ellipsization.</dl>
<h2>FIELDS</h2>
<p> The following fields are understood by the <code>&#8211;columns</code> option: </p>
<p> time</p>
<dl>
<dt>
<dd> Show when the change happened</dl>
<p> change</p>
<dl>
<dt>
<dd> Show the kind of change</dl>
<p> ref</p>
<dl>
<dt>
<dd> Show the ref</dl>
<p> application</p>
<dl>
<dt>
<dd> Show the application/runtime ID</dl>
<p> arch</p>
<dl>
<dt>
<dd> Show the architecture</dl>
<p> branch</p>
<dl>
<dt>
<dd> Show the branch</dl>
<p> installation</p>
<dl>
<dt>
<dd> Show the affected installation. </p>
<p> This will be either the ID of a Flatpak installation, or the path to a temporary OSTree repository.</dl>
<p> remote</p>
<dl>
<dt>
<dd> Show the remote that is used. </p>
<p> This will be either the name of a configured remote, or the path to a temporary OSTree repository.</dl>
<p> old-commit</p>
<dl>
<dt>
<dd> Show the previous commit. For pulls, this is the previous HEAD of the branch. For deploys, it is the previously active commit</dl>
<p> commit</p>
<dl>
<dt>
<dd> Show the current commit. For pulls, this is the HEAD of the branch. For deploys, it is the active commit</dl>
<p> url</p>
<dl>
<dt>
<dd> Show the remote url</dl>
<p> user</p>
<dl>
<dt>
<dd> Show the user doing the change. </p>
<p> If this is the system helper operating as root, also show which user triggered the change.</dl>
<p> tool</p>
<dl>
<dt>
<dd> Show the tool that was used. </p>
<p> If this is the system helper, also show which tool was used to triggered the change.</dl>
<p> all</p>
<dl>
<dt>
<dd> Show all columns</dl>
<p> help</p>
<dl>
<dt>
<dd> Show the list of available columns</dl>
<p> Note that field names can be abbreviated to a unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) </p>
<h2>Index</h2>
