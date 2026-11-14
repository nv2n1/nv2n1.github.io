---
title: "isosize(8)"
name: "isosize"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isosize/"
description: "isosize – output the length of an iso9660 filesystem"
---

<p>isosize &#8211; output the length of an iso9660 filesystem</p>
<h2>Synopsis</h2>
<p><code>isosize</code> [options] <i>iso9660_image_file</i></p>
<h2>Description</h2>
<p>This command outputs the length of an iso9660 filesystem that is contained in the specified file. This file may be a normal file or a block device (e.g. <i>/dev/hdd</i> or <i>/dev/sr0</i>). In the absence of any options (and errors), it will output the size of the iso9660 filesystem in bytes. This can now be a large number (&gt;&gt; 4 GB).</p>
<h2>Options</h2>
<p><code>-x</code>, <code>&#8211;sectors</code></p>
<dl>
<dd>Show the block count and block size in human-readable form. The output uses the term &quot;sectors&quot; for &quot;blocks&quot;.</dl>
<p> <code>-d</code>, <code>&#8211;divisor</code> <i>number</i></p>
<dl>
<dd>Only has an effect when <code>-x</code> is not given. The value shown (if no errors) is the iso9660 file size in bytes divided by <i>number</i>. So if <i>number</i> is the block size then the shown value will be the block count. </p>
<p> The size of the file (or block device) holding an iso9660 filesystem can be marginally larger than the actual size of the iso9660 filesystem. One reason for this is that cd writers are allowed to add &quot;run out&quot; sectors at the end of an iso9660 image.</dl>
<h2>Exit Status</h2>
<p><code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>1</code></p>
<dl>
<dd>generic failure, such as invalid usage</dl>
<p> <code>32</code></p>
<dl>
<dd>all failed</dl>
<p> <code>64</code></p>
<dl>
<dd>some failed</dl>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>isosize</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
