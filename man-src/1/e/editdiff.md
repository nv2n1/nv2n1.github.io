---

title: "editdiff(1)"
name: "editdiff"
section: "1"
letter: "e"
url: "/docs/linux/man/1-editdiff/"
description: "rediff, editdiff – fix offsets and counts of a hand-edited diff"
---

<dl>
<dt> <code>rediff</code> <i>ORIGINAL</i> <i>EDITED</i></dt>
<dt> <code>rediff</code> <i>EDITED</i></dt>
<dt> <code>rediff</code> {[&#8211;help] | [&#8211;version]}</dt>
<dt> <code>editdiff</code> <i>FILE</i></dt>
<dt> <code>editdiff</code> {[&#8211;help] | [&#8211;version]}</dt></dl>
<dd>You can use rediff to correct a hand-edited unified diff. Take a copy of the diff you want to edit, and edit it without changing any offsets or counts (the lines that begin &#8220;@@&#8221;). Then run rediff, telling it the name of the original diff file and the name of the one you have edited, and it will output the edited diff file but with corrected offsets and counts. </dd>
<p> A small script, editdiff, is provided for editing a diff file in-place. </p>
<p> The types of changes that are currently handled are: </p>
<dl>
<dt>
</dt><dd> &bull; Modifying the text of any file content line (of course).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Adding new line insertions or deletions.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Adding, changing or removing context lines. Lines at the context horizon are dealt with by adjusting the offset and/or count.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Adding a single hunk (@@-prefixed section).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Removing multiple hunk (@@-prefixed sections).</dd></dl>
<p> Alternatively, if only one argument is provided, it is taken to be the edited file and the counts and offsets are adjusted as appropriate. Some assumptions are made when used in this mode. See <code><a href="/docs/linux/man/1-recountdiff/">recountdiff</a></code>(1) for more information.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Display a short usage message.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Display the version number of rediff.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-interdiff/">interdiff</a></code>(1), <code><a href="/docs/linux/man/1-recountdiff/">recountdiff</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> Package maintainer</dd></dl>
