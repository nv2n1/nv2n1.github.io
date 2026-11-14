---
title: "fstrim(8)"
name: "fstrim"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fstrim/"
description: "fstrim – discard unused blocks on a mounted filesystem"
---

<p>fstrim &#8211; discard unused blocks on a mounted filesystem</p>
<h2>Synopsis</h2>
<p><code>fstrim</code> [<code>-Aa</code>] [<code>-o</code> <i>offset</i>] [<code>-l</code> <i>length</i>] [<code>-m</code> <i>minimum-size</i>] [<code>-v</code> <i>mountpoint</i>]</p>
<h2>Description</h2>
<p><code>fstrim</code> is used on a mounted filesystem to discard (or &quot;trim&quot;) blocks which are not in use by the filesystem. This is useful for solid-state drives (SSDs) and thinly-provisioned storage. </p>
<p> By default, <code>fstrim</code> will discard all unused blocks in the filesystem. Options may be used to modify this behavior based on range or size, as explained below. </p>
<p> The <i>mountpoint</i> argument is the pathname of the directory where the filesystem is mounted. </p>
<p> Running <code>fstrim</code> frequently, or even using <code>mount -o discard</code>, might negatively affect the lifetime of poor-quality SSD devices. For most desktop and server systems a sufficient trimming frequency is once a week. Note that not all devices support a queued trim, so each trim command incurs a performance penalty on whatever else might be trying to use the disk at the time.</p>
<h2>Options</h2>
<p>The <i>offset</i>, <i>length</i>, and <i>minimum-size</i> arguments may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
<p> <code>-A, &#8211;fstab</code></p>
<dl>
<dd>Trim all mounted filesystems mentioned in <i>/etc/fstab</i> on devices that support the discard operation. The root filesystem is determined from kernel command line if missing in the file. The other supplied options, like <code>&#8211;offset</code>, <code>&#8211;length</code> and <code>&#8211;minimum</code>, are applied to all these devices. Errors from filesystems that do not support the discard operation, read-only devices and read-only filesystems are silently ignored.</dl>
<p> <code>-a, &#8211;all</code></p>
<dl>
<dd>Trim all mounted filesystems on devices that support the discard operation. The other supplied options, like <code>&#8211;offset</code>, <code>&#8211;length</code> and <code>&#8211;minimum</code>, are applied to all these devices. Errors from filesystems that do not support the discard operation, read-only devices and read-only filesystems are silently ignored.</dl>
<p> <code>-n, &#8211;dry-run</code></p>
<dl>
<dd>This option does everything apart from actually call <code>FITRIM</code> ioctl.</dl>
<p> <code>-o, &#8211;offset</code> <i>offset</i></p>
<dl>
<dd>Byte offset in the filesystem from which to begin searching for free blocks to discard. The default value is zero, starting at the beginning of the filesystem.</dl>
<p> <code>-l, &#8211;length</code> <i>length</i></p>
<dl>
<dd>The number of bytes (after the starting point) to search for free blocks to discard. If the specified value extends past the end of the filesystem, <code>fstrim</code> will stop at the filesystem size boundary. The default value extends to the end of the filesystem.</dl>
<p> <code>-I, &#8211;listed-in</code> <i>list</i></p>
<dl>
<dd>Specifies a colon-separated list of files in fstab or kernel mountinfo format. All missing or empty files are silently ignored. The evaluation of the <i>list</i> stops after first non-empty file. For example: </p>
<p> <code>&#8211;listed-in /etc/fstab:/proc/self/mountinfo</code>.</dl>
<p> <code>-m, &#8211;minimum</code> <i>minimum-size</i></p>
<dl>
<dd>Minimum contiguous free range to discard, in bytes. (This value is internally rounded up to a multiple of the filesystem block size.) Free ranges smaller than this will be ignored and fstrim will adjust the minimum if it&#8217;s smaller than the device&#8217;s minimum, and report that (fstrim_range.minlen) back to userspace. By increasing this value, the fstrim operation will complete more quickly for filesystems with badly fragmented freespace, although not all blocks will be discarded. The default value is zero, discarding every free block.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>Verbose execution. With this option <code>fstrim</code> will output the number of bytes passed from the filesystem down the block stack to the device for potential discard. This number is a maximum discard amount from the storage device&#8217;s perspective, because <i>FITRIM</i> ioctl called repeated will keep sending the same sectors for discard repeatedly. </p>
<p> <code>fstrim</code> will report the same potential discard bytes each time, but only sectors which had been written to between the discards would actually be discarded by the storage device. Further, the kernel block layer reserves the right to adjust the discard ranges to fit raid stripe geometry, non-trim capable devices in a LVM setup, etc. These reductions would not be reflected in fstrim_range.len (the <code>&#8211;length</code> option).</dl>
<p> <code>&#8211;quiet-unsupported</code></p>
<dl>
<dd>Suppress error messages if trim operation (ioctl) is unsupported. This option is meant to be used in systemd service file or in cron scripts to hide warnings that are result of known problems, such as NTFS driver reporting <i>Bad file descriptor</i> when device is mounted read-only, or lack of file system support for ioctl FITRIM call. This option also cleans exit status when unsupported filesystem specified on fstrim command line.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Exit Status</h2>
<p>0</p>
<dl>
<dd>success</dl>
<p> 1</p>
<dl>
<dd>failure</dl>
<p> 32</p>
<dl>
<dd>all failed</dl>
<p> 64</p>
<dl>
<dd>some filesystem discards have succeeded, some failed</dl>
<p> The command <code>fstrim &#8211;all</code> returns 0 (all succeeded), 32 (all failed) or 64 (some failed, some succeeded).</p>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-blkdiscard/">blkdiscard</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>fstrim</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
