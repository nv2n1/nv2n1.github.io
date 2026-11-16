---
title: "backup-d(5)"
name: "backup-d"
section: "5"
letter: "b"
url: "/docs/linux/man/5-backup-d/"
description: "BACKUP.D – Action configuration files for backupninja(1)."
---

<p>BACKUP.D &#8211; Action configuration files for <code><a href="/docs/linux/man/1-backupninja/">backupninja</a>(1)</code>. </p>
<h2>Synopsis</h2>
<p><code>/etc/backup.d/* </code></p>
<h2>Description</h2>
<p>To preform the actual backup actions, backupninja processes each action configuration file in /etc/backup.d according to the file&#8217;s suffix.</p>
<dl>
<dt>.sh</dt>
<dd>run this file as a shell script.</dd>
<dt>.rdiff</dt>
<dd>backup action for rdiff-backup.</dd>
<dt>.dup</dt>
<dd>backup action for duplicity.</dd>
<dt>.maildir</dt>
<dd>backup action for slow, incremental rsyncs of tens of thousands of maildirs.</dd>
<dt>.mysql</dt>
<dd>backup action for safe MySQL dumps.</dd>
<dt>.pgsql</dt>
<dd>backup action for safe PostgreSQL dumps.</dd>
<dt>.sys</dt>
<dd>backup action for general system reports and hardware information.</dd>
<dt>.svn</dt>
<dd>backup action for safe backups of subversion repositories.</dd>
<dt>.trac</dt>
<dd>backup action for safe backups of trac repositories.</dd>
<dt>.makecd</dt>
<dd>backup action for burning backups to CD/DVD or creating ISOs.</dd>
<dt>These files must be owned by root and must not be world or group readable/writable. Support for additional configuration types can be added by dropping bash scripts with the name of the suffix into /usr/share/backupninja.</dt>
<dd>
</dd><dt>The configuration files are processed in alphabetical order. However, it is suggested that you name the config files in &quot;sysvinit style.&quot;</dt>
<dd>
</dd><dt>For example:</dt>
<dd>&nbsp;<wbr>10-local.pgsql.disabled<br />
&nbsp;<wbr>15-runthisfirst.sh<br />
&nbsp;<wbr>20-runthisnext.mysql<br />
&nbsp;<wbr>90-runthislast.rdiff</dd>
<dt>Typically, you will put a &#8216;.rdiff&#8217; config file last, so that any database dumps you make are included in the filesystem backup. Action configurations which end with .disabled are skipped.</dt>
<dd>
</dd><dt>Example templates for the action configuration files can be found in /usr/share/doc/backupninja/examples. You can also use <code><a href="/docs/linux/man/1-ninjahelper/">ninjahelper</a>(1)</code>, a console based &quot;wizard&quot; for creating backup actions.</dt>
<dd>
<h2>Scheduling</h2>
<p>By default, each configuration file is processed everyday at 01:00 (1 AM). This can be changed by specifying the &#8216;when&#8217; option in a backup action&#8217;s config file or in the global configuration file. Special value &#8216;manual&#8217; will disable scheduling for the backup action. It is possible to run the backup action manually by invoking <code><a href="/docs/linux/man/1-ninjahelper/">ninjahelper</a>(1)</code> with &#8211;run command line argument. </p>
<p> For example:<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>sundays at 02:00<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>30th at 22<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>30 at 22:00<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>everyday at 01<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>Tuesday at 05:00<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>hourly<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>manual </p>
<p> These values for &quot;when&quot; are invalid:<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>tuesday at 2am<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>tuesday at 2<br />
&nbsp;<wbr>&nbsp;<wbr>when&nbsp;<wbr>=&nbsp;<wbr>tues at 02 </p>
<p> A configuration file will be processed at the time(s) specified by the &quot;when&quot; option. If multiple &quot;when&quot; options are present, then they all apply. If two configurations files are scheduled to run in the same hour, then we fall back on the alphabetical ordering specified above. The &quot;when&quot; must occur before any sections in the action configuration file.</p>
<h2>File Format</h2>
<p>The file format of the action configuration files is &quot;ini style.&quot; Sections are created by using square bracket. Long lines are connected with a backslash. For example: </p>
<p>#&nbsp;<wbr>this is a comment<br />
[fishes]<br />
fish&nbsp;<wbr>=&nbsp;<wbr>red<br />
fish&nbsp;<wbr>=&nbsp;<wbr>blue<br />
[fruit]<br />
apple&nbsp;<wbr>=&nbsp;<wbr>yes<br />
pear&nbsp;<wbr>=&nbsp;<wbr>no thanks&nbsp;<wbr>\<br />
i will not have a pear.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-backupninja/">backupninja</a></code>(1), <code><a href="/docs/linux/man/1-ninjahelper/">ninjahelper</a></code>(1), <code><a href="/docs/linux/man/5-backupninja-conf/">backupninja.conf</a></code>(5),</p>
<h2>Author</h2>
<p>BACKUPNINJA was written by the riseup.net collective.</p>
</dd></dl>