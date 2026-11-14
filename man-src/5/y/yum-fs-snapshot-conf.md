---
title: "yum-fs-snapshot-conf(5)"
name: "yum-fs-snapshot-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yum-fs-snapshot-conf/"
description: "yum-fs-snapshot.conf(5)"
---

<p><code><a href="/docs/linux/man/5-yum-fs-snapshot-conf/">yum-fs-snapshot.conf</a>(5)</code> </p>
<h2>Synopsis</h2>
<p><code><a href="/docs/linux/man/5-yum-fs-snapshot-conf/">yum-fs-snapshot.conf</a>(5)</code> is the configuration file for <code><a href="/docs/linux/man/1-yum-fs-snapshot/">yum-fs-snapshot</a>(1)</code> Yum plugin for snapshotting your filesystems before running a yum transaction. By default, this plugin will snapshot all filesystems that it is capable of snapshotting. This includes block-level snapshots using LVM snapshots.</p>
<h2>Files</h2>
<p><i>/etc/yum/pluginconf.d/fs-snapshot.conf</i></p>
<h2>File Format</h2>
<p><code><a href="/docs/linux/man/5-yum-fs-snapshot-conf/">yum-fs-snapshot.conf</a>(5)</code> utilizes configuration options in the form of</p>
<dl>
<dt>OPTION=VALUE</p>
<dd></dl>
<h2>Option</h2>
<dl>
<dt>exclude</p>
<dd>This is a space delimited list of the mount points you do not wish to have snapshotted by this plugin.</dl>
<h2>Option</h2>
<dl>
<dt>create_snapshots_in_post</p>
<dd>This is a boolean value used to control whether snapshots are also created after running the yum transaction.</dl>
<h2>OPTION &#8211; [lvm] section</h2>
<dl>
<dt>enabled</p>
<dd>This is a boolean value used to control whether LVM snapshots will be created for filesystems built on LVM logical volumes.</dl>
<h2>OPTION &#8211; [lvm] section</h2>
<dl>
<dt>lvcreate_size_args</p>
<dd>This is the space delimited lvcreate argument list that is used to specify the size of the snapshot LV. Valid lvcreate size options are -l or -L. If not specified then LVM snapshots will not be created for volumes that are not thinly provisioned.</dl>
<h2>Author</h2>
<dl>
<dd>Josef Bacik &lt;josef [at] toxicpanda.com&gt;<br />
 Mike Snitzer &lt;msnitzer [at] fedoraproject.org&gt;</p>
<dl>
<dd></dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yum-fs-snapshot/">yum-fs-snapshot</a>(1)</code> </p>
