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
<p> <code>backup-light [option(s)]</code></p>
<p> Backup-light backups up the active users $HOME directory in eather .tar.bz2 or .tar.gz. It is able to backup to not only the internal hard drive, but any external hard drives, and removable mediums such as a CD or DVD or USB device. Backup-light also creates a md5sum of the backup archive and will only restore from a archive with a valid md5sum.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code></dt>
<dd> Saves the backup archive to an alternate directory/device.</dd>
<dt><code>-i</code></dt>
<dd> Preforms an incremental backup.</dd>
<dt><code>-f</code></dt>
<dd> Preforms a full backup.</dd>
<dt><code>-e</code></dt>
<dd> Specifies a directory to be excluded from the backup.</dd>
<dt><code>-r</code></dt>
<dd> Restores from a backup.</dd>
<dt><code>-R</code></dt>
<dd> Recovers from a full backup then restores all the incremental backups up to the user specified point.</dd>
<dt><code>-d</code></dt>
<dd> Creates a backup and burns it to a CD/DVD.</dd>
<dt><code>-m</code></dt>
<dd> Restores from a multi disk (split) backup.</dd>
<dt><code>-n</code></dt>
<dd> Prevents updating the timestamp if an incremental backup is done.</dd>
<dt><code>-l</code></dt>
<dd> Shows the log containing dates and types of backups preformed</dd>
<dt><code>-v</code></dt>
<dd> Prints the version and exit.</dd>
<dt><code>-h</code></dt>
<dd> Shows the help message.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>backup-light</code></dt>
<dd> Preforms the backup with all default settings.</dd>
<dt><code>backup-light -o ~/backup</code></dt>
<dd> Preform the default backup but saves it to ~/backup instead of the default location.</dd>
<dt><code>backup-light -i</code></dt>
<dd> Preforms a incremental backup and saves it to the default location.</dd>
<dt><code>backup-light -f</code></dt>
<dd> Preforms a full backup and saves it to the default location.</dd>
<dt><code>backup-light -e Music</code></dt>
<dd> Excludes the directory called &quot;Music&quot; from the backup process.</dd>
<dt><code>backup-light -r</code></dt>
<dd> Restores from a backup.</dd>
<dt><code>backup-light -R</code></dt>
<dd> Prompts the user for an end date for the backup recoveroy. Then restores from the newest full backup and any incremental backups done afterwards.</dd>
<dt><code>backup-light -d</code></dt>
<dd> Creates a backup and burns it to a CD/DVD.</dd>
<dt><code>backup-light -m</code></dt>
<dd> Restores from a multi disk (split) backup.</dd>
<dt><code>backup-light -n</code></dt>
<dd> Prevents the timestamp from being updated if doing a incremental backup.</dd>
<dt><code>backup-light -fd</code></dt>
<dd> Preforms a full backup and burns it to a CD/DVD.</dd>
<dt><code>backup-light -l</code></dt>
<dd> Shows the log containing the dates and types of backups preformed.</dd>
<dt><code>backup-light -v</code></dt>
<dd> Prints version info.</dd>
<dt><code>backup-light -h</code></dt>
<dd> Prints the help message</dd></dl>
<h2>BUGS</h2>
<dl>
<dt>Please report any bugs at &lt;<a rel="nofollow" href="http://code.google.com/p/backup-light/issues/list">http://code.google.com/p/backup-light/issues/list</a>&gt; or send an email or our mailing list &lt;backup-light [at] googlegroups.com&gt;.</dt>
<dd></dd></dl>
<h2>AUTHORS</h2>
<dl>
<dt>Adam Jimerson &lt;vendion [at] gmail.com&gt;</dt>
<dd>
</dd><dt>Robert A. Kelly III &lt;bluethegrappler [at] gmail.com&gt;</dt>
<dd></dd></dl>
