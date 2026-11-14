---
title: "lxc-snapshot(1)"
name: "lxc-snapshot"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-snapshot/"
description: "lxc-snapshot – Snapshot an existing container."
---

<h2>NAME</h2>
<p> lxc-snapshot &#8211; Snapshot an existing container.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-snapshot</code> {-n, &#8211;name <i>name</i>} [-c, &#8211;comment <i>file</i>] <code>lxc-snapshot</code> {-n, &#8211;name <i>name</i>} {-d, -destroy <i>snapshot-name</i>} <code>lxc-snapshot</code> {-n, &#8211;name <i>name</i>} {-L, &#8211;list } [-C, &#8211;showcomments ] <code>lxc-snapshot</code> {-n, &#8211;name <i>name</i>} {-r, -restore <i>snapshot-name</i>} [ <i>newname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-snapshot</code> creates, lists, and restores container snapshots. </p>
<p> Snapshots are stored as snapshotted containers under a private configuration path. For instance, if the container&#8217;s configuration path is <i>/var/lib/lxc</i> and the container is <i>c1</i>, then the first snapshot will be stored as container <i>snap0</i> under configuration path <i>/var/lib/lxcsnaps/c1</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c,&#8211;comment </code><i>comment_file</i></p>
<dd> Associate the comment in <i>comment_file</i> with the newly created snapshot.</p>
<dt><code>-d,&#8211;destroy snapshot-name</code></p>
<dd> Destroy the named snapshot.</p>
<dt><code>-L,&#8211;list </code></p>
<dd> List existing snapshots.</p>
<dt><code>-C,&#8211;showcomments </code></p>
<dd> Show snapshot comments in the snapshots listings.</p>
<dt><code>-r,&#8211;restore snapshot-name</code></p>
<dd> Restore the named snapshot, meaning a full new container is created which is a copy of the snapshot.</p>
<dt><code>newname</code></p>
<dd> When restoring a snapshot, the last optional argument is the name to use for the restored container. If no name is given, then the original container will be destroyed and the restored container will take its place. Note that deleting the original snapshot is not possible in the case of aufs, overlayfs or zfs backed snapshots.</dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print a longer usage message than normal.</p>
<dt><code>&#8211;usage</code></p>
<dd> Give the usage message</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> mute on</p>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></p>
<dd> Use an alternate container path. The default is /var/lib/lxc.</p>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></p>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</p>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></p>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </p>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></p>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version number.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Serge Hallyn &lt;serge.hallyn [at] ubuntu.com &gt; </p>
<h2>Index</h2>
