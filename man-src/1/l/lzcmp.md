---
title: "lzcmp(1)"
name: "lzcmp"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lzcmp/"
description: "xzcmp, xzdiff, lzcmp, lzdiff – compare compressed files"
---

<h2 class="name">NAME</h2>
<p> xzcmp, xzdiff, lzcmp, lzdiff &#8211; compare compressed files </p>
<h2>SYNOPSIS</h2>
<p> <code>xzcmp</code> [<i>cmp_options</i>] <i>file1</i> [<i>file2</i>]<br />
 <code>xzdiff</code> [<i>diff_options</i>] <i>file1</i> [<i>file2</i>]<br />
 <code>lzcmp</code> [<i>cmp_options</i>] <i>file1</i> [<i>file2</i>]<br />
 <code>lzdiff</code> [<i>diff_options</i>] <i>file1</i> [<i>file2</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xzcmp</code> and <code>xzdiff</code> invoke <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1) or <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) on files compressed with <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1), <code><a href="/docs/linux/man/1-lzma/">lzma</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), or <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1). All options specified are passed directly to <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1) or <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1). If only one file is specified, then the files compared are <i>file1</i> (which must have a suffix of a supported compression format) and <i>file1</i> from which the compression format suffix has been stripped. If two files are specified, then they are uncompressed if necessary and fed to <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1) or <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1). The exit status from <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1) or <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) is preserved. </p>
<p> The names <code>lzcmp</code> and <code>lzdiff</code> are provided for backward compatibility with LZMA Utils.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1), <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1), <code><a href="/docs/linux/man/1-zdiff/">zdiff</a></code>(1)</p>
<h2>BUGS</h2>
<p> Messages from the <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1) or <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) programs refer to temporary filenames instead of those specified. </p>
<h2>Index</h2>
