---
title: "eject(1)"
name: "eject"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eject/"
description: "eject – eject removable media"
---

<h2 class="name">NAME</h2>
<p> eject &#8211; eject removable media </p>
<p> <code>eject</code> [options] <i>device</i>|<i>mountpoint</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>eject</code> allows removable media (typically a CD-ROM, floppy disk, tape, JAZ, ZIP or USB disk) to be ejected under software control. The command can also control some multi-disc CD-ROM changers, the auto-eject feature supported by some devices, and close the disc tray of some CD-ROM drives. </p>
<p> The device corresponding to <i>device</i> or <i>mountpoint</i> is ejected. If no name is specified, the default name <code>/dev/cdrom</code> is used. The device may be addressed by device name (e.g., &#8216;sda&#8217;), device path (e.g., &#8216;/dev/sda&#8217;), UUID=<i>uuid</i> or LABEL=<i>label</i> tags. </p>
<p> There are four different methods of ejecting, depending on whether the device is a CD-ROM, SCSI device, removable floppy, or tape. By default <code>eject</code> tries all four methods in order until it succeeds. </p>
<p> If a device partition is specified, the whole-disk device is used. </p>
<p> If the device or a device partition is currently mounted, it is unmounted before ejecting. The eject is processed on exclusive open block device file descriptor if <code>&#8211;no-unmount</code> or <code>&#8211;force</code> are not specified.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;auto on</code>|<code>off</code></p>
<dl>
<dt>
<dd> This option controls the auto-eject mode, supported by some devices. When enabled, the drive automatically ejects when the device is closed.</dl>
<p> <code>-c</code>, <code>&#8211;changerslot</code> <i>slot</i></p>
<dl>
<dt>
<dd> With this option a CD slot can be selected from an ATAPI/IDE CD-ROM changer. The CD-ROM drive cannot be in use (mounted data CD or playing a music CD) for a change request to work. Please also note that the first slot of the changer is referred to as 0, not 1.</dl>
<p> <code>-d</code>, <code>&#8211;default</code></p>
<dl>
<dt>
<dd> List the default device name.</dl>
<p> <code>-F</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Force eject, don&#8217;t check device type, don&#8217;t open device with exclusive lock. The successful result may be false positive on non hot-pluggable devices.</dl>
<p> <code>-f</code>, <code>&#8211;floppy</code></p>
<dl>
<dt>
<dd> This option specifies that the drive should be ejected using a removable floppy disk eject command.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-i</code>, <code>&#8211;manualeject on</code>|<code>off</code></p>
<dl>
<dt>
<dd> This option controls locking of the hardware eject button. When enabled, the drive will not be ejected when the button is pressed. This is useful when you are carrying a laptop in a bag or case and don&#8217;t want it to eject if the button is inadvertently pressed.</dl>
<p> <code>-M</code>, <code>&#8211;no-partitions-unmount</code></p>
<dl>
<dt>
<dd> The option tells eject to not try to unmount other partitions on partitioned devices. If another partition is still mounted, the program will not attempt to eject the media. It will attempt to unmount only the device or mountpoint given on the command line.</dl>
<p> <code>-m</code>, <code>&#8211;no-unmount</code></p>
<dl>
<dt>
<dd> The option tells eject to not try to unmount at all. If this option is not specified than <code>eject</code> opens the device with <code>O_EXCL</code> flag to be sure that the device is not used (since v2.35).</dl>
<p> <code>-n</code>, <code>&#8211;noop</code></p>
<dl>
<dt>
<dd> With this option the selected device is displayed but no action is performed.</dl>
<p> <code>-p</code>, <code>&#8211;proc</code></p>
<dl>
<dt>
<dd> This option allows you to use <i>/proc/mounts</i> instead <i>/etc/mtab</i>. It also passes the <code>-n</code> option to <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8).</dl>
<p> <code>-q</code>, <code>&#8211;tape</code></p>
<dl>
<dt>
<dd> This option specifies that the drive should be ejected using a tape drive offline command.</dl>
<p> <code>-r</code>, <code>&#8211;cdrom</code></p>
<dl>
<dt>
<dd> This option specifies that the drive should be ejected using a CDROM eject command.</dl>
<p> <code>-s</code>, <code>&#8211;scsi</code></p>
<dl>
<dt>
<dd> This option specifies that the drive should be ejected using SCSI commands.</dl>
<p> <code>-T</code>, <code>&#8211;traytoggle</code></p>
<dl>
<dt>
<dd> With this option the drive is given a CD-ROM tray close command if it&#8217;s opened, and a CD-ROM tray eject command if it&#8217;s closed. Not all devices support this command, because it uses the above CD-ROM tray close command.</dl>
<p> <code>-t</code>, <code>&#8211;trayclose</code></p>
<dl>
<dt>
<dd> With this option the drive is given a CD-ROM tray close command. Not all devices support this command.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Run in verbose mode; more information is displayed about what the command is doing.</dl>
<p> <code>-X</code>, <code>&#8211;listspeed</code></p>
<dl>
<dt>
<dd> With this option the CD-ROM drive will be probed to detect the available speeds. The output is a list of speeds which can be used as an argument of the <code>-x</code> option. This only works with Linux 2.6.13 or higher, on previous versions solely the maximum speed will be reported. Also note that some drives may not correctly report the speed and therefore this option does not work with them.</dl>
<p> <code>-x</code>, <code>&#8211;cdspeed</code> <i>speed</i></p>
<dl>
<dt>
<dd> With this option the drive is given a CD-ROM select speed command. The <i>speed</i> argument is a number indicating the desired speed (e.g., 8 for 8X speed), or 0 for maximum data rate. Not all devices support this command and you can only specify speeds that the drive is capable of. Every time the media is changed this option is cleared. This option can be used alone, or with the <code>-t</code> and <code>-c</code> options.</dl>
<h2>EXIT STATUS</h2>
<p> Returns 0 if operation was successful, 1 if operation failed or command syntax was not valid.</p>
<h2>NOTES</h2>
<p> <code>eject</code> only works with devices that support one or more of the four methods of ejecting. This includes most CD-ROM drives (IDE, SCSI, and proprietary), some SCSI tape drives, JAZ drives, ZIP drives (parallel port, SCSI, and IDE versions), and LS120 removable floppies. Users have also reported success with floppy drives on Sun SPARC and Apple Macintosh systems. If <code>eject</code> does not work, it is most likely a limitation of the kernel driver for the device and not the <code>eject</code> program itself. </p>
<p> The <code>-r</code>, <code>-s</code>, <code>-f</code>, and <code>-q</code> options allow controlling which methods are used to eject. More than one method can be specified. If none of these options are specified, it tries all four (this works fine in most cases). </p>
<p> <code>eject</code> may not always be able to determine if the device is mounted (e.g., if it has several names). If the device name is a symbolic link, <code>eject</code> will follow the link and use the device that it points to. </p>
<p> If <code>eject</code> determines that the device can have multiple partitions, it will attempt to unmount all mounted partitions of the device before ejecting (see also <code>&#8211;no-partitions-unmount</code>). If an unmount fails, the program will not attempt to eject the media. </p>
<p> You can eject an audio CD. Some CD-ROM drives will refuse to open the tray if the drive is empty. Some devices do not support the tray close command. </p>
<p> If the auto-eject feature is enabled, then the drive will always be ejected after running this command. Not all Linux kernel CD-ROM drivers support the auto-eject mode. There is no way to find out the state of the auto-eject mode. </p>
<p> You need appropriate privileges to access the device files. Running as root is required to eject some devices (e.g., SCSI devices).</p>
<h2>AUTHORS</h2>
<p> &#8211; original author, and &#8211; util-linux version.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8), <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>eject</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
