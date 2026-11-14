---
title: "zramctl(8)"
name: "zramctl"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zramctl/"
description: "zramctl – set up and control zram devices"
---

<p>zramctl &#8211; set up and control zram devices</p>
<h2>Synopsis</h2>
<p>Get info:</p>
<dl>
<dd><code>zramctl</code> [options]</dl>
<p> Reset zram:</p>
<dl>
<dd><code>zramctl</code> <code>-r</code> <i>zramdev</i>&#8230;</dl>
<p> Print name of first unused zram device:</p>
<dl>
<dd><code>zramctl</code> <code>-f</code></dl>
<p> Set up a zram device:</p>
<dl>
<dd><code>zramctl</code> [<code>-f</code> | <i>zramdev</i>] [<code>-s</code> <i>size</i>] [<code>-t</code> <i>number</i>] [<code>-a</code> <i>algorithm</i>]</dl>
<h2>Description</h2>
<p><code>zramctl</code> is used to quickly set up zram device parameters, to reset zram devices, and to query the status of used zram devices. </p>
<p> If no option is given, all non-zero size zram devices are shown. </p>
<p> Note that <i>zramdev</i> node specified on command line has to already exist. The command <code>zramctl</code> creates a new <i>/dev/zram&lt;N&gt;</i> nodes only when <code>&#8211;find</code> option specified. It&#8217;s possible (and common) that after system boot <i>/dev/zram&lt;N&gt;</i> nodes are not created yet.</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;algorithm lzo</code>|<code>lz4</code>|<code>lz4hc</code>|<code>deflate</code>|<code>842</code></p>
<dl>
<dd>Set the compression algorithm to be used for compressing data in the zram device.</dl>
<p> <code>-f</code>, <code>&#8211;find</code></p>
<dl>
<dd>Find the first unused zram device. If a <code>&#8211;size</code> argument is present, then initialize the device.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line in status output.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Define the status output columns to be used. If no output arrangement is specified, then a default set is used. Use <code>&#8211;help</code> to get a list of all supported columns.</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>&#8211;raw</code></p>
<dl>
<dd>Use the raw format for status output.</dl>
<p> <code>-r</code>, <code>&#8211;reset</code></p>
<dl>
<dd>Reset the options of the specified zram device(s). Zram device settings can be changed only after a reset.</dl>
<p> <code>-s</code>, <code>&#8211;size</code> <i>size</i></p>
<dl>
<dd>Create a zram device of the specified <i>size</i>. Zram devices are aligned to memory pages; when the requested <i>size</i> is not a multiple of the page size, it will be rounded up to the next multiple. When not otherwise specified, the unit of the <i>size</i> parameter is bytes. </p>
<p> The <i>size</i> argument may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB.</dl>
<p> <code>-t</code>, <code>&#8211;streams</code> <i>number</i></p>
<dl>
<dd>Set the maximum number of compression streams that can be used for the device. The default is use all CPUs and one stream for kernels older than 4.6.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Exit Status</h2>
<p><code>zramctl</code> returns 0 on success, nonzero on failure.</p>
<h2>Files</h2>
<p><i>/dev/zram[0..N]</i></p>
<dl>
<dd>zram block devices</dl>
<h2>Example</h2>
<p>The following commands set up a zram device with a size of one gigabyte and use it as swap device. </p>
<dl>
<dd>
<pre> # zramctl --find --size 1024M
 /dev/zram0
 # mkswap /dev/zram0
 # swapon /dev/zram0
 ...
 # swapoff /dev/zram0
 # zramctl --reset /dev/zram0</pre>
</dl>
<h2>Authors</h2>
<h2>See Also</h2>
<p><i>Linux kernel documentation</i> &lt;<a rel="nofollow" href="http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/Documentation/admin-guide/blockdev/zram.rst">http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/Documentation/admin-guide/blockdev/zram.rst</a>&gt;</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>zramctl</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
