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
<dt>&#8211;</dt>
<dd> easy to read ini style configuration files.</dd>
<dt>&#8211;</dt>
<dd> you can drop in scripts to handle new types of backups.</dd>
<dt>&#8211;</dt>
<dd> backup actions can be scheduled.</dd>
<dt>&#8211;</dt>
<dd> you can choose when status report emails are mailed to you (always, on warning, on error, never).</dd>
<dt>&#8211;</dt>
<dd> console-based wizard (ninjahelper) makes it easy to create backup action configuration files.</dd>
<dt>&#8211;</dt>
<dd> passwords are never sent via the command line to helper programs.</dd>
<dt>&#8211;</dt>
<dd> in order to backup a db or sql database, you cannot simply copy database files. backupninja helps you safely export the data to a format which you can backup.</dd>
<dt>&#8211;</dt>
<dd> works with Linux-Vservers. </dd>
<p> <code>Backup types include:</code></p>
<dt>&#8211;</dt>
<dd> secure, remote, incremental filesytem backup (via rdiff-backup). incremental data is compressed. permissions are retained even with an unpriviledged backup user.</dd>
<dt>&#8211;</dt>
<dd> basic system and hardware information.</dd>
<dt>&#8211;</dt>
<dd> encrypted remote backups (via duplicity).</dd>
<dt>&#8211;</dt>
<dd> safe backup of MySQL, PostgreSQL, OpenLDAP, and subversion databases.</dd>
<dt>&#8211;</dt>
<dd> burn CD/DVDs or create ISOs. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help </code></dt>
<dd> Show summary of options</dd>
<dt><code>-d, &#8211;debug </code></dt>
<dd> Run in debug mode, where all log messages are output to the current shell.</dd>
<dt><code>-f, &#8211;conffile CONF_FILE </code></dt>
<dd> Use CONF_FILE for the main configuration instead of /etc/backupninja.conf</dd>
<dt><code>-t, &#8211;test </code></dt>
<dd> Run in test mode, no actions are actually taken.</dd>
<dt><code>-n, &#8211;now </code></dt>
<dd> Perform actions now, instead of when they might be scheduled.</dd>
<dt><code>&#8211;run ACTION_FILE</code></dt>
<dd> Runs the action configuration ACTION_FILE and exits. </dd>
</dl>
<h2>CONFIGURATION</h2>
<p> General settings are configured in /etc/backupninja.conf. In this file you can set the log level and change the default directory locations. See <code><a href="/docs/linux/man/5-backupninja-conf/">backupninja.conf</a>(5)</code>. </p>
<p> To preform the actual backup actions, backupninja processes each action configuration file in /etc/backup.d according to the file&#8217;s suffix. See <code><a href="/docs/linux/man/5-backup-d/">backup.d</a>(5)</code>. </p>
<h2>EXAMPLE USAGE</h2>
<dl>
<dt>Backupninja can be used to implement whatever backup strategy you choose. It is intended, however, to be used like so:</dt>
<dd>
</dd><dt>First, databases are safely copied or exported to /var/backups. Often, you cannot make a file backup of a database while it is in use, hence the need to use special tools to make a safe copy or export into /var/backups.</dt>
<dd>
</dd><dt>Then, vital parts of the file system, including /var/backups, are nightly pushed to a remote, off-site, hard disk (using rdiff-backup). The local user is root, but the remote user is not privileged. Hopefully, the remote filesystem is encrypted.</dt>
<dd>
</dd><dt>In order for this to work (ie for diff-backup to run unattended), you must create ssh keys on the source server and copy the public key to the remote user&#8217;s authorized keys file. For example:</dt>
<dd>
 root [at] srchost# ssh-keygen -t rsa -b 4096<br />
 root [at] srchost# ssh-copy-id -i /root/.ssh/id_dsa.pub backup [at] desthost</dd>
<dt>Now, you should be able to ssh from user &#8216;root&#8217; on srchost to user &#8216;backup&#8217; on desthost without specifying a password. When prompted for a password by ssh-keygen, just leave it blank by hitting return. The &quot;wizard&quot; <code><a href="/docs/linux/man/1-ninjahelper/">ninjahelper</a>(1)</code> will walk you through these steps.</dt>
<dd>
</dd></dl>
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
