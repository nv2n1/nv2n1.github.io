---
title: "fsck-btrfs(8)"
name: "fsck-btrfs"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-btrfs/"
description: "fsck.btrfs – do nothing, successfully"
---

<p>fsck.btrfs &#8211; do nothing, successfully</p>
<h2>Synopsis</h2>
<p><code>fsck.btrfs</code> [-aApy] [<i>&lt;device&gt;</i>&#8230;]</p>
<h2>Description</h2>
<p><code>fsck.btrfs</code> is a type of utility that should exist for any filesystem and is called during system setup when the corresponding <code>/etc/fstab</code> entries contain non-zero value for <code>fs_passno</code>, see <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) for more. </p>
<p> Traditional filesystems need to run their respective fsck utility in case the filesystem was not unmounted cleanly and the log needs to be replayed before mount. This is not needed for BTRFS. You should set fs_passno to 0. </p>
<p> If you wish to check the consistency of a BTRFS filesystem or repair a damaged filesystem, see <code><a href="/docs/linux/man/8-btrfs-check/">btrfs-check</a></code>(8). By default filesystem consistency is checked, the repair mode is enabled via the <i>&#8211;repair</i> option (use with care!).</p>
<h2>Options</h2>
<p>The options are all the same and detect if <code>fsck.btrfs</code> is executed in non-interactive mode and exits with success, otherwise prints a message about btrfs check.</p>
<h2>Exit Status</h2>
<p>There are two possible exit code returned: </p>
<p> 0</p>
<dl>
<dd>No error</dl>
<p> 8</p>
<dl>
<dd>Operational error, eg. device does not exist</dl>
<h2>Files</h2>
<p><code>/etc/fstab</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), </p>
