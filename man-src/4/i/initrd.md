---
title: "initrd(4)"
name: "initrd"
section: "4"
letter: "i"
url: "/docs/linux/man/4-initrd/"
description: "initrd – boot loader initialized RAM disk"
---

<p>initrd &#8211; boot loader initialized RAM disk</p>
<h2>Configuration</h2>
<p><i>/dev/initrd</i> is a read-only block device assigned major number 1 and minor number 250. Typically <i>/dev/initrd</i> is owned by root:disk with mode 0400 (read access by root only). If the Linux system does not have <i>/dev/initrd</i> already created, it can be created with the following commands: </p>
<p> mknod -m 400 /dev/initrd b 1 250 chown root:disk /dev/initrd </p>
<p> Also, support for both &quot;RAM disk&quot; and &quot;Initial RAM disk&quot; (e.g., <code>CONFIG_BLK_DEV_RAM=y</code> and <code>CONFIG_BLK_DEV_INITRD=y</code>) must be compiled directly into the Linux kernel to use <i>/dev/initrd</i>. When using <i>/dev/initrd</i>, the RAM disk driver cannot be loaded as a module.</p>
<h2>Description</h2>
<p>The special file <i>/dev/initrd</i> is a read-only block device. This device is a RAM disk that is initialized (e.g., loaded) by the boot loader before the kernel is started. The kernel then can use <i>/dev/initrd</i>&#8216;s contents for a two-phase system boot-up. </p>
<p> In the first boot-up phase, the kernel starts up and mounts an initial root filesystem from the contents of <i>/dev/initrd</i> (e.g., RAM disk initialized by the boot loader). In the second phase, additional drivers or other modules are loaded from the initial root device&#8217;s contents. After loading the additional modules, a new root filesystem (i.e., the normal root filesystem) is mounted from a different device.</p>
<h3>Boot-up operation</h3>
<p>When booting up with <code>initrd</code>, the system boots as follows:</p>
<dl>
<dt>1.</p>
<dd>The boot loader loads the kernel program and <i>/dev/initrd</i>&#8216;s contents into memory.</p>
<dt>2.</p>
<dd>On kernel startup, the kernel uncompresses and copies the contents of the device <i>/dev/initrd</i> onto device <i>/dev/ram0</i> and then frees the memory used by <i>/dev/initrd</i>.</p>
<dt>3.</p>
<dd>The kernel then read-write mounts the device <i>/dev/ram0</i> as the initial root filesystem.</p>
<dt>4.</p>
<dd>If the indicated normal root filesystem is also the initial root filesystem (e.g., <i>/dev/ram0</i>) then the kernel skips to the last step for the usual boot sequence.</p>
<dt>5.</p>
<dd>If the executable file <i>/linuxrc</i> is present in the initial root filesystem, <i>/linuxrc</i> is executed with UID 0. (The file <i>/linuxrc</i> must have executable permission. The file <i>/linuxrc</i> can be any valid executable, including a shell script.)</p>
<dt>6.</p>
<dd>If <i>/linuxrc</i> is not executed or when <i>/linuxrc</i> terminates, the normal root filesystem is mounted. (If <i>/linuxrc</i> exits with any filesystems mounted on the initial root filesystem, then the behavior of the kernel is <code>UNSPECIFIED</code>. See the NOTES section for the current kernel behavior.)</p>
<dt>7.</p>
<dd>If the normal root filesystem has a directory <i>/initrd</i>, the device <i>/dev/ram0</i> is moved from <i>/</i> to <i>/initrd</i>. Otherwise, if the directory <i>/initrd</i> does not exist, the device <i>/dev/ram0</i> is unmounted. (When moved from <i>/</i> to <i>/initrd</i>, <i>/dev/ram0</i> is not unmounted and therefore processes can remain running from <i>/dev/ram0</i>. If directory <i>/initrd</i> does not exist on the normal root filesystem and any processes remain running from <i>/dev/ram0</i> when <i>/linuxrc</i> exits, the behavior of the kernel is <code>UNSPECIFIED</code>. See the NOTES section for the current kernel behavior.)</p>
<dt>8.</p>
<dd>The usual boot sequence (e.g., invocation of <i>/sbin/init</i>) is performed on the normal root filesystem.</dl>
<h3>Options</h3>
<p>The following boot loader options, when used with <code>initrd</code>, affect the kernel&#8217;s boot-up operation:</p>
<dl>
<dt><code>initrd=</code><i>filename</i></p>
<dd>Specifies the file to load as the contents of <i>/dev/initrd</i>. For <code>LOADLIN</code> this is a command-line option. For <code>LILO</code> you have to use this command in the <code>LILO</code> configuration file <i>/etc/lilo.config</i>. The filename specified with this option will typically be a gzipped filesystem image.</p>
<dt><code>noinitrd</code></p>
<dd>This boot option disables the two-phase boot-up operation. The kernel performs the usual boot sequence as if <i>/dev/initrd</i> was not initialized. With this option, any contents of <i>/dev/initrd</i> loaded into memory by the boot loader contents are preserved. This option permits the contents of <i>/dev/initrd</i> to be any data and need not be limited to a filesystem image. However, device <i>/dev/initrd</i> is read-only and can be read only one time after system startup.</p>
<dt><code>root=</code><i>device-name</i></p>
<dd>Specifies the device to be used as the normal root filesystem. For <code>LOADLIN</code> this is a command-line option. For <code>LILO</code> this is a boot time option or can be used as an option line in the <code>LILO</code> configuration file <i>/etc/lilo.config</i>. The device specified by this option must be a mountable device having a suitable root filesystem.</dl>
<h3>Changing the normal root filesystem</h3>
<p>By default, the kernel&#8217;s settings (e.g., set in the kernel file with <code><a href="/docs/linux/man/8-rdev/">rdev</a></code>(8) or compiled into the kernel file), or the boot loader option setting is used for the normal root filesystems. For an NFS-mounted normal root filesystem, one has to use the <code>nfs_root_name</code> and <code>nfs_root_addrs</code> boot options to give the NFS settings. For more information on NFS-mounted root see the kernel documentation file <i>Documentation/filesystems/nfs/nfsroot.txt</i> (or <i>Documentation/filesystems/nfsroot.txt</i> before Linux 2.6.33). For more information on setting the root filesystem see also the <code>LILO</code> and <code>LOADLIN</code> documentation. </p>
<p> It is also possible for the <i>/linuxrc</i> executable to change the normal root device. For <i>/linuxrc</i> to change the normal root device, <i>/proc</i> must be mounted. After mounting <i>/proc</i>, <i>/linuxrc</i> changes the normal root device by writing into the proc files <i>/proc/sys/kernel/real-root-dev</i>, <i>/proc/sys/kernel/nfs-root-name</i>, and <i>/proc/sys/kernel/nfs-root-addrs</i>. For a physical root device, the root device is changed by having <i>/linuxrc</i> write the new root filesystem device number into <i>/proc/sys/kernel/real-root-dev</i>. For an NFS root filesystem, the root device is changed by having <i>/linuxrc</i> write the NFS setting into files <i>/proc/sys/kernel/nfs-root-name</i> and <i>/proc/sys/kernel/nfs-root-addrs</i> and then writing 0xff (e.g., the pseudo-NFS-device number) into file <i>/proc/sys/kernel/real-root-dev</i>. For example, the following shell command line would change the normal root device to <i>/dev/hdb1</i>: </p>
<p> echo 0x365 &gt;/proc/sys/kernel/real-root-dev </p>
<p> For an NFS example, the following shell command lines would change the normal root device to the NFS directory <i>/var/nfsroot</i> on a local networked NFS server with IP number 193.8.232.7 for a system with IP number 193.8.232.2 and named &quot;idefix&quot;: </p>
<p> echo /var/nfsroot &gt;/proc/sys/kernel/nfs-root-name echo 193.8.232.2:193.8.232.7::255.255.255.0:idefix \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;/proc/sys/kernel/nfs-root-addrs echo 255 &gt;/proc/sys/kernel/real-root-dev </p>
<p> <code>Note</code>: The use of <i>/proc/sys/kernel/real-root-dev</i> to change the root filesystem is obsolete. See the Linux kernel source file <i>Documentation/admin-guide/initrd.rst</i> (or <i>Documentation/initrd.txt</i> before Linux 4.10) as well as <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2) and <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8) for information on the modern method of changing the root filesystem.</p>
<h3>Usage</h3>
<p>The main motivation for implementing <code>initrd</code> was to allow for modular kernel configuration at system installation. </p>
<p> A possible system installation scenario is as follows:</p>
<dl>
<dt>1.</p>
<dd>The loader program boots from floppy or other media with a minimal kernel (e.g., support for <i>/dev/ram</i>, <i>/dev/initrd</i>, and the ext2 filesystem) and loads <i>/dev/initrd</i> with a gzipped version of the initial filesystem.</p>
<dt>2.</p>
<dd>The executable <i>/linuxrc</i> determines what is needed to (1) mount the normal root filesystem (i.e., device type, device drivers, filesystem) and (2) the distribution media (e.g., CD-ROM, network, tape, &#8230;). This can be done by asking the user, by auto-probing, or by using a hybrid approach.</p>
<dt>3.</p>
<dd>The executable <i>/linuxrc</i> loads the necessary modules from the initial root filesystem.</p>
<dt>4.</p>
<dd>The executable <i>/linuxrc</i> creates and populates the root filesystem. (At this stage the normal root filesystem does not have to be a completed system yet.)</p>
<dt>5.</p>
<dd>The executable <i>/linuxrc</i> sets <i>/proc/sys/kernel/real-root-dev</i>, unmounts <i>/proc</i>, the normal root filesystem and any other filesystems it has mounted, and then terminates.</p>
<dt>6.</p>
<dd>The kernel then mounts the normal root filesystem.</p>
<dt>7.</p>
<dd>Now that the filesystem is accessible and intact, the boot loader can be installed.</p>
<dt>8.</p>
<dd>The boot loader is configured to load into <i>/dev/initrd</i> a filesystem with the set of modules that was used to bring up the system. (e.g., device <i>/dev/ram0</i> can be modified, then unmounted, and finally, the image is written from <i>/dev/ram0</i> to a file.)</p>
<dt>9.</p>
<dd>The system is now bootable and additional installation tasks can be performed.</dl>
<p> The key role of <i>/dev/initrd</i> in the above is to reuse the configuration data during normal system operation without requiring initial kernel selection, a large generic kernel or, recompiling the kernel. </p>
<p> A second scenario is for installations where Linux runs on systems with different hardware configurations in a single administrative network. In such cases, it may be desirable to use only a small set of kernels (ideally only one) and to keep the system-specific part of configuration information as small as possible. In this case, create a common file with all needed modules. Then, only the <i>/linuxrc</i> file or a file executed by <i>/linuxrc</i> would be different. </p>
<p> A third scenario is more convenient recovery disks. Because information like the location of the root filesystem partition is not needed at boot time, the system loaded from <i>/dev/initrd</i> can use a dialog and/or auto-detection followed by a possible sanity check. </p>
<p> Last but not least, Linux distributions on CD-ROM may use <code>initrd</code> for easy installation from the CD-ROM. The distribution can use <code>LOADLIN</code> to directly load <i>/dev/initrd</i> from CD-ROM without the need of any floppies. The distribution could also use a <code>LILO</code> boot floppy and then bootstrap a bigger RAM disk via <i>/dev/initrd</i> from the CD-ROM.</p>
<h2>Files</h2>
<p><i>/dev/initrd</i><br />
 <i>/dev/ram0</i><br />
 <i>/linuxrc</i><br />
 <i>/initrd</i></p>
<h2>Notes</h2>
<dl>
<dt>1.</p>
<dd>With the current kernel, any filesystems that remain mounted when <i>/dev/ram0</i> is moved from <i>/</i> to <i>/initrd</i> continue to be accessible. However, the <i>/proc/mounts</i> entries are not updated.</p>
<dt>2.</p>
<dd>With the current kernel, if directory <i>/initrd</i> does not exist, then <i>/dev/ram0</i> will <code>not</code> be fully unmounted if <i>/dev/ram0</i> is used by any process or has any filesystem mounted on it. If <i>/dev/ram0</i> is <code>not</code> fully unmounted, then <i>/dev/ram0</i> will remain in memory.</p>
<dt>3.</p>
<dd>Users of <i>/dev/initrd</i> should not depend on the behavior given in the above notes. The behavior may change in future versions of the Linux kernel.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/4-ram/">ram</a></code>(4), <code><a href="/docs/linux/man/8-freeramdisk/">freeramdisk</a></code>(8), <code><a href="/docs/linux/man/8-rdev/">rdev</a></code>(8) </p>
<p> <i>Documentation/admin-guide/initrd.rst</i> (or <i>Documentation/initrd.txt</i> before Linux 4.10) in the Linux kernel source tree, the LILO documentation, the LOADLIN documentation, the SYSLINUX documentation</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
