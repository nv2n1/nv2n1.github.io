---
title: "sysfs(5)"
name: "sysfs"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sysfs/"
description: "sysfs – a filesystem for exporting kernel objects"
---

<p>sysfs &#8211; a filesystem for exporting kernel objects</p>
<h2>Description</h2>
<p>The <code>sysfs</code> filesystem is a pseudo-filesystem which provides an interface to kernel data structures. (More precisely, the files and directories in <code>sysfs</code> provide a view of the <i>kobject</i> structures defined internally within the kernel.) The files under <code>sysfs</code> provide information about devices, kernel modules, filesystems, and other kernel components. </p>
<p> The <code>sysfs</code> filesystem is commonly mounted at <i>/sys</i>. Typically, it is mounted automatically by the system, but it can also be mounted manually using a command such as: </p>
<p> mount -t sysfs sysfs /sys </p>
<p> Many of the files in the <code>sysfs</code> filesystem are read-only, but some files are writable, allowing kernel variables to be changed. To avoid redundancy, symbolic links are heavily used to connect entries across the filesystem tree.</p>
<h3>Files and directories</h3>
<p>The following list describes some of the files and directories under the <i>/sys</i> hierarchy.</p>
<dl>
<dt><i>/sys/block</i></p>
<dd>This subdirectory contains one symbolic link for each block device that has been discovered on the system. The symbolic links point to corresponding directories under <i>/sys/devices</i>.</p>
<dt><i>/sys/bus</i></p>
<dd>This directory contains one subdirectory for each of the bus types in the kernel. Inside each of these directories are two subdirectories:</p>
<dl>
<dd>
<dl>
<dt><i>devices</i></p>
<dd>This subdirectory contains symbolic links to entries in <i>/sys/devices</i> that correspond to the devices discovered on this bus.</p>
<dt><i>drivers</i></p>
<dd>This subdirectory contains one subdirectory for each device driver that is loaded on this bus.</dl>
</dl>
<dt><i>/sys/class</i></p>
<dd>This subdirectory contains a single layer of further subdirectories for each of the device classes that have been registered on the system (e.g., terminals, network devices, block devices, graphics devices, sound devices, and so on). Inside each of these subdirectories are symbolic links for each of the devices in this class. These symbolic links refer to entries in the <i>/sys/devices</i> directory.</p>
<dt><i>/sys/class/net</i></p>
<dd>Each of the entries in this directory is a symbolic link representing one of the real or virtual networking devices that are visible in the network namespace of the process that is accessing the directory. Each of these symbolic links refers to entries in the <i>/sys/devices</i> directory.</p>
<dt><i>/sys/dev</i></p>
<dd>This directory contains two subdirectories <i>block</i>/ and <i>char/</i>, corresponding, respectively, to the block and character devices on the system. Inside each of these subdirectories are symbolic links with names of the form <i>major-ID</i>:<i>minor-ID</i>, where the ID values correspond to the major and minor ID of a specific device. Each symbolic link points to the <code>sysfs</code> directory for a device. The symbolic links inside <i>/sys/dev</i> thus provide an easy way to look up the <code>sysfs</code> interface using the device IDs returned by a call to <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) (or similar).</p>
<dd>The following shell session shows an example from <i>/sys/dev</i>:</p>
<dd>$ <code>stat -c &quot;%t %T&quot; /dev/null</code> 1 3 $ <code>readlink /sys/dev/char/1\:3</code> ../../devices/virtual/mem/null $ <code>ls -Fd /sys/devices/virtual/mem/null</code> /sys/devices/virtual/mem/null/ $ <code>ls -d1 /sys/devices/virtual/mem/null/*</code> /sys/devices/virtual/mem/null/dev /sys/devices/virtual/mem/null/power/ /sys/devices/virtual/mem/null/subsystem@ /sys/devices/virtual/mem/null/uevent</p>
<dt><i>/sys/devices</i></p>
<dd>This is a directory that contains a filesystem representation of the kernel device tree, which is a hierarchy of <i>device</i> structures within the kernel.</p>
<dt><i>/sys/firmware</i></p>
<dd>This subdirectory contains interfaces for viewing and manipulating firmware-specific objects and attributes.</p>
<dt><i>/sys/fs</i></p>
<dd>This directory contains subdirectories for some filesystems. A filesystem will have a subdirectory here only if it chose to explicitly create the subdirectory.</p>
<dt><i>/sys/fs/cgroup</i></p>
<dd>This directory conventionally is used as a mount point for a <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) filesystem containing mount points for <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7) filesystems.</p>
<dt><i>/sys/fs/smackfs</i></p>
<dd>The directory contains configuration files for the SMACK LSM. See the kernel source file <i>Documentation/admin-guide/LSM/Smack.rst</i>.</p>
<dt><i>/sys/hypervisor</i></p>
<dd>[To be documented]</p>
<dt><i>/sys/kernel</i></p>
<dd>This subdirectory contains various files and subdirectories that provide information about the running kernel.</p>
<dt><i>/sys/kernel/cgroup/</i></p>
<dd>For information about the files in this directory, see <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7).</p>
<dt><i>/sys/kernel/debug/tracing</i></p>
<dd>Mount point for the <i>tracefs</i> filesystem used by the kernel&#8217;s <i>ftrace</i> facility. (For information on <i>ftrace</i>, see the kernel source file <i>Documentation/trace/ftrace.txt</i>.)</p>
<dt><i>/sys/kernel/mm</i></p>
<dd>This subdirectory contains various files and subdirectories that provide information about the kernel&#8217;s memory management subsystem.</p>
<dt><i>/sys/kernel/mm/hugepages</i></p>
<dd>This subdirectory contains one subdirectory for each of the huge page sizes that the system supports. The subdirectory name indicates the huge page size (e.g., <i>hugepages-2048kB</i>). Within each of these subdirectories is a set of files that can be used to view and (in some cases) change settings associated with that huge page size. For further information, see the kernel source file <i>Documentation/admin-guide/mm/hugetlbpage.rst</i>.</p>
<dt><i>/sys/module</i></p>
<dd>This subdirectory contains one subdirectory for each module that is loaded into the kernel. The name of each directory is the name of the module. In each of the subdirectories, there may be following files:</p>
<dl>
<dd>
<dl>
<dt><i>coresize</i></p>
<dd>[to be documented]</p>
<dt><i>initsize</i></p>
<dd>[to be documented]</p>
<dt><i>initstate</i></p>
<dd>[to be documented]</p>
<dt><i>refcnt</i></p>
<dd>[to be documented]</p>
<dt><i>srcversion</i></p>
<dd>[to be documented]</p>
<dt><i>taint</i></p>
<dd>[to be documented]</p>
<dt><i>uevent</i></p>
<dd>[to be documented]</p>
<dt><i>version</i></p>
<dd>[to be documented]</dl>
</dl>
<dd>In each of the subdirectories, there may be following subdirectories:</p>
<dl>
<dd>
<dl>
<dt><i>drivers</i></p>
<dd>[To be documented]</p>
<dt><i>holders</i></p>
<dd>[To be documented]</p>
<dt><i>notes</i></p>
<dd>[To be documented]</p>
<dt><i>parameters</i></p>
<dd>This directory contains one file for each module parameter, with each file containing the value of the corresponding parameter. Some of these files are writable, allowing the</p>
<dt><i>sections</i></p>
<dd>This subdirectories contains files with information about module sections. This information is mainly used for debugging.</p>
<dt><i>[To be documented]</i></p>
<dd></dl>
</dl>
<dt><i>/sys/power</i></p>
<dd>[To be documented]</dl>
<h2>Versions</h2>
<p>The <code>sysfs</code> filesystem first appeared in Linux 2.6.0.</p>
<h2>Conforming To</h2>
<p>The <code>sysfs</code> filesystem is Linux-specific.</p>
<h2>Notes</h2>
<p>This manual page is incomplete, possibly inaccurate, and is the kind of thing that needs to be updated very often.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) </p>
<p> P. Mochel. (2005). <i>The sysfs filesystem</i>. Proceedings of the 2005 Ottawa Linux Symposium. </p>
<p> The kernel source file <i>Documentation/filesystems/sysfs.txt</i> and various other files in <i>Documentation/ABI</i> and <i>Documentation/*/sysfs.txt</i></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
