---
title: "splitdiff(1)"
name: "splitdiff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-splitdiff/"
description: "splitdiff – separate out incremental patches"
---

<h2 class="name">NAME</h2>
<p> splitdiff &#8211; separate out incremental patches </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>splitdiff</code> [-a] [-d] [-D&nbsp;<i>dir</i>] [-p&nbsp;<i>n</i>] [-E] [<i>file</i>]</dt>
<dt> <code>splitdiff</code> {[&#8211;help] | [&#8211;version]}</dt></dl>
<h2>DESCRIPTION</h2>
<dd>If you have a patch file composed of several incremental patches, you can use splitdiff to separate them out. You may want to do this in preparation for re-combining them with <code><a href="/docs/linux/man/1-combinediff/">combinediff</a></code>(1). </dd>
<p> The effect of running splitdiff is to separate its input into a set of output files, with no output file patching the same file more than once.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code></p>
<dl>
<dt>
</dt><dd> Split out every single file-level patch.</dd></dl>
<p> <code>-d</code></p>
<dl>
<dt>
</dt><dd> Create file names such as a_b.c.patch for a patch that modifies a/b.c.</dd></dl>
<p> <code>-D</code> <i>dir</i></p>
<dl>
<dt>
</dt><dd> Write output files into subdirectory <i>dir</i>. Implies <code>-d</code>.</dd></dl>
<p> <code>-p</code> <i>n</i></p>
<dl>
<dt>
</dt><dd> Strip the first <i>n</i> components of the pathname to aid comparisons.</dd></dl>
<p> <code>-E</code></p>
<dl>
<dt>
</dt><dd> Don&#8217;t use .patch filename extension when writing output files.</dd></dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Display a short usage message.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Display the version number of splitdiff.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-combinediff/">combinediff</a></code>(1), <code><a href="/docs/linux/man/1-lsdiff/">lsdiff</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> Package maintainer</dd></dl>
<h2>Index</h2>
