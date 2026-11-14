---
title: "recountdiff(1)"
name: "recountdiff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-recountdiff/"
description: "recountdiff – recompute patch counts and offsets"
---

<h2 class="name">NAME</h2>
<p> recountdiff &#8211; recompute patch counts and offsets </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>recountdiff</code> [<i>file</i>&#8230;]</p>
<dt> <code>recountdiff</code> {[&#8211;help] | [&#8211;version]}</dl>
<h2>DESCRIPTION</h2>
<p> <code>recountdiff</code></p>
<dd>recomputes the counts and offsets in unified context diffs. It does this in two passes: first the counts are corrected by inspection of the actual patch lines, and then the offsets are adjusted according to the computed counts. </p>
<p> The corrected diff is sent to standard output.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of recountdiff.</dl>
<h2>LIMITATIONS</h2>
<p> There are some things that cannot be dealt with. If you have removed the first context line in a hunk, for example, there is no way for <code>recountdiff</code> to know that. For more precise fixing up, use <code><a href="/docs/linux/man/1-rediff/">rediff</a></code>(1), which uses the original and modified diffs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rediff/">rediff</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
