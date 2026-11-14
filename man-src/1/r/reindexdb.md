---
title: "reindexdb(1)"
name: "reindexdb"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reindexdb/"
description: "reindexdb – reindex a PostgreSQL database"
---

<h2 class="name">NAME</h2>
<p> reindexdb &#8211; reindex a PostgreSQL database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>reindexdb</code> [<i>connection-option</i>&#8230;] [<code>&#8211;table</code> | <code>-t</code> <i>table</i>] [<code>&#8211;index</code> | <code>-i</code> <i>index</i>] [<i>dbname</i>]</p>
<dt> <code>reindexdb</code> [<i>connection-option</i>&#8230;] <code>&#8211;all</code> | <code>-a</code></p>
<dt> <code>reindexdb</code> [<i>connection-option</i>&#8230;] <code>&#8211;system</code> | <code>-s</code> [<i>dbname</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>reindexdb is a utility for rebuilding indexes in a PostgreSQL database. </p>
<p> reindexdb is a wrapper around the SQL command <code><a href="/docs/linux/man/7-reindex/">REINDEX</a></code>(7). There is no effective difference between reindexing databases via this utility and via other methods for accessing the server.</p>
<h2>OPTIONS</h2>
<p> reindexdb accepts the following command-line arguments: </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Reindex all databases.</dl>
<p> <code>[-d]</code><i>dbname</i>, <code>[&#8211;dbname=]</code><i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to be reindexed. If this is not specified and <code>-a</code> (or <code>&#8211;all</code>) is not used, the database name is read from the environment variable <code>PGDATABASE</code>. If that is not set, the user name specified for the connection is used.</dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
<dd> Echo the commands that reindexdb generates and sends to the server.</dl>
<p> <code>-i </code><i>index</i>, <code>&#8211;index=</code><i>index</i></p>
<dl>
<dt>
<dd> Recreate <i>index</i> only.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Do not display progress messages.</dl>
<p> <code>-s</code>, <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Reindex database&#8217;s system catalogs.</dl>
<p> <code>-t </code><i>table</i>, <code>&#8211;table=</code><i>table</i></p>
<dl>
<dt>
<dd> Reindex <i>table</i> only.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the reindexdb version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about reindexdb command line arguments, and exit.</dl>
<p> reindexdb also accepts the following command-line arguments for connection parameters: </p>
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
<dd> Force reindexdb to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since reindexdb will automatically prompt for a password if the server demands password authentication. However, reindexdb will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> <code>&#8211;maintenance-db=</code><i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to connect to discover what other databases should be reindexed. If not specified, the postgres database will be used, and if that does not exist, template1 will be used.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATABASE</code>, <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> In case of difficulty, see <code><a href="/docs/linux/man/7-reindex/">REINDEX</a></code>(7) and <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>NOTES</h2>
<p> reindexdb might need to connect several times to the PostgreSQL server, asking for a password each time. It is convenient to have a ~/.pgpass file in such cases. See Section 31.15, &#8220;The Password File&#8221;, in the documentation for more information.</p>
<h2>EXAMPLES</h2>
<p> To reindex the database test: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>reindexdb test</code>
</pre>
</dl>
<p> To reindex the table foo and the index bar in a database named abcd: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>reindexdb --table foo --index bar abcd</code>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-reindex/">REINDEX</a></code>(7) </p>
<h2>Index</h2>
