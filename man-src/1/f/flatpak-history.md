---
title: "flatpak-history(1)"
name: "flatpak-history"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-history/"
description: "flatpak-history – Show history"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak history</code> [OPTION&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>Shows changes to the flatpak installations on the system. This includes installs, updates and removals of applications and runtimes. </dd>
<p> By default, both per-user and system-wide installations are shown. Use the <code>&#8211;user</code>, <code>&#8211;installation</code> or <code>&#8211;system</code> options to change this. </p>
<p> The information for the history command is taken from the systemd journal, and can also be accessed using e.g. the journalctl command.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help options and exit.</dd></dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
</dt><dd> Show changes to the user installation.</dd></dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
</dt><dd> Show changes to the default system-wide installation.</dd></dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
</dt><dd> Show changes to the installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dd></dl>
<p> <code>&#8211;since=TIME</code></p>
<dl>
<dt>
</dt><dd> Only show changes that are newer than the time specified by TIME. </dd>
<p> TIME can be either an absolute time in a format like YYYY-MM-DD HH:MM:SS, or a relative time like &quot;2h&quot;, &quot;7days&quot;, &quot;4days 2hours&quot;.</dl>
<p> <code>&#8211;until=TIME</code></p>
<dl>
<dt>
</dt><dd> Only show changes that are older than the time specified by TIME.</dd></dl>
<p> <code>&#8211;reverse</code></p>
<dl>
<dt>
</dt><dd> Show newest entries first.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Print debug information during command processing.</dd></dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
</dt><dd> Print OSTree debug information during command processing.</dd></dl>
<p> <code>&#8211;columns=FIELD,&#8230;</code></p>
<dl>
<dt>
</dt><dd> Specify what information to show about each ref. You can list multiple fields, or use this option multiple times. </dd>
<p> Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names to change ellipsization.</dl>
<h2>FIELDS</h2>
<p> The following fields are understood by the <code>&#8211;columns</code> option: </p>
<p> time</p>
<dl>
<dt>
</dt><dd> Show when the change happened</dd></dl>
<p> change</p>
<dl>
<dt>
</dt><dd> Show the kind of change</dd></dl>
<p> ref</p>
<dl>
<dt>
</dt><dd> Show the ref</dd></dl>
<p> application</p>
<dl>
<dt>
</dt><dd> Show the application/runtime ID</dd></dl>
<p> arch</p>
<dl>
<dt>
</dt><dd> Show the architecture</dd></dl>
<p> branch</p>
<dl>
<dt>
</dt><dd> Show the branch</dd></dl>
<p> installation</p>
<dl>
<dt>
</dt><dd> Show the affected installation. </dd>
<p> This will be either the ID of a Flatpak installation, or the path to a temporary OSTree repository.</dl>
<p> remote</p>
<dl>
<dt>
</dt><dd> Show the remote that is used. </dd>
<p> This will be either the name of a configured remote, or the path to a temporary OSTree repository.</dl>
<p> old-commit</p>
<dl>
<dt>
</dt><dd> Show the previous commit. For pulls, this is the previous HEAD of the branch. For deploys, it is the previously active commit</dd></dl>
<p> commit</p>
<dl>
<dt>
</dt><dd> Show the current commit. For pulls, this is the HEAD of the branch. For deploys, it is the active commit</dd></dl>
<p> url</p>
<dl>
<dt>
</dt><dd> Show the remote url</dd></dl>
<p> user</p>
<dl>
<dt>
</dt><dd> Show the user doing the change. </dd>
<p> If this is the system helper operating as root, also show which user triggered the change.</dl>
<p> tool</p>
<dl>
<dt>
</dt><dd> Show the tool that was used. </dd>
<p> If this is the system helper, also show which tool was used to triggered the change.</dl>
<p> all</p>
<dl>
<dt>
</dt><dd> Show all columns</dd></dl>
<p> help</p>
<dl>
<dt>
</dt><dd> Show the list of available columns</dd></dl>
<p> Note that field names can be abbreviated to a unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) </p>
