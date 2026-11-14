---
title: "xfs_fsr(8)"
name: "xfs_fsr"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_fsr/"
description: "xfs_fsr – filesystem reorganizer for XFS"
---

<p>xfs_fsr &#8211; filesystem reorganizer for XFS</p>
<h2>Synopsis</h2>
<pre><code>xfs_fsr</code> [<code>-vdg</code>] [<code>-t</code> seconds] [<code>-p</code> passes] [<code>-f</code> leftoff] [<code>-m</code> mtab]
<code>xfs_fsr</code> [<code>-vdg</code>] [xfsdev | file] ...
<br>
<code>xfs_fsr -V</code></pre>
<h2>Description</h2>
<p><i>xfs_fsr</i> is applicable only to XFS filesystems. <i>xfs_fsr</i> improves the organization of mounted filesystems. The reorganization algorithm operates on one file at a time, compacting or otherwise improving the layout of the file extents (contiguous blocks of file data). The following options are accepted by <i>xfs_fsr</i>. The <code>-m</code>, <code>-t</code>, and <code>-f</code> options have no meaning if any filesystems or files are specified on the command line.</p>
<dl>
<dt><code>-m</code><i> mtab</i></p>
<dd>Use this file for the list of filesystems to reorganize. The default is to use <i>/etc/mtab</i>.</p>
<dt><code>-t</code><i> seconds</i></p>
<dd>How long to reorganize. The default is 7200 seconds (2 hours).</p>
<dt><code>-p</code><i> passes</i></p>
<dd>Number of passes before terminating global re-org. The default is 10 passes.</p>
<dt><code>-f</code><i> leftoff</i></p>
<dd>Use this file instead of <i>/var/tmp/.fsrlast</i> to read the state of where to start and as the file to store the state of where reorganization left off.</p>
<dt><code>-v</code></p>
<dd>Verbose. Print cryptic information about each file being reorganized.</p>
<dt><code>-d</code></p>
<dd>Debug. Print even more cryptic information.</p>
<dt><code>-g</code></p>
<dd>Print to syslog (default if stdout not a tty).</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.  When invoked with no arguments <i>xfs_fsr</i> reorganizes all regular files in all mounted filesystems. <i>xfs_fsr</i> makes many cycles over <i>/etc/mtab</i> each time making a single pass over each XFS filesystem. Each pass goes through and selects files that have the largest number of extents. It attempts to defragment the top 10% of these files on each pass. It runs for up to two hours after which it records the filesystem where it left off, so it can start there the next time. This information is stored in the file <i>/var/tmp/.fsrlast_xfs.</i> If the information found here is somehow inconsistent or out of date it is ignored and reorganization starts at the beginning of the first filesystem found in <i>/etc/mtab</i>. <i>xfs_fsr</i> can be called with one or more arguments naming filesystems (block device name), and files to reorganize. In this mode <i>xfs_fsr</i> does not read or write <i>/var/tmp/.fsrlast_xfs</i> nor does it run for a fixed time interval. It makes one pass through each specified regular file and all regular files in each specified filesystem. A command line name referring to a symbolic link (except to a file system device), FIFO, or UNIX domain socket generates a warning message, but is otherwise ignored. While traversing the filesystem these types of files are silently skipped.</p>
<h2>Files</h2>
<dl>
<dt>/etc/mtab</p>
<dd>contains default list of filesystems to reorganize.</p>
<dt>/var/tmp/.fsrlast_xfs</p>
<dd>records the state where reorganization left off.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-xfs_fsr/">xfs_fsr</a>(8), <a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a>(8), <a href="/docs/linux/man/8-xfs_ncheck/">xfs_ncheck</a>(8), <a href="/docs/linux/man/5-xfs/">xfs</a>(5).</p>
<h2>Notes</h2>
<p><i>xfs_fsr</i> improves the layout of extents for each file by copying the entire file to a temporary location and then interchanging the data extents of the target and temporary files in an atomic manner. This method requires that enough free disk space be available to copy any given file and that the space be less fragmented than the original file. It also requires the owner of the file to have enough remaining filespace quota to do the copy on systems running quotas. <i>xfs_fsr</i> generates a warning message if space is not sufficient to improve the target file. A temporary file used in improving a file given on the command line is created in the same parent directory of the target file and is prefixed by the string &#8216;<code>.fsr</code>&#8216;. The temporary files used in improving an entire XFS device are stored in a directory at the root of the target device and use the same naming scheme. The temporary files are unlinked upon creation so data will not be readable by any other process. <i>xfs_fsr</i> does not operate on files that are currently mapped in memory. A &#8216;file busy&#8217; error can be seen for these files if the verbose flag (<code>-v</code>) is set. Files marked as no-defrag will be skipped. The <i><a href="/docs/linux/man/8-xfs_io/">xfs_io</a></i>(8) chattr command with the f attribute can be used to set or clear this flag. Files and directories created in a directory with the no-defrag flag will inherit the attribute. An entry in <i>/etc/mtab</i> or the file specified using the <code>-m</code> option must have the <code>rw</code> option specified for read and write access. If this option is not present, then <i>xfs_fsr</i> skips the filesystem described by that line. See the <i><a href="/docs/linux/man/5-fstab/">fstab</a></i>(5) reference page for more details. In general we do not foresee the need to run <i>xfs_fsr</i> on system partitions such as <i>/</i>, <i>/boot</i> and <i>/usr</i> as in general these will not suffer from fragmentation. There are also issues with defragmenting files <i><a href="/docs/linux/man/8-lilo/">lilo</a></i>(8) uses to boot your system. It is recommended that these files should be flagged as no-defrag with the <i><a href="/docs/linux/man/8-xfs_io/">xfs_io</a></i>(8) chattr command. Should these files be moved by <i>xfs_fsr</i> then you must rerun <i>lilo</i> before you reboot or you may have an unbootable system. </p>
