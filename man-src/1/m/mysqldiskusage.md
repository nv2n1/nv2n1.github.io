---
title: "mysqldiskusage(1)"
name: "mysqldiskusage"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqldiskusage/"
description: "mysqldiskusage – Show Database Disk Usage"
---

<h2 class="name">NAME</h2>
<p> mysqldiskusage &#8211; Show Database Disk Usage </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqldiskusage [</code><i>options</i><code>] </code><i>db</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility displays disk space usage for one or more databases. The utility optionally displays disk usage for the binary log, slow query log, error log, general query log, relay log, and InnoDB tablespaces. The default is to show only database disk usage. </p>
<p> If the command line lists no databases, the utility shows the disk space usage for all databases. </p>
<p> Sizes displayed without a unit indicator such as MB are in bytes. </p>
<p> The utility determines the the location of the data directory by requesting it from the server. For a local server, the utility obtains size information directly from files in the data directory and InnoDB home directory. In this case, you must have file system access to read those directories. Disk space usage shown includes the sum of all storage engine- specific files such as the .MYI and .MYD files for MyISAM and the tablespace files for InnoDB. </p>
<p> If the file system read fails, or if the server is not local, the utility cannot determine exact file sizes. It is limited to information that can be obtained from the system tables, which therefore should be considered an estimate. For information read from the server, the account used to connect to the server must have the appropriate permissions to read any objects accessed during the operation. </p>
<p> If information requested requires file system access but is not available that way, the utility prints a message that the information is not accessible. This occurs, for example, if you request log usage but the server is not local and the log files cannot be examined directly. </p>
<p> To specify how to display output, use one of the following values with the <code>&#8211;format</code> option: </p>
<dl>
<dt>
<dd> &bull; <code>grid</code> (default) </p>
<p> Display output in grid or table format like that of the <code>mysql</code> monitor.</dl>
<dl>
<dt>
<dd> &bull; <code>csv</code> </p>
<p> Display output in comma-separated values format.</dl>
<dl>
<dt>
<dd> &bull; <code>tab</code> </p>
<p> Display output in tab-separated format.</dl>
<dl>
<dt>
<dd> &bull; <code>vertical</code> </p>
<p> Display output in single-column format like that of the \G command for the <code>mysql</code> monitor.</dl>
<p> To turn off the headers for <code>csv</code> or <code>tab</code> display format, specify the <code>&#8211;no-headers</code> option.<br />
OPTIONS </p>
<p> <code>mysqldiskusage</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;all, -a </p>
<p> Display all disk usage. This includes usage for databases, logs, and InnoDB tablespaces.</dl>
<dl>
<dt>
<dd> &bull; &#8211;binlog, -b </p>
<p> Display binary log usage.</dl>
<dl>
<dt>
<dd> &bull; &#8211;empty, -m </p>
<p> Include empty databases.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;format&gt;, -f&lt;format&gt; </p>
<p> Specify the output display format. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, and <code>vertical</code>. The default is <code>grid</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;innodb, -i </p>
<p> Display InnoDB tablespace usage. This includes information about the shared InnoDB tablespace as well as .idb files for InnoDB tables with their own tablespace.</dl>
<dl>
<dt>
<dd> &bull; &#8211;logs, -l </p>
<p> Display general query log, error log, and slow query log usage.</dl>
<dl>
<dt>
<dd> &bull; &#8211;no-headers, -h </p>
<p> Do not display column headers. This option applies only for <code>csv</code> and <code>tab</code> output.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Suppress informational messages.</dl>
<dl>
<dt>
<dd> &bull; &#8211;relaylog, -r </p>
<p> Display relay log usage.</dl>
<dl>
<dt>
<dd> &bull; &#8211;server=&lt;server&gt; </p>
<p> Connection information for the server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p> For the <code>&#8211;format</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value.<br />
NOTES </p>
<p> You must provide connection parameters (user, host, password, and so forth) for an account that has the appropriate privileges for all objects accessed during the operation. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> To show only the disk space usage for the employees and test databases in grid format (the default), use this command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqldiskusage-- server = root[at] localhost employees test
#Source on localhost : ... connected.
#Database totals:
                                + -- -- -- -- -- --+-- -- -- -- -- -- --+ |
                            db_name | total |
                            +-- -- -- -- -- --+-- -- -- -- -- -- --+ | employees | 205,
                   979, 648 | | test | 4, 096 | +-- -- -- -- -- --+-- -- -- -- -- -- --+Total database disk usage = 205, 983, 744 bytes or 196.00 MB
#... done.
</code></pre>
</dl>
<p> To see all disk usage for the server in CSV format, use this command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqldiskusage-- server = root[at] localhost-- format = csv - a - vv
#Source on localhost : ... connected.
#Database totals:
                                                                        db_name,
                   db_dir_size, data_size, misc_files, total test1, 0, 0, 0, 0 db3, 0, 0, 0, 0 db2, 0, 0, 0, 0 db1, 0, 0, 0, 0 backup_test, 19410, 1117, 18293, 19410 employees, 242519463, 205979648, 242519463, 448499111 mysql, 867211, 657669, 191720, 849389 t1, 9849, 1024, 8825, 9849 test, 56162, 4096, 52066, 56162 util_test_a, 19625, 2048, 17577, 19625 util_test_b, 17347, 0, 17347, 17347 util_test_c, 19623, 2048, 17575, 19623 Total database disk usage = 449, 490, 516 bytes or 428.00 MB
#Log information.
#The general_log is turned off on the server.
#The slow_query_log is turned off on the server.
#binary log information:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Current binary log file =./ mysql - bin .000076 log_file,
                   size / data / mysql - bin .000076, 125 / data / mysql - bin .000077, 125 / data / mysql - bin .000078, 556 / data / mysql - bin .000079, 168398223 / data / mysql - bin.index, 76 Total size of binary logs = 168, 399, 105 bytes or 160.00 MB
#Server is not an active slave - no relay log information.
#InnoDB tablespace information:
                                                                                                                                                                                                                                                            InnoDB_file,
                   size, type, specificaton / data / ib_logfile0, 5242880, log file,
                   / data / ib_logfile1, 5242880, log file,
                   / data / ibdata1, 220200960, shared tablespace, ibdata1 : 210M / data / ibdata2, 10485760, shared tablespace, ibdata2 : 10M : autoextend / data / employees / departments.ibd, 114688, file tablespace,
                   / data / employees / dept_emp.ibd, 30408704, file tablespace,
                   / data / employees / dept_manager.ibd, 131072, file tablespace,
                   / data / employees / employees.ibd, 23068672, file tablespace,
                   / data / employees / salaries.ibd, 146800640, file tablespace,
                   / data / employees / titles.ibd, 41943040, file tablespace,
                   Total size of InnoDB files = 494, 125, 056 bytes or 471.00 MB
#... done.
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
