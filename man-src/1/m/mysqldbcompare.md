---
title: "mysqldbcompare(1)"
name: "mysqldbcompare"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqldbcompare/"
description: "mysqldbcompare – Compare Two Databases and Identify Differences"
---

<h2 class="name">NAME</h2>
<p> mysqldbcompare &#8211; Compare Two Databases and Identify Differences </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqldbcompare [</code><i>options</i><code>] </code><i>db1</i><code> [</code><i>:db2</i><code>] &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility compares the objects and data from two databases to find differences. It identifies objects having different definitions in the two databases and presents them in a diff-style format of choice. Differences in the data are shown using a similar diff-style format. Changed or missing rows are shown in a standard format of GRID, CSV, TAB, or VERTICAL. </p>
<p> Use the notation db1:db2 to name two databases to compare, or, alternatively just db1 to compare two databases with the same name. The latter case is a convenience notation for comparing same-named databases on different servers. </p>
<p> The comparison may be run against two databases of different names on a single server by specifying only the <code>&#8211;server1</code> option. The user can also connect to another server by specifying the <code>&#8211;server2</code> option. In this case, db1 is taken from server1 and db2 from server2. </p>
<p> Those objects considered in the database include tables, views, triggers, procedures, functions, and events. A count for each object type can be shown with the <code>-vv</code> option. </p>
<p> The check is performed using a series of steps called tests. By default, the utility stops on the first failed test, but you can specify the <code>&#8211;run-all-tests</code> option to cause the utility to run all tests regardless of their end state. </p>
<p> Note: Using <code>&#8211;run-all-tests</code> may produce expected cascade failures. For example, if the row counts differ among two tables being compared, the data consistency will also fail. </p>
<p> The tests include the following: </p>
<dl>
<dt>
<dd> 1. Check database definitions </p>
<p> A database existence precondition check ensures that both databases exist. If they do not, no further processing is possible and the <code>&#8211;run-all-tests</code> option is ignored.</dl>
<dl>
<dt>
<dd> 2. Check existence of objects in both databases </p>
<p> The test for objects in both databases identifies those objects missing from one or another database. The remaining tests apply only to those objects that appear in both databases. To skip this test, use the <code>&#8211;skip-object-compare</code> option. That can be useful when there are known missing objects among the databases.</dl>
<dl>
<dt>
<dd> 3. Compare object definitions </p>
<p> The definitions (the <code>CREATE</code> statements) are compared and differences are presented. To skip this test, use the <code>&#8211;skip-diff</code> option. That can be useful when there are object name differences only that you want to ignore.</dl>
<dl>
<dt>
<dd> 4. Check table row counts </p>
<p> This check ensures that both tables have the same number of rows. This does not ensure that the table data is consistent. It is merely a cursory check to indicate possible missing rows in one table or the other. The data consistency check identifies the missing rows. To skip this test, use the <code>&#8211;skip-row-count</code> option.</dl>
<dl>
<dt>
<dd> 5. Check table data consistency </p>
<p> This check identifies both changed rows as well as missing rows from one or another of the tables in the databases. Changed rows are displayed as a diff-style report with the format chosen (<code>GRID</code> by default) and missing rows are also displayed using the format chosen. To skip this test, use the <code>&#8211;skip-data-check</code> option.</dl>
<p> You may want to use the &#8211;skip-xxx options to run only one of the tests. This might be helpful when working to bring two databases into synchronization, to avoid running all of the tests repeatedly during the process. </p>
<p> Each test completes with one of the following states: </p>
<dl>
<dt>
<dd> &bull; <code>pass</code> </p>
<p> The test succeeded.</dl>
<dl>
<dt>
<dd> &bull; <code>FAIL</code> </p>
<p> The test failed. Errors are displayed following the test state line.</dl>
<dl>
<dt>
<dd> &bull; <code>SKIP</code> </p>
<p> The test was skipped due to a missing prerequisite or a skip option.</dl>
<dl>
<dt>
<dd> &bull; <code>WARN</code> </p>
<p> The test encountered an unusual but not fatal error.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;</code> </p>
<p> The test is not applicable to this object.</dl>
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
<p> To specify how to display output for changed or missing rows, use one of the following values with the <code>&#8211;format</code> option: </p>
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
<p> The <code>&#8211;changes-for</code> option controls the direction of the difference (by specifying the object to be transformed) in either the difference report (default) or the transformation report (designated with the <code>&#8211;difftype=sql</code> option). Consider the following command: </p>
<dl>
<dt>
<dd>
<pre><code>
mysqldbcompare-- server1 = root[at] host1-- server2 = root[at] host2-- difftype = sql
    db1 : dbx
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
<p> You must provide connection parameters (user, host, password, and so forth) for an account that has the appropriate privileges to access all objects in the operation. </p>
<p> If the utility is to be run on a server that has binary logging enabled, and you do not want the comparison steps logged, use the <code>&#8211;disable-binary-logging</code> option.<br />
OPTIONS </p>
<p> <code>mysqldbcompare</code> accepts the following command-line options: </p>
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
<dd> &bull; &#8211;disable-binary-logging </p>
<p> If binary logging is enabled, disable it during the operation to prevent comparison operations from being written to the binary log. Note: Disabling binary logging requires the <code>SUPER</code> privilege.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;format&gt;, -f&lt;format&gt; </p>
<p> Specify the display format for changed or missing rows. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, and <code>vertical</code>. The default is <code>grid</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Do not print anything. Return only an exit code of success or failure.</dl>
<dl>
<dt>
<dd> &bull; &#8211;run-all-tests, -a </p>
<p> Do not halt at the first difference found. Process all objects.</dl>
<dl>
<dt>
<dd> &bull; &#8211;server1=&lt;source&gt; </p>
<p> Connection information for the first server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;server2=&lt;source&gt; </p>
<p> Connection information for the second server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[::&lt;<i>port</i>&gt;][::&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-reverse </p>
<p> Produce a transformation report containing the SQL statements to conform the object definitions specified in reverse. For example, if &#8211;changes-for is set to server1, also generate the transformation for server2. Note: The reverse changes are annotated and marked as comments.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip-data-check </p>
<p> Skip the data consistency check.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip-diff </p>
<p> Skip the object definition difference check.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip-object-compare </p>
<p> Skip the object comparison check.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip-row-count </p>
<p> Skip the row count check.</dl>
<dl>
<dt>
<dd> &bull; &#8211;span-key-size=&lt;number of bytes to use for key&gt; </p>
<p> Change the size of the key used for compare table contents. A higher value can help to get more accurate results comparing large databases, but may slow the algorithm. </p>
<p> Default value is 8.</dl>
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
<p> The login user must have the appropriate permissions to read all databases and tables listed. </p>
<p> For the <code>&#8211;difftype</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;difftype=d</code> specifies the differ type. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf). </p>
<p> If any database identifier specified as an argument contains special characters or is a reserved word, then it must be appropriately quoted with backticks (<code>`</code>). In turn, names quoted with backticks must also be quoted with single or double quotes depending on the operating system, i.e. (<code>&quot;</code>) in Windows or (<code>&#8216;</code>) in non-Windows systems, in order for the utilities to read backtick quoted identifiers as a single argument. For example, to compare a database with the name <code>weird`db.name</code> with <code>other:weird`db.name</code>, the database pair must be specified using the following syntax (in non-Windows): <code>&#8216;`weird&#8220;db.name`:`other:weird&#8220;db.name`&#8217;</code>.<br />
EXAMPLES </p>
<p> Use the following command to compare the emp1 and emp2 databases on the local server, and run all tests even if earlier tests fail: </p>
<dl>
<dt>
<dd>
$ mysqldbcompare&#8211; server1 = root[at] localhost emp1 : emp2&#8211; run &#8211; all &#8211; tests<br />
#server1 on localhost : &#8230; connected.<br />
#Checking databases emp1 on server1 and emp2 on server2<br />
                                                                              WARNING : Objects in server2 : emp2 but not in server1 : emp1 : TRIGGER : trg PROCEDURE : p1 TABLE : t1 VIEW : v1 Defn Row Data Type Object Name Diff Count Check&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -FUNCTION f1 pass &#8211;<br />
                                                                                                                                                                                             -TABLE departments pass pass FAIL<br />
                                                                                                                                                                                                  Data differences found among rows : &#8212; -emp1.departments++ +<br />
                                                                                                                                                                                             emp2.departments<br />
                                                                                                                                                                                             @ @-1,<br />
                   4 + 1, 4 @ @ ************************ * 1. row *************************dept_no : d002 &#8211; dept_name : dunno + dept_name : Finance 1 rows.Rows in emp1.departments not in emp2.departments * ************************1. row * ************************dept_no : d008 dept_name : Research 1 rows.Rows in emp2.departments not in emp1.departments * ************************1. row * ************************dept_no : d100 dept_name : stupid 1 rows.TABLE dept_manager pass pass pass Database consistency check failed.<br />
#&#8230; done
</dl>
<p> Given: two databases with the same table layout. Data for each table contains: </p>
<dl>
<dt>
<dd>
mysql &gt; select *from db1.t1;<br />
+ &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | a | b |<br />
    +&#8211; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | 1 | Test 789 |<br />
    | 2 | Test 456 |<br />
    | 3 | Test 123 |<br />
    | 4 | New row &#8211; db1 |<br />
    +&#8211; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+4 rows in set(0.00 sec)<br />
                                    mysql<br />
        &gt; select *from db2.t1;<br />
+ &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | a | b |<br />
    +&#8211; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | 1 | Test 123 |<br />
    | 2 | Test 456 |<br />
    | 3 | Test 789 |<br />
    | 5 | New row &#8211; db2 |<br />
    +&#8211; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+4 rows in set(0.00 sec)
</dl>
<p> To generate the SQL statements for data transformations to make db1.t1 the same as db2.t1, use the <code>&#8211;changes-for=server1</code> option. We must also include the <code>-a</code> option to ensure that the data consistency test is run. The following command illustrates the options used and an excerpt from the results generated: </p>
<dl>
<dt>
<dd>
$ mysqldbcompare &#8211;server1=root:root [at] localhost \<br />
    &#8211;server2=root:root [at] localhost db1:db2 &#8211;changes-for=server1 -a \<br />
    &#8211;difftype=sql<br />
[&#8230;]<br />
#Defn Row Data<br />
#Type Object Name Diff Count<br />
Check #<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
#TABLE t1 pass pass FAIL<br />
# #Data transformations for direction = server1:<br />
#Data differences found among rows : UPDATE db1.t1 SET b = &#8216;Test 123&#8217;<br />
WHERE a = &#8216;1&#8217;;<br />
UPDATE db1.t1 SET b = &#8216;Test 789&#8217; WHERE a = &#8216;3&#8217;;<br />
DELETE<br />
FROM db1.t1 WHERE a = &#8216;4&#8217;; INSERT INTO db1.t1 (a, b) VALUES(&#8216;5&#8217;, &#8216;New<br />
row &#8211; db2&#8217;);<br />
#Database consistency check failed.# #&#8230; done
</dl>
<p> Similarly, when the same command is run with <code>&#8211;changes-for=server2</code> and <code>&#8211;difftype=sql</code>, the following report is generated: </p>
<dl>
<dt>
<dd>
$ mysqldbcompare &#8211;server1=root:root [at] localhost \<br />
    &#8211;server2=root:root [at] localhost db1:db2 &#8211;changes-for=server2 -a \<br />
    &#8211;difftype=sql<br />
[&#8230;]<br />
#Defn Row Data<br />
#Type Object Name Diff Count<br />
Check #<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
#TABLE t1 pass pass FAIL<br />
# #Data transformations for direction = server2:<br />
#Data differences found among rows : UPDATE db2.t1 SET b = &#8216;Test 789&#8217;<br />
WHERE a = &#8216;1&#8217;;<br />
UPDATE db2.t1 SET b = &#8216;Test 123&#8217; WHERE a = &#8216;3&#8217;;<br />
DELETE<br />
FROM db2.t1 WHERE a = &#8216;5&#8217;; INSERT INTO db2.t1 (a, b) VALUES(&#8216;4&#8217;, &#8216;New<br />
row &#8211; db1&#8217;);
</dl>
<p> With the <code>&#8211;difftype=sql</code> SQL generation option set, <code>&#8211;show-reverse</code> shows the object transformations in both directions. Here is an excerpt of the results: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqldbcompare --server1=root:root [at] localhost \
--server2=root:root [at] localhost db1:db2 --changes-for=server1 \
--show-reverse -a --difftype=sql
[...]
#Defn Row Data
#Type Object Name Diff Count
Check #
-------------------------------------------------------------------------
#TABLE t1 pass pass FAIL
# #Data transformations for direction = server1:
#Data differences found among rows : UPDATE db1.t1 SET b = 'Test 123'
WHERE a = '1';
UPDATE db1.t1 SET b = 'Test 789' WHERE a = '3';
DELETE
FROM db1.t1 WHERE a = '4'; INSERT INTO db1.t1 (a, b) VALUES('5', 'New
row - db2');
#Data transformations for direction = server2:
#Data differences found among rows : UPDATE db2.t1 SET b = 'Test 789'
WHERE a = '1'; UPDATE db2.t1 SET b = 'Test 123' WHERE a = '3'; DELETE
FROM db2.t1 WHERE a = '5'; INSERT INTO db2.t1 (a, b) VALUES('4', 'New
row - db1');
#Database consistency check failed.# #... done
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
