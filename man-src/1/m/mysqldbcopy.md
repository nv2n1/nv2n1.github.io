---
title: "mysqldbcopy(1)"
name: "mysqldbcopy"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqldbcopy/"
description: "mysqldbcopy – Copy Database Objects Between Servers"
---

<h2 class="name">NAME</h2>
<p> mysqldbcopy &#8211; Copy Database Objects Between Servers </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqldbcopy [</code><i>options</i><code>] </code><i>db_name</i><code> [</code><i>:new_db_name</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility copies a database on a source server to a database on a destination server. If the source and destination servers are different, the database names can be the same or different. If the source and destination servers are the same, the database names must be different. </p>
<p> The utility accepts one or more database pairs on the command line. To name a database pair, use <i>db_name</i>:<i>new_db_name</i> syntax to specify the source and destination names explicitly. If the source and destination database names are the same, <i>db_name</i> can be used as shorthand for <i>db_name</i>:<i>db_name</i>. </p>
<p> By default, the operation copies all objects (tables, views, triggers, events, procedures, functions, and database-level grants) and data to the destination server. There are options to turn off copying any or all of the objects as well as not copying the data. </p>
<p> To exclude specific objects by name, use the <code>&#8211;exclude</code> option with a name in <i>db</i>.*obj* format, or you can supply a search pattern. For example, <code>&#8211;exclude=db1.trig1</code> excludes the single trigger and <code>&#8211;exclude=trig_</code> excludes all objects from all databases having a name that begins with trig and has a following character. </p>
<p> By default, the utility creates each table on the destination server using the same storage engine as the original table. To override this and specify the storage engine to use for all tables created on the destination server, use the <code>&#8211;new-storage-engine</code> option. If the destination server supports the new engine, all tables use that engine. </p>
<p> To specify the storage engine to use for tables for which the destination server does not support the original storage engine on the source server, use the <code>&#8211;default-storage-engine</code> option. </p>
<p> The <code>&#8211;new-storage-engine</code> option takes precedence over <code>&#8211;default-storage-engine</code> if both are given. </p>
<p> If the <code>&#8211;new-storage-engine</code> or <code>&#8211;default-storage-engine</code> option is given and the destination server does not support the specified storage engine, a warning is issued and the server&#8217;s default storage engine setting is used instead. </p>
<p> By default, the operation uses a consistent snapshot to read the source databases. To change the locking mode, use the <code>&#8211;locking</code> option with a locking type value. Use a value of <code>no-locks</code> to turn off locking altogether or <code>lock-all</code> to use only table locks. The default value is <code>snapshot</code>. Additionally, the utility uses WRITE locks to lock the destination tables during the copy. </p>
<p> You can include replication statements for copying data among a master and slave or between slaves. The <code>&#8211;rpl</code> option permits you to select from the following replication statements to include in the export. </p>
<dl>
<dt>
<dd> &bull; <code>master</code> </p>
<p> Include the <code>CHANGE MASTER</code> statement to start a new slave with the current server acting as the master. This executes the appropriate STOP and START slave statements. The <code>STOP SLAVE</code> statement is executed at the start of the copy and the <code>CHANGE MASTER</code> followed by the <code>START SLAVE</code> statements are executed after the copy.</dl>
<dl>
<dt>
<dd> &bull; <code>slave</code> </p>
<p> Include the <code>CHANGE MASTER</code> statement to start a new slave using the current server&#8217;s master information. This executes the appropriate STOP and START slave statements. The STOP SLAVE statement is executed at the start of the copy and the <code>CHANGE MASTER</code> followed by the <code>START SLAVE</code> statements follow the copy.</dl>
<p> To include the replication user in the <code>CHANGE MASTER</code> statement, use the <code>&#8211;rpl-user</code> option to specify the user and password. If this option is omitted, the utility attempts to identify the replication user. In the event that there are multiple candidates or the user requires a password, the utility aborts with an error. </p>
<p> If you attempt to copy databases on a server with GTIDs enabled (GTID_MODE = ON), a warning will be generated if the copy does not include all databases. This is because the GTID statements generated include the GTIDs for all databases and not only those databases in the export. </p>
<p> The utility will also generate a warning if you copy databases on a GTID enabled server but use the <code>&#8211;skip-gtid </code> option. </p>
<p> To make the most use of GTIDs, you should copy all of the databases on the server with the <code>&#8211;all</code> option.<br />
OPTIONS </p>
<p> <code>mysqldbcopy</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;default-storage-engine=&lt;def_engine&gt; </p>
<p> The engine to use for tables if the destination server does not support the original storage engine on the source server.</dl>
<dl>
<dt>
<dd> &bull; &#8211;destination=&lt;destination&gt; </p>
<p> Connection information for the destination server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] (where &lt;passwd&gt; is optional and either &lt;port&gt; or &lt;socket&gt; must be provided).</dl>
<dl>
<dt>
<dd> &bull; &#8211;exclude=&lt;exclude&gt;, -x&lt;exclude&gt; </p>
<p> Exclude one or more objects from the operation using either a specific name such as db1.t1 or a search pattern. Use this option multiple times to specify multiple exclusions. By default, patterns use <code>LIKE</code> matching. With the <code>&#8211;regexp</code> option, patterns use <code>REGEXP</code> matching. </p>
<p> This option does not apply to grants.</dl>
<dl>
<dt>
<dd> &bull; &#8211;force </p>
<p> Drop each database to be copied if exists before copying anything into it. Without this option, an error occurs if you attempt to copy objects into an existing database.</dl>
<dl>
<dt>
<dd> &bull; &#8211;locking=&lt;locking&gt; </p>
<p> Choose the lock type for the operation. Permitted lock values are <code>no-locks</code> (do not use any table locks), <code>lock-all</code> (use table locks but no transaction and no consistent read), and <code>snapshot</code> (consistent read using a single transaction). The default is <code>snapshot</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;new-storage-engine=&lt;new_engine&gt; </p>
<p> The engine to use for all tables created on the destination server.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Turn off all messages for quiet execution.</dl>
<dl>
<dt>
<dd> &bull; &#8211;regexp, &#8211;basic-regexp, -G </p>
<p> Perform pattern matches using the <code>REGEXP</code> operator. The default is to use <code>LIKE</code> for matching.</dl>
<dl>
<dt>
<dd> &bull; &#8211;rpl=&lt;dump_option&gt;, &#8211;replication=&lt;dump_option&gt; </p>
<p> Include replication information. Permitted values are <code>master</code> (include the <code>CHANGE MASTER</code> statement using the source server as the master), <code>slave</code> (include the <code>CHANGE MASTER</code> statement using the destination server&#8217;s master information), and <code>both</code> (include the <code>master</code> and <code>slave</code> options where applicable).</dl>
<dl>
<dt>
<dd> &bull; &#8211;rpl-user=&lt;replication_user&gt; </p>
<p> The user and password for the replication user requirement in the form: &lt;<i>user</i>&gt;[:&lt;<i>password</i>&gt;] or &lt;<i>login-path</i>&gt;. E.g. rpl:passwd Default = None.</dl>
<dl>
<dt>
<dd> &bull; l &#8211;skip-gtid </p>
<p> Skip creation and execution of GTID statements during the copy operation.</dl>
<dl>
<dt>
<dd> &bull; &#8211;all </p>
<p> Copy all of the databases on the server.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip=&lt;objects&gt; </p>
<p> Specify objects to skip in the operation as a comma-separated list (no spaces). Permitted values are <code>CREATE_DB</code>, <code>DATA</code>, <code>EVENTS</code>, <code>FUNCTIONS</code>, <code>GRANTS</code>, <code>PROCEDURES</code>, <code>TABLES</code>, <code>TRIGGERS</code>, and <code>VIEWS</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;source=&lt;source&gt; </p>
<p> Connection information for the destination server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[::&lt;<i>port</i>&gt;][::&lt;<i>socket</i>&gt;] (where &lt;passwd&gt; is optional and either &lt;port&gt; or &lt;socket&gt; must be provided).</dl>
<dl>
<dt>
<dd> &bull; &#8211;threads </p>
<p> Use multiple threads for cross-server copy. The default is 1.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> You must provide connection parameters (user, host, password, and so forth) for an account that has the appropriate privileges to access all objects in the operation. </p>
<p> To copy all objects from a source, the user must have these privileges: <code>SELECT</code> and <code>SHOW VIEW</code> for the database, and <code>SELECT</code> for the mysql database. </p>
<p> To copy all objects to a destination, the user must have these privileges: <code>CREATE</code> for the database, <code>SUPER</code> (when binary logging is enabled) for procedures and functions, and <code>GRANT OPTION</code> to copy grants. </p>
<p> Actual privileges required may differ from installation to installation depending on the security privileges present and whether the database contains certain objects such as views or events and whether binary logging is enabled. </p>
<p> The <code>&#8211;new-storage-engine</code> and <code>&#8211;default-storage-engine</code> options apply to all destination tables in the operation. </p>
<p> Some option combinations may result in errors during the operation. For example, eliminating tables but not views may result in an error a the view is copied. </p>
<p> The <code>&#8211;rpl</code> option is not valid for copying databases on the same server. An error will be generated. </p>
<p> When copying data and including the GTID commands, you may encounter an error similar to &quot;GTID_PURGED can only be set when GTID_EXECUTED is empty&quot;. This occurs because the destination server is not in a clean replication state. To aleviate this problem, you can issue a &quot;RESET MASTER&quot; command on the destination prior to executing the copy. </p>
<p> Cloning databases that contain foreign key constraints does not change the constraint in the cloned table. For example, if table db1.t1 has a foreign key constraint on table db1.t2, when db1 is cloned to db2, table db2.t1 will have a foreign key constraint on db1.t2. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf). </p>
<p> If any database identifier specified as an argument contains special characters or is a reserved word, then it must be appropriately quoted with backticks (<code>`</code>). In turn, names quoted with backticks must also be quoted with single or double quotes depending on the operating system, i.e. (<code>&quot;</code>) in Windows or (<code>&#8216;</code>) in non-Windows systems, in order for the utilities to read backtick quoted identifiers as a single argument. For example, to copy a database with the name <code>weird`db.name</code> with <code>other:weird`db.name</code>, the database pair must be specified using the following syntax (in non-Windows): <code>&#8216;`weird&#8220;db.name`:`other:weird&#8220;db.name`&#8217;</code>.<br />
EXAMPLES </p>
<p> The following example demonstrates how to use the utility to copy a database named util_test to a new database named util_test_copy on the same server: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqldbcopy-- source = root : pass[at] localhost : 3310 : / test123 / mysql.sock-- destination = root : pass[at] localhost : 3310 : / test123 / mysql.sock util_test : util_test_copy
#Source on localhost : ... connected.
#Destination on localhost : ... connected.
#Copying database util_test renamed as util_test_copy
#Copying TABLE util_test.t1
#Copying table data.
#Copying TABLE util_test.t2
#Copying table data.
#Copying TABLE util_test.t3
#Copying table data.
#Copying TABLE util_test.t4
#Copying table data.
#Copying VIEW util_test.v1
#Copying TRIGGER util_test.trg
#Copying PROCEDURE util_test.p1
#Copying FUNCTION util_test.f1
#Copying EVENT util_test.e1
#Copying GRANTS from util_test
#... done.
</code></pre>
</dl>
<p> If the database to be copied does not contain only InnoDB tables and you want to ensure data integrity of the copied data by locking the tables during the read step, add a <code>&#8211;locking=lock-all</code> option to the command: </p>
<dl>
<dt>
<dd>
$ mysqldbcopy&#8211; source = root : pass[at] localhost : 3310 : / test123 / mysql.sock&#8211; destination = root : pass[at] localhost : 3310 : / test123 / mysql.sock util_test : util_test_copy&#8211; locking = lock &#8211; all<br />
#Source on localhost : &#8230; connected.<br />
#Destination on localhost : &#8230; connected.<br />
#Copying database util_test renamed as util_test_copy<br />
#Copying TABLE util_test.t1<br />
#Copying table data.<br />
#Copying TABLE util_test.t2<br />
#Copying table data.<br />
#Copying TABLE util_test.t3<br />
#Copying table data.<br />
#Copying TABLE util_test.t4<br />
#Copying table data.<br />
#Copying VIEW util_test.v1<br />
#Copying TRIGGER util_test.trg<br />
#Copying PROCEDURE util_test.p1<br />
#Copying FUNCTION util_test.f1<br />
#Copying EVENT util_test.e1<br />
#Copying GRANTS from util_test<br />
#&#8230; done.
</dl>
<p> To copy one or more databases from a master to a slave, you can use the following command to copy the databases. Use the master as the source and the slave as the destination: </p>
<dl>
<dt>
<dd>
$ mysqldbcopy&#8211; source = root[at] localhost : 3310 &#8211;destination = root[at] localhost : 3311 test123&#8211; rpl = master&#8211; rpl &#8211; user = rpl<br />
#Source on localhost : &#8230; connected.<br />
#Destination on localhost : &#8230; connected.<br />
#Source on localhost : &#8230; connected.<br />
#Stopping slave<br />
#Copying database test123<br />
#Copying TABLE test123.t1<br />
#Copying data for TABLE test123.t1<br />
#Connecting to the current server as master<br />
#Starting slave<br />
#&#8230; done.
</dl>
<p> To copy a database from one slave to another attached to the same master, you can use the following command using the slave with the database to be copied as the source and the slave where the database needs to copied to as the destination: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqldbcopy-- source = root[at] localhost : 3311 --destination = root[at] localhost : 3312 test123-- rpl = slave-- rpl - user = rpl
#Source on localhost : ... connected.
#Destination on localhost : ... connected.
#Source on localhost : ... connected.
#Stopping slave
#Copying database test123
#Copying TABLE test123.t1
#Copying data for TABLE test123.t1
#Connecting to the current server's master
#Starting slave
#... done.
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
