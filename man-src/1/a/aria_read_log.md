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
<p> <code>aria_read_log</code> <i>OPTIONS</i></p>
<p> Display and apply log records from a Aria transaction log found in the current directory (for now) </p>
<p> Note: Aria is compiled without <code>-DIDENTICAL_PAGES_AFTER_RECOVERY</code> which means that the table files are not byte-to-byte identical to files created during normal execution. This should be ok, except for test scripts that tries to compare files before and after recovery. </p>
<p> You need to use one of <code>-d</code> or <code>-a</code></p>
<dl>
<dt><code>-a</code>, <code>&#8211;apply</code></dt>
<dd> Apply log to tables: modifies tables! you should make a backup first! Displays a lot of information if not run with <code>&#8211;silent</code></dd>
<dt><code>&#8211;character-sets-dir</code>=<i>name</i></dt>
<dd> Directory where character sets are.</dd>
<dt><code>-c</code>, <code>&#8211;check</code></dt>
<dd> if <code>&#8211;display-only</code>, check if record is fully readable (for debugging)</dd>
<dt><code>-#</code>, <code>&#8211;debug</code>[=<i>name</i>]</dt>
<dd> Output debug log. Often the argument is &#8216;d:t:o,filename&#8217;.</dd>
<dt><code>&#8211;force-crash=</code>#</dt>
<dd> Force crash after # recovery events</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Display this help and exit.</dd>
<dt><code>-d</code>, <code>&#8211;display-only</code></dt>
<dd> display brief info read from records&#8217; header</dd>
<dt><code>-e</code>, <code>&#8211;end-lsn=</code>#</dt>
<dd> Stop applying at this lsn. If end-lsn is used, UNDO:s will not be applied</dd>
<dt><code>-h</code>, <code>&#8211;aria-log-dir-path</code>=<i>name</i></dt>
<dd> Path to the directory where to store transactional log</dd>
<dt><code>-P</code>, <code>&#8211;page-buffer-size=</code>#</dt>
<dd> The size of the buffer used for index blocks for Aria tables</dd>
<dt><code>-o</code>, <code>&#8211;start-from-lsn=</code>#</dt>
<dd> Start reading log from this lsn</dd>
<dt><code>-C</code>, <code>&#8211;start-from-checkpoint</code></dt>
<dd> Start applying from last checkpoint</dd>
<dt><code>-s</code>, <code>&#8211;silent</code></dt>
<dd> Print less information during apply/undo phase</dd>
<dt><code>-T</code>, <code>&#8211;tables-to-redo</code>=<i>name</i></dt>
<dd> List of tables sepearated with , that we should apply REDO on. Use this if you only want to recover some tables</dd>
<dt><code>-t</code>, <code>&#8211;tmpdir</code>=<i>name</i></dt>
<dd> Path for temporary files. Multiple paths can be specified, separated by colon (:)</dd>
<dt><code>&#8211;translog-buffer-size=</code>#</dt>
<dd> The size of the buffer used for transaction log for Aria tables</dd>
<dt><code>-u</code>, <code>&#8211;undo</code></dt>
<dd> Apply UNDO records to tables. (disable with <code>&#8211;disable-undo</code>) (Defaults to on; use <code>&#8211;skip-undo</code> to disable.)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print more information during apply/undo phase</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version and exit.</dd></dl>
<p> Default options are read from the following files in the given order: <code>/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf</code> </p>
<p> The following groups are read: <code>aria_read_log</code> </p>
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
<p> <code><a href="/docs/linux/man/1-myisamlog/">myisamlog</a>(1)</code> </p>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a> </p>
