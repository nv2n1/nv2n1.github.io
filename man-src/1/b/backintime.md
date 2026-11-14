---
title: "backintime(1)"
name: "backintime"
section: "1"
letter: "b"
url: "/docs/linux/man/1-backintime/"
description: "backintime – a simple backup tool for Linux."
---

<h2>NAME</h2>
<p> backintime &#8211; a simple backup tool for Linux. </p>
<p> This is command line tool. The graphical tools are: backintime-gnome and backintime-kde4.</p>
<h2>SYNOPSIS</h2>
<p> <code>backintime</code> [ &#8211;backup | &#8211;backup-job | &#8211;snapshots-path | &#8211;snapshots-list | &#8211;snapshots-list-path | &#8211;last-snapshot | &#8211;last-snapshot-path | &#8211;help | &#8211;version | &#8211;license ]</p>
<h2>DESCRIPTION</h2>
<p> Back In Time is a simple backup tool for Linux. The backup is done by taking snapshots of a specified set of folders. </p>
<p> All you have to do is configure: where to save snapshots, what folders to backup. You can also specify a backup schedule: disabled, every 5 minutes, every 10 minutes, every hour, every day, every week, every month. To configure it use one of the graphical interfaces available (backintime-gnome or backintime-kde4). </p>
<p> It acts as a &#8216;user mode&#8217; backup tool. This means that you can backup/restore only folders you have write access to (actually you can backup read-only folders, but you can&#8217;t restore them). </p>
<p> If you want to run it as root you need to use &#8216;su&#8217;. </p>
<p> A new snapshot is created only if something changed since the last snapshot (if any). </p>
<p> A snapshot contains all the files from the selected folders (except for exclude patterns). In order to reduce disk space it use hard-links (if possible) between snapshots for unchanged files. This way a file of 10Mb, unchanged for 10 snapshots, will use only 10Mb on the disk. </p>
<p> When you restore a file &#8216;A&#8217;, if it already exists on the file system it will be renamed to &#8216;A.backup.currentdate&#8217;. </p>
<p> For automatic backup it use &#8216;cron&#8217; so there is no need for a daemon, but &#8216;cron&#8217; must be running.</p>
<h3>user.callback</h3>
<p> During backup process the application can call a user callback at different steps. This callback is &quot;$XDG_CONFIG_HOME/backintime/user.callback&quot; (by default $XDG_CONFIG_HOME is ~/.config). The first argument is the reason:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> Backup process begins.</p>
<dt>2</p>
<dd> Backup process ends.</p>
<dt>3</p>
<dd> A new snapshot was taken. The extra arguments are snapshot ID and snapshot path.</p>
<dt>4</p>
<dd> There was an error. The second argument is the error code.</p>
<dl>
<dt>
<dd> Error codes:</p>
<dl>
<dt>1</p>
<dd> The application is not configured.</p>
<dt>2</p>
<dd> A &quot;take snapshot&quot; process is already running.</p>
<dt>3</p>
<dd> Can&#8217;t find snapshots folder (is it on a removable drive ?).</p>
<dt>4</p>
<dd> A snapshot for &quot;now&quot; already exist.</dl>
</dl>
</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-b, &#8211;backup</p>
<dd> take a snapshot now (if needed)</p>
<dt>&#8211;backup-job</p>
<dd> take a snapshot (if needed) depending on schedule rules (used for cron jobs)</p>
<dt>&#8211;snapshots-path</p>
<dd> display path where is saves the snapshots (if configured)</p>
<dt>&#8211;snapshots-list</p>
<dd> display the list of snapshot IDs (if any)</p>
<dt>&#8211;snapshots-list-path</p>
<dd> display the paths to snapshots (if any)</p>
<dt>&#8211;last-snapshot</p>
<dd> display last snapshot ID (if any)</p>
<dt>&#8211;last-snapshot-path</p>
<dd> display the path to the last snapshot (if any)</p>
<dt>-h, &#8211;help</p>
<dd> display a short help</p>
<dt>-v, &#8211;version</p>
<dd> show version</p>
<dt>&#8211;license</p>
<dd> show license</dl>
<h2>SEE ALSO</h2>
<p> backintime-gnome, backintime-kde4. </p>
<p> Back In Time also has a website: <a rel="nofollow" href="http://backintime.le-web.org">http://backintime.le-web.org</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Oprea Dan (&lt;dan [at] le-web.org&gt;). </p>
<h2>Index</h2>
