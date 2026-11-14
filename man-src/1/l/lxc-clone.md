---
title: "lxc-clone(1)"
name: "lxc-clone"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-clone/"
description: "lxc-clone – clone a new container from an existing one."
---

<h2>NAME</h2>
<p> lxc-clone &#8211; clone a new container from an existing one.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-clone</code> [-s ] [-K ] [-M ] [-H ] [-B <i>backingstore</i>] [-L <i>fssize</i>] [-p <i>lxcpath</i>] [-P <i>newlxcpath</i>] {-o <i>orig</i>} {-n <i>new</i>} [&#8211; hook arguments] <code>lxc-clone</code> [-s ] [-K ] [-M ] [-H ] [-B <i>backingstore</i>] [-L <i>fssize</i>] [-p <i>lxcpath</i>] [-P <i>newlxcpath</i>] {orig} {new} [&#8211; hook arguments]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-clone</code> Creates a new container as a clone of an existing container. Two types of clones are supported: copy and snapshot. A copy clone copies the root filessytem from the original container to the new. A snapshot filesystem uses the backing store&#8217;s snapshot functionality to create a very small copy-on-write snapshot of the original container. Snapshot clones require the new container backing store to support snapshotting. Currently this includes only aufs, btrfs, lvm, overlayfs and zfs. LVM devices do not support snapshots of snapshots. </p>
<p> The backing store of the new container will be the same type as the original container, with one exception, overlay containers. aufs and overlayfs snapshots can be created of directory backed containers. This can be requested by using (for overlayfs) the <i>-B overlayfs</i> arguments. </p>
<p> The names of the original and new container can be given (in that order) after all options, or can be specified with the <i>-o</i> and <i>-n</i> options, respectively.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s, &#8211;snapshot</code></p>
<dd> The new container&#8217;s rootfs will be a snapshot of the original. This option can be specified when the backing store is LVM, btrfs or zfs, and must be specified when you want to snapshot using aufs or overlayfs.</p>
<dt><code>-K, &#8211;keepname</code></p>
<dd> Do not change the hostname of the container (in the root filesystem).</p>
<dt><code>-M, &#8211;keepmac</code></p>
<dd> Use the same MAC address as the original container, rather than generating a new random one.</p>
<dt><code>-H, &#8211;copyhooks</code></p>
<dd> Copy all mount hooks into the new container&#8217;s directory, and update any lxcpaths and container names as needed.</p>
<dt><code>-L, &#8211;fssize </code><i>fssize</i></p>
<dd> In the case of a block device backed container, a size for the new block device. By default, the new device will be made the same size as the original.</p>
<dt><code>-p, &#8211;lxcpath </code><i>lxcpath</i></p>
<dd> The lxcpath of the original container. By default, the system wide configured lxcpath will be used.</p>
<dt><code>-P, &#8211;newpath </code><i>newlxcpath</i></p>
<dd> The lxcpath for the new container. By default the same lxcpath as the original will be used. Note that with btrfs snapshots, changing lxcpaths may not be possible, as subvolume snapshots must be in the same btrfs filesystem.</p>
<dt><code>-B, &#8211;backingstore </code><i>backingstore</i></p>
<dd> Select a different backing store for the new container. By default the same as the original container&#8217;s is used. Note that currently changing the backingstore is only supported for aufs and overlayfs snapshots of directory backed containers. Valid backing stores include dir (directory), aufs, btrfs, lvm, zfs, loop and overlayfs.</p>
<dt><code>-o, &#8211;orig </code><i>orig</i></p>
<dd> The name of the original container to clone.</p>
<dt><code>-n, &#8211;new </code><i>new</i></p>
<dd> The name of the new container to create.</dl>
<h2>CLONE HOOK</h2>
<p> If the container being cloned has one or more <i>lxc.hook.clone</i> specified, then the specified hooks will be called for the new container. The first 3 arguments passed to the clone hook will be the container name, a section (&#8216;lxc&#8217;), and the hook type (&#8216;clone&#8217;). Extra arguments passed <code>lxc-clone</code> will be passed to the hook program starting at argument 4. The <i>LXC_ROOTFS_MOUNT</i> environment variable gives the path under which the container&#8217;s root filesystem is mounted. The configuration file pathname is stored in <i>LXC_CONFIG_FILE</i>, the new container name in <i>LXC_NAME</i>, the old container name in <i>LXC_SRC_NAME</i>, and the path or device on which the rootfs is located is in <i>LXC_ROOTFS_PATH</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Serge Hallyn &lt;serge.hallyn [at] ubuntu.com&gt; </p>
<h2>Index</h2>
