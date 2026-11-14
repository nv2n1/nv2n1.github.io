---
title: "bzdiff(1)"
name: "bzdiff"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bzdiff/"
description: "bzcmp, bzdiff – compare bzip2 compressed files"
---

<h2 class="name">NAME</h2>
<p> bzcmp, bzdiff &#8211; compare bzip2 compressed files </p>
<h2>SYNOPSIS</h2>
<p> <code>bzcmp</code> [ cmp_options ] file1 [ file2 ]<br />
 <code>bzdiff</code> [ diff_options ] file1 [ file2 ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Bzcmp</i> and <i>bzdiff</i> are used to invoke the <i>cmp</i> or the <i>diff</i> program on bzip2 compressed files. All options specified are passed directly to <i>cmp</i> or <i>diff</i>. If only 1 file is specified, then the files compared are <i>file1</i> and an uncompressed <i>file1</i>.bz2. If two files are specified, then they are uncompressed if necessary and fed to <i>cmp</i> or <i>diff</i>. The exit status from <i>cmp</i> or <i>diff</i> is preserved.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cmp/">cmp</a>(1), <a href="/docs/linux/man/1-diff/">diff</a>(1), <a href="/docs/linux/man/1-bzmore/">bzmore</a>(1), <a href="/docs/linux/man/1-bzless/">bzless</a>(1), <a href="/docs/linux/man/1-bzgrep/">bzgrep</a>(1), <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1)</p>
<h2>BUGS</h2>
<p> Messages from the <i>cmp</i> or <i>diff</i> programs refer to temporary filenames instead of those specified. </p>
<h2>Index</h2>
