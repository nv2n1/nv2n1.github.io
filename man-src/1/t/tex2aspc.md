---
title: "tex2aspc(1)"
name: "tex2aspc"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tex2aspc/"
description: "tex2aspc – converts conventional MusiXTeX scores to .aspc format for processing by"
---

<h2 class="name">NAME</h2>
<p> tex2aspc &#8211; converts conventional MusiXTeX scores to .aspc format for processing by <code></p>
<p> <a href="/docs/linux/man/1-autosp/">autosp</a></code>(1). </p>
<h2>SYNOPSIS</h2>
<p> <code>tex2aspc </code> [<code>-v | &#8211;version | -h | &#8211;help</code>] </p>
<p> <code>tex2aspc</code> <i>infile</i>[.tex] [<i>outfile</i>[<i></i>.aspc]] </p>
<h2>DESCRIPTION</h2>
<p> This program re-factors (sequences of) conventional note-spacing commands (
otes \Notes \NOtes &#8230;) in a measure into a single notes command. This is intended for &quot;legacy&quot; scores in order to take advantage of features only provided by <code><a href="/docs/linux/man/1-autosp/">autosp</a></code>(1), such as &quot;global&quot; skips and processing of TransformNotes commands. </p>
<h2>LIMITATIONS</h2>
<p> <code>tex2aspc</code> assumes that &amp; and | (rather than 
extinstrument and 
extstaff) are used to separate instruments and staffs. </p>
<p> User-defined macros are not processed or expanded. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autosp/">autosp</a></code>(1) </p>
<p> musixdoc.pdf </p>
<h2>AUTHOR</h2>
<p> This program and manual page were written by Bob Tennent &lt;rdt [at] cs.queensu.ca&gt;. </p>
<h2>Index</h2>
