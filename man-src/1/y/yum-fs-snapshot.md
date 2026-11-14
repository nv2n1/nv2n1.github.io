---
title: "yum-fs-snapshot(1)"
name: "yum-fs-snapshot"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-fs-snapshot/"
description: "yum-fs-snapshot"
---

<h2>NAME</h2>
<p> <code>yum-fs-snapshot</code></p>
<h2>SYNOPSIS</h2>
<p> The <code>yum-fs-snapshot</code> package</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-yum-fs-snapshot/">yum-fs-snapshot</a>(1)</code> is a Yum plugin for taking snapshots of your filesystems before running a yum transaction. By default it will take a snapshot of any filesystem that can be snapshotted, which currently is limited to BTRFS filesystems. However, all filesystems built on LVM logical volumes may be snapshotted at the block level using LVM snapshots. LVM snapshot support is provided for the purpose of system rollback. As such LVM snapshots will only be created if the kernel supports the &quot;snapshot-merge&quot; DM target.</p>
<h2>FILES</h2>
<p> <code>yum-fs-snapshot</code> uses a configuration file for its specific actions: <i>/etc/yum/pluginconf.d/fs-snapshot.conf</i></p>
<dl>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum-fs-snapshot.conf (5)</i>
</pre>
<h2>AUTHORS</h2>
<pre><code>
Josef Bacik&lt;josef[at] toxicpanda.com&gt;

    Mike Snitzer&lt;msnitzer[at] fedoraproject.org&gt;
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yum/">yum</a></code>(1) <code><a href="/docs/linux/man/5-yum-fs-snapshot-conf/">yum-fs-snapshot.conf</a></code>(5) </p>
<h2>Index</h2>
