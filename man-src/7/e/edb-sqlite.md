---
title: "edb-sqlite(7)"
name: "edb-sqlite"
section: "7"
letter: "e"
url: "/docs/linux/man/7-edb-sqlite/"
description: "edb-sqlite – eurephia SQLite3 database driver"
---

<p><code>edb-sqlite</code> &#8211; eurephia SQLite3 database driver</p>
<h2>Description</h2>
<p>The <code>edb-sqlite</code> database driver is used to enable SQLite3 database in <code>eurephia</code>. The SQLite3 database is file based and requires no server setup at all. </p>
<p> The database driver takes only one argument, which is a full path to the database file.b</p>
<h2>Examples</h2>
<dl>
<dt><code>eurephia-auth</code> &#8211; This is configured via the OpenVPN configuration file.</p>
<dd>
<dd>plugin eurephia-auth.so &quot;-i edb-sqlite.so &#8212; &lt;full path to database file&gt;&quot;</p>
<dd>Plese notice the double dashes. They are separating the arguments between the eurephia-auth module and the database driver.</p>
<dt><code>eurephia_init</code> &#8211; This is set via the command line</p>
<dd>
<dd>user [at] server:~ $ eurephia_init &#8211;database-driver edb-sqlite.so \ &#8211;database-args &quot;&lt;full path to DB file&gt;&quot;</p>
<dt><code>eurephiadm</code> &#8211; This is configured in the <code>~/.eurephia/eurephiadm.cfg</code> file</p>
<dd>
<dd>database_driver = edb-sqlite.so<br />
 database_params = &lt;full path to DB file&gt;</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephia-auth/">eurephia-auth</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm/">eurephiadm</a></code>(7), <code><a href="/docs/linux/man/7-eurephia_init/">eurephia_init</a></code>(7) </p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
