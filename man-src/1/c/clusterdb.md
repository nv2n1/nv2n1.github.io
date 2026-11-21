---
title: "clusterdb(1)"
name: "clusterdb"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clusterdb/"
description: "clusterdb – cluster a PostgreSQL database"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>clusterdb</code> [<i>connection-option</i>&#8230;] [<code>&#8211;verbose</code> | <code>-v</code>] [<code>&#8211;table</code>&nbsp;<wbr>|&nbsp;<wbr><code>-t</code>&nbsp;<wbr><i>table</i>] [<i>dbname</i>]</dt>
<dt> <code>clusterdb</code> [<i>connection-option</i>&#8230;] [<code>&#8211;verbose</code> | <code>-v</code>] <code>&#8211;all</code> | <code>-a</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>clusterdb is a utility for reclustering tables in a PostgreSQL database. It finds tables that have previously been clustered, and clusters them again on the same index that was last used. Tables that have never been clustered are not affected. </dd>
<p> clusterdb is a wrapper around the SQL command <code><a href="/docs/linux/man/7-cluster/">CLUSTER</a></code>(7). There is no effective difference between clustering databases via this utility and via other methods for accessing the server.</p>
<h2>OPTIONS</h2>
<p> clusterdb accepts the following command-line arguments: </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
</dt><dd> Cluster all databases.</dd></dl>
<p> <code>[-d]</code><i>dbname</i>, <code>[&#8211;dbname=]</code><i>dbname</i></p>
<dl>
<dt>
</dt><dd> Specifies the name of the database to be clustered. If this is not specified and <code>-a</code> (or <code>&#8211;all</code>) is not used, the database name is read from the environment variable <code>PGDATABASE</code>. If that is not set, the user name specified for the connection is used.</dd></dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
</dt><dd> Echo the commands that clusterdb generates and sends to the server.</dd></dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
</dt><dd> Do not display progress messages.</dd></dl>
<p> <code>-t </code><i>table</i>, <code>&#8211;table=</code><i>table</i></p>
<dl>
<dt>
</dt><dd> Cluster <i>table</i> only.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Print detailed information during processing.</dd></dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print the clusterdb version and exit.</dd></dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help about clusterdb command line arguments, and exit.</dd></dl>
<p> clusterdb also accepts the following command-line arguments for connection parameters: </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
</dt><dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket.</dd></dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
</dt><dd> Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections.</dd></dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
</dt><dd> User name to connect as.</dd></dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
</dt><dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dd></dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
</dt><dd> Force clusterdb to prompt for a password before connecting to a database. </dd>
<p> This option is never essential, since clusterdb will automatically prompt for a password if the server demands password authentication. However, clusterdb will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> <code>&#8211;maintenance-db=</code><i>dbname</i></p>
<dl>
<dt>
</dt><dd> Specifies the name of the database to connect to discover what other databases should be clustered. If not specified, the postgres database will be used, and if that does not exist, template1 will be used.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATABASE</code>, <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
</dt><dd> Default connection parameters</dd></dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> In case of difficulty, see <code><a href="/docs/linux/man/7-cluster/">CLUSTER</a></code>(7) and <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>EXAMPLES</h2>
<p> To cluster the database test: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ <code>clusterdb test</code>
</pre>
</dd></dl>
<p> To cluster a single table foo in a database named xyzzy: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ <code>clusterdb --table foo xyzzy</code>
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-cluster/">CLUSTER</a></code>(7) </p>
