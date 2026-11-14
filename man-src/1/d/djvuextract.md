---
title: "djvuextract(1)"
name: "djvuextract"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvuextract/"
description: "djvuextract – Extract chunks from DjVu image files."
---

<h2 class="name">NAME</h2>
<p> djvuextract &#8211; Extract chunks from DjVu image files.</p>
<h2>SYNOPSIS</h2>
<p> <code>djvuextract [-page=</code><i>pagenum</i><code>] </code><i>djvufile</i><code> [</code><i>chkid</i><code>=</code><i>filename</i><code>]&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> Program <code>djvuextract</code> extracts raw chunk data from a DjVu file <i>djvufile</i>. These chunks can then be re-assembled into DjVu files using program <code>djvumake</code>. </p>
<p> Option <code>-page</code> can be used to specify a particular page. Otherwise the first page of the document is assumed. Each remaining argument specifies that the raw data associated with all the chunks named <i>chkid </i> will be concatenated into the file named <i>filename</i>. Chunks named <code>BG44</code> and <code>FG44</code> are handled slightly differently: the program generates legal <font SIZE="-1">IW44</font> files instead of simply saving the raw data. </p>
<p> See the man page <code><a href="/docs/linux/man/1-djvumake/">djvumake</a></code>(1) for related information. </p>
<h2>CREDITS</h2>
<p> This program was written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was then improved by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt;, Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvumake/">djvumake</a></code>(1) </p>
<h2>Index</h2>
