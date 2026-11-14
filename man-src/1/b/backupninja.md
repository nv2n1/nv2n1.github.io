---
title: "backupninja(1)"
name: "backupninja"
section: "1"
letter: "b"
url: "/docs/linux/man/1-backupninja/"
description: "BACKUPNINJA – A lightweight, extensible meta-backup system \"a silent flower blossom death strike to lost data.\""
---

<h2 class="name">NAME</h2>
<p> BACKUPNINJA &#8211; A lightweight, extensible meta-backup system<br />
 <i>&quot;a silent flower blossom death strike to lost data.&quot;</i> </p>
<h2>SYNOPSIS</h2>
<p> <code>backupninja [ -h ] [ -d ] [ -n ] [ -t ] [ -f filename ] [ &#8211;run filename ]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Backupninja </code> allows you to coordinate system backups by dropping a few simple configuration files into /etc/backup.d/. Most programs you might use for making backups don&#8217;t have their own configuration file format. Backupninja provides a centralized way to configure and coordinate many different backup utilities. </p>
<h2>FEATURES</h2>
<dl>
<dt>&#8211;</p>
<dd> easy to read ini style configuration files.</p>
<dt>&#8211;</p>
<dd> you can drop in scripts to handle new types of backups.</p>
<dt>&#8211;</p>
<dd> backup actions can be scheduled.</p>
<dt>&#8211;</p>
<dd> you can choose when status report emails are mailed to you (always, on warning, on error, never).</p>
<dt>&#8211;</p>
<dd> console-based wizard (ninjahelper) makes it easy to create backup action configuration files.</p>
<dt>&#8211;</p>
<dd> passwords are never sent via the command line to helper programs.</p>
<dt>&#8211;</p>
<dd> in order to backup a db or sql database, you cannot simply copy database files. backupninja helps you safely export the data to a format which you can backup.</p>
<dt>&#8211;</p>
<dd> works with Linux-Vservers. </p>
<p> <code>Backup types include:</code></p>
<dt>&#8211;</p>
<dd> secure, remote, incremental filesytem backup (via rdiff-backup). incremental data is compressed. permissions are retained even with an unpriviledged backup user.</p>
<dt>&#8211;</p>
<dd> basic system and hardware information.</p>
<dt>&#8211;</p>
<dd> encrypted remote backups (via duplicity).</p>
<dt>&#8211;</p>
<dd> safe backup of MySQL, PostgreSQL, OpenLDAP, and subversion databases.</p>
<dt>&#8211;</p>
<dd> burn CD/DVDs or create ISOs. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help </code></p>
<dd> Show summary of options</p>
<dt><code>-d, &#8211;debug </code></p>
<dd> Run in debug mode, where all log messages are output to the current shell.</p>
<dt><code>-f, &#8211;conffile CONF_FILE </code></p>
<dd> Use CONF_FILE for the main configuration instead of /etc/backupninja.conf</p>
<dt><code>-t, &#8211;test </code></p>
<dd> Run in test mode, no actions are actually taken.</p>
<dt><code>-n, &#8211;now </code></p>
<dd> Perform actions now, instead of when they might be scheduled.</p>
<dt><code>&#8211;run ACTION_FILE</code></p>
<dd> Runs the action configuration ACTION_FILE and exits. </p>
</dl>
<h2>CONFIGURATION</h2>
<p> General settings are configured in /etc/backupninja.conf. In this file you can set the log level and change the default directory locations. See <code><a href="/docs/linux/man/5-backupninja-conf/">backupninja.conf</a>(5)</code>. </p>
<p> To preform the actual backup actions, backupninja processes each action configuration file in /etc/backup.d according to the file&#8217;s suffix. See <code><a href="/docs/linux/man/5-backup-d/">backup.d</a>(5)</code>. </p>
<h2>EXAMPLE USAGE</h2>
<dl>
<dt>Backupninja can be used to implement whatever backup strategy you choose. It is intended, however, to be used like so:</p>
<dd>
<dt>First, databases are safely copied or exported to /var/backups. Often, you cannot make a file backup of a database while it is in use, hence the need to use special tools to make a safe copy or export into /var/backups.</p>
<dd>
<dt>Then, vital parts of the file system, including /var/backups, are nightly pushed to a remote, off-site, hard disk (using rdiff-backup). The local user is root, but the remote user is not privileged. Hopefully, the remote filesystem is encrypted.</p>
<dd>
<dt>In order for this to work (ie for diff-backup to run unattended), you must create ssh keys on the source server and copy the public key to the remote user&#8217;s authorized keys file. For example:</p>
<dd>
 root [at] srchost# ssh-keygen -t rsa -b 4096<br />
 root [at] srchost# ssh-copy-id -i /root/.ssh/id_dsa.pub backup [at] desthost</p>
<dt>Now, you should be able to ssh from user &#8216;root&#8217; on srchost to user &#8216;backup&#8217; on desthost without specifying a password. When prompted for a password by ssh-keygen, just leave it blank by hitting return. The &quot;wizard&quot; <code><a href="/docs/linux/man/1-ninjahelper/">ninjahelper</a>(1)</code> will walk you through these steps.</p>
<dd>
</dl>
<h2>FILES</h2>
<p> <code>/usr/sbin/backupninja</code> main script<br />
 <code>/etc/backupninja.conf</code> main configuration file; general options<br />
 <code>/etc/cron.d/backupninja</code> runs main script hourly<br />
 <code>/etc/logrotate.d/backupninja</code> rotates backupninja.log<br />
 <code>/etc/backup.d</code> directory for configuration files<br />
 <code>/usr/share/backupninja</code> directory for handler scripts<br />
 <code>/usr/share/doc/backupninja/examples</code> example action configuration files. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ninjahelper/">ninjahelper</a></code>(1), <code><a href="/docs/linux/man/5-backupninja-conf/">backupninja.conf</a></code>(5), <code><a href="/docs/linux/man/5-backup-d/">backup.d</a></code>(5), </p>
<h2>AUTHOR</h2>
<p> BACKUPNINJA was written by the riseup.net collective. </p>
<h2>Index</h2>
