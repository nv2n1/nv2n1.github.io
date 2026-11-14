---
title: "dump-f2fs(8)"
name: "dump-f2fs"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dump-f2fs/"
description: "dump.f2fs – retrieve directory and file entries from an F2FS-formated image"
---

<p>dump.f2fs &#8211; retrieve directory and file entries from an F2FS-formated image</p>
<h2>Synopsis</h2>
<p><code>dump.f2fs</code> [ <code>-i</code> <i>inode number</i> ] [ <code>-s</code> <i>SIT range</i> ] [ <code>-a</code> <i>SSA range</i> ] [ <code>-b</code> <i>block address</i> ] [ <code>-d</code> <i>debugging-level</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>dump.f2fs</code> is used to retrieve f2fs metadata (usually in a disk partition). <i>device</i> is the special file corresponding to the device (e.g. <i>/dev/sdXX</i>). </p>
<p> Currently, it can retrieve 1) a file given its inode number, 2) SIT entries into a file, 3) SSA entries into a file, 4) reverse information from the given block address. </p>
<p> The exit code returned by <code>dump.f2fs</code> is 0 on success and -1 on failure.</p>
<h2>Options</h2>
<dl>
<dt><code>-i</code><i> inode number</i></p>
<dd>Specify an inode number to dump out.</p>
<dt><code>-s</code><i> SIT range</i></p>
<dd>Specify a range presented by segment numbers to dump SIT entries.</p>
<dt><code>-a</code><i> SSA range</i></p>
<dd>Specify a range presented by segment numbers to dump SSA entries.</p>
<dt><code>-b</code><i> block address</i></p>
<dd>Specify a block address to retrieve its metadata information.</p>
<dt><code>-d</code><i> debug-level</i></p>
<dd>Specify the level of debugging options. The default number is 0, which shows basic debugging messages.</p>
<dt></dl>
<h2>Author</h2>
<dd>Initial checking code was written by Byoung Geun Kim &lt;bgbg.kim [at] samsung.com&gt;.</p>
<h2>Availability</h2>
<p><code>dump.f2fs</code> is available from <a href="git://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git.">git://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-f2fs/">mkfs.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-fsck-f2fs/">fsck.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-defrag-f2fs/">defrag.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-resize-f2fs/">resize.f2fs</a>(8),</code> <code><a href="/docs/linux/man/8-sload-f2fs/">sload.f2fs</a>(8).</code> </p>
