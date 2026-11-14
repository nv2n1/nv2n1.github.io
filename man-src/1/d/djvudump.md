---
title: "djvudump(1)"
name: "djvudump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvudump/"
description: "djvudump – Display internal structure of DjVu files."
---

<h2 class="name">NAME</h2>
<p> djvudump &#8211; Display internal structure of DjVu files.</p>
<h2>SYNOPSIS</h2>
<p> <code>djvudump [-o </code><i>outputfile</i><code>] </code><i>djvufiles</i><code>&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> Program <code>djvudump </code> prints an indented representation of the chunk structure of any DjVu files. Each line represent contains a chunk ID followed by the chunk size. Lines are indented in order to reflect the hierarchical structure of the IFF files. The page identifier is printed between curly braces when a bundled multi-page DjVu document is recognized. Additional information about each chunk is provided when <code>djvudump</code> recognizes the chunk name and knows how to summarize the chunk data. </p>
<h2>REMARKS</h2>
<p> This program is in fact able to describe any file complying with the Electronic Arts IFF 85 specification. This includes a number of graphical and sound file formats. </p>
<h2>CREDITS</h2>
<p> This program was written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was then improved by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt;, Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1) </p>
<h2>Index</h2>
