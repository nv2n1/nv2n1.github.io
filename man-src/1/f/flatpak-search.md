---

title: "flatpak-search(1)"
name: "flatpak-search"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-search/"
description: "flatpak-search – Search for applications and runtimes"
---

<p> flatpak-search &#8211; Search for applications and runtimes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak search</code> TEXT</dt></dl>
<h2>DESCRIPTION</h2>
<dd>Searches for applications and runtimes matching TEXT. Note that this uses appstream data that can be updated with the <code>flatpak update</code> command. The appstream data is updated automatically only if it&#8217;s at least a day old.</dd>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
</dt><dd> Only search through remotes in the per-user installation.</dd></dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
</dt><dd> Only search through remotes in the default system-wide installation.</dd></dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
</dt><dd> Show a system-wide installation by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dd></dl>
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
<p> <code>&#8211;columns=FIELD,&#8230;</code></p>
<dl>
<dt>
</dt><dd> Specify what information to show about each result. You can list multiple fields, or use this option multiple times. </dd>
<p> Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names to change ellipsization.</dl>
<h2>FIELDS</h2>
<p> The following fields are understood by the <code>&#8211;columns</code> option: </p>
<p> name</p>
<dl>
<dt>
</dt><dd> Show the name</dd></dl>
<p> description</p>
<dl>
<dt>
</dt><dd> Show the description</dd></dl>
<p> application</p>
<dl>
<dt>
</dt><dd> Show the application ID</dd></dl>
<p> version</p>
<dl>
<dt>
</dt><dd> Show the version</dd></dl>
<p> version</p>
<dl>
<dt>
</dt><dd> Show the branch</dd></dl>
<p> remotes</p>
<dl>
<dt>
</dt><dd> Show the remotes</dd></dl>
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
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1) </p>
