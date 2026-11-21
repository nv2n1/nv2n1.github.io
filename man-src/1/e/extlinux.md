---

title: "extlinux(1)"
name: "extlinux"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extlinux/"
description: "extlinux – install the SYSLINUX bootloader on an ext2/ext3/ext4/btrfs/xfs filesystem"
---

<p> extlinux &#8211; install the <font SIZE="-1">SYSLINUX</font> bootloader on an ext2/ext3/ext4/btrfs/xfs filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>extlinux</code> [<i>options</i>] <i>directory</i></p>
<h2>DESCRIPTION</h2>
<p> <code>EXTLINUX</code> is a new syslinux derivative, which boots from a Linux ext2/ext3/ext4/btrfs or xfs filesystem. It works the same way as <code>SYSLINUX</code>, with a few slight modifications. It is intended to simplify first-time installation of Linux, and for creation of rescue and other special-purpose boot disks. </p>
<p> The installer is designed to be run on a mounted directory. For example, if you have an ext2, ext3, ext4, or btrfs usb key mounted on /mnt, you can run the following command:</p>
<dl>
<dt>
</dt><dd> <code>extlinux &#8211;install /mnt</code></dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code>, <code>&#8211;heads</code>=#</dt>
<dd> Force the number of heads.</dd>
<dt><code>-i</code>, <code>&#8211;install</code></dt>
<dd> Install over the current bootsector.</dd>
<dt><code>-O</code>, <code>&#8211;clear-once</code></dt>
<dd> Clear the boot-once command.</dd>
<dt><code>-o</code>, <code>&#8211;once</code>=<i>command</i></dt>
<dd> Execute a command once upon boot.</dd>
<dt><code>-M</code>, <code>&#8211;menu-save</code>=<i>label</i></dt>
<dd> Set the label to select as default on the next boot</dd>
<dt><code>-r</code>, <code>&#8211;raid</code></dt>
<dd> Fall back to the next device on boot failure.</dd>
<dt><code>&#8211;reset-adv</code></dt>
<dd> Reset auxiliary data.</dd>
<dt><code>-S</code>, <code>&#8211;sectors</code>=<i>#</i></dt>
<dd> Force the number of sectors per track.</dd>
<dt><code>-U</code>, <code>&#8211;update</code></dt>
<dd> Updates a previous <code>EXTLINUX</code> installation.</dd>
<dt><code>-z</code>, <code>&#8211;zip</code></dt>
<dd> Force zipdrive geometry (-H 64 -S 32).</dd>
<dt><code>&#8211;device</code>=<i>devicename</i></dt>
<dd> Override the automatic detection of device names. This option is intended for special environments only and should not be used by normal users. Misuse of this option can cause disk corruption and lost data.</dd></dl>
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
