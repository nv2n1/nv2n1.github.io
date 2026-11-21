---
title: "lsblk(8)"
name: "lsblk"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lsblk/"
description: "lsblk – list block devices"
---
<p>lsblk &#8211; list block devices </p>
<h2>SYNOPSIS</h2>
<p> <code>lsblk</code> [options] [<i>device</i>...]  </p>
<h2>DESCRIPTION</h2>
<p> <code>lsblk</code> lists information about all available or the specified block devices. The <code>lsblk</code> command reads the <code>sysfs</code> filesystem and <code>udev db</code> to gather information. If the udev db is not available or <code>lsblk</code> is compiled without udev support, then it tries to read LABELs, UUIDs and filesystem types from the block device. In this case root permissions are necessary. </p>
<p>The command prints all block devices (except RAM disks) in a tree-like format by default. Use <code>lsblk --help</code> to get a list of all available columns. </p>
<p>The default output, as well as the default output from options like <code>--fs</code> and <code>--topology</code>, is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using <code>--output</code> <i>columns-list</i> and <code>--list</code> in environments where a stable output is required. </p>
<p>Note that <code>lsblk</code> might be executed in time when <code>udev</code> does not have all information about recently added or modified devices yet. In this case it is recommended to use <code>udevadm settle</code> before <code>lsblk</code> to synchronize with udev. </p>
<p>The relationship between block devices and filesystems is not always one-to-one. The filesystem may use more block devices, or the same filesystem may be accessible by more paths. This is the reason why <code>lsblk</code> provides MOUNTPOINT and MOUNTPOINTS (pl.) columns. The column MOUNTPOINT displays only one mount point (usually the last mounted instance of the filesystem), and the column MOUNTPOINTS displays by multi-line cell all mount points associated with the device.  </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>--all</code> </p>
<dl>
<dd> <p> Also list empty devices and RAM disk devices. </p>
 </dd></dl>
<p> <code>-b</code>, <code>--bytes</code> </p>
<dl>
<dd> <p> Print the SIZE column in bytes rather than in a human-readable format. </p>
 </dd></dl>
<p> <code>-D</code>, <code>--discard</code> </p>
<dl>
<dd> <p> Print information about the discarding capabilities (TRIM, UNMAP) for each device. </p>
 </dd></dl>
<p> <code>-d</code>, <code>--nodeps</code> </p>
<dl>
<dd> <p> Do not print holder devices or slaves. For example, <code>lsblk --nodeps /dev/sda</code> prints information about the sda device only. </p>
 </dd></dl>
<p> <code>-E</code>, <code>--dedup</code> <i>column</i> </p>
<dl>
<dd> <p> Use <i>column</i> as a de-duplication key to de-duplicate output tree. If the key is not available for the device, or the device is a partition and parental whole-disk device provides the same key than the device is always printed. </p>
<p>The usual use case is to de-duplicate output on system multi-path devices, for example by <code>-E WWN</code>. </p>
 </dd></dl>
<p> <code>-e</code>, <code>--exclude</code> <i>list</i> </p>
<dl>
<dd> <p> Exclude the devices specified by the comma-separated <i>list</i> of major device numbers. Note that RAM disks (major=1) are excluded by default if <code>--all</code> is not specified. The filter is applied to the top-level devices only. This may be confusing for <code>--list</code> output format where hierarchy of the devices is not obvious. </p>
 </dd></dl>
<p> <code>-f</code>, <code>--fs</code> </p>
<dl>
<dd> <p> Output info about filesystems. This option is equivalent to <code>-o NAME,FSTYPE,FSVER,LABEL,UUID,FSAVAIL,FSUSE%,MOUNTPOINTS</code>. The authoritative information about filesystems and raids is provided by the <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8) command. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<p> <code>-I</code>, <code>--include</code> <i>list</i> </p>
<dl>
<dd> <p> Include devices specified by the comma-separated <i>list</i> of major device numbers. The filter is applied to the top-level devices only. This may be confusing for <code>--list</code> output format where hierarchy of the devices is not obvious. </p>
 </dd></dl>
<p> <code>-i</code>, <code>--ascii</code> </p>
<dl>
<dd> <p> Use ASCII characters for tree formatting. </p>
 </dd></dl>
<p> <code>-J</code>, <code>--json</code> </p>
<dl>
<dd> <p> Use JSON output format. It&#8217;s strongly recommended to use <code>--output</code> and also <code>--tree</code> if necessary. </p>
 </dd></dl>
<p> <code>-l</code>, <code>--list</code> </p>
<dl>
<dd> <p> Produce output in the form of a list. The output does not provide information about relationships between devices and since version 2.34 every device is printed only once if <code>--pairs</code> or <code>--raw</code> not specified (the parsable outputs are maintained in backwardly compatible way). </p>
 </dd></dl>
<p> <code>-M</code>, <code>--merge</code> </p>
<dl>
<dd> <p> Group parents of sub-trees to provide more readable output for RAIDs and Multi-path devices. The tree-like output is required. </p>
 </dd></dl>
<p> <code>-m</code>, <code>--perms</code> </p>
<dl>
<dd> <p> Output info about device owner, group and mode. This option is equivalent to <code>-o NAME,SIZE,OWNER,GROUP,MODE</code>. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--noheadings</code> </p>
<dl>
<dd> <p> Do not print a header line. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--output</code> <i>list</i> </p>
<dl>
<dd> <p> Specify which output columns to print. Use <code>--help</code> to get a list of all supported columns. The columns may affect tree-like output. The default is to use tree for the column &#8216;NAME&#8217; (see also <code>--tree</code>). </p>
<p>The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i> (e.g., <code>lsblk -o +UUID</code>). </p>
 </dd></dl>
<p> <code>-O</code>, <code>--output-all</code> </p>
<dl>
<dd> <p> Output all available columns. </p>
 </dd></dl>
<p> <code>-P</code>, <code>--pairs</code> </p>
<dl>
<dd> <p> Produce output in the form of key=&quot;value&quot; pairs. The output lines are still ordered by dependencies. All potentially unsafe value characters are hex-escaped (\x&lt;code&gt;). </p>
 </dd></dl>
<p> <code>-p</code>, <code>--paths</code> </p>
<dl>
<dd> <p> Print full device paths. </p>
 </dd></dl>
<p> <code>-r</code>, <code>--raw</code> </p>
<dl>
<dd> <p> Produce output in raw format. The output lines are still ordered by dependencies. All potentially unsafe characters are hex-escaped (\x&lt;code&gt;) in the NAME, KNAME, LABEL, PARTLABEL and MOUNTPOINT columns. </p>
 </dd></dl>
<p> <code>-S</code>, <code>--scsi</code> </p>
<dl>
<dd> <p> Output info about SCSI devices only. All partitions, slaves and holder devices are ignored. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--inverse</code> </p>
<dl>
<dd> <p> Print dependencies in inverse order. If the <code>--list</code> output is requested then the lines are still ordered by dependencies. </p>
 </dd></dl>
<p> <code>-T</code>, <code>--tree</code>[<code>=</code><i>column</i>] </p>
<dl>
<dd> <p> Force tree-like output format. If <i>column</i> is specified, then a tree is printed in the column. The default is NAME column. </p>
 </dd></dl>
<p> <code>-t</code>, <code>--topology</code> </p>
<dl>
<dd> <p> Output info about block-device topology. This option is equivalent to </p>
<p> <code>-o NAME,ALIGNMENT,MIN-IO,OPT-IO,PHY-SEC,LOG-SEC,ROTA,SCHED,RQ-SIZE,RA,WSAME</code>. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<p> <code>-w</code>, <code>--width</code> <i>number</i> </p>
<dl>
<dd> <p> Specifies output width as a number of characters. The default is the number of the terminal columns, and if not executed on a terminal, then output width is not restricted at all by default. This option also forces <code>lsblk</code> to assume that terminal control characters and unsafe characters are not allowed. The expected use-case is for example when <code>lsblk</code> is used by the <code><a href="/docs/linux/man/1-watch/">watch</a></code>(1) command. </p>
 </dd></dl>
<p> <code>-x</code>, <code>--sort</code> <i>column</i> </p>
<dl>
<dd> <p> Sort output lines by <i>column</i>. This option enables <code>--list</code> output format by default. It is possible to use the option <code>--tree</code> to force tree-like output and than the tree branches are sorted by the <i>column</i>. </p>
 </dd></dl>
<p> <code>-z</code>, <code>--zoned</code> </p>
<dl>
<dd> <p> Print the zone model for each device. </p>
 </dd></dl>
<p> <code>--sysroot</code> <i>directory</i> </p>
<dl>
<dd> <p> Gather data for a Linux instance other than the instance from which the <code>lsblk</code> command is issued. The specified directory is the system root of the Linux instance to be inspected. The real device nodes in the target directory can be replaced by text files with udev attributes. </p>
 </dd></dl>
<h2>EXIT STATUS</h2>
<p>0 </p>
<dl>
<dd> <p> success </p>
 </dd></dl>
<p>1 </p>
<dl>
<dd> <p> failure </p>
 </dd></dl>
<p>32 </p>
<dl>
<dd> <p> none of specified devices found </p>
 </dd></dl>
<p>64 </p>
<dl>
<dd> <p> some specified devices found, some not found </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p>LSBLK_DEBUG=all </p>
<dl>
<dd> <p> enables <code>lsblk</code> debug output. </p>
 </dd></dl>
<p>LIBBLKID_DEBUG=all </p>
<dl>
<dd> <p> enables <code>libblkid</code> debug output. </p>
 </dd></dl>
<p>LIBMOUNT_DEBUG=all </p>
<dl>
<dd> <p> enables <code>libmount</code> debug output. </p>
 </dd></dl>
<p>LIBSMARTCOLS_DEBUG=all </p>
<dl>
<dd> <p> enables <code>libsmartcols</code> debug output. </p>
 </dd></dl>
<p>LIBSMARTCOLS_DEBUG_PADDING=on </p>
<dl>
<dd> <p> use visible padding characters. </p>
 </dd></dl>
<h2>NOTES</h2>
<p>For partitions, some information (e.g., queue attributes) is inherited from the parent device. </p>
<p>The <code>lsblk</code> command needs to be able to look up each block device by major:minor numbers, which is done by using <i>/sys/dev/block</i>. This sysfs block directory appeared in kernel 2.6.27 (October 2008). In case of problems with a new enough kernel, check that CONFIG_SYSFS was enabled at the time of the kernel build.  </p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8), <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8)  </p>
<h2>REPORTING BUGS</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p>The <code>lsblk</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
