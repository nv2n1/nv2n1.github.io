---
title: "rediff(1)"
name: "rediff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rediff/"
description: "rediff, editdiff – fix offsets and counts of a hand-edited diff"
---

<h2 class="name">NAME</h2>
<p> rediff, editdiff &#8211; fix offsets and counts of a hand-edited diff </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>rediff</code> <i>ORIGINAL</i> <i>EDITED</i></p>
<dt> <code>rediff</code> <i>EDITED</i></p>
<dt> <code>rediff</code> {[&#8211;help] | [&#8211;version]}</p>
<dt> <code>editdiff</code> <i>FILE</i></p>
<dt> <code>editdiff</code> {[&#8211;help] | [&#8211;version]}</dl>
<h2>DESCRIPTION</h2>
<dd>You can use rediff to correct a hand-edited unified diff. Take a copy of the diff you want to edit, and edit it without changing any offsets or counts (the lines that begin &#8220;@@&#8221;). Then run rediff, telling it the name of the original diff file and the name of the one you have edited, and it will output the edited diff file but with corrected offsets and counts. </p>
<p> A small script, editdiff, is provided for editing a diff file in-place. </p>
<p> The types of changes that are currently handled are: </p>
<dl>
<dt>
<dd> &bull; Modifying the text of any file content line (of course).</dl>
<dl>
<dt>
<dd> &bull; Adding new line insertions or deletions.</dl>
<dl>
<dt>
<dd> &bull; Adding, changing or removing context lines. Lines at the context horizon are dealt with by adjusting the offset and/or count.</dl>
<dl>
<dt>
<dd> &bull; Adding a single hunk (@@-prefixed section).</dl>
<dl>
<dt>
<dd> &bull; Removing multiple hunk (@@-prefixed sections).</dl>
<p> Alternatively, if only one argument is provided, it is taken to be the edited file and the counts and offsets are adjusted as appropriate. Some assumptions are made when used in this mode. See <code><a href="/docs/linux/man/1-recountdiff/">recountdiff</a></code>(1) for more information.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of rediff.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-interdiff/">interdiff</a></code>(1), <code><a href="/docs/linux/man/1-recountdiff/">recountdiff</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
