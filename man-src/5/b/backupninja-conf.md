---
title: "backupninja-conf(5)"
name: "backupninja-conf"
section: "5"
letter: "b"
url: "/docs/linux/man/5-backupninja-conf/"
description: "BACKUPNINJA.CONF – Configuration file(s) for backupninja (1)."
---

<p>BACKUPNINJA.CONF &#8211; Configuration file(s) for <code>backupninja (1)</code>. </p>
<h2>Synopsis</h2>
<p><code>/etc/backupninja.conf </code></p>
<h2>Description</h2>
<p><code>backupninja.conf</code> is the general configuration file. In this file you can set the log level and change the default directory locations. You can force a different general configuration file with &quot;backupninja -f /path/to/conf&quot;. </p>
<h2>Options</h2>
<dl>
<dt><code>loglevel</code></p>
<dd>How verbose to make the logs.<br />
 5 = Debugging messages<br />
 4 = Informational messages<br />
 3 = Warnings<br />
 2 = Errors<br />
 1 = Fatal errors </p>
<dt><code>reportemail</code></p>
<dd>Send a summary of the backup status to this email address </p>
<dt><code>reportsuccess</code></p>
<dd>If set to &#8216;yes&#8217;, a report email will be generated even if all modules reported success. </p>
<dt><code>reportwarning</code></p>
<dd>If set to &#8216;yes&#8217;, a report email will be generated even if there was no error. </p>
<dt><code>logfile</code></p>
<dd>The path of the logfile. </p>
<dt><code>configdirectory</code></p>
<dd>The directory where all the backup action configuration files live. </p>
<dt><code>scriptdirectory </code></p>
<dd>Where backupninja handler scripts are found </p>
<dt><code>usecolors</code></p>
<dd>If set to &#8216;yes&#8217;, use colors in the log file and debug output. </p>
<dt><code>when</code></p>
<dd>When to process each configuration file. The value used here will be applied for each configuration file. It is possibile to override this &quot;when&quot; in each each configuration file, see also section &quot;Scheduling&quot; in <a href="/docs/linux/man/5-backup-d/">backup.d</a>(5). </p>
<p> For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>sundays at 02:00<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>30th at 22<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>30 at 22:00<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>everyday at 01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;&#8211; the default<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>Tuesday at 05:00 </p>
<p> These values for &#8216;when&#8217; are equivalent: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>tuesday at 05:30<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>TUESDAYS at 05 </p>
<p> These values for &#8216;when&#8217; are invalid:<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>tuesday at 2am<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>tuesday at 2<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>tues at 02 </p>
<dt><code>vservers</code></p>
<dd>If you are using Linux-Vservers (<a rel="nofollow" href="http://linux-vserver.org">http://linux-vserver.org</a>), there are some special capabilities that different handlers have to make vserver backups easier. See the example configuration files for each handler to configure the vserver specific variables. </p>
</dl>
<h2>Defaults</h2>
<p>loglevel = 4<br />
 reportemail = root<br />
 reportsuccess = yes<br />
 reportwarning = yes<br />
 logfile = /var/log/backupninja.log<br />
 configdirectory = /etc/backup.d<br />
 scriptdirectory = /usr/share/backupninja<br />
 usecolors = yes<br />
 when = everyday at 01:00<br />
 vservers = no</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-backupninja/">backupninja</a></code>(1), <code><a href="/docs/linux/man/1-ninjahelper/">ninjahelper</a></code>(1), <code><a href="/docs/linux/man/5-backup-d/">backup.d</a></code>(5),</p>
<h2>Author</h2>
<p>BACKUPNINJA was written by the riseup.net collective.</p>
