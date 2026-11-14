---
title: "iodbctestw(1)"
name: "iodbctestw"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iodbctestw/"
description: "iodbctest, iodbctestw – iODBC Demonstration programs"
---

<h2 class="name">NAME</h2>
<p> iodbctest, iodbctestw &#8211; iODBC Demonstration programs</p>
<h2>SYNOPSIS</h2>
<p> <code>iodbctest</code> [<code>&quot;DSN=xxxx[;UID=xxxx][;PWD=xxxx][;OPT=value]&quot;</code>]<br />
 <code>iodbctestw</code> [<code>&quot;DSN=xxxx[;UID=xxxx][;PWD=xxxx][;OPT=value]&quot;</code>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>iodbctest</code> program and <code>iodbtestw</code> programs are simple ODBC sample programs, showing the strength of the ODBC API to connect to any ODBC enabled database, issue SQL commands and retrieve the query results. </p>
<p> The <code>iodbctest</code> program uses the standard ODBC API calls to connect using any DSN, but retrieves all results in ASCII mode. </p>
<p> The <code>iodbctestw</code> program uses the ODBC Unicode API calls to connect using any DSN, and retrieves all results in Unicode mode. </p>
<h2>OPTIONS</h2>
<p> The <code>iodbctest</code> program uses the SQLDriverConnect function to make a connection using any available ODBC compliant driver. This allows the user to override any ODBC connect attribute in the DSN string. </p>
<p> Connect strings should start with either a <i>DSN=xxx</i> or a <i>DRIVER=xxxx</i> attribute optionally followed by other DSN attributes separated by a semicolon e.g: </p>
<pre>
        DSN=ora9;UID=scott;PWD=tiger;DATABASE=ora9u
</pre>
<p> Any attributes required for a proper connection that are not entered in the DSN connect string, must be present in the odbc.ini file. </p>
<p> If the connect string is passed as an argument to the <code>iodbctest</code> program, the string should be quoted as most shells use the semicolon as their command separator. If the connect string is entered on the interactive prompt, no quotes should be used. </p>
<p> After a successful connection has been established, the user is prompted for a SQL command to be send to the database. A SQL command cannot span multiple lines. </p>
<p> If the SQL command returns one or more result sets, each result set is fetched using character buffers and displayed in a table. </p>
<p> Additionally, the <code>iodbctest</code> program understands a few special commands: </p>
<dl>
<dt><code>qualifiers</code></p>
<dd>
 Show a list of qualifiers using the SQLTables catalog call. </p>
<dt><code>owners</code></p>
<dd>
 Show a list of owners using the SQLTables catalog call. </p>
<dt><code>tables</code></p>
<dd>
 Show a list of tables using the SQLTables catalog call. </p>
<dt><code>types</code></p>
<dd>
 Show a list of tables types using the SQLTables catalog call. </p>
<dt><code>datatypes</code></p>
<dd>
 Show a list of data types using the SQLGetTypeInfo catalog call. </p>
<dt><code>reconnect</code></p>
<dd>
 Perform a disconnect/reconnect with the information saved during the first SQLDriverConnect. </p>
<dt><code>quit (or exit)</code></p>
<dd>
 Exit the program and return to the shell. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Start the iodbctest program and get a list of DSNs before making a connection: </p>
<pre><code>
    $ iodbctest
    OpenLink ODBC Demonstration program
    This program shows an interactive SQL processor
    Enter ODBC connect string (? shows list): ?
    DSN                              | Driver
    -----------------------------------------------------------------
    ora9                             | OpenLink Generic ODBC Driver
    mysql                            | OpenLink Generic ODBC Driver
    mysqllite                        | OpenLink Lite for MySQL
    myodbc                           | MyODBC Driver
    pgsql                            | OpenLink Generic ODBC Driver
    tds                              | OpenLink Generic ODBC Driver
    Enter ODBC connect string (? shows list): DSN=ora9;
    PWD = tiger
              Driver : 05.20.0316 OpenLink Generic ODBC
              Driver(oplodbc.so)
                  SQL &gt;
</code></pre>
<p> Connect to an Oracle 9 instance which has been previously setup in the odbc.ini file: </p>
<pre><code>
$ iodbctest "DSN=ora9;UID=scott;PWD=tiger" iODBC Demonstration program
            This program shows an interactive SQL processor
                Driver : 05.20.0316 OpenLink Generic ODBC
                Driver(oplodbc.so)
                    SQL
        &gt; select *from emp
        ID
    | NAME-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -1 | Record 1 2 | Record 2 2 | Record 3 result set 1 returned 3 rows.SQL &gt; quit
</code></pre>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1996-2009 by OpenLink Software </p>
<h2>AUTHOR</h2>
<p> iODBC Administrator &lt;iodbc [at] openlinksw.com&gt; </p>
<h2>Index</h2>
