---
title: "vacuumdb(1)"
name: "vacuumdb"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vacuumdb/"
description: "vacuumdb – garbage-collect and analyze a PostgreSQL database"
---

<h2 class="name">NAME</h2>
<p> vacuumdb &#8211; garbage-collect and analyze a PostgreSQL database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>vacuumdb</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;] [<code>&#8211;table</code>&nbsp;<wbr>|&nbsp;<wbr><code>-t</code>&nbsp;<wbr><i>table</i>&nbsp;<wbr>[(&nbsp;<wbr><i>column</i>&nbsp;<wbr>[,&#8230;]&nbsp;<wbr>)]] [<i>dbname</i>]</p>
<dt> <code>vacuumdb</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;] <code>&#8211;all</code> | <code>-a</code></dl>
<h2>DESCRIPTION</h2>
<dd>vacuumdb is a utility for cleaning a PostgreSQL database. vacuumdb will also generate internal statistics used by the PostgreSQL query optimizer. </p>
<p> vacuumdb is a wrapper around the SQL command <code><a href="/docs/linux/man/7-vacuum/">VACUUM</a></code>(7). There is no effective difference between vacuuming and analyzing databases via this utility and via other methods for accessing the server.</p>
<h2>OPTIONS</h2>
<p> vacuumdb accepts the following command-line arguments: </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Vacuum all databases.</dl>
<p> <code>[-d]</code><i>dbname</i>, <code>[&#8211;dbname=]</code><i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to be cleaned or analyzed. If this is not specified and <code>-a</code> (or <code>&#8211;all</code>) is not used, the database name is read from the environment variable <code>PGDATABASE</code>. If that is not set, the user name specified for the connection is used.</dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
<dd> Echo the commands that vacuumdb generates and sends to the server.</dl>
<p> <code>-f</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Perform &#8220;full&#8221; vacuuming.</dl>
<p> <code>-F</code>, <code>&#8211;freeze</code></p>
<dl>
<dt>
<dd> Aggressively &#8220;freeze&#8221; tuples.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Do not display progress messages.</dl>
<p> <code>-t </code><i>table</i><code> [ (</code><i>column</i><code> [,&#8230;]) ]</code>, <code>&#8211;table=</code><i>table</i><code> [ (</code><i>column</i><code> [,&#8230;]) ]</code></p>
<dl>
<dt>
<dd> Clean or analyze <i>table</i> only. Column names can be specified only in conjunction with the <code>&#8211;analyze</code> or <code>&#8211;analyze-only</code> options. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Tip</code> </font><br />
 If you specify columns, you probably have to escape the parentheses from the shell. (See examples below.) </p>
</dl>
</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print detailed information during processing.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the vacuumdb version and exit.</dl>
<p> <code>-z</code>, <code>&#8211;analyze</code></p>
<dl>
<dt>
<dd> Also calculate statistics for use by the optimizer.</dl>
<p> <code>-Z</code>, <code>&#8211;analyze-only</code></p>
<dl>
<dt>
<dd> Only calculate statistics for use by the optimizer (no vacuum).</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about vacuumdb command line arguments, and exit.</dl>
<p> vacuumdb also accepts the following command-line arguments for connection parameters: </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
<dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket.</dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
<dd> Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections.</dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
<dd> User name to connect as.</dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
<dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
<dd> Force vacuumdb to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since vacuumdb will automatically prompt for a password if the server demands password authentication. However, vacuumdb will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> <code>&#8211;maintenance-db=</code><i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to connect to discover what other databases should be vacuumed. If not specified, the postgres database will be used, and if that does not exist, template1 will be used.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATABASE</code>, <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> In case of difficulty, see <code><a href="/docs/linux/man/7-vacuum/">VACUUM</a></code>(7) and <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>NOTES</h2>
<p> vacuumdb might need to connect several times to the PostgreSQL server, asking for a password each time. It is convenient to have a ~/.pgpass file in such cases. See Section 31.15, &#8220;The Password File&#8221;, in the documentation for more information.</p>
<h2>EXAMPLES</h2>
<p> To clean the database test: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>vacuumdb test</code>
</pre>
</dl>
<p> To clean and analyze for the optimizer a database named bigdb: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>vacuumdb --analyze bigdb</code>
</pre>
</dl>
<p> To clean a single table foo in a database named xyzzy, and analyze a single column bar of the table for the optimizer: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>vacuumdb --analyze --verbose --table 'foo(bar)' xyzzy</code>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-vacuum/">VACUUM</a></code>(7) </p>
<h2>Index</h2>
