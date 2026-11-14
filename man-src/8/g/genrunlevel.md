---
title: "genrunlevel(8)"
name: "genrunlevel"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genrunlevel/"
description: "genrunlevel – create initng’s runlevels"
---

<p>genrunlevel &#8211; create initng&#8217;s runlevels</p>
<h2>Synopsis</h2>
<p><code>genrunlevel</code> [<code>&#8211;overwrite</code>] [<code>&#8211;path </code><i>PATH</i>] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[<code>&#8211;destdir </code><i>PATH</i>] [<code>&#8211;confdir </code><i>PATH</i>]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[<code>&#8211;all</code> | <i>file1 file2 &#8230;</i>]<br />
 <code>genrunlevel &#8211;migrate</code> </p>
<h2>Description</h2>
<p><code>genrunlevel</code> creates the runlevels and virtuals used by initng. Generally these are <i>default.runlevel</i> and <i>system.virtual</i>. <code>genrunlevel &#8211;migrate</code> fixes your runlevels when there&#8217;s a change in initng-ifiles. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;overwrite</code></p>
<dd>Overwrite files if they exist.</p>
<dt><code>&#8211;path </code><i>PATH</i></p>
<dd>Sets the search path for executables.</p>
<dt><code>&#8211;destdir </code><i>PATH</i></p>
<dd>Destination path prefix (default: /).</p>
<dt><code>&#8211;confdir </code><i>PATH</i></p>
<dd>Configuration directory (default: /etc/initng).</p>
<dt><code>&#8211;all</code></p>
<dd>Create all runlevels.</p>
<dt><i>file1 file2 &#8230;</i></p>
<dd>Create file1 file2 &#8230; fileN runlevels. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-initng/">initng</a>(8),</code> <code><a href="/docs/linux/man/8-ngc/">ngc</a>(8),</code> <code><a href="/docs/linux/man/8-ngdc/">ngdc</a>(8),</code> <code><a href="/docs/linux/man/8-ng-update/">ng-update</a>(8),</code> <code><a href="/docs/linux/man/8-install_service/">install_service</a>(8),</code> <code><a href="/docs/linux/man/8-system_off/">system_off</a>(8).</code></p>
<h2>Author</h2>
<p>initng was written by Jimmy Wennlund &lt;jimmy.wennlund [at] gmail.com&gt; and can be found at <a rel="nofollow" href="http://www.initng.org/.">http://www.initng.org/.</a> </p>
<p> This manual page was written by Ismael Luceno &lt;ismael.luceno [at] gmail.com&gt;. Loosely based on gen_system_runlevel manual page, by Armin Berres &lt;a.berres [at] web.de&gt;.</p>
