---
title: "gparted(8)"
name: "gparted"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gparted/"
description: "gparted – Gnome partition editor for manipulating disk partitions."
---

<p>gparted &#8211; Gnome partition editor for manipulating disk partitions.</p>
<h2>Synopsis</h2>
<p><code>gparted [device]&#8230;</code></p>
<h2>Description</h2>
<p>The <code>gparted</code> application is the GNOME partition editor for creating, reorganizing, and deleting disk partitions. </p>
<p> A disk device can be subdivided into one or more partitions. The <code>gparted</code> application enables you to change the partition organization on a disk device while preserving the contents of the partition. </p>
<p> With <code>gparted</code> you can accomplish the following tasks:<br />
 &#8211; Create a partition table on a disk device.<br />
 &#8211; Enable and disable partition flags such as boot and hidden.<br />
 &#8211; Perform actions with partitions such as create, delete, resize, move, check, label, copy, and paste. </p>
<p> More documentation can be found in the application help manual, and online at:<br />
 <a rel="nofollow" href="http://gparted.org">http://gparted.org</a></p>
<h2>Examples</h2>
<p>You can run <code>gparted</code> from a command line and specify one or more disk devices. </p>
<p> For example, to start gparted with the devices /dev/sda and /dev/sdc you would use the following command: </p>
<p> <code>gparted</code> /dev/sda /dev/sdc</p>
<h2>Notes</h2>
<p>Editing partitions has the potential to cause LOSS of DATA. </p>
<p> The <code>gparted</code> application is designed to enable you to edit partitions while reducing the risk of data loss. The application is carefully tested and is used by the GParted project team. However, loss of data might occur due to software bugs, hardware problems, or power failure. </p>
<p> You can help to reduce the risk of data loss by not mounting or unmounting partitions outside of the <code>gparted</code> application while <code>gparted</code> is running. </p>
<p> You are advised to BACKUP your DATA before using the <code>gparted</code> application.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs at:<br />
 <a rel="nofollow" href="http://gparted.org/bugs.php">http://gparted.org/bugs.php</a></p>
<h2>Author</h2>
<p>Manual page written by Curtis Gedak &lt;gedakc [at] users.sf.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
