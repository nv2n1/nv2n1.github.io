---
title: "mysqldiff(1)"
name: "mysqldiff"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqldiff/"
description: "mysqldiff – Identify Differences Among Database Objects"
---

<h2 class="name">NAME</h2>
<p> mysqldiff &#8211; Identify Differences Among Database Objects </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqldiff [</code><i>options</i><code>] {</code><i>db1</i><code>[</code><i>:db1</i><code>] | {</code><i>db1.obj1</i><code>[</code><i>:db2.obj2</i><code>]} &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility reads the definitions of objects and compares them using a diff-like method to determine whether they are the same. The utility displays the differences for objects that are not the same. </p>
<p> Use the notation db1:db2 to name two databases to compare, or, alternatively just db1 to compare two databases with the same name. The latter case is a convenience notation for comparing same-named databases on different servers. </p>
<p> The comparison may be run against two databases of different names on a single server by specifying only the <code>&#8211;server1</code> option. The user can also connect to another server by specifying the <code>&#8211;server2</code> option. In this case, db1 is taken from server1 and db2 from server2. </p>
<p> When a database pair is specified, all objects in one database are compared to the corresponding objects in the other. Any objects not appearing in either database produce an error. </p>
<p> To compare a specific pair of objects, add an object name to each database name in <i>db.obj</i> format. For example, use db1.obj1:db2.obj2 to compare two named objects, or db1.obj1 to compare an object with the same name in databases with the same name. It is not legal to mix a database name with an object name. For example, db1.obj1:db2 and db1:db2.obj2 are illegal. </p>
<p> The comparison may be run against a single server for comparing two databases of different names on the same server by specifying only the <code>&#8211;server1</code> option. Alternatively, you can also connect to another server by specifying the <code>&#8211;server2</code> option. In this case, the first object to compare is taken from server1 and the second from server2. </p>
<p> By default, the utility generates object differences as a difference report. However, you can generate a transformation report containing SQL statements for transforming the objects for conformity instead. Use the &#8216;sql&#8217; value for the <code>&#8211;difftype</code> option to produce a listing that contains the appropriate ALTER commands to conform the object definitions for the object pairs specified. If a transformation cannot be formed, the utility reports the diff of the object along with a warning statement. See important limitations in the NOTES section. </p>
<p> To specify how to display diff-style output, use one of the following values with the <code>&#8211;difftype</code> option: </p>
<dl>
<dt>
<dd> &bull; <code>unified</code> (default) </p>
<p> Display unified format output.</dl>
<dl>
<dt>
<dd> &bull; <code>context</code> </p>
<p> Display context format output.</dl>
<dl>
<dt>
<dd> &bull; <code>differ</code> </p>
<p> Display differ-style format output.</dl>
<dl>
<dt>
<dd> &bull; <code>sql</code> </p>
<p> Display SQL transformation statement output.</dl>
<p> The <code>&#8211;changes-for</code> option controls the direction of the difference (by specifying the object to be transformed) in either the difference report (default) or the transformation report (designated with the <code>&#8211;difftype=sql</code> option). Consider the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
mysqldiff-- server1 = root[at] host1-- server2 = root[at] host2-- difftype = sql
                                                                                 db1.table1 : dbx.table3
</code></pre>
</dl>
<p> The leftmost database (db1) exists on the server designated by the <code>&#8211;server1</code> option (host1). The rightmost database (dbx) exists on the server designated by the <code>&#8211;server2</code> option (host2). </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;changes-for=server1</code>: Produce output that shows how to make the definitions of objects on server1 like the definitions of the corresponding objects on server2.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;changes-for=server2</code>: Produce output that shows how to make the definitions of objects on server2 like the definitions of the corresponding objects on server1.</dl>
<p> The default direction is server1. </p>
<p> For <code>sql</code> difference format, you can also see the reverse transformation by specifying the <code>&#8211;show-reverse</code> option. </p>
<p> The utility stops on the first occurrence of missing objects or when an object does not match. To override this behavior, specify the <code>&#8211;force</code> option to cause the utility to attempt to compare all objects listed as arguments.<br />
OPTIONS </p>
<p> <code>mysqldiff</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;changes-for=&lt;direction&gt; </p>
<p> Specify the server to show transformations to match the other server. For example, to see the transformation for transforming object definitions on server1 to match the corresponding definitions on server2, use <code>&#8211;changes-for=server1</code>. Permitted values are <code>server1</code> and <code>server2</code>. The default is <code>server1</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;difftype=&lt;difftype&gt;, -d&lt;difftype&gt; </p>
<p> Specify the difference display format. Permitted format values are <code>unified</code>, <code>context</code>, <code>differ</code>, and <code>sql</code>. The default is <code>unified</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;force </p>
<p> Do not halt at the first difference found. Process all objects to find all differences.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Do not print anything. Return only an exit code of success or failure.</dl>
<dl>
<dt>
<dd> &bull; &#8211;server1=&lt;source&gt; </p>
<p> Connection information for the first server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;server2=&lt;source&gt; </p>
<p> Connection information for the second server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-reverse </p>
<p> Produce a transformation report containing the SQL statements to conform the object definitions specified in reverse. For example, if <code>&#8211;changes-for</code> is set to server1, also generate the transformation for server2. Note: The reverse changes are annotated and marked as comments.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;width=&lt;number&gt; </p>
<p> Change the display width of the test report. The default is 75 characters.</dl>
<p>NOTES </p>
<p> You must provide connection parameters (user, host, password, and so forth) for an account that has the appropriate privileges to access all objects to be compared. </p>
<p> The SQL transformation feature has these known limitations: </p>
<dl>
<dt>
<dd> &bull; When tables with partition differences are encountered, the utility generates the <code>ALTER TABLE</code> statement for all other changes but prints a warning and omits the partition differences.</dl>
<dl>
<dt>
<dd> &bull; If the transformation detects table options in the source table (specified with the <code>&#8211;changes-for</code> option) that are not changed or do not exist in the target table, the utility generates the <code>ALTER TABLE</code> statement for all other changes but prints a warning and omits the table option differences.</dl>
<dl>
<dt>
<dd> &bull; Rename for events is not supported. This is because <code>mysqldiff</code> compares objects by name. In this case, depending on the direction of the diff, the event is identified as needing to be added or a <code>DROP EVENT</code> statement is generated.</dl>
<dl>
<dt>
<dd> &bull; Changes in the definer clause for events are not supported.</dl>
<dl>
<dt>
<dd> &bull; SQL extensions specific to MySQL Cluster are not supported.</dl>
<p> For the <code>&#8211;difftype</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;difftype=d</code> specifies the differ type. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf). </p>
<p> If any database object identifier specified as an argument contains special characters or is a reserved word, then it must be appropriately quoted with backticks (<code>`</code>). In turn, names quoted with backticks must also be quoted with single or double quotes depending on the operating system, i.e. (<code>&quot;</code>) in Windows or (<code>&#8216;</code>) in non-Windows systems, in order for the utilities to read backtick quoted identifiers as a single argument. For example, to show the difference between table <code>weird`table1</code> from database <code>weird`db.name</code> and table <code>weird`table2</code> from database <code>other:weird`db.name</code>, the objects pair must be specified using the following syntax (in non-Windows): <code>&#8216;`weird&#8220;db.name`.`weird&#8220;table1`:`other:weird&#8220;db.name`.`weird&#8220;table2`&#8217;</code>.<br />
EXAMPLES </p>
<p> To compare the employees and emp databases on the local server, use this command: </p>
<dl>
<dt>
<dd>
$ mysqldiff&#8211; server1 = root[at] localhost employees : emp1<br />
#server1 on localhost : &#8230; connected.<br />
                                                           WARNING : Objects in server1 : employees but not in server2 : emp1 : EVENT : e1<br />
                                                                                                                                            Compare failed.One or<br />
                        more differences found.$ mysqldiff&#8211; server1 = root[at] localhost<br />
                                                                           employees.t1 : emp1.t1 employees.t3 : emp1.t3<br />
#server1 on localhost : &#8230; connected.<br />
#Comparing employees.t1 to emp1.t1[PASS]<br />
#server1 on localhost : &#8230; connected.<br />
#Comparing employees.t3 to emp1.t3[PASS]<br />
                                                                                                                     Success.All objects are the same.$ mysqldiff&#8211; server1 = root[at] localhost<br />
                                                                                                                                                                                  employees.salaries : emp1.salaries&#8211; differ<br />
#server1 on localhost : &#8230; connected.<br />
#Comparing employees.salaries to emp1.salaries[FAIL]<br />
#Object definitions are not the same:<br />
                                                                                                                                                                                                           CREATE TABLE `salaries` (<br />
    `emp_no` int(11) NOT NULL,<br />
    `salary` int(11) NOT NULL,<br />
    `from_date` date NOT NULL,<br />
    `to_date` date NOT NULL,<br />
                                                                                                                                                                                                               PRIMARY KEY(`emp_no`,`from_date`),<br />
                                                                                                                                                                                                               KEY `emp_no` (`emp_no`) -) ENGINE = InnoDB DEFAULT CHARSET = latin1<br />
    ? ^^^^^+) ENGINE = MyISAM DEFAULT CHARSET = latin1<br />
    ? ++^^^Compare failed.One or more differences found.
</dl>
<p> The following examples show how to generate a transformation report. Assume the following object definitions: </p>
<p> Host1: </p>
<dl>
<dt>
<dd>
CREATE TABLE db1.table1(num int, misc char(30));
</dl>
<p> Host2: </p>
<dl>
<dt>
<dd>
CREATE TABLE dbx.table3(num int, notes char(30), misc char(55));
</dl>
<p> To generate a set of SQL statements that transform the definition of db1.table1 to dbx.table3, use this command: </p>
<dl>
<dt>
<dd>
$ mysqldiff &#8211;server1=root [at] host1 &#8211;server2=root [at] host2 \<br />
      &#8211;changes-for=server1 &#8211;difftype=sql \<br />
      db1.table1:dbx.table3<br />
#server1 on host1 : &#8230; connected.<br />
#server2 on host2 : &#8230; connected.<br />
#Comparing db1.table1 to dbx.table3[FAIL]<br />
#Transformation statements:<br />
ALTER TABLE db1.table1<br />
  ADD COLUMN notes char(30) AFTER a,<br />
  CHANGE COLUMN misc misc char(55);<br />
Compare failed.One or more differences found.
</dl>
<p> To generate a set of SQL statements that transform the definition of dbx.table3 to db1.table1, use this command: </p>
<dl>
<dt>
<dd>
$ mysqldiff &#8211;server1=root [at] host1 &#8211;server2=root [at] host2 \<br />
      &#8211;changes-for=server2 &#8211;difftype=sql \<br />
      db1.table1:dbx.table3<br />
#server1 on host1 : &#8230; connected.<br />
#server2 on host2 : &#8230; connected.<br />
#Comparing db1.table1 to dbx.table3[FAIL]<br />
#Transformation statements:<br />
ALTER TABLE dbx.table3<br />
  DROP COLUMN notes,<br />
  CHANGE COLUMN misc misc char(30);<br />
Compare failed.One or more differences found.
</dl>
<p> To generate a set of SQL statements that transform the definitions of dbx.table3 and db1.table1 in both directions, use this command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqldiff-- server1 = root[at] host1-- server2 = root[at] host2-- show - reverse-- difftype = sql
                                                                                                    db1.table1 : dbx.table3
#server1 on host1 : ... connected.
#server2 on host2 : ... connected.
#Comparing db1.table1 to dbx.table3[FAIL]
#Transformation statements:
#-- destination = server1:
                                                                                                                     ALTER TABLE db1.table1
                                                                                                                         ADD COLUMN notes char(30) AFTER a,
              CHANGE COLUMN misc misc char(55);
#-- destination = server2:
#ALTER TABLE dbx.table3
#DROP COLUMN notes,
#CHANGE COLUMN misc misc char(30);
Compare failed.One or more differences found.
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
