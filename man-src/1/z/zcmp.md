---
title: "zcmp(1)"
name: "zcmp"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zcmp/"
description: "zcmp, zdiff – compare compressed files"
---

<h2 class="name">NAME</h2>
<p> zcmp, zdiff &#8211; compare compressed files </p>
<h2>SYNOPSIS</h2>
<p> <code>zcmp</code> [ cmp_options ] file1 [ file2 ]<br />
 <code>zdiff</code> [ diff_options ] file1 [ file2 ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Zcmp</i> and <i>zdiff</i> are used to invoke the <i>cmp</i> or the <i>diff</i> program on files compressed via <i>gzip</i>. All options specified are passed directly to <i>cmp</i> or <i>diff</i>. If only <i>file1</i> is specified, it is compared to the uncompressed contents of <i>file1</i>.gz. If two files are specified, their contents (uncompressed if necessary) are fed to <i>cmp</i> or <i>diff</i>. The input files are not modified. The exit status from <i>cmp</i> or <i>diff</i> is preserved.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cmp/">cmp</a>(1), <a href="/docs/linux/man/1-diff/">diff</a>(1), <a href="/docs/linux/man/1-zmore/">zmore</a>(1), <a href="/docs/linux/man/1-zgrep/">zgrep</a>(1), <a href="/docs/linux/man/1-znew/">znew</a>(1), <a href="/docs/linux/man/1-zforce/">zforce</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1), <a href="/docs/linux/man/1-gzexe/">gzexe</a>(1)</p>
<h2>BUGS</h2>
<p> Messages from the <i>cmp</i> or <i>diff</i> programs may refer to file names such as &quot;-&quot; instead of to the file names specified. </p>
<h2>Index</h2>
