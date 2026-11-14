---
title: "mysqlindexcheck(1)"
name: "mysqlindexcheck"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlindexcheck/"
description: "mysqlindexcheck – Identify Potentially Redundant Table Indexes"
---

<h2 class="name">NAME</h2>
<p> mysqlindexcheck &#8211; Identify Potentially Redundant Table Indexes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlindexcheck [</code><i>options</i><code>] </code><i>db</i><code>[</code><i>:table</i><code>] &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility reads the indexes for one or more tables and identifies duplicate and potentially redundant indexes. </p>
<p> To check all tables in a database, specify only the database name. To check a specific table, name the table in <i>db.table</i> format. It is possible to mix database and table names. </p>
<p> You can scan tables in any database except the internal databases <code>mysql</code>, <code>INFORMATION_SCHEMA</code>, and <code>performance_schema</code>. </p>
<p> Depending on the index type, the utility applies the following rules to compare indexes (designated as idx_a and idx_b): </p>
<dl>
<dt>
<dd> &bull; <code>BTREE</code> </p>
<p> idx_b is redundant to idx_a if and only if the first <i>n</i> columns in idx_b also appear in idx_a. Order and uniqueness count.</dl>
<dl>
<dt>
<dd> &bull; <code>HASH</code> </p>
<p> idx_a and idx_b are duplicates if and only if they contain the same columns in the same order. Uniqueness counts.</dl>
<dl>
<dt>
<dd> &bull; <code>SPATIAL</code> </p>
<p> idx_a and idx_b are duplicates if and only if they contain the same column (only one column is permitted).</dl>
<dl>
<dt>
<dd> &bull; <code>FULLTEXT</code> </p>
<p> idx_b is redundant to idx_a if and only if all columns in idx_b are included in idx_a. Order counts.</dl>
<p> To see <code>DROP</code> statements to drop redundant indexes, specify the <code>&#8211;show-drops</code> option. To examine the existing indexes, use the <code>&#8211;verbose</code> option, which prints the equivalent <code>CREATE INDEX</code> (or <code>ALTER TABLE</code> for primary keys. </p>
<p> To display the best or worst nonprimary key indexes for each table, use the <code>&#8211;best</code> or <code>&#8211;worst</code> option. This causes the output to show the best or worst indexes from tables with 10 or more rows. By default, each option shows five indexes. To override that, provide an integer value for the option. </p>
<p> To change the format of the index lists displayed for the <code>&#8211;show-indexes</code>, <code>&#8211;best</code>, and <code>&#8211;worst</code> options, use one of the following values with the <code>&#8211;format</code> option: </p>
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
<dd> &bull; <code>sql</code> </p>
<p> print SQL statements rather than a list.</dl>
<dl>
<dt>
<dd> &bull; <code>vertical</code> </p>
<p> Display output in single-column format like that of the \G command for the <code>mysql</code> monitor.</dl>
<p> Note: The <code>&#8211;best</code> and <code>&#8211;worst</code> lists cannot be printed as SQL statements.<br />
OPTIONS </p>
<p> <code>mysqlindexcheck</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;best[=&lt;N&gt;] </p>
<p> If <code>&#8211;stats</code> is given, limit index statistics to the best <i>N</i> indexes. The default value of <i>N</i> is 5 if omitted.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;index_format&gt;, -f&lt;index_format&gt; </p>
<p> Specify the index list display format for output produced by <code>&#8211;stats</code>. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, <code>sql</code>, and <code>vertical</code>. The default is <code>grid</code>.</dl>
<dl>
<dt>
<dd> &bull; &#8211;server=&lt;source&gt; </p>
<p> Connection information for the server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-drops, -d </p>
<p> Display <code>DROP</code> statements for dropping indexes.</dl>
<dl>
<dt>
<dd> &bull; &#8211;show-indexes, -i </p>
<p> Display indexes for each table.</dl>
<dl>
<dt>
<dd> &bull; &#8211;skip, -s </p>
<p> Skip tables that do not exist.</dl>
<dl>
<dt>
<dd> &bull; &#8211;stats </p>
<p> Show index performance statistics.</dl>
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
<dd> &bull; &#8211;worst[=&lt;N&gt;] </p>
<p> If <code>&#8211;stats</code> is given, limit index statistics to the worst <i>N</i> indexes. The default value of <i>N</i> is 5 if omitted.</dl>
<p>NOTES </p>
<p> You must provide connection parameters (user, host, password, and so forth) for an account that has the appropriate privileges to read all objects accessed during the operation. </p>
<p> For the <code>&#8211;format</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> To check all tables in the employees database on the local server to see the possible redundant and duplicate indexes, use this command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqlindexcheck-- server = root[at] localhost employees
#Source on localhost : ... connected.
#The following indexes are duplicates or redundant for table employees.dept_emp:
#
                                 CREATE INDEX emp_no ON employees.dept_emp(emp_no) USING BTREE
#may be redundant or duplicate of:
                                     ALTER TABLE employees.dept_emp ADD PRIMARY
                                     KEY(emp_no, dept_no)
#The following indexes are duplicates or redundant for table employees.dept_manager:
#
CREATE INDEX emp_no ON employees.dept_manager(emp_no) USING BTREE
#may be redundant or duplicate of:
    ALTER TABLE employees.dept_manager ADD PRIMARY KEY(emp_no, dept_no)
#The following indexes are duplicates or redundant for table employees.salaries:
#
CREATE INDEX emp_no ON employees.salaries(emp_no) USING BTREE
#may be redundant or duplicate of:
    ALTER TABLE employees.salaries ADD PRIMARY KEY(emp_no, from_date)
#The following indexes are duplicates or redundant for table employees.titles:
#
CREATE INDEX emp_no ON employees.titles(emp_no) USING BTREE
#may be redundant or duplicate of:
    ALTER TABLE employees.titles ADD PRIMARY KEY(emp_no, title, from_date)
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
