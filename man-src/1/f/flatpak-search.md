---
title: "flatpak-search(1)"
name: "flatpak-search"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-search/"
description: "flatpak-search – Search for applications and runtimes"
---

<h2 class="name">NAME</h2>
<p> flatpak-search &#8211; Search for applications and runtimes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak search</code> TEXT</dl>
<h2>DESCRIPTION</h2>
<dd>Searches for applications and runtimes matching TEXT. Note that this uses appstream data that can be updated with the <code>flatpak update</code> command. The appstream data is updated automatically only if it&#8217;s at least a day old.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Only search through remotes in the per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Only search through remotes in the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Show a system-wide installation by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
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
<p> <code>&#8211;columns=FIELD,&#8230;</code></p>
<dl>
<dt>
<dd> Specify what information to show about each result. You can list multiple fields, or use this option multiple times. </p>
<p> Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names to change ellipsization.</dl>
<h2>FIELDS</h2>
<p> The following fields are understood by the <code>&#8211;columns</code> option: </p>
<p> name</p>
<dl>
<dt>
<dd> Show the name</dl>
<p> description</p>
<dl>
<dt>
<dd> Show the description</dl>
<p> application</p>
<dl>
<dt>
<dd> Show the application ID</dl>
<p> version</p>
<dl>
<dt>
<dd> Show the version</dl>
<p> version</p>
<dl>
<dt>
<dd> Show the branch</dl>
<p> remotes</p>
<dl>
<dt>
<dd> Show the remotes</dl>
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
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1) </p>
<h2>Index</h2>
