---
title: "extlinux(1)"
name: "extlinux"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extlinux/"
description: "extlinux – install the SYSLINUX bootloader on an ext2/ext3/ext4/btrfs/xfs filesystem"
---

<h2 class="name">NAME</h2>
<p> extlinux &#8211; install the <font SIZE="-1">SYSLINUX</font> bootloader on an ext2/ext3/ext4/btrfs/xfs filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>extlinux</code> [<i>options</i>] <i>directory</i></p>
<h2>DESCRIPTION</h2>
<p> <code>EXTLINUX</code> is a new syslinux derivative, which boots from a Linux ext2/ext3/ext4/btrfs or xfs filesystem. It works the same way as <code>SYSLINUX</code>, with a few slight modifications. It is intended to simplify first-time installation of Linux, and for creation of rescue and other special-purpose boot disks. </p>
<p> The installer is designed to be run on a mounted directory. For example, if you have an ext2, ext3, ext4, or btrfs usb key mounted on /mnt, you can run the following command:</p>
<dl>
<dt>
<dd> <code>extlinux &#8211;install /mnt</code></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code>, <code>&#8211;heads</code>=#</p>
<dd> Force the number of heads.</p>
<dt><code>-i</code>, <code>&#8211;install</code></p>
<dd> Install over the current bootsector.</p>
<dt><code>-O</code>, <code>&#8211;clear-once</code></p>
<dd> Clear the boot-once command.</p>
<dt><code>-o</code>, <code>&#8211;once</code>=<i>command</i></p>
<dd> Execute a command once upon boot.</p>
<dt><code>-M</code>, <code>&#8211;menu-save</code>=<i>label</i></p>
<dd> Set the label to select as default on the next boot</p>
<dt><code>-r</code>, <code>&#8211;raid</code></p>
<dd> Fall back to the next device on boot failure.</p>
<dt><code>&#8211;reset-adv</code></p>
<dd> Reset auxiliary data.</p>
<dt><code>-S</code>, <code>&#8211;sectors</code>=<i>#</i></p>
<dd> Force the number of sectors per track.</p>
<dt><code>-U</code>, <code>&#8211;update</code></p>
<dd> Updates a previous <code>EXTLINUX</code> installation.</p>
<dt><code>-z</code>, <code>&#8211;zip</code></p>
<dd> Force zipdrive geometry (-H 64 -S 32).</p>
<dt><code>&#8211;device</code>=<i>devicename</i></p>
<dd> Override the automatic detection of device names. This option is intended for special environments only and should not be used by normal users. Misuse of this option can cause disk corruption and lost data.</dl>
<h2>FILES</h2>
<p> The extlinux configuration file needs to be named syslinux.cfg or extlinux.conf and needs to be stored in the extlinux installation directory. For more information about the contents of extlinux.conf, see <a href="/docs/linux/man/1-syslinux/">syslinux</a>(1) manpage, section files.</p>
<h2>LIMITATIONS</h2>
<p> Booting from XFS only works when an MBR partition table is used (not on GPT partition tables).</p>
<h2>BUGS</h2>
<p> I would appreciate hearing of any problems you have with <font SIZE="-1">SYSLINUX</font>. I would also like to hear from you if you have successfully used <font SIZE="-1">SYSLINUX</font>, especially if you are using it for a distribution. </p>
<p> If you are reporting problems, please include all possible information about your system and your BIOS; the vast majority of all problems reported turn out to be BIOS or hardware bugs, and I need as much information as possible in order to diagnose the problems. </p>
<p> There is a mailing list for discussion among <font SIZE="-1">SYSLINUX</font> users and for announcements of new and test versions. You can subscribe to this mailing list</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-syslinux/">syslinux</a></code>(1) </p>
<h2>Index</h2>
