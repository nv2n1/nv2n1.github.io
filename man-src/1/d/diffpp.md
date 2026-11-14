---
title: "diffpp(1)"
name: "diffpp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diffpp/"
description: "diffpp – pretty-print diff outputs with GNU enscript"
---

<h2 class="name">NAME</h2>
<p> diffpp &#8211; pretty-print diff outputs with GNU enscript</p>
<h2>SYNOPSIS</h2>
<p> <code>diffpp </code><i>currentfile</i> &lt; <i>diff-file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>Diffpp</code> converts <code><a href="/docs/linux/man/1-diff/">diff</a>(1)</code>-program&#8217;s output files to a format suitable to be printed with GNU <code><a href="/docs/linux/man/1-enscript/">enscript</a>(1)</code>. Program annotates the changes with enscript&#8217;s special escapes so enscript can highlight the modified portions of the file. All changed and added lines are printed with gray-background, deleted lines are marked with minus (`-&#8216;) characters; <code>diffpp</code> prints one minus character for each deleted line. </p>
<h2>EXAMPLES</h2>
<p> The easiest way to use <code>diffpp</code> is to use it as an input filter for enscript. If an input filter is specified for enscript it is used to pre-process the incoming data-stream. Filtering does not alter any header strings or file-timestamps which might be printed on enscript headers; only the incoming data is modified. </p>
<dl>
<dt><code>enscript -G2re &#8211;filter=&#8217;rcsdiff %s | diffpp %s&#8217; *.c *.h</code></p>
<dd> Print the changes between current source files and their latest RCS-versions.</p>
<dt><code>enscript -G2re &#8211;filter=&#8217;diff %s~ %s | diffpp %s&#8217; *.c *.h</code></p>
<dd> Print changes between source files and the corresponding backup-files. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-diff/">diff</a>(1), <a href="/docs/linux/man/1-enscript/">enscript</a>(1) </p>
<h2>AUTHOR</h2>
<p> Markku Rossi &lt;mtr [at] iki.fi&gt; &lt;<a rel="nofollow" href="http://www.iki.fi/~mtr/">http://www.iki.fi/~mtr/</a>&gt; </p>
<h2>Index</h2>
