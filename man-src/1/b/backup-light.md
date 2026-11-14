---
title: "backup-light(1)"
name: "backup-light"
section: "1"
letter: "b"
url: "/docs/linux/man/1-backup-light/"
description: "Backup-light – backups up the active users $HOME directory"
---

<h2>NAME</h2>
<p> Backup-light &#8211; backups up the active users $HOME directory</p>
<h2>SYNOPSIS</h2>
<p> <code>backup-light [option(s)]</code></p>
<h2>DESCRIPTION</h2>
<p> Backup-light backups up the active users $HOME directory in eather .tar.bz2 or .tar.gz. It is able to backup to not only the internal hard drive, but any external hard drives, and removable mediums such as a CD or DVD or USB device. Backup-light also creates a md5sum of the backup archive and will only restore from a archive with a valid md5sum.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code></p>
<dd> Saves the backup archive to an alternate directory/device.</p>
<dt><code>-i</code></p>
<dd> Preforms an incremental backup.</p>
<dt><code>-f</code></p>
<dd> Preforms a full backup.</p>
<dt><code>-e</code></p>
<dd> Specifies a directory to be excluded from the backup.</p>
<dt><code>-r</code></p>
<dd> Restores from a backup.</p>
<dt><code>-R</code></p>
<dd> Recovers from a full backup then restores all the incremental backups up to the user specified point.</p>
<dt><code>-d</code></p>
<dd> Creates a backup and burns it to a CD/DVD.</p>
<dt><code>-m</code></p>
<dd> Restores from a multi disk (split) backup.</p>
<dt><code>-n</code></p>
<dd> Prevents updating the timestamp if an incremental backup is done.</p>
<dt><code>-l</code></p>
<dd> Shows the log containing dates and types of backups preformed</p>
<dt><code>-v</code></p>
<dd> Prints the version and exit.</p>
<dt><code>-h</code></p>
<dd> Shows the help message.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>backup-light</code></p>
<dd> Preforms the backup with all default settings.</p>
<dt><code>backup-light -o ~/backup</code></p>
<dd> Preform the default backup but saves it to ~/backup instead of the default location.</p>
<dt><code>backup-light -i</code></p>
<dd> Preforms a incremental backup and saves it to the default location.</p>
<dt><code>backup-light -f</code></p>
<dd> Preforms a full backup and saves it to the default location.</p>
<dt><code>backup-light -e Music</code></p>
<dd> Excludes the directory called &quot;Music&quot; from the backup process.</p>
<dt><code>backup-light -r</code></p>
<dd> Restores from a backup.</p>
<dt><code>backup-light -R</code></p>
<dd> Prompts the user for an end date for the backup recoveroy. Then restores from the newest full backup and any incremental backups done afterwards.</p>
<dt><code>backup-light -d</code></p>
<dd> Creates a backup and burns it to a CD/DVD.</p>
<dt><code>backup-light -m</code></p>
<dd> Restores from a multi disk (split) backup.</p>
<dt><code>backup-light -n</code></p>
<dd> Prevents the timestamp from being updated if doing a incremental backup.</p>
<dt><code>backup-light -fd</code></p>
<dd> Preforms a full backup and burns it to a CD/DVD.</p>
<dt><code>backup-light -l</code></p>
<dd> Shows the log containing the dates and types of backups preformed.</p>
<dt><code>backup-light -v</code></p>
<dd> Prints version info.</p>
<dt><code>backup-light -h</code></p>
<dd> Prints the help message</dl>
<h2>BUGS</h2>
<dl>
<dt>Please report any bugs at &lt;<a rel="nofollow" href="http://code.google.com/p/backup-light/issues/list">http://code.google.com/p/backup-light/issues/list</a>&gt; or send an email or our mailing list &lt;backup-light [at] googlegroups.com&gt;.</p>
<dd></dl>
<h2>AUTHORS</h2>
<dl>
<dt>Adam Jimerson &lt;vendion [at] gmail.com&gt;</p>
<dd>
<dt>Robert A. Kelly III &lt;bluethegrappler [at] gmail.com&gt;</p>
<dd></dl>
<h2>Index</h2>
