---
title: "aria_pack(1)"
name: "aria_pack"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aria_pack/"
description: "aria_pack – generate compressed, read-only Aria tables"
---

<h2>NAME</h2>
<p> aria_pack &#8211; generate compressed, read-only Aria tables</p>
<h2>SYNOPSIS</h2>
<p> <code>aria_pack</code> [<i>OPTIONS</i>] <i>filename</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Pack a Aria-table to take much less space. Keys are not updated, you must run <code>aria_chk -rq</code> on the index (.MAI) file afterwards to update the keys. You should give the .MAI file as the filename argument. To unpack a packed table, run <code>aria_chk -u</code> on the table</p>
<dl>
<dt><code>-b</code>, <code>&#8211;backup</code></p>
<dd> Make a backup of the table as table_name.OLD.</p>
<dt><code>&#8211;character-sets-dir</code>=<i>name</i></p>
<dd> Directory where character sets are.</p>
<dt><code>-#</code>, <code>&#8211;debug</code>[=<i>name</i>]</p>
<dd> Output debug log. Often this is &#8216;d:t:o,filename&#8217;.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force packing of table even if it gets bigger or if tempfile exists.</p>
<dt><code>-j</code>, <code>&#8211;join</code>=<i>name</i></p>
<dd> Join all given tables into &#8216;new_table_name&#8217;. All tables MUST have identical layouts.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display this help and exit.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Be more silent.</p>
<dt><code>-T</code>, <code>&#8211;tmpdir</code>=<i>name</i></p>
<dd> Use temporary directory to store temporary table.</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> Don&#8217;t pack table, only test packing it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Write info about progress and packing result. Use many <code>-v</code> for more verbosity!</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>-w</code>, <code>&#8211;wait</code></p>
<dd> Wait and retry if table is in use.</dl>
<p> Default options are read from the following files in the given order: <code>/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf</code> </p>
<p> The following groups are read: <code>ariapack</code> </p>
<p> The following options may be given as the first argument:</p>
<dl>
<dt><code>&#8211;print-defaults</code></p>
<dd> Print the program argument list and exit.</p>
<dt><code>&#8211;no-defaults</code></p>
<dd> Don&#8217;t read default options from any option file.</p>
<dt><code>&#8211;defaults-file=</code>#</p>
<dd> Only read default options from the given file #.</p>
<dt><code>&#8211;defaults-extra-file=</code>#</p>
<dd> Read this file after the global files are read.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-myisampack/">myisampack</a>(1)</code> </p>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a> </p>
<h2>Index</h2>
