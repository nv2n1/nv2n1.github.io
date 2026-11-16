---
title: "radsqlrelay(8)"
name: "radsqlrelay"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radsqlrelay/"
description: "radsqlrelay – relay SQL queries to a central database server"
---

<p>radsqlrelay &#8211; relay SQL queries to a central database server</p>
<h2>Synopsis</h2>
<p><code>radsqlrelay</code> [<code>-?</code>] [<code>-d</code> <i>sql_driver</i>] [<code>-b</code> <i>database</i>] [<code>-f</code> <i>file</i>] [<code>-h</code> <i>host</i>] [<code>-u</code> <i>user</i>] [<code>-P</code> <i>port</i>] [<code>-p</code> <i>password</i>] [<code>-1</code>] [<code>-x</code>] <i>file_path</i> </p>
<h2>Description</h2>
<p><code>radsqlrelay</code> tails a SQL <i>logfile</i> and forwards the queries to a database server. Used to replicate accounting records to one (central) database, even if the database has extended downtime. The SQL logfile is created by the <code>rlm_sql_log</code> module. The module must be configured in the <code>radiusd</code> server before you can use <code>radsqlrelay</code>. </p>
<h2>Options</h2>
<dl>
<dt>-?</dt>
<dd>Print usage help information.</dd>
<dt>-d <i>sql_driver</i></dt>
<dd>Driver to use: mysql, pg, oracle.</dd>
<dt>-b <i>database</i></dt>
<dd>Name of the database to use.</dd>
<dt>-f <i>file</i></dt>
<dd>Read password from file, instead of command line.</dd>
<dt>-h <i>host</i></dt>
<dd>Connect to host.</dd>
<dt>-u <i>user</i></dt>
<dd>User for login.</dd>
<dt>-P <i>port</i></dt>
<dd>Port number to use for connection.</dd>
<dt>-p <i>password</i></dt>
<dd>Password to use when connecting to server.</dd>
<dt>-1</dt>
<dd>One-shot mode: push the file to database and exit.</dd>
<dt>-x</dt>
<dd>Turn on debugging.</dd>
<dt>file_path</dt>
<dd>The pathname of the SQL logfile to use. </dd>
</dl>
<h2>Notes</h2>
<h3>Oracle driver</h3>
<p>The command &quot;radsqlrelay -d oracle -b db.domain.tld sql-relay&quot; reads the database description stored in $TNS_ADMIN/tnsnames.ora:</p>
<dl>
<dd>
<pre>db.domain.tld =
 (DESCRIPTION =
 (ADDRESS_LIST =
 (ADDRESS = (PROTOCOL = TCP)(HOST = db.domain.tld)(PORT = 1521))
 )
 (CONNECT_DATA =
 (SERVICE_NAME = &lt;DB SID&gt;)
 )
 )</pre>
</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-rlm_sql_log/">rlm_sql_log</a></code>(5) </p>
<h2>Author</h2>
<p>Nicolas Baradakis &lt;nicolas.baradakis [at] cegetel.net&gt;</p>
