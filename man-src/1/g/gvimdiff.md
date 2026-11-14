---
title: "gvimdiff(1)"
name: "gvimdiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvimdiff/"
description: "vimdiff – edit two, three or four versions of a file with Vim and show differences"
---

<h2 class="name">NAME</h2>
<p> vimdiff &#8211; edit two, three or four versions of a file with Vim and show differences </p>
<h2>SYNOPSIS</h2>
<p> <code>vimdiff</code> [options] file1 file2 [file3 [file4]] </p>
<p> <code>gvimdiff</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Vimdiff</code> starts <code>Vim</code> on two (or three or four) files. Each file gets its own window. The differences between the files are highlighted. This is a nice way to inspect changes and to move changes from one version to another version of the same file. </p>
<p> See <a href="/docs/linux/man/1-vim/">vim</a>(1) for details about Vim itself. </p>
<p> When started as <code>gvimdiff</code> the GUI will be started, if available. </p>
<p> In each window the &#8216;diff&#8217; option will be set, which causes the differences to be highlighted.<br />
 The &#8216;wrap&#8217; and &#8216;scrollbind&#8217; options are set to make the text look good.<br />
 The &#8216;foldmethod&#8217; option is set to &quot;diff&quot;, which puts ranges of lines without changes in a fold. &#8216;foldcolumn&#8217; is set to two to make it easy to spot the folds and open or close them.</p>
<h2>OPTIONS</h2>
<p> Vertical splits are used to align the lines, as if the &quot;-O&quot; argument was used. To use horizontal splits instead, use the &quot;-o&quot; argument. </p>
<p> For all other arguments see <a href="/docs/linux/man/1-vim/">vim</a>(1).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-vim/">vim</a>(1)</p>
<h2>AUTHOR</h2>
<p> Most of <code>Vim</code> was made by Bram Moolenaar, with a lot of help from others. See &quot;:help credits&quot; in <code>Vim.</code> </p>
<h2>Index</h2>
