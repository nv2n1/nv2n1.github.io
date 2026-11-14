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
<dt>-?</p>
<dd>Print usage help information.</p>
<dt>-d <i>sql_driver</i></p>
<dd>Driver to use: mysql, pg, oracle.</p>
<dt>-b <i>database</i></p>
<dd>Name of the database to use.</p>
<dt>-f <i>file</i></p>
<dd>Read password from file, instead of command line.</p>
<dt>-h <i>host</i></p>
<dd>Connect to host.</p>
<dt>-u <i>user</i></p>
<dd>User for login.</p>
<dt>-P <i>port</i></p>
<dd>Port number to use for connection.</p>
<dt>-p <i>password</i></p>
<dd>Password to use when connecting to server.</p>
<dt>-1</p>
<dd>One-shot mode: push the file to database and exit.</p>
<dt>-x</p>
<dd>Turn on debugging.</p>
<dt>file_path</p>
<dd>The pathname of the SQL logfile to use. </p>
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
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-rlm_sql_log/">rlm_sql_log</a></code>(5) </p>
<h2>Author</h2>
<p>Nicolas Baradakis &lt;nicolas.baradakis [at] cegetel.net&gt;</p>
