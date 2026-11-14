---
title: "sheep(8)"
name: "sheep"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sheep/"
description: "sheep – Distributed Block Storage System for KVM"
---

<p>sheep &#8211; Distributed Block Storage System for KVM</p>
<h2>Snynopsis</h2>
<p><code>sheep [options] [PATH]</code></p>
<h2>Description</h2>
<p><code>sheep</code> Sheepdog is a distributed storage system for KVM/QEMU. It provides highly available block level storage volumes to virtual machines. Sheepdog supports advanced volume management features such as snapshot, cloning, and thin provisioning. The architecture of Sheepdog is fully symmetric; there is no central node such as a meta-data server. </p>
<p> The server daemon is called <a href="/docs/linux/man/8-sheep/">sheep</a>(8). A command line utility is available via <a href="/docs/linux/man/8-collie/">collie</a>(8). KVM/QEMU virtual machines use the sheep daemon via a block driver available in <a href="/docs/linux/man/1-qemu/">qemu</a>(1).</p>
<h2>Options</h2>
<dl>
<dt><code>-p</code><i></i>, <code>&#8211;port</code><i> port</i></p>
<dd>This option specifies the IP port over which <code>sheep</code> looks for other sheepdog cluster nodes.</p>
<dt><code>-f</code><i></i>, <code>&#8211;foreground</code></p>
<dd>This option forces the sheepdog daemon to run in the foreground.</p>
<dt><code>-l</code><i></i>, <code>&#8211;loglevel</code><i> loglevel</i></p>
<dd>This option specifies the message level printed.</p>
<dt><code>-d</code><i></i>, <code>&#8211;debug</code></p>
<dd>This option displays debug messages.</p>
<dt><code>-h</code><i></i>, <code>&#8211;help</code></p>
<dd>Display help and exit.</dl>
<h2>Path</h2>
<p>Proper LSB systems will store sheepdog files in /var/lib/sheepdog. The init script uses this directory by default. The directory must be on a filesystem with xattr support. In the case of ext3, user_xattr should be added to the mount options. </p>
<p> mount -o remount,user_xattr /var/lib/shepdog</p>
<h2>Dependencies</h2>
<p><code>sheepdog</code> requires QEMU 0.13.z or later and Corosync 1.y.z.</p>
<h2>Files</h2>
<p><code>/var/lib/sheepdog &#8211; Directory containing block storage information</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-collie/">collie</a>(8),<a href="/docs/linux/man/1-qemu/">qemu</a>(1),<a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a>(8)</code> </p>
<h2>Authors</h2>
<p>This software is developed by the sheepdog community which may be reached via mailing list at &lt;sheepdog [at] lists.wpkg.org&gt;.</p>
