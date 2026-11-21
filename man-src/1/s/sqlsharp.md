---
title: "sqlsharp(1)"
name: "sqlsharp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sqlsharp/"
description: "sqlsharp – Mono SQL Query command-line tool"
---

<h2>NAME</h2>
<p> sqlsharp &#8211; Mono SQL Query command-line tool</p>
<h2>SYNOPSIS</h2>
<p> <code>sqlsharp </code> [-f filename] [-o filename] [-s]</p>
<h2>DESCRIPTION</h2>
<p> sqlsharp is a Mono SQL tool used for entering SQL queries to a database using Mono data providers. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>-f filename</i></dt>
<dd> Output file to load SQL commands from.</dd>
<dt><i>-o filename</i></dt>
<dd> Output file to send results.</dd>
<dt><i>-s</i></dt>
<dd> Silent mode.</dd></dl>
<h2>HOW TO USE</h2>
<p> The SQL tool accepts commands via its command line interface. Commands begin with a backslash followed by the command name. </p>
<p> Example: </p>
<pre>
        \open
</pre>
<p> Basically, there are five commands a user should know: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>\provider, \connectionstring, \open, \quit, and \help<br />
 </p>
<p> To connect to a database, you need to do the following: </p>
<p> 1. set your data provider via \provider </p>
<pre><code>        Example:
                SQL# \provider mysql
</code></pre>
<p> 2. set your connection string via \connectionstring </p>
<pre><code>        Example:
                SQL# \connectionstring Database=test
</code></pre>
<p> 3. open a connection to the database via \open </p>
<pre><code>        Example:
                SQL# \open
</code></pre>
<h2>CONNECTION AND PROVIDER COMMANDS</h2>
<p> These commands are used to setup the provider, connection string, and open/close the database connnection </p>
<dl>
<dt><i>ConnectionString</i></dt>
<dd> <p> Sets the Connection String </p>
<pre><code>Example:
        SQL# \ConnectionString Database=testdb
        or
        SQL# \cs Database=testdb
For more examples, see section CONNECTION STRING EXAMPLES.
</code></pre>
 </dd>
<dt><i>Provider</i></dt>
<dd> <p> Sets the Provider of the Data Source. For list of Providers, see section PROVIDERS. </p>
<pre><code>Example: to set the provider for MySQL:
        SQL# \provider mysql
           or
        SQL# \p mysql
Note: if you need to load an external provider in SQL#,
      see the SQL# command \loadextprovider
</code></pre>
 </dd>
<dt><i>ListProviders</i></dt>
<dd> <p> List ADO.NET 2.0 Providers available </p>
<pre><code>Example:
        SQL# \ListProviders
           or
        SQL# \listp
</code></pre>
 </dd>
<dt><i>BCS</i></dt>
<dd> <p> Prompts you for building each connection parameter and builds the connection string and also allows you to enter a password wich does not echo. </p>
<pre><code>Example:
        SQL# \bcs
        ConnectionString Option: Data Source [] SQL# blazer
        ConnectionString Option: Persist Security Info [False] SQL#
        ConnectionString Option: Integrated Security [False] SQL#
        ConnectionString Option: User ID [] SQL# scott
        Password: *****
        ConnectionString Option: Enlist [False] SQL#
        ConnectionString Option: Pooling [True] SQL#
        ConnectionString Option: Min Pool Size [0] SQL#
        ConnectionString Option: Max Pool Size [100] SQL#
        ConnectionString Option: Unicode [False] SQL#
        ConnectionString Option: Load Balance Timeout [0] SQL#
        ConnectionString Option: Omit Oracle Connection Name [False] SQL#
        ConnectionString is set.
</code></pre>
 </dd>
<dt><i>LoadExtProvider</i></dt>
<dd> <p> ASSEMBLY CLASS to load an external provider. Use the complete name of its assembly and its Connection class. </p>
<pre><code>Example: to load the MySQL provider Mono.Data.MySql
        SQL# \loadextprovider Mono.Data.MySql Mono.Data.MySql.MySqlConnection
</code></pre>
 </dd>
<dt><i>Open</i></dt>
<dd> <p> Opens a connection to the database </p>
<pre><code>Example:
        SQL# \open
</code></pre>
 </dd>
<dt><i>Close</i></dt>
<dd> <p> Closes the connection to the database </p>
<pre><code>Example:
        SQL# \close
</code></pre>
 </dd>
<dt><i>Default</i></dt>
<dd> <p> show default variables, such as, Provider and ConnectionString. </p>
<pre><code>Example:
        SQL# \defaults
</code></pre>
 </dd>
<dt><i>Q</i></dt>
<dd> <p> Quit </p>
<pre><code>Example:
        SQL# \q
</code></pre>
 </dd></dl>
<h2>SQL EXECUTION COMMANDS</h2>
<p> Commands to execute SQL statements </p>
<p> <i>e</i> execute SQL query (SELECT) </p>
<pre><code>Example: to execute a query
        SQL# SELECT * FROM EMPLOYEE
        SQL# \e
Note: to get \e to automatically work after entering a query, put a
      semicolon ; at the end of the query.
Example: to enter and exectue query at the same time
        SQL# SELECT * FROM EMPLOYEE;
</code></pre>
<dl>
<dt><i>exenonquery</i></dt>
<dd> <p> execute a SQL non query (not a SELECT) </p>
<pre><code>Example: to insert a row into a table:
        SQL# INSERT INTO SOMETABLE (COL1, COL2) VALUES('ABC','DEF')
        SQL# \exenonquery
Note: this can be used for those providers that are new and do not have
      the ability to execute queries yet.
</code></pre>
 </dd>
<dt><i>exescalar </i></dt>
<dd> <p> execute SQL to get a single row and single column. </p>
<pre><code>Example: to execute a Maxium aggregate
                SQL# SELECT MAX(grade) FROM class
                SQL# \exescalar
</code></pre>
 </dd>
<dt><i>exexml</i></dt>
<dd> <p> FILENAME to execute SQL and save output to XML file </p>
<pre><code>Example:
        SQL# SELECT fname, lname, hire_date FROM employee
        SQL# \exexml employee.xml
Note: this depends on DataAdapter, DataTable, and DataSet
      to be working properly
</code></pre>
 </dd></dl>
<h2>FILE COMMANDS</h2>
<dd> <p> Commands for importing commands from file to SQL# and vice versa </p>
 </dd>
<dl>
<dt><i>f</i></dt>
<dd> <p> FILENAME to read a batch of SQL# commands from file </p>
<pre><code>Example:
        SQL# \f batch.sql#
Note: the SQL# commands are interpreted as they are read. If there is
      any SQL statements, the are executed.
</code></pre>
 </dd>
<dt><i>o</i></dt>
<dd> <p> FILENAME to write result of commands executed to file. </p>
<pre><code>Example:
        SQL# \o result.txt
</code></pre>
 </dd>
<dt><i>load</i></dt>
<dd> <p> FILENAME to load from file SQL commands into SQL buffer. </p>
<pre><code>Example:
        SQL# \load commands.sql
</code></pre>
 </dd>
<dt><i>save</i></dt>
<dd> <p> FILENAME to save SQL commands from SQL buffer to file. </p>
<pre><code>Example:
        SQL# \save commands.sql
</code></pre>
 </dd></dl>
<h2>GENERAL PURPOSE COMMANDS</h2>
<p> General commands to use. </p>
<dl>
<dt><i>h</i></dt>
<dd> <p> show help (all commands). </p>
<pre><code>Example:
        SQL# \h
</code></pre>
 </dd>
<dt><i>s</i></dt>
<dd> <p> TRUE, FALSE to silent messages. </p>
<pre><code>Example 1:
        SQL# \s true
Example 2:
        SQL# \s false
</code></pre>
 </dd>
<dt><i>r</i></dt>
<dd> <p> reset or clear the query buffer. </p>
<pre><code>Example:
        SQL# \r
</code></pre>
 </dd>
<dt><i>print</i></dt>
<dd> <p> show what&#8217;s in the SQL buffer now. </p>
<pre><code>Example:
        SQL# \print
</code></pre>
<p> SH VARIABLES WHICH CAN BE USED AS PARAMETERS Commands to set variables which can be used as Parameters in an SQL statement. If the SQL contains any parameters, the parameter does not have a variable set, the user will be prompted for the value for each missing parameter. </p>
 </dd>
<dt><i>set</i></dt>
<dd> <p> NAME VALUE to set an internal variable. </p>
<pre><code>Example:
        SQL# \set sFirstName John
</code></pre>
 </dd>
<dt><i>unset</i></dt>
<dd> <p> NAME to remove an internal variable. </p>
<pre><code>Example:
        SQL# \unset sFirstName
</code></pre>
 </dd>
<dt><i>variable</i></dt>
<dd> <p> NAME to display the value of an internal variable. </p>
<pre><code>Example:
        SQL# \variable sFirstName
</code></pre>
 </dd></dl>
<h2>PROVIDER SUPPORT OPTIONS</h2>
<p> Enable or Disble support for a particular provider option </p>
<dl>
<dt><i>UseParameters</i></dt>
<dd> <p> TRUE,FALSE to use parameters when executing SQL which use the variables that were set. </p>
 </dd></dl>
<p> If this option is true, the SQL contains parameters, and for each parameter which does not have a SQL# variable set, the user will be prompted to enter the value For that parameter. </p>
<pre><code>Example:
        SQL# \useparameter true
</code></pre>
<p> Default: false </p>
<dl>
<dt><i>UseSimpleReader</i></dt>
<dd> <p> TRUE,FALSE to use simple reader when displaying results. </p>
<pre><code>Example:
        SQL# \usesimplereader true
</code></pre>
 </dd></dl>
<p> Default: false. Mostly, this is dependent on the provider. If the provider does not have enough of IDataReader implemented to have the normal reader working, then the simple reader can be used. Providers like SqlClient, MySQL, and PostgreSQL have this ption defaulting to true. </p>
<h2>PROVIDERS</h2>
<pre><code>PROVIDER NAME NAMESPACE ASSEMBLY
oracle Oracle 8i-11g System.Data.OracleClient System.Data.OracleClient
postgresql NetPostgreSQL Npgsql Npgsql
bytefx ByteFX MySQL ByteFX.Data.MySqlClient ByteFX.Data
sqlclient MS SQL 7-2008 System.Data.SqlClient System.Data
odbc ODBC System.Data.Odbc System.Data
sqlite SQL Lite Mono.Data.SqliteClient Mono.Data.SqliteClient
sybase Sybase Mono.Data.SybaseClient Mono.Data.SybaseClient
firebird Firebird SQL FirebirdSql.Data.FirebirdSql FirebirdSql.Data.Firebird
mysql MySQL AB MySql.Data.MySqlClient MySql.Data
NOTES:
Ngsql is the .Net Data Provider for PosgreSQL. The
latest verison can be downloaded from
http://npgsql.projects.postgresql.org/MySql.Data is the MySQL Connector/Net for connecting to MySql databases.
For MySQL, it is strongly recommend to use MySql.Data instead of the old
ByteFX.Data provider. Unfortunately, MySql.Data is not included with Mono.
You can download the latest MySQL Connector/Net from MySQL AB at
http://dev.mysql.com/downloads/FirebirdSql.Data.Firebird can be downloaded from here:
http://www.firebirdsql.org/index.php?op=files&amp;id=netprovider
</code></pre>
<h2>CONNECTION STRING SAMPLES</h2>
<p> Example connection strings for various providers to be used via the command \ConnectionString </p>
<pre><code>Example of usage:
        \connectionstring Database=testdb
Connection String examples:
Microsoft SQL Server via System.Data.SqlClient
        Server=DANPC;Database=pubs;User ID=saPassword=;
        For Integrated Security, bear in mind that Mono is not
        integrated with Windows, SQL Server client nor server, nor
        Windows Server. Therefore, you must provide the Windows Domain
        name and domain user name and password for this user.
        Server=DANPC;Database=pubs;User ID=DOMAINser;Password=pass;Integrated Security=SSPI
        For a server locally, you can use localhost.
ODBC via System.Data.Odbc provider using
a DSN named &quot;MSSQLDSN&quot; I set up
in the Windows control panel's ODBC Data Sources
which connects to Microsoft SQL Server 2000:
        DSN=MSSQLDSN;UID=danmorg;PWD=freetds
To use ODBC ON Unix, consider unixODBC fromhttp://www.unixodbc.org/or use iODBC fromhttp://www.iodbc.org/SQL Lite via Mono.Data.SqliteClient
provider which connects to the
database file SqliteTest.db; if not found,
the file is created:
        URI=file:SqliteTest.db
Oracle via System.Data.OracleClient
        Data Source=testdb;User ID=scott;Password=tiger
        If you prefer to not use a tnsnames.ora file, you can
        use a connection string which allows a
        TNS network description that is parentheses delimited
        like the following which has the host, port, and
        service name. For host, you can specify an IP address
        instead of a hostname.
User ID=SCOTT;
Password=TIGER;
Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.101)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=TESTDB)))
Npgsql (.NET PostgreSQL) from
http://gborg.postgresql.org/project/npgsql/projdisplay.php        Server=localhost;Database=test;User ID=postgres;Password=fun2db
ByteFX (ByteFX MySQL) from
        Please use MySql.Data instead.
        Server=localhost;Database=test;User ID=mysql;Password=
FirebirdSql via FirebirdSql.Data.Firebird (download latest form FirebirdSql.org)
        Database=C:\FIREBIRD\EXAMPLES\EMPLOYEE.FDB;User=SYSDBA;Password=masterkey;Dialect=3;Server=localhost
MySQL via (MySql.Data) MySQL Connector/Net fromhttp://www.mysql.com/        Server=localhost;Database=test;User ID=mysql;Password=mypass;Pooling=false
</code></pre>
<h2>TRACING SUPPORT</h2>
<p> No support for tracing right now.  </p>
<h2>AUTHORS</h2>
<p> The Mono SQL Query Tool was written </p>
<pre><code>by Daniel Morgan &lt;monodanmorg [at] yahoo.com&gt;
</code></pre>
<h2>LICENSE</h2>
<p> The Mono SQL Query Tool is released under the terms of the GNU GPL. Please read the accompanying `COPYING&#8217; file for details. Alternative licenses are available from Novell or Daniel Morgan.  </p>
<h2>BUGS</h2>
<p> To report bugs in the compiler, you can use `bug-buddy&#8217;, or you can file bug reports in our bug tracking system: </p>
<pre><code>
http://bugzilla.xamarin.com.
</code></pre>
<h2>MAILING LISTS</h2>
<p> For details, visit: </p>
<pre><code>
http://lists.ximian.com/mailman/listinfo/mono-devel-list
</code></pre>
<h2>WEB SITE</h2>
<p> For details, visit: </p>
<pre><code>
http://www.mono-project.com
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mono/">mono</a>(1) </p>
<h2>Index</h2>
