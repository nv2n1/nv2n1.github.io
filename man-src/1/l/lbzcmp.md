---
title: "lbzcmp(1)"
name: "lbzcmp"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lbzcmp/"
description: "lbzcmp, lbzdiff – compare compressed files"
---

<h2>NAME</h2>
<p> lbzcmp, lbzdiff &#8211; compare compressed files</p>
<h2>SYNOPSIS</h2>
<p> <code>lbzcmp</code> [ cmp_options ] file1 [ file2 ]<br />
 <code>lbzdiff</code> [ diff_options ] file1 [ file2 ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Zcmp</i> and <i>lbzdiff</i> are used to invoke the <i>cmp</i> or the <i>diff</i> program on files compressed via <i>lbzip2</i>. All options specified are passed directly to <i>cmp</i> or <i>diff</i>. If only <i>file1</i> is specified, it is compared to the uncompressed contents of <i>file1</i>.bz2. If two files are specified, their contents (uncompressed if necessary) are fed to <i>cmp</i> or <i>diff</i>. The input files are not modified. The exit status from <i>cmp</i> or <i>diff</i> is preserved.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cmp/">cmp</a>(1), <a href="/docs/linux/man/1-diff/">diff</a>(1), <a href="/docs/linux/man/1-lbzmore/">lbzmore</a>(1), <a href="/docs/linux/man/1-lbzgrep/">lbzgrep</a>(1), <a href="/docs/linux/man/1-lbzforce/">lbzforce</a>(1), <a href="/docs/linux/man/1-lbzip2/">lbzip2</a>(1), <a href="/docs/linux/man/1-lbzexe/">lbzexe</a>(1)</p>
<h2>BUGS</h2>
<p> Messages from the <i>cmp</i> or <i>diff</i> programs may refer to file names such as &quot;-&quot; instead of to the file names specified. </p>
<h2>Index</h2>
