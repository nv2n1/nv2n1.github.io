---
title: "partx(8)"
name: "partx"
section: "8"
letter: "p"
url: "/docs/linux/man/8-partx/"
description: "partx – tell the kernel about the presence and numbering of on-disk partitions"
---

<p>partx &#8211; tell the kernel about the presence and numbering of on-disk partitions</p>
<h2>Synopsis</h2>
<p><code>partx</code> [<code>-a</code>|<code>-d</code>|<code>-P</code>|<code>-r</code>|<code>-s</code>|<code>-u</code>] [<code>-t</code> <i>type</i>] [<code>-n</code> <i>M</i>:_N_] [-] <i>disk</i> </p>
<p> <code>partx</code> [<code>-a</code>|<code>-d</code>|<code>-P</code>|<code>-r</code>|<code>-s</code>|<code>-u</code>] [<code>-t</code> <i>type</i>] <i>partition</i> [<i>disk</i>]</p>
<h2>Description</h2>
<p>Given a device or disk-image, <code>partx</code> tries to parse the partition table and list its contents. It can also tell the kernel to add or remove partitions from its bookkeeping. </p>
<p> The <i>disk</i> argument is optional when a <i>partition</i> argument is provided. To force scanning a partition as if it were a whole disk (for example to list nested subpartitions), use the argument &quot;-&quot; (hyphen-minus). For example:</p>
<dl>
<dd>partx &#8211;show &#8211; /dev/sda3
</dl>
<p> This will see sda3 as a whole-disk rather than as a partition. </p>
<p> <code>partx is not an fdisk program</code> &#8211; adding and removing partitions does not change the disk, it just tells the kernel about the presence and numbering of on-disk partitions.</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;add</code></p>
<dl>
<dd>Add the specified partitions, or read the disk and add all partitions.</dl>
<p> <code>-b</code>, <code>&#8211;bytes</code></p>
<dl>
<dd>Print the SIZE column in bytes rather than in human-readable format.</dl>
<p> <code>-d</code>, <code>&#8211;delete</code></p>
<dl>
<dd>Delete the specified partitions or all partitions. It is not error to remove non-existing partitions, so this option is possible to use together with large <code>&#8211;nr</code> ranges without care about the current partitions set on the device.</dl>
<p> <code>-g</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line with <code>&#8211;show</code> or <code>&#8211;raw</code>.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>List the partitions. Note that all numbers are in 512-byte sectors. This output format is DEPRECATED in favour of <code>&#8211;show</code>. Do not use it in newly written scripts.</dl>
<p> <code>-n</code>, <code>&#8211;nr</code> <i>M</i><code>:</code><i>N</i></p>
<dl>
<dd>Specify the range of partitions. For backward compatibility also the format <i>M</i><code>&#8211;</code><i>N</i> is supported. The range may contain negative numbers, for example <code>&#8211;nr -1:-1</code> means the last partition, and <code>&#8211;nr -2:-1</code> means the last two partitions. Supported range specifications are: </p>
<p> <i>M</i></p>
<dl>
<dd>Specifies just one partition (e.g. <code>&#8211;nr 3</code>).</dl>
<p> <i>M</i><code>:</code></p>
<dl>
<dd>Specifies the lower limit only (e.g. <code>&#8211;nr 2:</code>).</dl>
<p> <code>:</code><i>N</i></p>
<dl>
<dd>Specifies the upper limit only (e.g. <code>&#8211;nr :4</code>).</dl>
<p> <i>M</i><code>:</code><i>N</i></p>
<dl>
<dd>Specifies the lower and upper limits (e.g. <code>&#8211;nr 2:4</code>).</dl>
</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Define the output columns to use for <code>&#8211;show</code>, <code>&#8211;pairs</code> and <code>&#8211;raw</code> output. If no output arrangement is specified, then a default set is used. Use <code>&#8211;help</code> to get <i>list</i> of all supported columns. This option cannot be combined with the <code>&#8211;add</code>, <code>&#8211;delete</code>, <code>&#8211;update</code> or <code>&#8211;list</code> options.</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>-P</code>, <code>&#8211;pairs</code></p>
<dl>
<dd>List the partitions using the KEY=&quot;value&quot; format.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dd>List the partitions using the raw output format.</dl>
<p> <code>-s</code>, <code>&#8211;show</code></p>
<dl>
<dd>List the partitions. The output columns can be selected and rearranged with the <code>&#8211;output</code> option. All numbers (except SIZE) are in 512-byte sectors.</dl>
<p> <code>-t</code>, <code>&#8211;type</code> <i>type</i></p>
<dl>
<dd>Specify the partition table type.</dl>
<p> <code>&#8211;list-types</code></p>
<dl>
<dd>List supported partition types and exit.</dl>
<p> <code>-u</code>, <code>&#8211;update</code></p>
<dl>
<dd>Update the specified partitions.</dl>
<p> <code>-S</code>, <code>&#8211;sector-size</code> <i>size</i></p>
<dl>
<dd>Overwrite default sector size.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose mode.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Environment</h2>
<p>LIBBLKID_DEBUG=all</p>
<dl>
<dd>enables libblkid debug output.</dl>
<h2>Example</h2>
<p>partx &#8211;show /dev/sdb3, partx &#8211;show &#8211;nr 3 /dev/sdb, partx &#8211;show /dev/sdb3 /dev/sdb</p>
<dl>
<dd>All three commands list partition 3 of /dev/sdb.</dl>
<p> partx &#8211;show &#8211; /dev/sdb3</p>
<dl>
<dd>Lists all subpartitions on <i>/dev/sdb3</i> (the device is used as whole-disk).</dl>
<p> partx -o START -g &#8211;nr 5 /dev/sdb</p>
<dl>
<dd>Prints the start sector of partition 5 on <i>/dev/sdb</i> without header.</dl>
<p> partx -o SECTORS,SIZE /dev/sda5 /dev/sda</p>
<dl>
<dd>Lists the length in sectors and human-readable size of partition 5 on <i>/dev/sda</i>.</dl>
<p> partx &#8211;add &#8211;nr 3:5 /dev/sdd</p>
<dl>
<dd>Adds all available partitions from 3 to 5 (inclusive) on <i>/dev/sdd</i>.</dl>
<p> partx -d &#8211;nr :-1 /dev/sdd</p>
<dl>
<dd>Removes the last partition on <i>/dev/sdd</i>.</dl>
<h2>Authors</h2>
<p>The original version was written by</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-addpart/">addpart</a></code>(8), <code><a href="/docs/linux/man/8-delpart/">delpart</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-partprobe/">partprobe</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>partx</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
