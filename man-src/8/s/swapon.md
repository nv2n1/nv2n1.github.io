---
title: "swapon(8)"
name: "swapon"
section: "8"
letter: "s"
url: "/docs/linux/man/8-swapon/"
description: "swapon, swapoff – enable/disable devices and files for paging and swapping"
---

<p>swapon, swapoff &#8211; enable/disable devices and files for paging and swapping</p>
<h2>Synopsis</h2>
<p><code>swapon</code> [options] [<i>specialfile</i>&#8230;] </p>
<p> <code>swapoff</code> [<code>-va</code>] [<i>specialfile</i>&#8230;]</p>
<h2>Description</h2>
<p><code>swapon</code> is used to specify devices on which paging and swapping are to take place. </p>
<p> The device or file used is given by the <i>specialfile</i> parameter. It may be of the form <code>-L</code> <i>label</i> or <code>-U</code> <i>uuid</i> to indicate a device by label or uuid. </p>
<p> Calls to <code>swapon</code> normally occur in the system boot scripts making all swap devices available, so that the paging and swapping activity is interleaved across several devices and files. </p>
<p> <code>swapoff</code> disables swapping on the specified devices and files. When the <code>-a</code> flag is given, swapping is disabled on all known swap devices and files (as found in <i>/proc/swaps</i> or <i>/etc/fstab</i>).</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>All devices marked as &quot;swap&quot; in <i>/etc/fstab</i> are made available, except for those with the &quot;noauto&quot; option. Devices that are already being used as swap are silently skipped.</dl>
<p> <code>-d</code>, <code>&#8211;discard</code>[<code>=</code><i>policy</i>]</p>
<dl>
<dd>Enable swap discards, if the swap backing device supports the discard or trim operation. This may improve performance on some Solid State Devices, but often it does not. The option allows one to select between two available swap discard policies: </p>
<p> <code>&#8211;discard=once</code></p>
<dl>
<dd>to perform a single-time discard operation for the whole swap area at swapon; or</dl>
<p> <code>&#8211;discard=pages</code></p>
<dl>
<dd>to asynchronously discard freed swap pages before they are available for reuse.</dl>
<p> If no policy is selected, the default behavior is to enable both discard types. The <i>/etc/fstab</i> mount options <code>discard</code>, <code>discard=once</code>, or <code>discard=pages</code> may also be used to enable discard flags.</dl>
<p> <code>-e</code>, <code>&#8211;ifexists</code></p>
<dl>
<dd>Silently skip devices that do not exist. The <i>/etc/fstab</i> mount option <code>nofail</code> may also be used to skip non-existing device.</dl>
<p> <code>-f</code>, <code>&#8211;fixpgsz</code></p>
<dl>
<dd>Reinitialize (exec mkswap) the swap space if its page size does not match that of the current running kernel. <code><a href="/docs/linux/man/8-mkswap/">mkswap</a></code>(8) initializes the whole device and does not check for bad blocks.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-L</code> <i>label</i></p>
<dl>
<dd>Use the partition that has the specified <i>label</i>. (For this, access to <i>/proc/partitions</i> is needed.)</dl>
<p> <code>-o</code>, <code>&#8211;options</code> <i>opts</i></p>
<dl>
<dd>Specify swap options by an fstab-compatible comma-separated string. For example: </p>
<p> <code>swapon -o pri=1,discard=pages,nofail /dev/sda2</code> </p>
<p> The <i>opts</i> string is evaluated last and overrides all other command line options.</dl>
<p> <code>-p</code>, <code>&#8211;priority</code> <i>priority</i></p>
<dl>
<dd>Specify the priority of the swap device. <i>priority</i> is a value between -1 and 32767. Higher numbers indicate higher priority. See <code><a href="/docs/linux/man/2-swapon/">swapon</a></code>(2) for a full description of swap priorities. Add <code>pri=</code><i>value</i> to the option field of <i>/etc/fstab</i> for use with <code>swapon -a</code>. When no priority is defined, it defaults to -1.</dl>
<p> <code>-s</code>, <code>&#8211;summary</code></p>
<dl>
<dd>Display swap usage summary by device. Equivalent to <code>cat /proc/swaps</code>. This output format is DEPRECATED in favour of <code>&#8211;show</code> that provides better control on output data.</dl>
<p> <code>&#8211;show</code>[<code>=</code><i>column</i>&#8230;]</p>
<dl>
<dd>Display a definable table of swap areas. See the <code>&#8211;help</code> output for a list of available columns.</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print headings when displaying <code>&#8211;show</code> output.</dl>
<p> <code>&#8211;raw</code></p>
<dl>
<dd>Display <code>&#8211;show</code> output without aligning table columns.</dl>
<p> <code>&#8211;bytes</code></p>
<dl>
<dd>Display swap size in bytes in <code>&#8211;show</code> output instead of in user-friendly units.</dl>
<p> <code>-U</code> <i>uuid</i></p>
<dl>
<dd>Use the partition that has the specified <i>uuid</i>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Be verbose.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Exit Status</h2>
<p><code>swapoff</code> has the following exit status values since v2.36: </p>
<p> <code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>2</code></p>
<dl>
<dd>system has insufficient memory to stop swapping (OOM)</dl>
<p> <code>4</code></p>
<dl>
<dd>swapoff syscall failed for another reason</dl>
<p> <code>8</code></p>
<dl>
<dd>non-swapoff syscall system error (out of memory, &#8230;)</dl>
<p> <code>16</code></p>
<dl>
<dd>usage or syntax error</dl>
<p> <code>32</code></p>
<dl>
<dd>all swapoff failed on <code>&#8211;all</code></dl>
<p> <code>64</code></p>
<dl>
<dd>some swapoff succeeded on <code>&#8211;all</code></dl>
<p> The command <code>swapoff &#8211;all</code> returns 0 (all succeeded), 32 (all failed), or 64 (some failed, some succeeded). </p>
<p> + The old versions before v2.36 has no documented exit status, 0 means success in all versions.</p>
<h2>Environment</h2>
<p>LIBMOUNT_DEBUG=all</p>
<dl>
<dd>enables <code>libmount</code> debug output.</dl>
<p> LIBBLKID_DEBUG=all</p>
<dl>
<dd>enables <code>libblkid</code> debug output.</dl>
<h2>Files</h2>
<p><i>/dev/sd??</i></p>
<dl>
<dd>standard paging devices</dl>
<p> <i>/etc/fstab</i></p>
<dl>
<dd>ascii filesystem description table</dl>
<h2>Notes</h2>
<h3>Files with holes</h3>
<p>The swap file implementation in the kernel expects to be able to write to the file directly, without the assistance of the filesystem. This is a problem on files with holes or on copy-on-write files on filesystems like Btrfs. </p>
<p> Commands like <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) or <code><a href="/docs/linux/man/1-truncate/">truncate</a></code>(1) create files with holes. These files will be rejected by <code>swapon</code>. </p>
<p> Preallocated files created by <code><a href="/docs/linux/man/1-fallocate/">fallocate</a></code>(1) may be interpreted as files with holes too depending of the filesystem. Preallocated swap files are supported on XFS since Linux 4.18. </p>
<p> The most portable solution to create a swap file is to use <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1) and <i>/dev/zero</i>.</p>
<h3>Btrfs</h3>
<p>Swap files on Btrfs are supported since Linux 5.0 on files with nocow attribute. See the <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5) manual page for more details.</p>
<h3>Nfs</h3>
<p>Swap over <code>NFS</code> may not work.</p>
<h3>Suspend</h3>
<p><code>swapon</code> automatically detects and rewrites a swap space signature with old software suspend data (e.g., S1SUSPEND, S2SUSPEND, &#8230;). The problem is that if we don&#8217;t do it, then we get data corruption the next time an attempt at unsuspending is made.</p>
<h2>History</h2>
<p>The <code>swapon</code> command appeared in 4.0BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-swapoff/">swapoff</a></code>(2), <code><a href="/docs/linux/man/2-swapon/">swapon</a></code>(2), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/1-fallocate/">fallocate</a></code>(1), <code><a href="/docs/linux/man/8-mkswap/">mkswap</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-rc/">rc</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>swapon</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
