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
<p> <code>aria_pack</code> [<i>OPTIONS</i>] <i>filename</i>&#8230;</p>
<p> Pack a Aria-table to take much less space. Keys are not updated, you must run <code>aria_chk -rq</code> on the index (.MAI) file afterwards to update the keys. You should give the .MAI file as the filename argument. To unpack a packed table, run <code>aria_chk -u</code> on the table</p>
<dl>
<dt><code>-b</code>, <code>&#8211;backup</code></dt>
<dd> Make a backup of the table as table_name.OLD.</dd>
<dt><code>&#8211;character-sets-dir</code>=<i>name</i></dt>
<dd> Directory where character sets are.</dd>
<dt><code>-#</code>, <code>&#8211;debug</code>[=<i>name</i>]</dt>
<dd> Output debug log. Often this is &#8216;d:t:o,filename&#8217;.</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> Force packing of table even if it gets bigger or if tempfile exists.</dd>
<dt><code>-j</code>, <code>&#8211;join</code>=<i>name</i></dt>
<dd> Join all given tables into &#8216;new_table_name&#8217;. All tables MUST have identical layouts.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Display this help and exit.</dd>
<dt><code>-s</code>, <code>&#8211;silent</code></dt>
<dd> Be more silent.</dd>
<dt><code>-T</code>, <code>&#8211;tmpdir</code>=<i>name</i></dt>
<dd> Use temporary directory to store temporary table.</dd>
<dt><code>-t</code>, <code>&#8211;test</code></dt>
<dd> Don&#8217;t pack table, only test packing it.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Write info about progress and packing result. Use many <code>-v</code> for more verbosity!</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Output version information and exit.</dd>
<dt><code>-w</code>, <code>&#8211;wait</code></dt>
<dd> Wait and retry if table is in use.</dd></dl>
<p> Default options are read from the following files in the given order: <code>/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf</code> </p>
<p> The following groups are read: <code>ariapack</code> </p>
<p> The following options may be given as the first argument:</p>
<dl>
<dt><code>&#8211;print-defaults</code></dt>
<dd> Print the program argument list and exit.</dd>
<dt><code>&#8211;no-defaults</code></dt>
<dd> Don&#8217;t read default options from any option file.</dd>
<dt><code>&#8211;defaults-file=</code>#</dt>
<dd> Only read default options from the given file #.</dd>
<dt><code>&#8211;defaults-extra-file=</code>#</dt>
<dd> Read this file after the global files are read.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-myisampack/">myisampack</a>(1)</code> </p>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a> </p>
