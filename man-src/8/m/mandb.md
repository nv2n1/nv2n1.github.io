---
title: "mandb(8)"
name: "mandb"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mandb/"
description: "mandb – create or update the manual page index caches"
---

<p>mandb &#8211; create or update the manual page index caches</p>
<h2>Synopsis</h2>
<p><code>mandb</code> [<code>-dqsucpt?V</code>] [<code>-C</code> <i>file</i>] [<i>manpath</i>]<br />
 <code>mandb</code> [<code>-dqsut</code>] [<code>-C</code> <i>file</i>] <code>-f</code> <i>filename</i>&nbsp;&#8230;</p>
<h2>Description</h2>
<p><code>mandb</code> is used to initialise or manually update <code>index</code> database caches. The caches contain information relevant to the current state of the manual page system and the information stored within them is used by the man-db utilities to enhance their speed and functionality. </p>
<p> When creating or updating an <code>index</code>, <code>mandb</code> will warn of bad ROFF .so requests, bogus manual page filenames and manual pages from which the <code>whatis</code> cannot be parsed. </p>
<p> Supplying <code>mandb</code> with an optional colon-delimited path will override the internal system manual page hierarchy search path, determined from information found within the man-db configuration file.</p>
<h2>Database Caches</h2>
<p><code>mandb</code> can be compiled with support for any one of the following database types. </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Async</td>
<td>Filename
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Berkeley db</td>
<td>Yes</td>
<td><i>index.bt</i>
</td>
</tr>
<tr VALIGN=top>
<td>GNU gdbm</td>
<td>Yes</td>
<td><i>index.db</i>
</td>
</tr>
<tr VALIGN=top>
<td>UNIX ndbm</td>
<td>No</td>
<td><i>index.(dir|pag)</i>
</td>
</tr>
</table>
<p> Those database types that support asynchronous updates provide enhanced speed at the cost of possible corruption in the event of unusual termination. In an unusual case where this has occurred, it may be necessary to rerun <code>mandb</code> with the <code>-c</code> option to re-create the databases from scratch.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Print debugging information.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Produce no warnings.</p>
<dt><code>-s</code>, <code>&#8211;no-straycats</code></p>
<dd>Do not spend time looking for or adding information to the databases regarding stray cats.</p>
<dt><code>-p</code>, <code>&#8211;no-purge</code></p>
<dd>Do not spend time checking for deleted manual pages and purging them from the databases.</p>
<dt><code>-c</code>, <code>&#8211;create</code></p>
<dd>By default, <code>mandb</code> will try to update any previously created databases. If a database does not exist, it will create it. This option forces <code>mandb</code> to delete previous databases and re-create them from scratch, and implies <code>&#8211;no-purge.</code> This may be necessary if a database becomes corrupt or if a new database storage scheme is introduced in the future.</p>
<dt><code>-u</code>, <code>&#8211;user-db</code></p>
<dd>Create user databases only, even with write permissions necessary to create system databases.</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd>Perform correctness checks on manual pages in the hierarchy search path. With this option, <code>mandb</code> will not alter existing databases.</p>
<dt><code>-f</code>, <code>&#8211;filename</code></p>
<dd>Update only the entries for the given filename. This option is not for general use; it is used internally by <code>man</code> when it has been compiled with the <code>MAN_DB_UPDATES</code> option and finds that a page is out of date. It implies <code>-p</code> and disables <code>-c</code> and <code>-s</code>.</p>
<dt><code>-C&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;config-file=</code><i>file</i></p>
<dd>Use this user configuration file rather than the default of <i>~/.manpath</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Show the usage message, then exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Print a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version, then exit.</dl>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></p>
<dd>Successful program execution.</p>
<dt><code>1</code></p>
<dd>Usage, syntax, or configuration file error.</p>
<dt><code>2</code></p>
<dd>Operational error.</p>
<dt><code>3</code></p>
<dd>A child process failed.</dl>
<h2>Diagnostics</h2>
<p>The following warning messages can be emitted during database building.</p>
<dl>
<dt><code>&lt;filename&gt;: whatis parse for page(sec) failed</code></p>
<dd>An attempt to extract whatis line(s) from the given &lt;filename&gt; failed. This is usually due to a poorly written manual page, but if many such messages are emitted it is likely that the system contains non-standard manual pages which are incompatible with the man-db whatis parser. See the <code>WHATIS PARSING</code> section in <code><a href="/docs/linux/man/1-lexgrog/">lexgrog</a></code>(1) for more information.</p>
<dt><code>&lt;filename&gt;: is a dangling symlink</code></p>
<dd>&lt;filename&gt; does not exist but is referenced by a symbolic link. Further diagnostics are usually emitted to identify the &lt;filename&gt; of the offending link.</p>
<dt><code>&lt;filename&gt;: bad symlink or ROFF `.so&#8217; request</code></p>
<dd>&lt;filename&gt; is either a symbolic link to, or contains a ROFF include request to, a non existent file.</p>
<dt><code>&lt;filename&gt;: ignoring bogus filename</code></p>
<dd>The &lt;filename&gt; may or may not be a valid manual page but its name is invalid. This is usually due to a manual page with sectional extension &lt;x&gt; being put in manual page section &lt;y&gt;.</p>
<dt><code>&lt;filename_mask&gt;: competing extensions</code></p>
<dd>The wildcard &lt;filename_mask&gt; is not unique. This is usually caused by the existence of both a compressed and uncompressed version of the same manual page. All but the most recent are ignored.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/manpath.config</i></p>
<dd>man-db configuration file.</p>
<dt><i>/var/cache/man/index.(bt|db|dir|pag)</i></p>
<dd>An FHS compliant global <i>index</i> database cache.</dl>
<p> Older locations for the database cache included:</p>
<dl>
<dt><i>/usr/man/index.(bt|db|dir|pag)</i></p>
<dd>A traditional global <i>index</i> database cache.</p>
<dt><i>/var/catman/index.(bt|db|dir|pag)</i></p>
<dd>An alternate or FSSTND compliant global <i>index</i> database cache.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lexgrog/">lexgrog</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5), <code><a href="/docs/linux/man/8-catman/">catman</a></code>(8) </p>
<p> The <code>WHATIS PARSING</code> section formerly in this manual page is now part of <code><a href="/docs/linux/man/1-lexgrog/">lexgrog</a></code>(1).</p>
<h2>Author</h2>
<pre>Wilf. (G.Wilford [at] ee.surrey.ac.uk).
Fabrizio Polacco (fpolacco [at] debian.org).
Colin Watson (cjwatson [at] debian.org).</pre>
<h2>Bugs</h2>
<p><a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
