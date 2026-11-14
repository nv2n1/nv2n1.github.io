---
title: "radrelay-conf(5)"
name: "radrelay-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-radrelay-conf/"
description: "radrelay.conf – configuration file for the FreeRADIUS server \"radrelay\" personality"
---

<p>radrelay.conf &#8211; configuration file for the FreeRADIUS server &quot;radrelay&quot; personality</p>
<h2>Description</h2>
<p>The <code>radrelay.conf</code> file resides in the radius database directory, by default <code>/etc/raddb</code>. It defines the global configuration for the FreeRADIUS server, when the server is operating as &quot;radrelay&quot;.</p>
<h2>File Format</h2>
<p>For a detailed description of the file format, see &quot;man radiusd.conf&quot;. The configuration entries are much the same for radrelay.conf, with a few differences as noted here.</p>
<h2>Replication For Backups</h2>
<p>Many sites run multiple radius servers; at least one primary and one backup server. When the primary goes down, most NASes detect that and switch to the backup server. </p>
<p> That will cause your accounting packets to go the the backup server &#8211; and some NASes don&#8217;t even switch back to the primary server when it comes back up. </p>
<p> The result is that accounting records are missed, and/or the administrator must jump through hoops in order to combine the different detail files from multiple servers. It also means that the session database (&quot;radutmp&quot;, used for radwho and simultaneous use detection) gets out of sync. </p>
<p> radrelay solves this issue by &quot;relaying&quot; packets from one server to another, so they both have the same set of accounting data.</p>
<h2>Buffering For High-Load Servers</h2>
<p>If the RADIUS server suddenly receives a many accounting packets, there may be insufficient CPU power to process them all in a timely manner. This problem is especially noticable when the accounting packets are going to a back-end database. </p>
<p> Similarly, you may have one database that tracks &quot;live&quot; sessions, and another that tracks historical accounting data. In that case, accessing the first database is fast, as it is small. Accessing the second database many be slower, as it may contain multiple gigabytes of data. In addition, writing to the first database in a timely manner is important, while data may be written to the second database with a few minutes delay, without any harm being done.</p>
<h2>Relaying Of Accounting Packets</h2>
<p>The <code>radrelay.conf</code> file controls the &quot;radrelay&quot; personality of the server, which can perform both of the functions above at the same time.</p>
<h2>Usage</h2>
<p>First, you should configure the main radius server to log to an extra, single detail file. This may be done by adding an extra instance of the detail module to <code>radiusd.conf</code>: </p>
<p> For example: </p>
<dl>
<dd>
<pre> detail radrelay-detail {
<br>
 filename = ${radacctdir}/radrelay/detail
<br>
 permissions = 0600
<br>
 dir_permissions = 0755
<br>
 locking = yes
<br>
 }
<br>
 ...
<br>
 accounting {
<br>
 ...
<br>
 radrelay-detail
<br>
 ...
<br>
 }
<br></pre>
</dl>
<p> This configuration will cause accounting packets to be logged to the <i>${radacctdir}/radrelay/detail</i> file. This file should not be rotated by standard log rotation scripts, as the <code>radrelay</code> program will read and rotate it.</p>
<h2>Radrelay.Conf Example</h2>
<p>See the <code>radrelay.conf</code> file for detailed instructions on configuration entries, what they mean, and how to use them. </p>
<p> To have the &quot;radrelay&quot; portion of the server read the above detail file, configure <code>radrelay.conf</code> with the following section: </p>
<dl>
<dd>
<pre><br>
 listen {
<br>
 type = detail
<br>
 filename = ${radacctdir}/radrelay/detail
<br>
 max_outstanding = 100
<br>
 identity = radrelay
<br>
 }
<br></pre>
</dl>
<p> The server will read the accounting packets from the detail file, and process them just as if it had received them from the NAS. Therefore, you should configure the &quot;accounting&quot; section of <code>radrelay.conf</code> to write the accounting records to an &quot;sql&quot; module, or to proxy them to another RADIUS server. </p>
<p> Then, start the server via the following command: </p>
<p> $ radiusd -n radrelay </p>
<p> The server should start up, read the detail file, and process accounting packets from it.</p>
<h2>Notes</h2>
<p>The <code>radiusd.conf</code> file is not read at all when the server is running as radrelay. Please edit <code>radrelay.conf</code>.</p>
<h2>Credits</h2>
<p>The original &quot;radrelay&quot; program was written by Miquel van Smoorenburg for the Cistron radius project, and ported to FreeRADIUS by Simon Ekstrand. The &quot;radsqlrelay&quot; was written by Kostas Kalavras. It was never released as part of an offical FreeRADIUS release, but served as a basis for the design of this implementation.</p>
<h2>Files</h2>
<p>/etc/raddb/radrelay.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] ox.org&gt;</p>
