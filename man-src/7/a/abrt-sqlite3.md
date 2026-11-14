---
title: "abrt-sqlite3(7)"
name: "abrt-sqlite3"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-sqlite3/"
description: "SQLite3 database plugin for abrt(8)"
---

<p>SQLite3 database plugin for <a href="/docs/linux/man/8-abrt/">abrt</a>(8)</p>
<h2>Description</h2>
<p><i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>SQLite3</i> database plugin for <i>abrt</i>. This is a database plugin: <i>abrt</i> needs a database in which to store its metadata. You can choose one by specifying &quot;Database&quot; in the <i>abrt.conf</i> configuration file. Currently SQLite3 is the only choice supported.</p>
<h2>Invocation</h2>
<p>The plugin is invoked in the <i>abrt.conf</i> configuration file, like this:<br />
 [common]<br />
 Database = SQLite3</p>
<h2>Configuration</h2>
<p>The <i>SQLite3.conf</i> configuration file contains one entry:</p>
<h3>DBPath</h3>
<p>The path to the database.</p>
<h2>Examples</h2>
<p>see <code>INVOCATION</code></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a href="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a href="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)</p>
<h2>Author</h2>
<p>Written by Zdenek Prikryl &lt;zprikryl [at] redhat.com&gt; and Jiri Moskovcak &lt;jmoskovc [at] redhat.com&gt;. Manual page by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.</p>
