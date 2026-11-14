---
title: "mount-ntfs-3g(8)"
name: "mount-ntfs-3g"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-ntfs-3g/"
description: "ntfs-3g – Third Generation Read/Write NTFS Driver"
---

<p>ntfs-3g &#8211; Third Generation Read/Write NTFS Driver</p>
<h2>Synopsis</h2>
<p><code>ntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i><br />
 <code>mount -t ntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i><br />
 <code>lowntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i><br />
 <code>mount -t lowntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i></p>
<h2>Description</h2>
<p><code>ntfs-3g</code> is an NTFS driver, which can create, remove, rename, move files, directories, hard links, and streams; it can read and write files, including streams, sparse files and transparently compressed files; it can handle special files like symbolic links, devices, and FIFOs; moreover it provides standard management of file ownership and permissions, including POSIX ACLs. </p>
<p> It comes in two variants <code>ntfs-3g</code> and <code>lowntfs-3g</code> with a few differences mentioned below in relevant options descriptions. </p>
<p> The <i>volume</i> to be mounted can be either a block device or an image file, either by using the mount command or starting the drive.</p>
<h3>Windows hibernation and fast restarting</h3>
<p>On computers which can be dual-booted into Windows or Linux, Windows has to be fully shut down before booting into Linux, otherwise the NTFS file systems on internal disks may be left in an inconsistent state and changes made by Linux may be ignored by Windows. </p>
<p> So, Windows may not be left in hibernation when starting Linux, in order to avoid inconsistencies. Moreover, the fast restart feature available on recent Windows systems has to be disabled. This can be achieved by issuing as an Administrator the Windows command which disables both hibernation and fast restarting :</p>
<dl>
<dd>powercfg /h off </p>
</dl>
<p> If either Windows is hibernated or its fast restart is enabled, partitions on internal disks are forced to be mounted in read-only mode.</p>
<h3>Access Handling and Security</h3>
<p>By default, files and directories are owned by the effective user and group of the mounting process, and everybody has full read, write, execution and directory browsing permissions. You can also assign permissions to a single user by using the <code>uid</code> and/or the <code>gid </code> options together with the <code>umask,</code> or <code>fmask</code> and <code>dmask</code> options. </p>
<p> Doing so, all Windows users have full access to the files created by <code>ntfs-3g.</code> </p>
<p> But, by setting the <code>permissions</code> option, you can benefit from the full ownership and permissions features as defined by POSIX. Moreover, by defining a Windows-to-Linux user mapping, the ownerships and permissions are even applied to Windows users and conversely. </p>
<p> If <code>ntfs-3g </code> is set setuid-root then non-root users will be also able to mount volumes.</p>
<h3>Windows Filename Compatibility</h3>
<p>NTFS supports several filename namespaces: DOS, Win32 and POSIX. While the <code>ntfs-3g</code> driver handles all of them, it always creates new files in the POSIX namespace for maximum portability and interoperability reasons. This means that filenames are case sensitive and all characters are allowed except &#8216;/&#8217; and &#8216;
