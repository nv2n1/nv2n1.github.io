---
title: "aria_chk(1)"
name: "aria_chk"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aria_chk/"
description: "aria_chk – Aria table-maintenance utility"
---

<h2>NAME</h2>
<p> aria_chk &#8211; Aria table-maintenance utility</p>
<h2>SYNOPSIS</h2>
<p> <code>aria_chk</code> [<i>OPTIONS</i>] <i>tables</i>[<i>.MAI</i>]</p>
<h2>DESCRIPTION</h2>
<p> Describe, check and repair of Aria tables. Used without options all tables on the command will be checked for errors</p>
<h3>Global options</h3>
<dl>
<dt><code>-#</code>, <code>&#8211;debug=</code>&#8230;</p>
<dd> Output debug log. Often this is &#8216;d:t:o,filename&#8217;.</p>
<dt><code>-H</code>, <code>&#8211;HELP</code></p>
<dd> Print all argument options sorted alphabetically.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print all options by groups</p>
<dt><code>&#8211;datadir</code>=<i>path</i></p>
<dd> Path for control file (and logs if <code>&#8211;logdir</code> not used)</p>
<dt><code>&#8211;logdir</code>=<i>path</i></p>
<dd> Path for log files</p>
<dt><code>&#8211;ignore-control-file</code></p>
<dd> Don&#8217;t open the control file. Only use this if you are sure the tables are not in use by another program!</p>
<dt><code>&#8211;require-control-file</code></p>
<dd> Abort if we can&#8217;t find/read the maria_log_control file</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Only print errors. One can use two <code>-s</code> to make maria_chk very silent.</p>
<dt><code>-t</code>, <code>&#8211;tmpdir</code>=<i>path</i></p>
<dd> Path for temporary files. Multiple paths can be specified, separated by colon (:), they will be used in a round-robin fashion.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print more information. This can be used with <code>&#8211;description</code> and <code>&#8211;check</code>. Use many <code>-v</code> for more verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit.</p>
<dt><code>-w</code>, <code>&#8211;wait</code></p>
<dd> Wait if table is locked.</dl>
<h3>Check options (check is the default action for aria_chk)</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> Check table for errors.</p>
<dt><code>-e</code>, <code>&#8211;extend-check</code></p>
<dd> Check the table VERY throughly. Only use this in extreme cases as aria_chk should normally be able to find out if the table is ok even without this switch.</p>
<dt><code>-F</code>, <code>&#8211;fast</code></p>
<dd> Check only tables that haven&#8217;t been closed properly.</p>
<dt><code>-C</code>, <code>&#8211;check-only-changed</code></p>
<dd> Check only tables that have changed since last check.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Restart with &#8216;-r&#8217; if there are any errors in the table. States will be updated as with &#8216;&#8211;update-state&#8217;.</p>
<dt><code>-i</code>, <code>&#8211;information</code></p>
<dd> Print statistics information about table that is checked.</p>
<dt><code>-m</code>, <code>&#8211;medium-check</code></p>
<dd> Faster than extend-check, but only finds 99.99% of all errors. Should be good enough for most cases.</p>
<dt><code>-T</code>, <code>&#8211;read-only</code></p>
<dd> Don&#8217;t mark table as checked.</p>
<dt><code>-U</code>, <code>&#8211;update-state</code></p>
<dd> Mark tables as crashed if any errors were found and clean if check didn&#8217;t find any errors but table was marked as &#8216;not clean&#8217; before. This allows one to get rid of warnings like &#8216;table not properly closed&#8217;. If table was updated, update also the timestamp for when the check was made. This option is on by default! Use <code>&#8211;skip-update-state</code> to disable.</p>
<dt> <code>&#8211;warning-for-wrong-transaction-id</code></p>
<dt>
<dd>
<dd>Give a warning if we find a transaction id in the table that is bigger than what exists in the control file. Use <code>&#8211;skip-</code>&#8230; to disable warning</dl>
<h3>Recover (repair)/ options (When using &#8216;&#8211;recover&#8217; or &#8216;&#8211;safe-recover&#8217;)</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;backup</code></p>
<dd> Make a backup of the .MAD file as &#8216;filename-time.BAK&#8217;.</p>
<dt><code>&#8211;correct-checksum</code></p>
<dd> Correct checksum information for table.</p>
<dt><code>-D</code>, <code>&#8211;data-file-length=</code>#</p>
<dd> Max length of data file (when recreating data file when it&#8217;s full).</p>
<dt><code>-e</code>, <code>&#8211;extend-check</code></p>
<dd> Try to recover every possible row from the data file Normally this will also find a lot of garbage rows; Don&#8217;t use this option if you are not totally desperate.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Overwrite old temporary files.</p>
<dt><code>-k</code>, <code>&#8211;keys-used=</code>#</p>
<dd> Tell Aria to update only some specific keys. # is a bit mask of which keys to use. This can be used to get faster inserts.</p>
<dt><code>&#8211;max-record-length=</code>#</p>
<dd> Skip rows bigger than this if aria_chk can&#8217;t allocate memory to hold it.</p>
<dt><code>-r</code>, <code>&#8211;recover</code></p>
<dd> Can fix almost anything except unique keys that aren&#8217;t unique.</p>
<dt><code>-n</code>, <code>&#8211;sort-recover</code></p>
<dd> Forces recovering with sorting even if the temporary file would be very big.</p>
<dt><code>-p</code>, <code>&#8211;parallel-recover</code></p>
<dd> Uses the same technique as &#8216;-r&#8217; and &#8216;-n&#8217;, but creates all the keys in parallel, in different threads.</p>
<dt><code>-o</code>, <code>&#8211;safe-recover</code></p>
<dd> Uses old recovery method; Slower than &#8216;-r&#8217; but can handle a couple of cases where &#8216;-r&#8217; reports that it can&#8217;t fix the data file.</p>
<dt><code>&#8211;transaction-log</code></p>
<dd> Log repair command to transaction log. This is needed if one wants to use the aria_read_log to repeat the repair</p>
<dt><code>&#8211;character-sets-dir=</code>&#8230;</p>
<dd> Directory where character sets are.</p>
<dt><code>&#8211;set-collation</code>=<i>name</i></p>
<dd> Change the collation used by the index.</p>
<dt><code>-q</code>, <code>&#8211;quick</code></p>
<dd> Faster repair by not modifying the data file. One can give a second &#8216;-q&#8217; to force aria_chk to modify the original datafile in case of duplicate keys. NOTE: Tables where the data file is currupted can&#8217;t be fixed with this option.</p>
<dt><code>-u</code>, <code>&#8211;unpack</code></p>
<dd> Unpack file packed with ariapack.</dl>
<h3>Other actions</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;analyze</code></p>
<dd> Analyze distribution of keys. Will make some joins in MariaDB faster. You can check the calculated distribution by using &#8216;&#8211;description <code>&#8211;verbose</code> table_name&#8217;.</p>
<dt><code>&#8211;stats_method</code>=<i>name</i></p>
<dd> Specifies how index statistics collection code should treat NULLs. Possible values of name are &quot;nulls_unequal&quot; (default for 4.1/5.0), &quot;nulls_equal&quot; (emulate 4.0), and &quot;nulls_ignored&quot;.</p>
<dt><code>-d</code>, <code>&#8211;description</code></p>
<dd> Prints some information about table.</p>
<dt><code>-A</code>, <code>&#8211;set-auto-increment</code>[=<i>value</i>]</p>
<dd> Force auto_increment to start at this or higher value If no value is given, then sets the next auto_increment value to the highest used value for the auto key + 1.</p>
<dt><code>-S</code>, <code>&#8211;sort-index</code></p>
<dd> Sort index blocks. This speeds up &#8216;read-next&#8217; in applications.</p>
<dt><code>-R</code>, <code>&#8211;sort-records=</code>#</p>
<dd> Sort records according to an index. This makes your data much more localized and may speed up things (It may be VERY slow to do a sort the first time!).</p>
<dt><code>-b</code>, <code>&#8211;block-search=</code>#</p>
<dd> Find a record, a block at given offset belongs to.</p>
<dt><code>-z</code>, <code>&#8211;zerofill</code></p>
<dd> Fill empty space in data and index files with zeroes. This makes the data file movable between different servers.</p>
<dt><code>&#8211;zerofill-keep-lsn</code></p>
<dd> Like <code>&#8211;zerofill</code> but does not zero out LSN of data/index pages.</dl>
<h3>Variables</h3>
<dl>
<dt><code>&#8211;page_buffer_size=</code>#</p>
<dd> Size of page buffer. Used by <code>&#8211;safe-repair</code></p>
<dt><code>&#8211;read_buffer_size=</code>#</p>
<dd> Read buffer size for sequential reads during scanning</p>
<dt><code>&#8211;sort_buffer_size=</code>#</p>
<dd> Size of sort buffer. Used by <code>&#8211;recover</code></p>
<dt><code>&#8211;sort_key_blocks=</code>#</p>
<dd> Internal buffer for sorting keys; Don&#8217;t touch.</p>
<dt><code>&#8211;write_buffer_size=</code>#</p>
<dd> Write buffer size for sequential writes during repair</dl>
<p> Default options are read from the following files in the given order: <code>/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf</code> </p>
<p> The following groups are read: <code>aria_chk</code> </p>
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
<p> <code><a href="/docs/linux/man/1-myisamchk/">myisamchk</a>(1)</code> </p>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a> </p>
<h2>Index</h2>
