---
title: "yumdb(8)"
name: "yumdb"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yumdb/"
description: "yumdb – query and alter the Yum database"
---

<p>yumdb &#8211; query and alter the Yum database</p>
<h2>Synopsis</h2>
<p><code>yumdb</code> [command] [packages &#8230;]</p>
<h2>Description</h2>
<p>This command is used to query and alter the yum database, which is a simple key value store used in conjunction with the rpm database. Any installed package can have arbitrary data in the yum database, however the main use case is to store extra data about packages as they are installed. yumdb <i>command</i>s are: </p>
<dl>
<dt><code>yumdb get &lt;key&gt; [pkg-wildcard]&#8230;</code></p>
<dd></dl>
<p> This command will get the value for the given key, limiting to any specified packages. </p>
<dl>
<dt><code>yumdb set &lt;key&gt; &lt;value&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will set the value for the given key, to the given value, limiting to any specified packages. </p>
<dl>
<dt>yumdb del &lt;key&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will delete the given key, limiting to any specified packages. </p>
<dl>
<dt>yumdb rename &lt;old-key&gt; &lt;new-key&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will rename the given old-key, to the given new-key, limiting to any specified packages. If the old-key does not exist, nothing happens. </p>
<dl>
<dt>yumdb rename-force &lt;old-key&gt; &lt;new-key&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will rename the given old-key, to the given new-key, limiting to any specified packages. If the old-key does not exist, new-key is deleted. </p>
<dl>
<dt>yumdb copy &lt;old-key&gt; &lt;new-key&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will copy the given old-key, to the given new-key, limiting to any specified packages. If the old-key does not exist, nothing happens. </p>
<dl>
<dt>yumdb copy-force &lt;old-key&gt; &lt;new-key&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will copy the given old-key, to the given new-key, limiting to any specified packages. If the old-key does not exist, new-key is deleted. </p>
<dl>
<dt>yumdb search &lt;key&gt; &lt;wildcard&gt;&#8230;</p>
<dd></dl>
<p> This command will search all packages for the given key, against any of the given wildcard values. </p>
<dl>
<dt>yumdb exist &lt;key&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will print any packages which have the given key, limiting to any specified packages. </p>
<dl>
<dt>yumdb unset &lt;key&gt; [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will print any packages which do not have the given key, limiting to any specified packages. </p>
<dl>
<dt>yumdb info [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will display all the data stored in the yumdb, limiting to any specified packages. </p>
<dl>
<dt>yumdb sync [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will add any missing data to the yumdb from the repositories, limiting to any specified packages. This is useful to run if you have had any aborted transactions (and thus. missing yumdb data). Note that &quot;yumdb sync&quot; cannot know all the information that would have been put into the yumdb at the time. </p>
<dl>
<dt>yumdb sync-force [pkg-wildcard]&#8230;</p>
<dd></dl>
<p> This command will replace any data in the yumdb from the repositories, limiting to any specified packages. </p>
<h2>Examples</h2>
<p>List all the packages which don&#8217;t have a from_repo key/value:</p>
<dl>
<dd>yumdb unset from_repo</dl>
<p> List all the packages which were installed as dependencies:</p>
<dl>
<dd>yumdb search reason dep </p>
<h2>Well Known Keys</h2>
<p>Note that there is no limit to the number of keys that can be created or what they may contain (for installed packages only). However this is a list of well known keys, and what they store. </p>
<pre><br>
<dl><dt><code>checksum_data<dd><dt>checksum_type<dd></dl>
These keys store the createrepo checksum, and it's type, of the available
package yum installed. Note that these are used by &quot;yum version&quot; to calculate
the rpmdb version.
<br>
<dl><dt>command_line<dd></dl>
This key stores the entire command line, of the yum command (if it was called).
<br>
<dl><dt>from_repo<dd><dt>from_repo_revision<dd><dt>from_repo_timestamp<dd></dl>
These keys take values from the available package yum installed, and store the
repo id, it's revision and timestamp.
<br>
<dl><dt>reason<dd></dl>
This key stores either &quot;user&quot; or &quot;dep&quot;, currently. To mark if the user requested
the package to be installed, or if it was brought in automatically as a
dependency. Note that this is kept over updates.
<br>
<dl><dt>releasever<dd></dl>
This key stores the value of releasever, when the package was installed.
<br>
<dl><dt>installonly<dd></dl>
If this attribute has the value &quot;keep&quot; then this package will not be
removed automatically by the installonly process (and does not count towards
the installonly_limit).
</code></pre>
<h2>See Also</h2>
<pre><i>yum (8)</i>
<i>rpm (8)</i></pre>
<h2>Authors</h2>
<pre>James Antill &lt;james.antill [at] redhat.com&gt;.</pre>
