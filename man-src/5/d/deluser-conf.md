---
title: "deluser-conf(5)"
name: "deluser-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deluser-conf/"
description: "/etc/deluser.conf – configuration file for"
---

<p>/etc/deluser.conf &#8211; configuration file for <code></p>
<p> <a href="/docs/linux/man/8-deluser/">deluser</a>(8) </code> and <code><a href="/docs/linux/man/8-delgroup/">delgroup</a>(8)</code>.</p>
<h2>Description</h2>
<p>The file <i>/etc/deluser.conf</i> contains defaults for the programs <code><a href="/docs/linux/man/8-deluser/">deluser</a>(8) </code> and <code><a href="/docs/linux/man/8-delgroup/">delgroup</a>(8)</code>. Each option takes the form <i>option</i> = <i>value</i>. Double or single quotes are allowed around the value. Comment lines must have a hash sign (#) at the beginning of the line. <code><a href="/docs/linux/man/8-deluser/">deluser</a>(8) </code> and <code><a href="/docs/linux/man/8-delgroup/">delgroup</a>(8) </code> also read <i>/etc/adduser.conf,</i> see <code><a href="/docs/linux/man/5-adduser-conf/">adduser.conf</a>(5); </code> settings in <i>deluser.conf </i> may overwrite settings made in <i>adduser.conf.</i> The valid configuration options are:</p>
<dl>
<dt><code>REMOVE_HOME</code></p>
<dd>Removes the home directory and mail spool of the user to be removed. Value may be 0 (don&#8217;t delete) or 1 (do delete).</p>
<dt><code>REMOVE_ALL_FILES</code></p>
<dd>Removes all files on the system owned by the user to be removed. If this option is activated <code>REMOVE_HOME</code> has no effect. Values may be 0 or 1.</p>
<dt><code>BACKUP</code></p>
<dd>If <code>REMOVE_HOME</code> or <code>REMOVE_ALL_FILES</code> is activated all files are backuped before they are removed. The backup file that is created defaults to username.tar(.gz|.bz2) in the directory specified by the <code>BACKUP_TO</code> option. The compression method is chosen to the best that is available. Values may be 0 or 1.</p>
<dt><code>BACKUP_TO</code></p>
<dd>If <code>BACKUP</code> is activated, <code>BACKUP_TO</code> specifies the directory the backup is written to. Default is the current directory.</p>
<dt><code>NO_DEL_PATHS</code></p>
<dd>A list of regular expressions, space separated. All files to be deleted in course of deleting home directories or deleting files owned by the user to be deleted are checked against each of these regular expressions. If a match is detected, the file is not deleted. Defaults to a list of system directories, leaving only /home. In other words: By default only files below /home belonging to that specific user are going to be deleted.</p>
<dt><code>ONLY_IF_EMPTY</code></p>
<dd>Only delete a group if there are no users belonging to this group. Defaults to 0.</p>
<dt><code>EXCLUDE_FSTYPES</code></p>
<dd>A regular expression which describes all file systems which should be excluded when looking for files of a user to be deleted. Defaults to &quot;(proc|sysfs|usbfs|devpts|tmpfs|afs)&quot;. </p>
<h2>Files</h2>
<p><i>/etc/deluser.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-adduser-conf/">adduser.conf</a></code>(5), <code><a href="/docs/linux/man/8-delgroup/">delgroup</a></code>(8), <code><a href="/docs/linux/man/8-deluser/">deluser</a>(8)</code> </p>
