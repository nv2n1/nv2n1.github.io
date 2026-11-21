---
title: "flatpak-remotes(1)"
name: "flatpak-remotes"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-remotes/"
description: "flatpak-remotes – List remote repositories"
---

<h2 class="name">NAME</h2>
<p> flatpak-remotes &#8211; List remote repositories </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak remotes</code> [OPTION&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>Lists the known remote repositories, in priority order. </dd>
<p> By default, both per-user and system-wide installations are shown. Use the <code>&#8211;user</code>, <code>&#8211;system</code> or <code>&#8211;installation</code> options to change this.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help options and exit.</dd></dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
</dt><dd> Show the per-user configuration.</dd></dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
</dt><dd> Show the default system-wide configuration.</dd></dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
</dt><dd> Show a system-wide installation by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dd></dl>
<p> <code>-d</code>, <code>&#8211;show-details</code></p>
<dl>
<dt>
</dt><dd> Show more information for each repository in addition to the name. Equivalent to <code>&#8211;columns=all</code>.</dd></dl>
<p> <code>&#8211;show-disabled</code></p>
<dl>
<dt>
</dt><dd> Show disabled repos.</dd></dl>
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
<p> name</p>
<dl>
<dt>
</dt><dd> Show the name of the remote</dd></dl>
<p> title</p>
<dl>
<dt>
</dt><dd> Show the title of the remote</dd></dl>
<p> url</p>
<dl>
<dt>
</dt><dd> Show the URL of the remote</dd></dl>
<p> filter</p>
<dl>
<dt>
</dt><dd> Show the path to the client-side filter of the remote.</dd></dl>
<p> collection</p>
<dl>
<dt>
</dt><dd> Show the collection ID of the remote</dd></dl>
<p> priority</p>
<dl>
<dt>
</dt><dd> Show the priority of the remote</dd></dl>
<p> options</p>
<dl>
<dt>
</dt><dd> Show options</dd></dl>
<p> comment</p>
<dl>
<dt>
</dt><dd> Show comment</dd></dl>
<p> description</p>
<dl>
<dt>
</dt><dd> Show description</dd></dl>
<p> homepage</p>
<dl>
<dt>
</dt><dd> Show homepage</dd></dl>
<p> icon</p>
<dl>
<dt>
</dt><dd> Show icon</dd></dl>
<p> all</p>
<dl>
<dt>
</dt><dd> Show all columns</dd></dl>
<p> help</p>
<dl>
<dt>
</dt><dd> Show the list of available columns</dd></dl>
<p> Note that field names can be abbreviated to a unique prefix.</p>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak remotes &#8211;user &#8211;show-details</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
testrepo        Test Repository  <a rel="nofollow" href="http://209.132.179.91/repo/">http://209.132.179.91/repo/</a> no-gpg-verify
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-add/">flatpak-remote-add</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-delete/">flatpak-remote-delete</a></code>(1) </p>
