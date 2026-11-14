---
title: "nilfs(8)"
name: "nilfs"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nilfs/"
description: "NILFS – the new implementation of a log-structured file system"
---

<p>NILFS &#8211; the new implementation of a log-structured file system</p>
<h2>Synopsis</h2>
<p>Overview of the NILFS file system and the related tools.</p>
<h2>Description</h2>
<p>NILFS is a log-structured file system developed for Linux. NILFS provides versioning capability of an entire file system and continuous snapshotting that allows users to restore files mistakenly overwritten or destroyed a while ago. </p>
<p> The current major version of NILFS is version 2, which is referred to as NILFS2. NILFS2 is equipped with an online garbage collector (also called cleaner) that reclaims disk space in the background with keeping multiple snapshots. </p>
<p> When data is written or any change is made to a NILFS2 file system, it automatically creates a checkpoint. A checkpoint represents a consistent state of the NILFS2 file system of a certain instant. It becomes mountable after being changed into a snapshot. A snapshot is the checkpoint marked not to be deleted by the cleaner. NILFS2 creates a number of checkpoints at regular intervals (unless there is no change) or with synchronous writings. There is no practical limit on the number of checkpoints and snapshots. </p>
<p> The following tools are available to manage the checkpoint and the snapshot:</p>
<dl>
<dt><code>lscp</p>
<dd>lists checkpoints or snapshots</p>
<dt>mkcp</p>
<dd>makes a checkpoint or a snapshot</p>
<dt>chcp</p>
<dd>changes an existing checkpoint to a snapshot or vice versa</p>
<dt>rmcp</p>
<dd>invalidates specified checkpoint(s)</dl>
<p> These tools give the versioning capability to NILFS2; a user can select significant versions among continuously created checkpoints and can change them to snapshots to be preserved for long periods. </p>
<p> Every checkpoint except for the snapshot will become unprotected from the cleaner after a given period of time. This period is controlled by the protection_period</code> parameter defined in the <code>/etc/<a href="/docs/linux/man/5-nilfs_cleanerd-conf/">nilfs_cleanerd.conf</a></code>(5) file.</p>
<h2>Mount Options</h2>
<p>Refer to the <code><a href="/docs/linux/man/8-mount-nilfs2/">mount.nilfs2</a></code>(8).</p>
<h2>Examples</h2>
<dl>
<dt><code>mkfs -t nilfs2 </code>/dev/sdb1</p>
<dd>creates a NILFS2 file system on a block device `/dev/sdb1&#8242;.</p>
<dt><code>mount -t nilfs2 </code>/dev/sdb1 /nilfs</p>
<dd>mounts the NILFS2 file system on a mount point `/nilfs&#8217; like an ordinary POSIX file system. This will invoke a cleaner process <code><a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a></code>(8) through an external mount program (i.e. <code><a href="/docs/linux/man/8-mount-nilfs2/">mount.nilfs2</a></code>(8)).</p>
<dt><code>lscp</code></p>
<dd>lists checkpoints created in the file system as follows:</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>CNO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DATE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TIME&nbsp;<wbr>&nbsp;<wbr>MODE&nbsp;<wbr>&nbsp;<wbr>FLG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NBLKINC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ICNT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>2008-05-08 14:45:49&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>2008-05-08 14:50:22&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>200523&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>81<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>2008-05-08 20:40:34&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>136&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>61<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>2008-05-08 20:41:20&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>187666&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1604<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>2008-05-08 20:41:42&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>51&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1634<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;</p>
<dl>
<dt><code>chcp ss </code>2</p>
<dd>changes the checkpoint whose <i>checkpoint-number</i> is two to a snapshot. Then the checkpoint list will become as follows:</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>CNO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DATE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TIME&nbsp;<wbr>&nbsp;<wbr>MODE&nbsp;<wbr>&nbsp;<wbr>FLG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NBLKINC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ICNT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>2008-05-08 14:45:49&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>2008-05-08 14:50:22&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>200523&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>81<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>2008-05-08 20:40:34&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>136&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>61<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>2008-05-08 20:41:20&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>187666&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1604<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>2008-05-08 20:41:42&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>51&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1634<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;</p>
<dl>
<dt><code>mount -t nilfs2 -r -o cp=2 </code>/dev/sdb1 /snapshot</p>
<dd>mounts the snapshot on another directory `/snapshot&#8217; as a read-only file system. Here the snapshot mount requires at least two options, a read-only option (<code>-r</code> or <code>-o ro</code>) and the <code>cp</code> option (<code>-o cp=</code><i>checkpoint-number</i>). Note that a read/write mount and one or more snapshots are mountable independently, so the online backup is possible through the snapshot mounts.</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>mount -t nilfs2<br />
&nbsp;<wbr>&nbsp;<wbr>/dev/sdb1 on&nbsp;<wbr>/nilfs type nilfs2&nbsp;<wbr>(rw,gcpid=13296)<br />
&nbsp;<wbr>&nbsp;<wbr>/dev/sdb1 on&nbsp;<wbr>/snapshot type nilfs2&nbsp;<wbr>(ro,cp=2)</p>
<dl>
<dt><code>umount </code>/nilfs</p>
<dd>unmounts the NILFS2 file system mounted on `/nilfs&#8217; and will shutdown the <code><a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a></code>(8) through an external umount program (<code><a href="/docs/linux/man/8-umount-nilfs2/">umount.nilfs2</a></code>(8)) for the read/write mount.</dl>
<h2>Authors</h2>
<p><code>NILFS2</code> was developed by NILFS development team &lt;nilfs [at] osrg.net&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-nilfs2/">mkfs.nilfs2</a></code>(8), <code><a href="/docs/linux/man/8-mount-nilfs2/">mount.nilfs2</a></code>(8), <code><a href="/docs/linux/man/8-umount-nilfs2/">umount.nilfs2</a></code>(8), <code><a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a></code>(8), <code><a href="/docs/linux/man/5-nilfs_cleanerd-conf/">nilfs_cleanerd.conf</a></code>(5), <code><a href="/docs/linux/man/1-lscp/">lscp</a></code>(1), <code><a href="/docs/linux/man/8-mkcp/">mkcp</a></code>(8), <code><a href="/docs/linux/man/8-chcp/">chcp</a></code>(8), <code><a href="/docs/linux/man/8-rmcp/">rmcp</a></code>(8), <code><a href="/docs/linux/man/1-lssu/">lssu</a></code>(1), <code><a href="/docs/linux/man/8-dumpseg/">dumpseg</a></code>(8) <a rel="nofollow" href="http://www.nilfs.org/">http://www.nilfs.org/</a> </p>
