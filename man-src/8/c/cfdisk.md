---
title: "cfdisk(8)"
name: "cfdisk"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfdisk/"
description: "cfdisk – display or manipulate a disk partition table"
---

<p>cfdisk &#8211; display or manipulate a disk partition table</p>
<h2>Synopsis</h2>
<p><code>cfdisk</code> [options] [<i>device</i>]</p>
<h2>Description</h2>
<p><code>cfdisk</code> is a curses-based program for partitioning any block device. The default device is <i>/dev/sda</i>. </p>
<p> Note that <code>cfdisk</code> provides basic partitioning functionality with a user-friendly interface. If you need advanced features, use <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) instead. </p>
<p> All disk label changes will remain in memory only, and the disk will be unmodified until you decide to write your changes. Be careful before using the write command. </p>
<p> Since version 2.25 <code>cfdisk</code> supports MBR (DOS), GPT, SUN and SGI disk labels, but no longer provides any functionality for CHS (Cylinder-Head-Sector) addressing. CHS has never been important for Linux, and this addressing concept does not make any sense for new devices. </p>
<p> Since version 2.25 <code>cfdisk</code> also does not provide a &#8216;print&#8217; command any more. This functionality is provided by the utilities <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8) and <code><a href="/docs/linux/man/8-lsblk/">lsblk</a></code>(8) in a very comfortable and rich way. </p>
<p> If you want to remove an old partition table from a device, use <code><a href="/docs/linux/man/8-wipefs/">wipefs</a></code>(8).</p>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-L</code>, <code>&#8211;color</code>[<code>=</code><i>when</i>]</p>
<dl>
<dd>Colorize the output. The optional argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. If the <i>when</i> argument is omitted, it defaults to <code>auto</code>. The colors can be disabled, for the current built-in default see <code>&#8211;help</code> output. See also the COLORS section.</dl>
<p> <code>&#8211;lock</code>[=<i>mode</i>]</p>
<dl>
<dd>Use exclusive BSD lock for device or file it operates. The optional argument <i>mode</i> can be <code>yes</code>, <code>no</code> (or 1 and 0) or <code>nonblock</code>. If the <i>mode</i> argument is omitted, it defaults to <code>&quot;yes&quot;</code>. This option overwrites environment variable <code>$LOCK_BLOCK_DEVICE</code>. The default is not to use any lock at all, but it&#8217;s recommended to avoid collisions with udevd or other tools.</dl>
<p> <code>-r</code>, <code>&#8211;read-only</code></p>
<dl>
<dd>Forced open in read-only mode.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-z</code>, <code>&#8211;zero</code></p>
<dl>
<dd>Start with an in-memory zeroed partition table. This option does not zero the partition table on the disk; rather, it simply starts the program without reading the existing partition table. This option allows you to create a new partition table from scratch or from an <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8)-compatible script.</dl>
<h2>Commands</h2>
<p>The commands for <code>cfdisk</code> can be entered by pressing the corresponding key (pressing <i>Enter</i> after the command is not necessary). Here is a list of the available commands: </p>
<p> <code>b</code></p>
<dl>
<dd>Toggle the bootable flag of the current partition. This allows you to select which primary partition is bootable on the drive. This command may not be available for all partition label types.</dl>
<p> <code>d</code></p>
<dl>
<dd>Delete the current partition. This will convert the current partition into free space and merge it with any free space immediately surrounding the current partition. A partition already marked as free space or marked as unusable cannot be deleted.</dl>
<p> <code>h</code></p>
<dl>
<dd>Show the help screen.</dl>
<p> <code>n</code></p>
<dl>
<dd>Create a new partition from free space. <code>cfdisk</code> then prompts you for the size of the partition you want to create. The default size is equal to the entire available free space at the current position. </p>
<p> The size may be followed by a multiplicative suffix: KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;).</dl>
<p> <code>q</code></p>
<dl>
<dd>Quit the program. This will exit the program without writing any data to the disk.</dl>
<p> <code>r</code></p>
<dl>
<dd>Reduce or enlarge the current partition. <code>cfdisk</code> then prompts you for the new size of the partition. The default size is the current size. A partition marked as free space or marked as unusable cannot be resized. </p>
<p> <code>Note that reducing the size of a partition might destroy data on that partition.</code></dl>
<p> <code>s</code></p>
<dl>
<dd>Sort the partitions in ascending start-sector order. When deleting and adding partitions, it is likely that the numbering of the partitions will no longer match their order on the disk. This command restores that match.</dl>
<p> <code>t</code></p>
<dl>
<dd>Change the partition type. By default, new partitions are created as <i>Linux</i> partitions.</dl>
<p> <code>u</code></p>
<dl>
<dd>Dump the current in-memory partition table to an sfdisk-compatible script file. </p>
<p> The script files are compatible between <code>cfdisk</code>, <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8) and other libfdisk applications. For more details see <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8). </p>
<p> It is also possible to load an sfdisk-script into <code>cfdisk</code> if there is no partition table on the device or when you start <code>cfdisk</code> with the <code>&#8211;zero</code> command-line option.</dl>
<p> <code>W</code></p>
<dl>
<dd>Write the partition table to disk (you must enter an uppercase W). Since this might destroy data on the disk, you must either confirm or deny the write by entering `yes&#8217; or `no&#8217;. If you enter `yes&#8217;, <code>cfdisk</code> will write the partition table to disk and then tell the kernel to re-read the partition table from the disk. </p>
<p> The re-reading of the partition table does not always work. In such a case you need to inform the kernel about any new partitions by using <code><a href="/docs/linux/man/8-partprobe/">partprobe</a></code>(8) or <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8), or by rebooting the system.</dl>
<p> <code>x</code></p>
<dl>
<dd>Toggle extra information about a partition.</dl>
<p> <i>Up Arrow</i>, <i>Down Arrow</i></p>
<dl>
<dd>Move the cursor to the previous or next partition. If there are more partitions than can be displayed on a screen, you can display the next (previous) set of partitions by moving down (up) at the last (first) partition displayed on the screen.</dl>
<p> <i>Left Arrow</i>, <i>Right Arrow</i></p>
<dl>
<dd>Select the preceding or the next menu item. Hitting <i>Enter</i> will execute the currently selected item.</dl>
<p> All commands can be entered with either uppercase or lowercase letters (except for <code>W</code>rite). When in a submenu or at a prompt, you can hit the <i>Esc</i> key to return to the main menu.</p>
<h2>Colors</h2>
<p>Implicit coloring can be disabled by creating the empty file <i>/etc/terminal-colors.d/cfdisk.disable</i>. </p>
<p> See <code><a href="/docs/linux/man/5-terminal-colors-d/">terminal-colors.d</a></code>(5) for more details about colorization configuration. </p>
<p> <code>cfdisk</code> does not support color customization with a color-scheme file.</p>
<h2>Environment</h2>
<p><code>CFDISK_DEBUG</code>=all</p>
<dl>
<dd>enables cfdisk debug output.</dl>
<p> <code>LIBFDISK_DEBUG</code>=all</p>
<dl>
<dd>enables libfdisk debug output.</dl>
<p> <code>LIBBLKID_DEBUG</code>=all</p>
<dl>
<dd>enables libblkid debug output.</dl>
<p> <code>LIBSMARTCOLS_DEBUG</code>=all</p>
<dl>
<dd>enables libsmartcols debug output.</dl>
<p> <code>LIBSMARTCOLS_DEBUG_PADDING</code>=on</p>
<dl>
<dd>use visible padding characters. Requires enabled <code>LIBSMARTCOLS_DEBUG</code>.</dl>
<p> <code>LOCK_BLOCK_DEVICE</code>=&lt;mode&gt;</p>
<dl>
<dd>use exclusive BSD lock. The mode is &quot;1&quot; or &quot;0&quot;. See <code>&#8211;lock</code> for more details.</dl>
<h2>Authors</h2>
<p>The current <code>cfdisk</code> implementation is based on the original <code>cfdisk</code> from</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-partprobe/">partprobe</a></code>(8), <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8), <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>cfdisk</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
