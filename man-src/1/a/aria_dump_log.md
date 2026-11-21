---

title: "aria_dump_log(1)"
name: "aria_dump_log"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aria_dump_log/"
description: "aria_dump_log – Dump content of Aria log pages."
---

<p> aria_dump_log &#8211; Dump content of Aria log pages.</p>
<h2>SYNOPSIS</h2>
<p> <code>aria_dump_log</code> <i>-f file OPTIONS</i></p>
<h2>DESCRIPTION</h2>
<p> Dump content of Aria log pages.</p>
<dl>
<dt><code>-#</code>, <code>&#8211;debug</code>[=<i>name</i>]</dt>
<dd> Output debug log. Often the argument is &#8216;d:t:o,filename&#8217;.</dd>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>name</i></dt>
<dd> Path to file which will be read</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Display this help and exit.</dd>
<dt><code>-o</code>, <code>&#8211;offset=</code>#</dt>
<dd> Start reading log from this offset</dd>
<dt><code>-n</code>, <code>&#8211;pages=</code>#</dt>
<dd> Number of pages to read</dd>
<dt><code>-U</code>, <code>&#8211;unit-test</code></dt>
<dd> Use unit test record table (for logs created by unittests</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version and exit.</dd></dl>
<p> Default options are read from the following files in the given order: <code>/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf </p>
<p> The following groups are read: aria_dump_log</code> </p>
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
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a></p>
<h2>AUTHOR</h2>
<p> MariaDB Foundation (<a rel="nofollow" href="http://www.mariadb.org/">http://www.mariadb.org/</a>). </p>
