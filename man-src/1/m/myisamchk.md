---
title: "myisamchk(1)"
name: "myisamchk"
section: "1"
letter: "m"
url: "/docs/linux/man/1-myisamchk/"
description: "myisamchk – MyISAM table-maintenance utility"
---

<h2 class="name">NAME</h2>
<p> myisamchk &#8211; MyISAM table-maintenance utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>myisamchk [</code><i>options</i><code>] </code><i>tbl_name</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>myisamchk</code> utility gets information about your database tables or checks, repairs, or optimizes them. <code>myisamchk</code> works with MyISAM tables (tables that have .MYD and .MYI files for storing data and indexes). </p>
<p> You can also use the CHECK TABLE and REPAIR TABLE statements to check and repair MyISAM tables. See Section 13.7.3.2, &#8220;CHECK TABLE Statement&#8221;, and Section 13.7.3.5, &#8220;REPAIR TABLE Statement&#8221;. </p>
<p> The use of <code>myisamchk</code> with partitioned tables is not supported. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Caution</code> </font> </p>
<p> It is best to make a backup of a table before performing a table repair operation; under some circumstances the operation might cause data loss. Possible causes include but are not limited to file system errors. </p>
</dl>
<p> Invoke <code>myisamchk</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisamchk [</code><i>options</i><code>] </code><i>tbl_name</i><code> ...</code>
</pre>
</dl>
<p> The <i>options</i> specify what you want <code>myisamchk</code> to do. They are described in the following sections. You can also get a list of options by invoking <code>myisamchk &#8211;help</code>. </p>
<p> With no options, <code>myisamchk</code> simply checks your table as the default operation. To get more information or to tell <code>myisamchk</code> to take corrective action, specify options as described in the following discussion. </p>
<p> <i>tbl_name</i> is the database table you want to check or repair. If you run <code>myisamchk</code> somewhere other than in the database directory, you must specify the path to the database directory, because <code>myisamchk</code> has no idea where the database is located. In fact, <code>myisamchk</code> does not actually care whether the files you are working on are located in a database directory. You can copy the files that correspond to a database table into some other location and perform recovery operations on them there. </p>
<p> You can name several tables on the <code>myisamchk</code> command line if you wish. You can also specify a table by naming its index file (the file with the .MYI suffix). This enables you to specify all tables in a directory by using the pattern *.MYI. For example, if you are in a database directory, you can check all the MyISAM tables in that directory like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisamchk *.MYI</code>
</pre>
</dl>
<p> If you are not in the database directory, you can check all the tables there by specifying the path to the directory: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisamchk </code><i>/path/to/database_dir/</i><code>*.MYI</code>
</pre>
</dl>
<p> You can even check all tables in all databases by specifying a wildcard with the path to the MySQL data directory: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisamchk </code><i>/path/to/datadir/*/*</i><code>.MYI</code>
</pre>
</dl>
<p> The recommended way to quickly check all MyISAM tables is: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisamchk --silent --fast </code><i>/path/to/datadir/*/*</i><code>.MYI</code>
</pre>
</dl>
<p> If you want to check all MyISAM tables and repair any that are corrupted, you can use the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; myisamchk-- silent-- force-- fast-- update - state-- key_buffer_size = 64M --myisam_sort_buffer_size = 64M --read_buffer_size = 1M --write_buffer_size = 1M / path / to / datadir/*/*.MYI
</code></pre>
</dl>
<p> This command assumes that you have more than 64MB free. For more information about memory allocation with <code>myisamchk</code>, see the section called &#8220;MYISAMCHK MEMORY USAGE&#8221;. </p>
<p> For additional information about using <code>myisamchk</code>, see Section 7.6, &#8220;MyISAM Table Maintenance and Crash Recovery&#8221;. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> <i>You must ensure that no other program is using the tables while you are running </i><i></i><code>myisamchk</code>. The most effective means of doing so is to shut down the MySQL server while running <code>myisamchk</code>, or to lock all tables that <code>myisamchk</code> is being used on. </p>
<p> Otherwise, when you run <code>myisamchk</code>, it may display the following error message: </p>
<dl>
<dt>
<dd>
<pre>
warning: clients are using or haven't closed the table properly
</pre>
</dl>
<p> This means that you are trying to check a table that has been updated by another program (such as the <code>mysqld</code> server) that hasn&#8217;t yet closed the file or that has died without closing the file properly, which can sometimes lead to the corruption of one or more MyISAM tables. </p>
<p> If <code>mysqld</code> is running, you must force it to flush any table modifications that are still buffered in memory by using FLUSH TABLES. You should then ensure that no one is using the tables while you are running <code>myisamchk</code> </p>
<p> However, the easiest way to avoid this problem is to use CHECK TABLE instead of <code>myisamchk</code> to check tables. See Section 13.7.3.2, &#8220;CHECK TABLE Statement&#8221;. </p>
</dl>
<p> <code>myisamchk</code> supports the following options, which can be specified on the command line or in the [myisamchk] group of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;.</p>
<h2>MYISAMCHK GENERAL OPTIONS</h2>
<p> The options described in this section can be used for any type of table maintenance operation performed by <code>myisamchk</code>. The sections following this one describe options that pertain only to specific operations, such as table checking or repairing. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit. Options are grouped by type of operation.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;HELP</code>, <code>-H</code> </p>
<p> Display a help message and exit. Options are presented in a single list.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug=</code><i>debug_options</i>, <code>-# </code><i>debug_options</i> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o,/tmp/myisamchk.trace. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-extra-file=</code><i>file_name</i> </p>
<p> Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-file=</code><i>file_name</i> </p>
<p> Use only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-group-suffix=</code><i>str</i> </p>
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>myisamchk</code> normally reads the [myisamchk] group. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>myisamchk</code> also reads the [myisamchk_other] group. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;print-defaults</code> </p>
<p> Print the program name and all options that it gets from option files. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Silent mode. Write output only when errors occur. You can use <code>-s</code> twice (<code>-ss</code>) to make <code>myisamchk</code> very silent.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does. This can be used with <code>-d</code> and <code>-e</code>. Use <code>-v</code> multiple times (<code>-vv</code>, <code>-vvv</code>) for even more output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;wait</code>, <code>-w</code> </p>
<p> Instead of terminating with an error if the table is locked, wait until the table is unlocked before continuing. If you are running <code>mysqld</code> with external locking disabled, the table can be locked only by another <code>myisamchk</code> command.</dl>
<p> You can also set the following variables by using <code>&#8212;</code><i>var_name</i><code>=</code><i>value</i> syntax: </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Variable </code></td>
<td><code> Default Value </code>
</td>
</tr>
<tr VALIGN=top>
<td> decode_bits </td>
<td> 9
</td>
</tr>
<tr VALIGN=top>
<td> ft_max_word_len </td>
<td> version-dependent
</td>
</tr>
<tr VALIGN=top>
<td> ft_min_word_len </td>
<td> 4
</td>
</tr>
<tr VALIGN=top>
<td> ft_stopword_file </td>
<td> built-in list
</td>
</tr>
<tr VALIGN=top>
<td> key_buffer_size </td>
<td> 523264
</td>
</tr>
<tr VALIGN=top>
<td> myisam_block_size </td>
<td> 1024
</td>
</tr>
<tr VALIGN=top>
<td> myisam_sort_key_blocks </td>
<td> 16
</td>
</tr>
<tr VALIGN=top>
<td> read_buffer_size </td>
<td> 262136
</td>
</tr>
<tr VALIGN=top>
<td> sort_buffer_size </td>
<td> 2097144
</td>
</tr>
<tr VALIGN=top>
<td> sort_key_blocks </td>
<td> 16
</td>
</tr>
<tr VALIGN=top>
<td> stats_method </td>
<td> nulls_unequal
</td>
</tr>
<tr VALIGN=top>
<td> write_buffer_size </td>
<td> 262136
</td>
</tr>
</table>
<p> The possible <code>myisamchk</code> variables and their default values can be examined with <code>myisamchk &#8211;help</code>: </p>
<p> myisam_sort_buffer_size is used when the keys are repaired by sorting keys, which is the normal case when you use <code>&#8211;recover</code>. sort_buffer_size is a deprecated synonym for myisam_sort_buffer_size. </p>
<p> key_buffer_size is used when you are checking the table with <code>&#8211;extend-check</code> or when the keys are repaired by inserting keys row by row into the table (like when doing normal inserts). Repairing through the key buffer is used in the following cases: </p>
<dl>
<dt>
<dd> &bull; You use <code>&#8211;safe-recover</code>.</dl>
<dl>
<dt>
<dd> &bull; The temporary files needed to sort the keys would be more than twice as big as when creating the key file directly. This is often the case when you have large key values for CHAR, VARCHAR, or TEXT columns, because the sort operation needs to store the complete key values as it proceeds. If you have lots of temporary space and you can force <code>myisamchk</code> to repair by sorting, you can use the <code>&#8211;sort-recover</code> option.</dl>
<p> Repairing through the key buffer takes much less disk space than using sorting, but is also much slower. </p>
<p> If you want a faster repair, set the key_buffer_size and myisam_sort_buffer_size variables to about 25% of your available memory. You can set both variables to large values, because only one of them is used at a time. </p>
<p> myisam_block_size is the size used for index blocks. </p>
<p> stats_method influences how NULL values are treated for index statistics collection when the <code>&#8211;analyze</code> option is given. It acts like the myisam_stats_method system variable. For more information, see the description of myisam_stats_method in Section 5.1.8, &#8220;Server System Variables&#8221;, and Section 8.3.8, &#8220;InnoDB and MyISAM Index Statistics Collection&#8221;. </p>
<p> ft_min_word_len and ft_max_word_len indicate the minimum and maximum word length for FULLTEXT indexes on MyISAM tables. ft_stopword_file names the stopword file. These need to be set under the following circumstances. </p>
<p> If you use <code>myisamchk</code> to perform an operation that modifies table indexes (such as repair or analyze), the FULLTEXT indexes are rebuilt using the default full-text parameter values for minimum and maximum word length and the stopword file unless you specify otherwise. This can result in queries failing. </p>
<p> The problem occurs because these parameters are known only by the server. They are not stored in MyISAM index files. To avoid the problem if you have modified the minimum or maximum word length or the stopword file in the server, specify the same ft_min_word_len, ft_max_word_len, and ft_stopword_file values to <code>myisamchk</code> that you use for <code>mysqld</code>. For example, if you have set the minimum word length to 3, you can repair a table with <code>myisamchk</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>myisamchk --recover --ft_min_word_len=3 </code><i>tbl_name</i><code>.MYI</code>
</pre>
</dl>
<p> To ensure that <code>myisamchk</code> and the server use the same values for full-text parameters, you can place each one in both the [mysqld] and [myisamchk] sections of an option file: </p>
<dl>
<dt>
<dd>
[mysqld] ft_min_word_len = 3<br />
    [myisamchk] ft_min_word_len = 3
</dl>
<p> An alternative to using <code>myisamchk</code> is to use the REPAIR TABLE, ANALYZE TABLE, OPTIMIZE TABLE, or ALTER TABLE. These statements are performed by the server, which knows the proper full-text parameter values to use.</p>
<h2>MYISAMCHK CHECK OPTIONS</h2>
<p> <code>myisamchk</code> supports the following options for table checking operations: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;check</code>, <code>-c</code> </p>
<p> Check the table for errors. This is the default operation if you specify no option that selects an operation type explicitly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;check-only-changed</code>, <code>-C</code> </p>
<p> Check only tables that have changed since the last check.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;extend-check</code>, <code>-e</code> </p>
<p> Check the table very thoroughly. This is quite slow if the table has many indexes. This option should only be used in extreme cases. Normally, <code>myisamchk</code> or <code>myisamchk &#8211;medium-check</code> should be able to determine whether there are any errors in the table. </p>
<p> If you are using <code>&#8211;extend-check</code> and have plenty of memory, setting the key_buffer_size variable to a large value helps the repair operation run faster. </p>
<p> See also the description of this option under table repair options. </p>
<p> For a description of the output format, see the section called &#8220;OBTAINING TABLE INFORMATION WITH MYISAMCHK&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;fast</code>, <code>-F</code> </p>
<p> Check only tables that haven&#8217;t been closed properly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code>, <code>-f</code> </p>
<p> Do a repair operation automatically if <code>myisamchk</code> finds any errors in the table. The repair type is the same as that specified with the <code>&#8211;recover</code> or <code>-r</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;information</code>, <code>-i</code> </p>
<p> Print informational statistics about the table that is checked.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;medium-check</code>, <code>-m</code> </p>
<p> Do a check that is faster than an <code>&#8211;extend-check</code> operation. This finds only 99.99% of all errors, which should be good enough in most cases.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;read-only</code>, <code>-T</code> </p>
<p> Do not mark the table as checked. This is useful if you use <code>myisamchk</code> to check a table that is in use by some other application that does not use locking, such as <code>mysqld</code> when run with external locking disabled.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;update-state</code>, <code>-U</code> </p>
<p> Store information in the .MYI file to indicate when the table was checked and whether the table crashed. This should be used to get full benefit of the <code>&#8211;check-only-changed</code> option, but you shouldn&#8217;t use this option if the <code>mysqld</code> server is using the table and you are running it with external locking disabled.</dl>
<h2>MYISAMCHK REPAIR OPTIONS</h2>
<p> <code>myisamchk</code> supports the following options for table repair operations (operations performed when an option such as <code>&#8211;recover</code> or <code>&#8211;safe-recover</code> is given): </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;backup</code>, <code>-B</code> </p>
<p> Make a backup of the .MYD file as <i>file_name</i>&#8211;<i>time</i>.BAK</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;character-sets-dir=</code><i>dir_name</i> </p>
<p> The directory where character sets are installed. See Section 10.15, &#8220;Character Set Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;correct-checksum</code> </p>
<p> Correct the checksum information for the table.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;data-file-length=</code><i>len</i>, <code>-D </code><i>len</i> </p>
<p> The maximum length of the data file (when re-creating data file when it is &#8220;full&#8221;).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;extend-check</code>, <code>-e</code> </p>
<p> Do a repair that tries to recover every possible row from the data file. Normally, this also finds a lot of garbage rows. Do not use this option unless you are desperate. </p>
<p> See also the description of this option under table checking options. </p>
<p> For a description of the output format, see the section called &#8220;OBTAINING TABLE INFORMATION WITH MYISAMCHK&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code>, <code>-f</code> </p>
<p> Overwrite old intermediate files (files with names like <i>tbl_name</i>.TMD) instead of aborting.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;keys-used=</code><i>val</i>, <code>-k </code><i>val</i> </p>
<p> For <code>myisamchk</code>, the option value is a bit value that indicates which indexes to update. Each binary bit of the option value corresponds to a table index, where the first index is bit 0. An option value of 0 disables updates to all indexes, which can be used to get faster inserts. Deactivated indexes can be reactivated by using <code>myisamchk -r</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-symlinks</code>, <code>-l</code> </p>
<p> Do not follow symbolic links. Normally <code>myisamchk</code> repairs the table that a symlink points to. This option does not exist as of MySQL 4.0 because versions from 4.0 on do not remove symlinks during repair operations.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;max-record-length=</code><i>len</i> </p>
<p> Skip rows larger than the given length if <code>myisamchk</code> cannot allocate memory to hold them.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;parallel-recover</code>, <code>-p</code> </p>
<p> Use the same technique as <code>-r</code> and <code>-n</code>, but create all the keys in parallel, using different threads. <i>This is beta-quality code. Use at your own risk!</i></dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;quick</code>, <code>-q</code> </p>
<p> Achieve a faster repair by modifying only the index file, not the data file. You can specify this option twice to force <code>myisamchk</code> to modify the original data file in case of duplicate keys.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;recover</code>, <code>-r</code> </p>
<p> Do a repair that can fix almost any problem except unique keys that are not unique (which is an extremely unlikely error with MyISAM tables). If you want to recover a table, this is the option to try first. You should try <code>&#8211;safe-recover</code> only if <code>myisamchk</code> reports that the table cannot be recovered using <code>&#8211;recover</code>. (In the unlikely case that <code>&#8211;recover</code> fails, the data file remains intact.) </p>
<p> If you have lots of memory, you should increase the value of myisam_sort_buffer_size.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;safe-recover</code>, <code>-o</code> </p>
<p> Do a repair using an old recovery method that reads through all rows in order and updates all index trees based on the rows found. This is an order of magnitude slower than <code>&#8211;recover</code>, but can handle a couple of very unlikely cases that <code>&#8211;recover</code> cannot. This recovery method also uses much less disk space than <code>&#8211;recover</code>. Normally, you should repair first using <code>&#8211;recover</code>, and then with <code>&#8211;safe-recover</code> only if <code>&#8211;recover</code> fails. </p>
<p> If you have lots of memory, you should increase the value of key_buffer_size.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-collation=</code><i>name</i> </p>
<p> Specify the collation to use for sorting table indexes. The character set name is implied by the first part of the collation name.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;sort-recover</code>, <code>-n</code> </p>
<p> Force <code>myisamchk</code> to use sorting to resolve the keys even if the temporary files would be very large.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tmpdir=</code><i>dir_name</i>, <code>-t </code><i>dir_name</i> </p>
<p> The path of the directory to be used for storing temporary files. If this is not set, <code>myisamchk</code> uses the value of the TMPDIR environment variable. <code>&#8211;tmpdir</code> can be set to a list of directory paths that are used successively in round-robin fashion for creating temporary files. The separator character between directory names is the colon (:) on Unix and the semicolon (;) on Windows.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;unpack</code>, <code>-u</code> </p>
<p> Unpack a table that was packed with <code>myisampack</code>.</dl>
<h2>OTHER MYISAMCHK OPTIONS</h2>
<p> <code>myisamchk</code> supports the following options for actions other than table checks and repairs: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;analyze</code>, <code>-a</code> </p>
<p> Analyze the distribution of key values. This improves join performance by enabling the join optimizer to better choose the order in which to join the tables and which indexes it should use. To obtain information about the key distribution, use a <code>myisamchk &#8211;description &#8211;verbose </code><i>tbl_name</i> command or the SHOW INDEX FROM <i>tbl_name</i> statement.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;block-search=</code><i>offset</i>, <code>-b </code><i>offset</i> </p>
<p> Find the record that a block at the given offset belongs to.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;description</code>, <code>-d</code> </p>
<p> Print some descriptive information about the table. Specifying the <code>&#8211;verbose</code> option once or twice produces additional information. See the section called &#8220;OBTAINING TABLE INFORMATION WITH MYISAMCHK&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-auto-increment[=</code><i>value</i><code>]</code>, <code>-A[</code><i>value</i><code>]</code> </p>
<p> Force AUTO_INCREMENT numbering for new records to start at the given value (or higher, if there are existing records with AUTO_INCREMENT values this large). If <i>value</i> is not specified, AUTO_INCREMENT numbers for new records begin with the largest value currently in the table, plus one.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;sort-index</code>, <code>-S</code> </p>
<p> Sort the index tree blocks in high-low order. This optimizes seeks and makes table scans that use indexes faster.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;sort-records=</code><i>N</i>, <code>-R </code><i>N</i> </p>
<p> Sort records according to a particular index. This makes your data much more localized and may speed up range-based SELECT and ORDER BY operations that use this index. (The first time you use this option to sort a table, it may be very slow.) To determine a table&#8217;s index numbers, use SHOW INDEX, which displays a table&#8217;s indexes in the same order that <code>myisamchk</code> sees them. Indexes are numbered beginning with 1. </p>
<p> If keys are not packed (PACK_KEYS=0), they have the same length, so when <code>myisamchk</code> sorts and moves records, it just overwrites record offsets in the index. If keys are packed (PACK_KEYS=1), <code>myisamchk</code> must unpack key blocks first, then re-create indexes and pack the key blocks again. (In this case, re-creating indexes is faster than updating offsets for each index.)</dl>
<h2>OBTAINING TABLE INFORMATION WITH MYISAMCHK</h2>
<p> To obtain a description of a MyISAM table or statistics about it, use the commands shown here. The output from these commands is explained later in this section. </p>
<dl>
<dt>
<dd> &bull; <code>myisamchk -d </code><i>tbl_name</i> </p>
<p> Runs <code>myisamchk</code> in &#8220;describe mode&#8221; to produce a description of your table. If you start the MySQL server with external locking disabled, <code>myisamchk</code> may report an error for a table that is updated while it runs. However, because <code>myisamchk</code> does not change the table in describe mode, there is no risk of destroying data.</dl>
<dl>
<dt>
<dd> &bull; <code>myisamchk -dv </code><i>tbl_name</i> </p>
<p> Adding <code>-v</code> runs <code>myisamchk</code> in verbose mode so that it produces more information about the table. Adding <code>-v</code> a second time produces even more information.</dl>
<dl>
<dt>
<dd> &bull; <code>myisamchk -eis </code><i>tbl_name</i> </p>
<p> Shows only the most important information from a table. This operation is slow because it must read the entire table.</dl>
<dl>
<dt>
<dd> &bull; <code>myisamchk -eiv </code><i>tbl_name</i> </p>
<p> This is like <code>-eis</code>, but tells you what is being done.</dl>
<p> The <i>tbl_name</i> argument can be either the name of a MyISAM table or the name of its index file, as described in <code><a href="/docs/linux/man/1-myisamchk/">myisamchk</a></code>(1). Multiple <i>tbl_name</i> arguments can be given. </p>
<p> Suppose that a table named person has the following structure. (The MAX_ROWS table option is included so that in the example output from <code>myisamchk</code> shown later, some values are smaller and fit the output format more easily.) </p>
<dl>
<dt>
<dd>
CREATE TABLE person(<br />
    id INT NOT NULL AUTO_INCREMENT,<br />
    last_name VARCHAR(20) NOT NULL,<br />
    first_name VARCHAR(20) NOT NULL,<br />
    birth DATE,<br />
    death DATE,<br />
    PRIMARY KEY(id),<br />
    INDEX(last_name, first_name),<br />
    INDEX(birth)) MAX_ROWS = 1000000 ENGINE = MYISAM;
</dl>
<p> Suppose also that the table has these data and index file sizes: </p>
<dl>
<dt>
<dd>
&#8211; rw &#8211; rw&#8211; &#8211;1 mysql mysql 9347072 Aug 19 11:47 person.MYD &#8211; rw &#8211; rw&#8211; &#8211;1 mysql mysql 6066176 Aug 19 11:47 person.MYI
</dl>
<p> Example of <code>myisamchk -dvv</code> output: </p>
<dl>
<dt>
<dd>
<pre>
MyISAM file:         person
Record format:       Packed
Character set:       utf8mb4_0900_ai_ci (255)
File-version:        1
Creation time:       2017-03-30 21:21:30
Status:              checked,analyzed,optimized keys,sorted index pages
Auto increment key:              1  Last value:                306688
Data records:               306688  Deleted blocks:                 0
Datafile parts:             306688  Deleted data:                   0
Datafile pointer (bytes):        4  Keyfile pointer (bytes):        3
Datafile length:           9347072  Keyfile length:           6066176
Max datafile length:    4294967294  Max keyfile length:   17179868159
Recordlength:                   54
table description:
Key Start Len Index   Type                     Rec/key         Root  Blocksize
1   2     4   unique  long                           1                    1024
2   6     80  multip. varchar prefix                 0                    1024
    87    80          varchar                        0
3   168   3   multip. uint24 NULL                    0                    1024
Field Start Length Nullpos Nullbit Type
1     1     1                                                         
2     2     4                      no zeros                           
3     6     81                     varchar                            
4     87    81                     varchar                            
5     168   3      1       1       no zeros                           
6     171   3      1       2       no zeros                           
</pre>
</dl>
<p> Explanations for the types of information <code>myisamchk</code> produces are given here. &#8220;Keyfile&#8221; refers to the index file. &#8220;Record&#8221; and &#8220;row&#8221; are synonymous, as are &#8220;field&#8221; and &#8220;column.&#8221; </p>
<p> The initial part of the table description contains these values: </p>
<dl>
<dt>
<dd> &bull; MyISAM file </p>
<p> Name of the MyISAM (index) file.</dl>
<dl>
<dt>
<dd> &bull; Record format </p>
<p> The format used to store table rows. The preceding examples use Fixed length. Other possible values are Compressed and Packed. (Packed corresponds to what SHOW TABLE STATUS reports as Dynamic.)</dl>
<dl>
<dt>
<dd> &bull; Chararacter set </p>
<p> The table default character set.</dl>
<dl>
<dt>
<dd> &bull; File-version </p>
<p> Version of MyISAM format. Always 1.</dl>
<dl>
<dt>
<dd> &bull; Creation time </p>
<p> When the data file was created.</dl>
<dl>
<dt>
<dd> &bull; Recover time </p>
<p> When the index/data file was last reconstructed.</dl>
<dl>
<dt>
<dd> &bull; Status </p>
<p> Table status flags. Possible values are crashed, open, changed, analyzed, optimized keys, and sorted index pages.</dl>
<dl>
<dt>
<dd> &bull; Auto increment key, Last value </p>
<p> The key number associated the table&#8217;s AUTO_INCREMENT column, and the most recently generated value for this column. These fields do not appear if there is no such column.</dl>
<dl>
<dt>
<dd> &bull; Data records </p>
<p> The number of rows in the table.</dl>
<dl>
<dt>
<dd> &bull; Deleted blocks </p>
<p> How many deleted blocks still have reserved space. You can optimize your table to minimize this space. See Section 7.6.4, &#8220;MyISAM Table Optimization&#8221;.</dl>
<dl>
<dt>
<dd> &bull; Datafile parts </p>
<p> For dynamic-row format, this indicates how many data blocks there are. For an optimized table without fragmented rows, this is the same as Data records.</dl>
<dl>
<dt>
<dd> &bull; Deleted data </p>
<p> How many bytes of unreclaimed deleted data there are. You can optimize your table to minimize this space. See Section 7.6.4, &#8220;MyISAM Table Optimization&#8221;.</dl>
<dl>
<dt>
<dd> &bull; Datafile pointer </p>
<p> The size of the data file pointer, in bytes. It is usually 2, 3, 4, or 5 bytes. Most tables manage with 2 bytes, but this cannot be controlled from MySQL yet. For fixed tables, this is a row address. For dynamic tables, this is a byte address.</dl>
<dl>
<dt>
<dd> &bull; Keyfile pointer </p>
<p> The size of the index file pointer, in bytes. It is usually 1, 2, or 3 bytes. Most tables manage with 2 bytes, but this is calculated automatically by MySQL. It is always a block address.</dl>
<dl>
<dt>
<dd> &bull; Max datafile length </p>
<p> How long the table data file can become, in bytes.</dl>
<dl>
<dt>
<dd> &bull; Max keyfile length </p>
<p> How long the table index file can become, in bytes.</dl>
<dl>
<dt>
<dd> &bull; Recordlength </p>
<p> How much space each row takes, in bytes.</dl>
<p> The table description part of the output includes a list of all keys in the table. For each key, <code>myisamchk</code> displays some low-level information: </p>
<dl>
<dt>
<dd> &bull; Key </p>
<p> This key&#8217;s number. This value is shown only for the first column of the key. If this value is missing, the line corresponds to the second or later column of a multiple-column key. For the table shown in the example, there are two table description lines for the second index. This indicates that it is a multiple-part index with two parts.</dl>
<dl>
<dt>
<dd> &bull; Start </p>
<p> Where in the row this portion of the index starts.</dl>
<dl>
<dt>
<dd> &bull; Len </p>
<p> How long this portion of the index is. For packed numbers, this should always be the full length of the column. For strings, it may be shorter than the full length of the indexed column, because you can index a prefix of a string column. The total length of a multiple-part key is the sum of the Len values for all key parts.</dl>
<dl>
<dt>
<dd> &bull; Index </p>
<p> Whether a key value can exist multiple times in the index. Possible values are unique or multip. (multiple).</dl>
<dl>
<dt>
<dd> &bull; Type </p>
<p> What data type this portion of the index has. This is a MyISAM data type with the possible values packed, stripped, or empty.</dl>
<dl>
<dt>
<dd> &bull; Root </p>
<p> Address of the root index block.</dl>
<dl>
<dt>
<dd> &bull; Blocksize </p>
<p> The size of each index block. By default this is 1024, but the value may be changed at compile time when MySQL is built from source.</dl>
<dl>
<dt>
<dd> &bull; Rec/key </p>
<p> This is a statistical value used by the optimizer. It tells how many rows there are per value for this index. A unique index always has a value of 1. This may be updated after a table is loaded (or greatly changed) with <code>myisamchk -a</code>. If this is not updated at all, a default value of 30 is given.</dl>
<p> The last part of the output provides information about each column: </p>
<dl>
<dt>
<dd> &bull; Field </p>
<p> The column number.</dl>
<dl>
<dt>
<dd> &bull; Start </p>
<p> The byte position of the column within table rows.</dl>
<dl>
<dt>
<dd> &bull; Length </p>
<p> The length of the column in bytes.</dl>
<dl>
<dt>
<dd> &bull; Nullpos, Nullbit </p>
<p> For columns that can be NULL, MyISAM stores NULL values as a flag in a byte. Depending on how many nullable columns there are, there can be one or more bytes used for this purpose. The Nullpos and Nullbit values, if nonempty, indicate which byte and bit contains that flag indicating whether the column is NULL. </p>
<p> The position and number of bytes used to store NULL flags is shown in the line for field 1. This is why there are six Field lines for the person table even though it has only five columns.</dl>
<dl>
<dt>
<dd> &bull; Type </p>
<p> The data type. The value may contain any of the following descriptors: </p>
<dl>
<dt>
<dd> &bull; constant </p>
<p> All rows have the same value.</dl>
<dl>
<dt>
<dd> &bull; no endspace </p>
<p> Do not store endspace.</dl>
<dl>
<dt>
<dd> &bull; no endspace, not_always </p>
<p> Do not store endspace and do not do endspace compression for all values.</dl>
<dl>
<dt>
<dd> &bull; no endspace, no empty </p>
<p> Do not store endspace. Do not store empty values.</dl>
<dl>
<dt>
<dd> &bull; table-lookup </p>
<p> The column was converted to an ENUM.</dl>
<dl>
<dt>
<dd> &bull; zerofill(<i>N</i>) </p>
<p> The most significant <i>N</i> bytes in the value are always 0 and are not stored.</dl>
<dl>
<dt>
<dd> &bull; no zeros </p>
<p> Do not store zeros.</dl>
<dl>
<dt>
<dd> &bull; always zero </p>
<p> Zero values are stored using one bit.</dl>
</dl>
<dl>
<dt>
<dd> &bull; Huff tree </p>
<p> The number of the Huffman tree associated with the column.</dl>
<dl>
<dt>
<dd> &bull; Bits </p>
<p> The number of bits used in the Huffman tree.</dl>
<p> The Huff tree and Bits fields are displayed if the table has been compressed with <code>myisampack</code>. See <code><a href="/docs/linux/man/1-myisampack/">myisampack</a></code>(1), for an example of this information. </p>
<p> Example of <code>myisamchk -eiv</code> output: </p>
<dl>
<dt>
<dd>
<pre>
Checking MyISAM file: person
Data records:  306688   Deleted blocks:       0
- check file-size
- check record delete-chain
No recordlinks
- check key delete-chain
block_size 1024:
- check index reference
- check data record references index: 1
Key:  1:  Keyblocks used:  98%  Packed:    0%  Max levels:  3
- check data record references index: 2
Key:  2:  Keyblocks used:  99%  Packed:   97%  Max levels:  3
- check data record references index: 3
Key:  3:  Keyblocks used:  98%  Packed:  -14%  Max levels:  3
Total:    Keyblocks used:  98%  Packed:   89%
- check records and index references<i>*** LOTS OF ROW NUMBERS DELETED ***</i>
Records:            306688  M.recordlength:       25  Packed:            83%
Recordspace used:       97% Empty space:           2% Blocks/Record:   1.00
Record blocks:      306688  Delete blocks:         0
Record data:       7934464  Deleted data:          0
Lost space:         256512  Linkdata:        1156096
User time 43.08, System time 1.68
Maximum resident set size 0, Integral resident set size 0
Non-physical pagefaults 0, Physical pagefaults 0, Swaps 0
Blocks in 0 out 7, Messages in 0 out 0, Signals 0
Voluntary context switches 0, Involuntary context switches 0
Maximum memory usage: 1046926 bytes (1023k)
</pre>
</dl>
<p> <code>myisamchk -eiv</code> output includes the following information: </p>
<dl>
<dt>
<dd> &bull; Data records </p>
<p> The number of rows in the table.</dl>
<dl>
<dt>
<dd> &bull; Deleted blocks </p>
<p> How many deleted blocks still have reserved space. You can optimize your table to minimize this space. See Section 7.6.4, &#8220;MyISAM Table Optimization&#8221;.</dl>
<dl>
<dt>
<dd> &bull; Key </p>
<p> The key number.</dl>
<dl>
<dt>
<dd> &bull; Keyblocks used </p>
<p> What percentage of the keyblocks are used. When a table has just been reorganized with <code>myisamchk</code>, the values are very high (very near theoretical maximum).</dl>
<dl>
<dt>
<dd> &bull; Packed </p>
<p> MySQL tries to pack key values that have a common suffix. This can only be used for indexes on CHAR and VARCHAR columns. For long indexed strings that have similar leftmost parts, this can significantly reduce the space used. In the preceding example, the second key is 40 bytes long and a 97% reduction in space is achieved.</dl>
<dl>
<dt>
<dd> &bull; Max levels </p>
<p> How deep the B-tree for this key is. Large tables with long key values get high values.</dl>
<dl>
<dt>
<dd> &bull; Records </p>
<p> How many rows are in the table.</dl>
<dl>
<dt>
<dd> &bull; M.recordlength </p>
<p> The average row length. This is the exact row length for tables with fixed-length rows, because all rows have the same length.</dl>
<dl>
<dt>
<dd> &bull; Packed </p>
<p> MySQL strips spaces from the end of strings. The Packed value indicates the percentage of savings achieved by doing this.</dl>
<dl>
<dt>
<dd> &bull; Recordspace used </p>
<p> What percentage of the data file is used.</dl>
<dl>
<dt>
<dd> &bull; Empty space </p>
<p> What percentage of the data file is unused.</dl>
<dl>
<dt>
<dd> &bull; Blocks/Record </p>
<p> Average number of blocks per row (that is, how many links a fragmented row is composed of). This is always 1.0 for fixed-format tables. This value should stay as close to 1.0 as possible. If it gets too large, you can reorganize the table. See Section 7.6.4, &#8220;MyISAM Table Optimization&#8221;.</dl>
<dl>
<dt>
<dd> &bull; Recordblocks </p>
<p> How many blocks (links) are used. For fixed-format tables, this is the same as the number of rows.</dl>
<dl>
<dt>
<dd> &bull; Deleteblocks </p>
<p> How many blocks (links) are deleted.</dl>
<dl>
<dt>
<dd> &bull; Recorddata </p>
<p> How many bytes in the data file are used.</dl>
<dl>
<dt>
<dd> &bull; Deleted data </p>
<p> How many bytes in the data file are deleted (unused).</dl>
<dl>
<dt>
<dd> &bull; Lost space </p>
<p> If a row is updated to a shorter length, some space is lost. This is the sum of all such losses, in bytes.</dl>
<dl>
<dt>
<dd> &bull; Linkdata </p>
<p> When the dynamic table format is used, row fragments are linked with pointers (4 to 7 bytes each). Linkdata is the sum of the amount of storage used by all such pointers.</dl>
<h2>MYISAMCHK MEMORY USAGE</h2>
<p> Memory allocation is important when you run <code>myisamchk</code>. <code>myisamchk</code> uses no more memory than its memory-related variables are set to. If you are going to use <code>myisamchk</code> on very large tables, you should first decide how much memory you want it to use. The default is to use only about 3MB to perform repairs. By using larger values, you can get <code>myisamchk</code> to operate faster. For example, if you have more than 512MB RAM available, you could use options such as these (in addition to any other options you might specify): </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; myisamchk-- myisam_sort_buffer_size = 256M --key_buffer_size = 512M --read_buffer_size = 64M --write_buffer_size = 64M ...
</code></pre>
</dl>
<p> Using <code>&#8211;myisam_sort_buffer_size=16M</code> is probably enough for most cases. </p>
<p> Be aware that <code>myisamchk</code> uses temporary files in TMPDIR. If TMPDIR points to a memory file system, out of memory errors can easily occur. If this happens, run <code>myisamchk</code> with the <code>&#8211;tmpdir=</code><i>dir_name</i> option to specify a directory located on a file system that has more space. </p>
<p> When performing repair operations, <code>myisamchk</code> also needs a lot of disk space: </p>
<dl>
<dt>
<dd> &bull; Twice the size of the data file (the original file and a copy). This space is not needed if you do a repair with <code>&#8211;quick</code>; in this case, only the index file is re-created. <i>This space must be available on the same file system as the original data file</i>, as the copy is created in the same directory as the original.</dl>
<dl>
<dt>
<dd> &bull; Space for the new index file that replaces the old one. The old index file is truncated at the start of the repair operation, so you usually ignore this space. This space must be available on the same file system as the original data file.</dl>
<dl>
<dt>
<dd> &bull; When using <code>&#8211;recover</code> or <code>&#8211;sort-recover</code> (but not when using <code>&#8211;safe-recover</code>), you need space on disk for sorting. This space is allocated in the temporary directory (specified by TMPDIR or <code>&#8211;tmpdir=</code><i>dir_name</i>). The following formula yields the amount of space required: </p>
<dl>
<dt>
<dd>
<pre>
(<i>largest_key</i> + <i>row_pointer_length</i>) * <i>number_of_rows</i> * 2
</pre>
</dl>
<p> You can check the length of the keys and the <i>row_pointer_length</i> with <code>myisamchk -dv </code><i>tbl_name</i> (see the section called &#8220;OBTAINING TABLE INFORMATION WITH MYISAMCHK&#8221;). The <i>row_pointer_length</i> and <i>number_of_rows</i> values are the Datafile pointer and Data records values in the table description. To determine the <i>largest_key</i> value, check the Key lines in the table description. The Len column indicates the number of bytes for each key part. For a multiple-column index, the key size is the sum of the Len values for all key parts.</dl>
<p> If you have a problem with disk space during repair, you can try <code>&#8211;safe-recover</code> instead of <code>&#8211;recover</code>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
