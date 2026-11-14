---
title: "radrelay(8)"
name: "radrelay"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radrelay/"
description: "radrelay — Deprecated command."
---

<p>radrelay &#8212; Deprecated command.</p>
<h2>Description</h2>
<p>The functions of <i>radrelay</i> have been added to <i>radiusd</i>. One benefit is that one instance of <i>radiusd</i> can read multiple detail files, among others. </p>
<p> The <i>rlm_sql_log</i> module does something similar, but for SQL queries. See it&#8217;s man page for details.</p>
<h2>Replication For Backups</h2>
<p>Many sites run multiple radius servers; at least one primary and one backup server. When the primary goes down, most NASes detect that and switch to the backup server. </p>
<p> That will cause your accounting packets to go the the backup server &#8211; and some NASes don&#8217;t even switch back to the primary server when it comes back up. </p>
<p> The result is that accounting records are missed, and/or the administrator must jump through hoops in order to combine the different detail files from multiple servers. It also means that the session database (&quot;radutmp&quot;, used for radwho and simultaneous use detection) gets out of sync. </p>
<p> We solve this issue by &quot;relaying&quot; packets from one server to another, so they both have the same set of accounting data. </p>
<p> See raddb/sites-available/buffered-sql for more information.</p>
<h2>Buffering For High-Load Servers</h2>
<p>If the RADIUS server suddenly receives a many accounting packets, there may be insufficient CPU power to process them all in a timely manner. This problem is especially noticable when the accounting packets are going to a back-end database. </p>
<p> Similarly, you may have one database that tracks &quot;live&quot; sessions, and another that tracks historical accounting data. In that case, accessing the first database is fast, as it is small. Accessing the second database many be slower, as it may contain multiple gigabytes of data. In addition, writing to the first database in a timely manner is important, while data may be written to the second database with a few minutes delay, without any harm being done. </p>
<p> See raddb/sites-available/copy-to-home-server for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8),</code> <code><a href="/docs/linux/man/5-rlm_sql_log/">rlm_sql_log</a>(5)</code></p>
<h2>Author</h2>
<p>The FreeRADIUS Server Project</p>
