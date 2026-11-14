---
title: "fsck(8)"
name: "fsck"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck/"
description: "fsck – check and repair a Linux filesystem"
---

<p>fsck &#8211; check and repair a Linux filesystem</p>
<h2>Synopsis</h2>
<p><code>fsck</code> [<code>-lsAVRTMNP</code>] [<code>-r</code> [<i>fd</i>]] [<code>-C</code> [<i>fd</i>]] [<code>-t</code> <i>fstype</i>] [<i>filesystem</i>&#8230;] [<code>&#8212;</code>] [<i>fs-specific-options</i>]</p>
<h2>Description</h2>
<p><code>fsck</code> is used to check and optionally repair one or more Linux filesystems. <i>filesystem</i> can be a device name (e.g., <i>/dev/hdc1</i>, <i>/dev/sdb2</i>), a mount point (e.g., <i>/</i>, <i>/usr</i>, <i>/home</i>), or an filesystem label or UUID specifier (e.g., UUID=8868abf6-88c5-4a83-98b8-bfc24057f7bd or LABEL=root). Normally, the <code>fsck</code> program will try to handle filesystems on different physical disk drives in parallel to reduce the total amount of time needed to check all of them. </p>
<p> If no filesystems are specified on the command line, and the <code>-A</code> option is not specified, <code>fsck</code> will default to checking filesystems in <i>/etc/fstab</i> serially. This is equivalent to the <code>-As</code> options. </p>
<p> The exit status returned by <code>fsck</code> is the sum of the following conditions: </p>
<p> <code>0</code></p>
<dl>
<dd>No errors</dl>
<p> <code>1</code></p>
<dl>
<dd>Filesystem errors corrected</dl>
<p> <code>2</code></p>
<dl>
<dd>System should be rebooted</dl>
<p> <code>4</code></p>
<dl>
<dd>Filesystem errors left uncorrected</dl>
<p> <code>8</code></p>
<dl>
<dd>Operational error</dl>
<p> <code>16</code></p>
<dl>
<dd>Usage or syntax error</dl>
<p> <code>32</code></p>
<dl>
<dd>Checking canceled by user request</dl>
<p> <code>128</code></p>
<dl>
<dd>Shared-library error</dl>
<p> The exit status returned when multiple filesystems are checked is the bit-wise OR of the exit statuses for each filesystem that is checked. </p>
<p> In actuality, <code>fsck</code> is simply a front-end for the various filesystem checkers (<code>fsck</code>.<i>fstype</i>) available under Linux. The filesystem-specific checker is searched for in the <code>PATH</code> environment variable. If the <code>PATH</code> is undefined then fallback to <i>/sbin</i>. </p>
<p> Please see the filesystem-specific checker manual pages for further details.</p>
<h2>Options</h2>
<p><code>-l</code></p>
<dl>
<dd>Create an exclusive <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) lock file (<i>/run/fsck/&lt;diskname&gt;.lock</i>) for whole-disk device. This option can be used with one device only (this means that <code>-A</code> and <code>-l</code> are mutually exclusive). This option is recommended when more <code>fsck</code> instances are executed in the same time. The option is ignored when used for multiple devices or for non-rotating disks. <code>fsck</code> does not lock underlying devices when executed to check stacked devices (e.g. MD or DM) &#8211; this feature is not implemented yet.</dl>
<p> <code>-r</code> [<i>fd</i>]</p>
<dl>
<dd>Report certain statistics for each fsck when it completes. These statistics include the exit status, the maximum run set size (in kilobytes), the elapsed all-clock time and the user and system CPU time used by the fsck run. For example: </p>
<p> <code>/dev/sda1: status 0, rss 92828, real 4.002804, user 2.677592, sys 0.86186</code> </p>
<p> GUI front-ends may specify a file descriptor <i>fd</i>, in which case the progress bar information will be sent to that file descriptor in a machine parsable format. For example: </p>
<p> <code>/dev/sda1 0 92828 4.002804 2.677592 0.86186</code></dl>
<p> <code>-s</code></p>
<dl>
<dd>Serialize <code>fsck</code> operations. This is a good idea if you are checking multiple filesystems and the checkers are in an interactive mode. (Note: <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) runs in an interactive mode by default. To make <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) run in a non-interactive mode, you must either specify the <code>-p</code> or <code>-a</code> option, if you wish for errors to be corrected automatically, or the <code>-n</code> option if you do not.)</dl>
<p> <code>-t</code> <i>fslist</i></p>
<dl>
<dd>Specifies the type(s) of filesystem to be checked. When the <code>-A</code> flag is specified, only filesystems that match <i>fslist</i> are checked. The <i>fslist</i> parameter is a comma-separated list of filesystems and options specifiers. All of the filesystems in this comma-separated list may be prefixed by a negation operator &#8216;<code>no</code>&#8216; or &#8216;<code>!</code>&#8216;, which requests that only those filesystems not listed in <i>fslist</i> will be checked. If none of the filesystems in <i>fslist</i> is prefixed by a negation operator, then only those listed filesystems will be checked. </p>
<p> Options specifiers may be included in the comma-separated <i>fslist</i>. They must have the format <code>opts=</code><i>fs-option</i>. If an options specifier is present, then only filesystems which contain <i>fs-option</i> in their mount options field of <i>/etc/fstab</i> will be checked. If the options specifier is prefixed by a negation operator, then only those filesystems that do not have <i>fs-option</i> in their mount options field of <i>/etc/fstab</i> will be checked. </p>
<p> For example, if <code>opts=ro</code> appears in <i>fslist</i>, then only filesystems listed in <i>/etc/fstab</i> with the <code>ro</code> option will be checked. </p>
<p> For compatibility with Mandrake distributions whose boot scripts depend upon an unauthorized UI change to the <code>fsck</code> program, if a filesystem type of <code>loop</code> is found in <i>fslist</i>, it is treated as if <code>opts=loop</code> were specified as an argument to the <code>-t</code> option. </p>
<p> Normally, the filesystem type is deduced by searching for <i>filesys</i> in the <i>/etc/fstab</i> file and using the corresponding entry. If the type cannot be deduced, and there is only a single filesystem given as an argument to the <code>-t</code> option, <code>fsck</code> will use the specified filesystem type. If this type is not available, then the default filesystem type (currently ext2) is used.</dl>
<p> <code>-A</code></p>
<dl>
<dd>Walk through the <i>/etc/fstab</i> file and try to check all filesystems in one run. This option is typically used from the <i>/etc/rc</i> system initialization file, instead of multiple commands for checking a single filesystem. </p>
<p> The root filesystem will be checked first unless the <code>-P</code> option is specified (see below). After that, filesystems will be checked in the order specified by the <i>fs_passno</i> (the sixth) field in the <i>/etc/fstab</i> file. Filesystems with a <i>fs_passno</i> value of 0 are skipped and are not checked at all. Filesystems with a <i>fs_passno</i> value of greater than zero will be checked in order, with filesystems with the lowest <i>fs_passno</i> number being checked first. If there are multiple filesystems with the same pass number, <code>fsck</code> will attempt to check them in parallel, although it will avoid running multiple filesystem checks on the same physical disk. </p>
<p> <code>fsck</code> does not check stacked devices (RAIDs, dm-crypt, &#8230;) in parallel with any other device. See below for <code>FSCK_FORCE_ALL_PARALLEL</code> setting. The <i>/sys</i> filesystem is used to determine dependencies between devices. </p>
<p> Hence, a very common configuration in <i>/etc/fstab</i> files is to set the root filesystem to have a <i>fs_passno</i> value of 1 and to set all other filesystems to have a <i>fs_passno</i> value of 2. This will allow <code>fsck</code> to automatically run filesystem checkers in parallel if it is advantageous to do so. System administrators might choose not to use this configuration if they need to avoid multiple filesystem checks running in parallel for some reason &#8211; for example, if the machine in question is short on memory so that excessive paging is a concern. </p>
<p> <code>fsck</code> normally does not check whether the device actually exists before calling a filesystem specific checker. Therefore non-existing devices may cause the system to enter filesystem repair mode during boot if the filesystem specific checker returns a fatal error. The <i>/etc/fstab</i> mount option <code>nofail</code> may be used to have <code>fsck</code> skip non-existing devices. <code>fsck</code> also skips non-existing devices that have the special filesystem type <code>auto</code>.</dl>
<p> <code>-C</code> [<i>fd</i>]</p>
<dl>
<dd>Display completion/progress bars for those filesystem checkers (currently only for ext[234]) which support them. <code>fsck</code> will manage the filesystem checkers so that only one of them will display a progress bar at a time. GUI front-ends may specify a file descriptor <i>fd</i>, in which case the progress bar information will be sent to that file descriptor.</dl>
<p> <code>-M</code></p>
<dl>
<dd>Do not check mounted filesystems and return an exit status of 0 for mounted filesystems.</dl>
<p> <code>-N</code></p>
<dl>
<dd>Don&#8217;t execute, just show what would be done.</dl>
<p> <code>-P</code></p>
<dl>
<dd>When the <code>-A</code> flag is set, check the root filesystem in parallel with the other filesystems. This is not the safest thing in the world to do, since if the root filesystem is in doubt things like the <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) executable might be corrupted! This option is mainly provided for those sysadmins who don&#8217;t want to repartition the root filesystem to be small and compact (which is really the right solution).</dl>
<p> <code>-R</code></p>
<dl>
<dd>When checking all filesystems with the <code>-A</code> flag, skip the root filesystem. (This is useful in case the root filesystem has already been mounted read-write.)</dl>
<p> <code>-T</code></p>
<dl>
<dd>Don&#8217;t show the title on startup.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Produce verbose output, including all filesystem-specific commands that are executed.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Filesystem Specific Options</h2>
<p><code>Options which are not understood by fsck are passed to the filesystem-specific checker!</code> </p>
<p> These options <code>must</code> not take arguments, as there is no way for <code>fsck</code> to be able to properly guess which options take arguments and which don&#8217;t. </p>
<p> Options and arguments which follow the <code>&#8212;</code> are treated as filesystem-specific options to be passed to the filesystem-specific checker. </p>
<p> Please note that <code>fsck</code> is not designed to pass arbitrarily complicated options to filesystem-specific checkers. If you&#8217;re doing something complicated, please just execute the filesystem-specific checker directly. If you pass <code>fsck</code> some horribly complicated options and arguments, and it doesn&#8217;t do what you expect, <code>don&#8217;t bother reporting it as a bug.</code> You&#8217;re almost certainly doing something that you shouldn&#8217;t be doing with <code>fsck</code>. Options to different filesystem-specific fsck&#8217;s are not standardized.</p>
<h2>Environment</h2>
<p>The <code>fsck</code> program&#8217;s behavior is affected by the following environment variables: </p>
<p> <code>FSCK_FORCE_ALL_PARALLEL</code></p>
<dl>
<dd>If this environment variable is set, <code>fsck</code> will attempt to check all of the specified filesystems in parallel, regardless of whether the filesystems appear to be on the same device. (This is useful for RAID systems or high-end storage systems such as those sold by companies such as IBM or EMC.) Note that the <i>fs_passno</i> value is still used.</dl>
<p> <code>FSCK_MAX_INST</code></p>
<dl>
<dd>This environment variable will limit the maximum number of filesystem checkers that can be running at one time. This allows configurations which have a large number of disks to avoid <code>fsck</code> starting too many filesystem checkers at once, which might overload CPU and memory resources available on the system. If this value is zero, then an unlimited number of processes can be spawned. This is currently the default, but future versions of <code>fsck</code> may attempt to automatically determine how many filesystem checks can be run based on gathering accounting data from the operating system.</dl>
<p> <code>PATH</code></p>
<dl>
<dd>The <code>PATH</code> environment variable is used to find filesystem checkers.</dl>
<p> <code>FSTAB_FILE</code></p>
<dl>
<dd>This environment variable allows the system administrator to override the standard location of the <i>/etc/fstab</i> file. It is also useful for developers who are testing <code>fsck</code>.</dl>
<p> <code>LIBBLKID_DEBUG=all</code></p>
<dl>
<dd>enables libblkid debug output.</dl>
<p> <code>LIBMOUNT_DEBUG=all</code></p>
<dl>
<dd>enables libmount debug output.</dl>
<h2>Files</h2>
<p><i>/etc/fstab</i></p>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-ext2/">fsck.ext2</a></code>(8) or <code><a href="/docs/linux/man/8-fsck-ext3/">fsck.ext3</a></code>(8) or <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-fsck-cramfs/">fsck.cramfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-jfs/">fsck.jfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-nfs/">fsck.nfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-minix/">fsck.minix</a></code>(8), <code><a href="/docs/linux/man/8-fsck-msdos/">fsck.msdos</a></code>(8), <code><a href="/docs/linux/man/8-fsck-vfat/">fsck.vfat</a></code>(8), <code><a href="/docs/linux/man/8-fsck-xfs/">fsck.xfs</a></code>(8), <code><a href="/docs/linux/man/8-reiserfsck/">reiserfsck</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>fsck</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
