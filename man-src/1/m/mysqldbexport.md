---
title: "mysqldbexport(1)"
name: "mysqldbexport"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqldbexport/"
description: "mysqldbexport – Export Object Definitions or Data from a Database"
---

<h2 class="name">NAME</h2>
<p> mysqldbexport &#8211; Export Object Definitions or Data from a Database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqldbexport [</code><i>options</i><code>] </code><i>db_name</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility exports metadata (object definitions) or data or both from one or more databases. By default, the export includes only definitions. </p>
<p> <code>mysqldbexport</code> differs from <code>mysqldump</code> in that it can produce output in a variety of formats to make your data extraction/transport much easier. It permits you to export your data in the format most suitable to an external tool, another MySQL server, or other use without the need to reformat the data. </p>
<p> To exclude specific objects by name, use the <code>&#8211;exclude</code> option with a name in <i>db</i>.*obj* format, or you can supply a search pattern. For example, <code>&#8211;exclude=db1.trig1</code> excludes the single trigger and <code>&#8211;exclude=trig_</code> excludes all objects from all databases having a name that begins with trig and has a following character. </p>
<p> To skip objects by type, use the <code>&#8211;skip</code> option with a list of the objects to skip. This enables you to extract a particular set of objects, say, for exporting only events (by excluding all other types). Similarly, to skip creation of <code>UPDATE</code> statements for BLOB data, specify the <code>&#8211;skip-blobs</code> option. </p>
<p> To specify how to display output, use one of the following values with the <code>&#8211;format</code> option: </p>
<dl>
<dt>
<dd> &bull; <code>sql</code> (default) </p>
<p> Display output using SQL statements. For definitions, this consists of the appropriate <code>CREATE</code> and <code>GRANT</code> statements. For data, this is an <code>INSERT</code> statement (or bulk insert if the <code>&#8211;bulk-insert</code> option is specified).</dl>
<dl>
<dt>
<dd> &bull; <code>grid</code> </p>
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
<p> To specify how much data to display, use one of the following values with the <code>&#8211;display</code> option: </p>
<dl>
<dt>
<dd> &bull; <code>brief</code> </p>
<p> Display only the minimal columns for recreating the objects.</dl>
<dl>
<dt>
<dd> &bull; <code>full</code> </p>
<p> Display the complete column list for recreating the objects.</dl>
<dl>
<dt>
<dd> &bull; <code>names</code> </p>
<p> Display only the object names.</dl>
<p> Note: For SQL-format output, the <code>&#8211;display</code> option is ignored. </p>
<p> To turn off the headers for <code>csv</code> or <code>tab</code> display format, specify the <code>&#8211;no-headers</code> option. </p>
<p> To turn off all feedback information, specify the <code>&#8211;quiet</code> option. </p>
<p> To write the data for individual tables to separate files, use the <code>&#8211;file-per-table</code> option. The name of each file is composed of the database and table names followed by the file format. For example, the following command produces files named db1.*table_name*.csv: </p>
<dl>
<dt>
<dd>
<pre><code>
mysqldbexport-- server = root[at] server1 : 3306 --format = csv db1-- export = data
</code></pre>
</dl>
<p> By default, the operation uses a consistent snapshot to read the source databases. To change the locking mode, use the <code>&#8211;locking</code> option with a locking type value. Use a value of <code>no-locks</code> to turn off locking altogether or <code>lock-all</code> to use only table locks. The default value is <code>snapshot</code>. Additionally, the utility uses WRITE locks to lock the destination tables during the copy. </p>
<p> You can include replication statements for exporting data among a master and slave or between slaves. The <code>&#8211;rpl</code> option permits you to select from the following replication statements to include in the export. </p>
<dl>
<dt>
<dd> &bull; <code>master</code> </p>
<p> Include the <code>CHANGE MASTER</code> statement to start a new slave with the current server acting as the master. This places the appropriate STOP and START slave statements in the export whereby the <code>STOP SLAVE</code> statement is placed at the start of the export and the <code>CHANGE MASTER</code> followed by the <code>START SLAVE</code> statements are placed after the export stream.</dl>
<dl>
<dt>
<dd> &bull; <code>slave</code> </p>
<p> Include the <code>CHANGE MASTER</code> statement to start a new slave using the current server&#8217;s master information. This places the appropriate STOP and START slave statements in the export whereby the <code>STOP SLAVE</code> statement is placed at the start of the export and the <code>CHANGE MASTER</code> followed by the <code>START SLAVE</code> statements are placed after the export stream.</dl>
<dl>
<dt>
<dd> &bull; <code>both</code> </p>
<p> Include both the &#8216;master&#8217; and &#8216;slave&#8217; information for <code>CHANGE MASTER</code> statements for either spawning a new slave with the current server&#8217;s master or using the current server as the master. All statements generated are labeled and commented to enable the user to choose which to include when imported.</dl>
<p> To include the replication user in the <code>CHANGE MASTER</code> statement, use the <code>&#8211;rpl-user</code> option to specify the user and password. If this option is omitted, the utility attempts to identify the replication user. In the event that there are multiple candidates or the user requires a password, these statements are placed inside comments for the <code>CHANGE MASTER</code> statement. </p>
<p> You can also use the <code>&#8211;comment-rpl</code> option to place the replication statements inside comments for later examination. </p>
<p> If you specify the <code>&#8211;rpl-file</code> option, the utility writes the replication statements to the file specified instead of including them in the export stream. </p>
<p> If you attempt to export databases on a server with GTIDs enabled (GTID_MODE = ON), a warning will be generated if the export does not include all databases. This is because the GTID statements generated include the GTIDs for all databases and not only those databases in the export. </p>
<p> The utility will also generate a warning if you export databases on a GTID enabled server but use the <code>&#8211;skip-gtid </code> option. </p>
<p> To make the most use of GTIDs and export/import, you should export all of the databases on the server with the <code>&#8211;all</code> option. This will generate an export file with all of the databases and the GTIDs executed to that point. </p>
<p> Importing this file on another server will ensure that server has all of the data as well as all of the GTIDs recorded correctly in its logs.<br />
OPTIONS </p>
<p> <code>mysqldbexport</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;bulk-insert, -b </p>
<p> Use bulk insert statements for data.</dl>
<dl>
<dt>
<dd> &bull; &#8211;comment-rpl </p>
<p> Place the replication statements in comment statements. Valid only with the <code>&#8211;rpl</code> option.</dl>
<dl>
<dt>
<dd> &bull; &#8211;display=&lt;display&gt;, -d&lt;display&gt; </p>
<p> Control the number of columns shown. Permitted display values are <code>brief</code> (minimal columns for object creation), <code>full* (all columns), and **names</code> (only object names; not valid for <code>&#8211;format=sql</code>). The default is <code>brief</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;exclude=&lt;exclude&gt;, -x&lt;exclude&gt; </p>
<p> Exclude one or more objects from the operation using either a specific name such as db1.t1 or a search pattern. Use this option multiple times to specify multiple exclusions. By default, patterns use <code>LIKE</code> matching. With the <code>&#8211;regexp</code> option, patterns use <code>REGEXP</code> matching. </p>
<p> This option does not apply to grants.</dl>
<dl>
<dt>
<dd> &bull; &#8211;export=&lt;export&gt;, -e&lt;export&gt; </p>
<p> Specify the export format. Permitted format values are <code>definitions</code> = export only the definitions (metadata) for the objects in the database list, <code>data</code> = export only the table data for the tables in the database list, and <code>both</code> = export the definitions and the data. The default is <code>definitions</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;file-per-table </p>
<p> Write table data to separate files. This is Valid only if the export output includes data (that is, if <code>&#8211;export=data</code> or <code>&#8211;export=both</code> are given). This option produces files named <i>db_name</i>.*tbl_name*.*format*. For example, a <code>csv</code> export of two tables named t1 and t2 in database d1, results in files named db1.t1.csv and db1.t2.csv. If table definitions are included in the export, they are written to stdout as usual.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;format&gt;, -f&lt;format&gt; </p>
<p> Specify the output display format. Permitted format values are <code>sql</code>, <code>grid</code>, <code>tab</code>, <code>csv</code>, and <code>vertical</code>. The default is <code>sql</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;locking=&lt;locking&gt; </p>
<p> Choose the lock type for the operation. Permitted lock values are <code>no-locks</code> (do not use any table locks), <code>lock-all</code> (use table locks but no transaction and no consistent read), and <code>snapshot</code> (consistent read using a single transaction). The default is <code>snapshot</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;no-headers, -h </p>
<p> Do not display column headers. This option applies only for <code>csv</code> and <code>tab</code> output.</dl>
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
<dd> &bull; &#8211;rpl-file=RPL_FILE, &#8211;replication-file=RPL_FILE </p>
<p> The path and file name where the generated replication information should be written. Valid only with the <code>&#8211;rpl</code> option.</dl>
<dl>
<dt>
<dd> &bull; &#8211;rpl-user=&lt;replication_user&gt; </p>
<p> The user and password for the replication user requirement, in the format: &lt;<i>user</i>&gt;[:&lt;<i>password</i>&gt;] or &lt;<i>login-path</i>&gt;. For example, rpl:passwd. The default is None.</dl>
<dl>
<dt>
<dd> &bull; &#8211;server=&lt;server&gt; </p>
<p> Connection information for the server in &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[::&lt;<i>port</i>&gt;][::&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip=&lt;skip-objects&gt; </p>
<p> Specify objects to skip in the operation as a comma-separated list (no spaces). Permitted values are <code>CREATE_DB</code>, <code>DATA</code>, <code>EVENTS</code>, <code>FUNCTIONS</code>, <code>GRANTS</code>, <code>PROCEDURES</code>, <code>TABLES</code>, <code>TRIGGERS</code>, and <code>VIEWS</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip-blobs </p>
<p> Do not export BLOB data.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip-gtid </p>
<p> Skip creation of GTID_PURGED statements.</dl>
<dl>
<dt>
<dd> &bull; &#8211;all </p>
<p> Generate an export file with all of the databases and the GTIDs executed to that point.</dl>
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
<p> To export all objects from a source database, the user must have these privileges: <code>SELECT</code> and <code>SHOW VIEW</code> on the database as well as <code>SELECT</code> on the mysql database. </p>
<p> Actual privileges needed may differ from installation to installation depending on the security privileges present and whether the database contains certain objects such as views or events. </p>
<p> Some combinations of the options may result in errors when the export is imported later. For example, eliminating tables but not views may result in an error when a view is imported on another server. </p>
<p> For the <code>&#8211;format</code>, <code>&#8211;export</code>, and <code>&#8211;display</code> options, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf). </p>
<p> If any database identifier specified as an argument contains special characters or is a reserved word, then it must be appropriately quoted with backticks (<code>`</code>). In turn, names quoted with backticks must also be quoted with single or double quotes depending on the operating system, i.e. (<code>&quot;</code>) in Windows or (<code>&#8216;</code>) in non-Windows systems, in order for the utilities to read backtick quoted identifiers as a single argument. For example, to export a database with the name <code>weird`db.name</code>, it must be specified as argument using the following syntax (in non-Windows): <code>&#8216;`weird&#8220;db.name`&#8217;</code>.<br />
EXAMPLES </p>
<p> To export the definitions of the database dev from a MySQL server on the local host via port 3306, producing output consisting of <code>CREATE</code> statements, use this command: </p>
<dl>
<dt>
<dd>
$ mysqldbexport&#8211; server = root : pass[at] localhost&#8211; skip = GRANTS&#8211; export = DEFINITIONS util_test<br />
#Source on localhost : &#8230; connected.<br />
#Exporting metadata from util_test<br />
                                      DROP DATABASE IF EXISTS util_test;<br />
CREATE DATABASE util_test;<br />
USE util_test;<br />
#TABLE : util_test.t1<br />
CREATE TABLE `t1` (<br />
  `a` char(30) DEFAULT NULL)ENGINE = MEMORY DEFAULT CHARSET = latin1;<br />
#TABLE : util_test.t2<br />
CREATE TABLE `t2` (<br />
  `a` char(30) DEFAULT NULL)ENGINE = MyISAM DEFAULT CHARSET = latin1;<br />
#TABLE : util_test.t3<br />
CREATE TABLE `t3` (<br />
  `a` int(11) NOT NULL AUTO_INCREMENT,<br />
  `b` char(30) DEFAULT NULL,<br />
    PRIMARY KEY(`a`))ENGINE = InnoDB AUTO_INCREMENT = 4 DEFAULT CHARSET = latin1;<br />
#TABLE : util_test.t4<br />
CREATE TABLE `t4` (<br />
  `c` int(11) NOT NULL,<br />
  `d` int(11) NOT NULL,<br />
    KEY `ref_t3` (`c`),<br />
    CONSTRAINT `ref_t3` FOREIGN KEY(`c`) REFERENCES `t3` (`a`))ENGINE = InnoDB DEFAULT CHARSET = latin1;<br />
#VIEW : util_test.v1<br />
[&#8230;]<br />
#&#8230; done.
</dl>
<p> Similarly, to export the data of the database util_test, producing bulk insert statements, use this command: </p>
<dl>
<dt>
<dd>
$ mysqldbexport&#8211; server = root : pass[at] localhost&#8211; export = DATA&#8211; bulk &#8211; insert util_test<br />
#Source on localhost : &#8230; connected.<br />
                                                                                  USE util_test;<br />
#Exporting data from util_test<br />
#Data for table util_test.t1:<br />
INSERT INTO util_test.t1 VALUES(&#8217;01 Test Basic database example&#8217;),<br />
    (&#8217;02 Test Basic database example&#8217;),<br />
    (&#8217;03 Test Basic database example&#8217;),<br />
    (&#8217;04 Test Basic database example&#8217;),<br />
    (&#8217;05 Test Basic database example&#8217;),<br />
    (&#8217;06 Test Basic database example&#8217;),<br />
    (&#8217;07 Test Basic database example&#8217;);<br />
#Data for table util_test.t2:<br />
INSERT INTO util_test.t2 VALUES(&#8217;11 Test Basic database example&#8217;),<br />
    (&#8217;12 Test Basic database example&#8217;),<br />
    (&#8217;13 Test Basic database example&#8217;);<br />
#Data for table util_test.t3:<br />
INSERT INTO util_test.t3 VALUES(1, &#8217;14 test fkeys&#8217;),<br />
    (2, &#8217;15 test fkeys&#8217;),<br />
    (3, &#8217;16 test fkeys&#8217;);<br />
#Data for table util_test.t4:<br />
INSERT INTO util_test.t4 VALUES(3, 2);<br />
#&#8230; done.
</dl>
<p> If the database to be exported does not contain only InnoDB tables and you want to ensure data integrity of the exported data by locking the tables during the read step, add a <code>&#8211;locking=lock-all</code> option to the command: </p>
<dl>
<dt>
<dd>
$ mysqldbexport&#8211; server = root : pass[at] localhost&#8211; export = DATA&#8211; bulk &#8211; insert util_test&#8211; locking = lock &#8211; all<br />
#Source on localhost : &#8230; connected.<br />
                                                                                                                      USE util_test;<br />
#Exporting data from util_test<br />
#Data for table util_test.t1:<br />
INSERT INTO util_test.t1 VALUES(&#8217;01 Test Basic database example&#8217;),<br />
    (&#8217;02 Test Basic database example&#8217;),<br />
    (&#8217;03 Test Basic database example&#8217;),<br />
    (&#8217;04 Test Basic database example&#8217;),<br />
    (&#8217;05 Test Basic database example&#8217;),<br />
    (&#8217;06 Test Basic database example&#8217;),<br />
    (&#8217;07 Test Basic database example&#8217;);<br />
#Data for table util_test.t2:<br />
INSERT INTO util_test.t2 VALUES(&#8217;11 Test Basic database example&#8217;),<br />
    (&#8217;12 Test Basic database example&#8217;),<br />
    (&#8217;13 Test Basic database example&#8217;);<br />
#Data for table util_test.t3:<br />
INSERT INTO util_test.t3 VALUES(1, &#8217;14 test fkeys&#8217;),<br />
    (2, &#8217;15 test fkeys&#8217;),<br />
    (3, &#8217;16 test fkeys&#8217;);<br />
#Data for table util_test.t4:<br />
INSERT INTO util_test.t4 VALUES(3, 2);<br />
#&#8230; done.
</dl>
<p> To export a database and include the replication commands to use the current server as the master (for example, to start a new slave using the current server as the master), use the following command: </p>
<dl>
<dt>
<dd>
$ mysqldbexport&#8211; server = root[at] localhost : 3311 util_test&#8211; export = both&#8211; rpl &#8211; user = rpl : rpl&#8211; rpl = master &#8211; v<br />
#Source on localhost : &#8230; connected.<br />
#<br />
#Stopping slave<br />
                                                                                                                             STOP SLAVE;<br />
#<br />
#Source on localhost : &#8230; connected.<br />
#Exporting metadata from util_test<br />
DROP DATABASE IF EXISTS util_test;<br />
CREATE DATABASE util_test;<br />
USE util_test;<br />
#TABLE : util_test.t1<br />
CREATE TABLE `t1` (<br />
  `a` char(30) DEFAULT NULL)ENGINE = MEMORY DEFAULT CHARSET = latin1;<br />
#&#8230; done.<br />
#Source on localhost : &#8230; connected.<br />
USE util_test;<br />
#Exporting data from util_test<br />
#Data for table util_test.t1:<br />
INSERT INTO util_test.t1 VALUES(&#8217;01 Test Basic database example&#8217;);<br />
INSERT INTO util_test.t1 VALUES(&#8217;02 Test Basic database example&#8217;);<br />
INSERT INTO util_test.t1 VALUES(&#8217;03 Test Basic database example&#8217;);<br />
INSERT INTO util_test.t1 VALUES(&#8217;04 Test Basic database example&#8217;);<br />
INSERT INTO util_test.t1 VALUES(&#8217;05 Test Basic database example&#8217;);<br />
INSERT INTO util_test.t1 VALUES(&#8217;06 Test Basic database example&#8217;);<br />
INSERT INTO util_test.t1 VALUES(&#8217;07 Test Basic database example&#8217;);<br />
#&#8230; done.<br />
#<br />
#Connecting to the current server as master<br />
CHANGE MASTER TO MASTER_HOST = &#8216;localhost&#8217;,<br />
                 MASTER_USER = &#8216;rpl&#8217;,<br />
                 MASTER_PASSWORD = &#8216;rpl&#8217;,<br />
                 MASTER_PORT = 3311,<br />
                 MASTER_LOG_FILE = &#8216;clone-bin.000001&#8217;,<br />
                 MASTER_LOG_POS = 106;<br />
#<br />
#Starting slave<br />
START SLAVE;<br />
#
</dl>
<p> Similarly, to export a database and include the replication commands to use the current server&#8217;s master (for example, to start a new slave using the same the master), use the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqldbexport-- server = root[at] localhost : 3311 util_test-- export = both-- rpl - user = rpl : rpl-- rpl = slave - v
#Source on localhost : ... connected.
#
#Stopping slave
                                                                                                                            STOP SLAVE;
#
#Source on localhost : ... connected.
#Exporting metadata from util_test
DROP DATABASE IF EXISTS util_test;
CREATE DATABASE util_test;
USE util_test;
#TABLE : util_test.t1
CREATE TABLE `t1` (
  `a` char(30) DEFAULT NULL)ENGINE = MEMORY DEFAULT CHARSET = latin1;
#... done.
#Source on localhost : ... connected.
USE util_test;
#Exporting data from util_test
#Data for table util_test.t1:
INSERT INTO util_test.t1 VALUES('01 Test Basic database example');
INSERT INTO util_test.t1 VALUES('02 Test Basic database example');
INSERT INTO util_test.t1 VALUES('03 Test Basic database example');
INSERT INTO util_test.t1 VALUES('04 Test Basic database example');
INSERT INTO util_test.t1 VALUES('05 Test Basic database example');
INSERT INTO util_test.t1 VALUES('06 Test Basic database example');
INSERT INTO util_test.t1 VALUES('07 Test Basic database example');
#... done.
#
#Connecting to the current server's master
CHANGE MASTER TO MASTER_HOST = 'localhost',
                 MASTER_USER = 'rpl',
                 MASTER_PASSWORD = 'rpl',
                 MASTER_PORT = 3310,
                 MASTER_LOG_FILE = 'clone-bin.000001',
                 MASTER_LOG_POS = 1739;
#
#Starting slave
START SLAVE;
#
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
