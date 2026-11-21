---
title: "wipefs(8)"
name: "wipefs"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wipefs/"
description: "wipefs – wipe a signature from a device"
---
<p>wipefs &#8211; wipe a signature from a device </p>
<h2>SYNOPSIS</h2>
<p> <code>wipefs</code> [options] <i>device</i>... </p>
<p> <code>wipefs</code> [<code>--backup</code>] <code>-o</code> <i>offset device</i>... </p>
<p> <code>wipefs</code> [<code>--backup</code>] <code>-a</code> <i>device</i>...  </p>
<h2>DESCRIPTION</h2>
<p> <code>wipefs</code> can erase filesystem, raid or partition-table signatures (magic strings) from the specified <i>device</i> to make the signatures invisible for libblkid. <code>wipefs</code> does not erase the filesystem itself nor any other data from the device. </p>
<p>When used without any options, <code>wipefs</code> lists all visible filesystems and the offsets of their basic signatures. The default output is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using <code>--output</code> <i>columns-list</i> in environments where a stable output is required. </p>
<p> <code>wipefs</code> calls the BLKRRPART ioctl when it has erased a partition-table signature to inform the kernel about the change. The ioctl is called as the last step and when all specified signatures from all specified devices are already erased. This feature can be used to wipe content on partitions devices as well as partition table on a disk device, for example by <code>wipefs -a /dev/sdc1 /dev/sdc2 /dev/sdc</code>. </p>
<p>Note that some filesystems and some partition tables store more magic strings on the device (e.g., FAT, ZFS, GPT). The <code>wipefs</code> command (since v2.31) lists all the offset where a magic strings have been detected. </p>
<p>When option <code>-a</code> is used, all magic strings that are visible for <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3) are erased. In this case the <code>wipefs</code> scans the device again after each modification (erase) until no magic string is found. </p>
<p>Note that by default <code>wipefs</code> does not erase nested partition tables on non-whole disk devices. For this the option <code>--force</code> is required.  </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>--all</code> </p>
<dl>
<dd> <p> Erase all available signatures. The set of erased signatures can be restricted with the <code>-t</code> option. </p>
 </dd></dl>
<p> <code>-b</code>, <code>--backup</code> </p>
<dl>
<dd> <p> Create a signature backup to the file <i>$HOME/wipefs-&lt;devname&gt;-&lt;offset&gt;.bak</i>. For more details see the <code>EXAMPLE</code> section. </p>
 </dd></dl>
<p> <code>-f</code>, <code>--force</code> </p>
<dl>
<dd> <p> Force erasure, even if the filesystem is mounted. This is required in order to erase a partition-table signature on a block device. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<p> <code>-J</code>, <code>--json</code> </p>
<dl>
<dd> <p> Use JSON output format. </p>
 </dd></dl>
<p> <code>--lock</code>[=<i>mode</i>] </p>
<dl>
<dd> <p> Use exclusive BSD lock for device or file it operates. The optional argument <i>mode</i> can be <code>yes</code>, <code>no</code> (or 1 and 0) or <code>nonblock</code>. If the <i>mode</i> argument is omitted, it defaults to <code>&quot;yes&quot;</code>. This option overwrites environment variable <code>$LOCK_BLOCK_DEVICE</code>. The default is not to use any lock at all, but it&#8217;s recommended to avoid collisions with udevd or other tools. </p>
 </dd></dl>
<p> <code>-i</code>, <code>--noheadings</code> </p>
<dl>
<dd> <p> Do not print a header line. </p>
 </dd></dl>
<p> <code>-O</code>, <code>--output</code> <i>list</i> </p>
<dl>
<dd> <p> Specify which output columns to print. Use <code>--help</code> to get a list of all supported columns. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--no-act</code> </p>
<dl>
<dd> <p> Causes everything to be done except for the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) call. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--offset</code> <i>offset</i> </p>
<dl>
<dd> <p> Specify the location (in bytes) of the signature which should be erased from the device. The <i>offset</i> number may include a &quot;0x&quot; prefix; then the number will be interpreted as a hex value. It is possible to specify multiple <code>-o</code> options. </p>
<p>The <i>offset</i> argument may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;), or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
 </dd></dl>
<p> <code>-p</code>, <code>--parsable</code> </p>
<dl>
<dd> <p> Print out in parsable instead of printable format. Encode all potentially unsafe characters of a string to the corresponding hex value prefixed by &#8216;\x&#8217;. </p>
 </dd></dl>
<p> <code>-q</code>, <code>--quiet</code> </p>
<dl>
<dd> <p> Suppress any messages after a successful signature wipe. </p>
 </dd></dl>
<p> <code>-t</code>, <code>--types</code> <i>list</i> </p>
<dl>
<dd> <p> Limit the set of printed or erased signatures. More than one type may be specified in a comma-separated list. The list or individual types can be prefixed with &#8216;no&#8217; to specify the types on which no action should be taken. For more details see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p>LIBBLKID_DEBUG=all </p>
<dl>
<dd> <p> enables <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3) debug output. </p>
 </dd></dl>
<p>LOCK_BLOCK_DEVICE=&lt;mode&gt; </p>
<dl>
<dd> <p> use exclusive BSD lock. The mode is &quot;1&quot; or &quot;0&quot;. See <code>--lock</code> for more details. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> <code>wipefs /dev/sda</code>* </p>
<dl>
<dd> <p> Prints information about sda and all partitions on sda. </p>
 </dd></dl>
<p> <code>wipefs --all --backup /dev/sdb</code> </p>
<dl>
<dd> <p> Erases all signatures from the device <i>/dev/sdb</i> and creates a signature backup file <i>~/wipefs-sdb-&lt;offset&gt;.bak</i> for each signature. </p>
 </dd></dl>
<p> <code>dd if=~/wipefs-sdb-0x00000438.bak of=/dev/sdb seek=$0x00000438 bs=1 conv=notrunc</code> </p>
<dl>
<dd> <p> Restores an ext2 signature from the backup file <i>~/wipefs-sdb-0x00000438.bak</i>. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8), <code><a href="/docs/linux/man/8-findfs/">findfs</a></code>(8)  </p>
<h2>REPORTING BUGS</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p>The <code>wipefs</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">ENVIRONMENT</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">REPORTING BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">AVAILABILITY</a></dt>
<dd>  </dd></dl>
