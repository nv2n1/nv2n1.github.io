---
title: "aria_read_log(1)"
name: "aria_read_log"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aria_read_log/"
description: "aria_read_log – display Aria log file contents"
---

<h2>NAME</h2>
<p> aria_read_log &#8211; display Aria log file contents</p>
<h2>SYNOPSIS</h2>
<p> <code>aria_read_log</code> <i>OPTIONS</i></p>
<h2>DESCRIPTION</h2>
<p> Display and apply log records from a Aria transaction log found in the current directory (for now) </p>
<p> Note: Aria is compiled without <code>-DIDENTICAL_PAGES_AFTER_RECOVERY</code> which means that the table files are not byte-to-byte identical to files created during normal execution. This should be ok, except for test scripts that tries to compare files before and after recovery. </p>
<p> You need to use one of <code>-d</code> or <code>-a</code></p>
<dl>
<dt><code>-a</code>, <code>&#8211;apply</code></p>
<dd> Apply log to tables: modifies tables! you should make a backup first! Displays a lot of information if not run with <code>&#8211;silent</code></p>
<dt><code>&#8211;character-sets-dir</code>=<i>name</i></p>
<dd> Directory where character sets are.</p>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> if <code>&#8211;display-only</code>, check if record is fully readable (for debugging)</p>
<dt><code>-#</code>, <code>&#8211;debug</code>[=<i>name</i>]</p>
<dd> Output debug log. Often the argument is &#8216;d:t:o,filename&#8217;.</p>
<dt><code>&#8211;force-crash=</code>#</p>
<dd> Force crash after # recovery events</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display this help and exit.</p>
<dt><code>-d</code>, <code>&#8211;display-only</code></p>
<dd> display brief info read from records&#8217; header</p>
<dt><code>-e</code>, <code>&#8211;end-lsn=</code>#</p>
<dd> Stop applying at this lsn. If end-lsn is used, UNDO:s will not be applied</p>
<dt><code>-h</code>, <code>&#8211;aria-log-dir-path</code>=<i>name</i></p>
<dd> Path to the directory where to store transactional log</p>
<dt><code>-P</code>, <code>&#8211;page-buffer-size=</code>#</p>
<dd> The size of the buffer used for index blocks for Aria tables</p>
<dt><code>-o</code>, <code>&#8211;start-from-lsn=</code>#</p>
<dd> Start reading log from this lsn</p>
<dt><code>-C</code>, <code>&#8211;start-from-checkpoint</code></p>
<dd> Start applying from last checkpoint</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Print less information during apply/undo phase</p>
<dt><code>-T</code>, <code>&#8211;tables-to-redo</code>=<i>name</i></p>
<dd> List of tables sepearated with , that we should apply REDO on. Use this if you only want to recover some tables</p>
<dt><code>-t</code>, <code>&#8211;tmpdir</code>=<i>name</i></p>
<dd> Path for temporary files. Multiple paths can be specified, separated by colon (:)</p>
<dt><code>&#8211;translog-buffer-size=</code>#</p>
<dd> The size of the buffer used for transaction log for Aria tables</p>
<dt><code>-u</code>, <code>&#8211;undo</code></p>
<dd> Apply UNDO records to tables. (disable with <code>&#8211;disable-undo</code>) (Defaults to on; use <code>&#8211;skip-undo</code> to disable.)</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print more information during apply/undo phase</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit.</dl>
<p> Default options are read from the following files in the given order: <code>/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf</code> </p>
<p> The following groups are read: <code>aria_read_log</code> </p>
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
<p> <code><a href="/docs/linux/man/1-myisamlog/">myisamlog</a>(1)</code> </p>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a> </p>
<h2>Index</h2>
