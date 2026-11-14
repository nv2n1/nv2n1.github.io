---
title: "debugreiserfs(8)"
name: "debugreiserfs"
section: "8"
letter: "d"
url: "/docs/linux/man/8-debugreiserfs/"
description: "debugreiserfs – The debugging tool for the ReiserFS filesystem."
---

<p>debugreiserfs &#8211; The debugging tool for the ReiserFS filesystem.</p>
<h2>Synopsis</h2>
<p><code>debugreiserfs</code> [ <code>-dDJmoqpuSV</code> ] [ <code>-j </code><i>device</i> ] [ <code>-B </code><i>file</i> ] [ <code>-1 </code><i>N</i> ] </p>
<p> <i>device</i></p>
<h2>Description</h2>
<p><code>debugreiserfs</code> sometimes helps to solve problems with reiserfs filesystems. When run without options it prints the super block of the ReiserFS filesystem found on the <i>device</i>.</p>
<dl>
<dt><i>device</i></p>
<dd>is the special file corresponding to the device (e.g /dev/hdXX for an IDE disk partition or /dev/sdXX for a SCSI disk partition).</dl>
<h2>Options</h2>
<dl>
<dt><code>-j</code> <i>device</i></p>
<dd>prints the contents of the journal. The option -p allows it to pack the journal with other metadata into the archive.</p>
<dt><code>-J</code></p>
<dd>prints the journal header.</p>
<dt><code>-d</code></p>
<dd>prints the formatted nodes of the internal tree of the filesystem.</p>
<dt><code>-D</code></p>
<dd>prints the formatted nodes of all used blocks of the filesystem.</p>
<dt><code>-m</code></p>
<dd>prints the contents of the bitmap (slightly useful).</p>
<dt><code>-o</code></p>
<dd>prints the objectid map (slightly useful).</p>
<dt><code>-B</code> <i>file</i></p>
<dd>takes the list of bad blocks stored in the internal ReiserFS tree and translates it into an ascii list written to the specified file.</p>
<dt><code>-1</code> <i>blocknumber</i></p>
<dd>prints the specified block of the filesystem.</p>
<dd><code>-p</code> extracts the filesystem&#8217;s metadata with <code>debugreiserfs</code> -p /dev/xxx | gzip -c &gt; xxx.gz. None of your data are packed unless a filesystem corruption presents when the whole block having this corruption is packed. You send us the output, and we use it to create a filesystem with the same strucure as yours using <code>debugreiserfs -u</code>. When the data file is not too large, this usually allows us to quickly reproduce and debug the problem.</p>
<dt><code>-u</code></p>
<dd>builds the ReiserFS filesystem image with gunzip -c xxx.gz | <code>debugreiserfs</code> -u /dev/image of the previously packed metadata with <code>debugreiserfs -p</code>. The result image is not the same as the original filesystem, because mostly only metadata were packed with <code>debugreiserfs -p</code>, but the filesystem structure is completely recreated.</p>
<dt><code>-S </code></p>
<dd>When -S is not specified -p deals with blocks marked used in the filesystem bitmap only. With this option set <code>debugreiserfs</code> will work with the entire device.</p>
<dt><code>-q</code></p>
<dd>When -p is in use, suppress showing the speed of progress.</dl>
<h2>Author</h2>
<p>This version of <code>debugreiserfs</code> has been written by Vitaly Fertman &lt;vitaly [at] namesys.com&gt;.</p>
<h2>Bugs</h2>
<p>Please report bugs to the ReiserFS developers &lt;reiserfs-devel [at] vger.kernel.org&gt;, providing as much information as possible&#8211;your hardware, kernel, patches, settings, all printed messages; check the syslog file for any related information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-reiserfsck/">reiserfsck</a></code>(8), <code><a href="/docs/linux/man/8-mkreiserfs/">mkreiserfs</a></code>(8) </p>
