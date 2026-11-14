---
title: "g3cat(1)"
name: "g3cat"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g3cat/"
description: "g3cat – concatenate multiple g3 documents"
---

<h2 class="name">NAME</h2>
<p> g3cat &#8211; concatenate multiple g3 documents </p>
<h2>SYNOPSIS</h2>
<p> g3cat [-l] [-a] g3-file1 &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>g3cat </i> concatenates g3 files. These can either be &#8216;raw&#8217;, that is, bitmaps packed according to the CCITT T.4 standard for one-dimensional bitmap encoding, or &#8216;digifax&#8217; files, created by GNU&#8217;s GhostScript package with the <code>digifax </code> drivers. Its output is a concatenation of all the input files, in raw G3 format, with two white lines in between. </p>
<p> If a &#8211; is given as input file, stdin is used. </p>
<p> If the input data is malformed, a warning is printed to stderr, and the output file will have a blank line at this place. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l </code></p>
<dd> separate files with a one-pixel wide black line.</p>
<dt><code>-h &lt;blank lines&gt;</code></p>
<dd> specifies the number of blank lines <i>g3cat</i> should prepend to each page. Default is 0.</p>
<dt><code>-L &lt;lines&gt;</code></p>
<dd> limit lenght of output page to maximum &lt;lines&gt; lines.</dl>
<h2>SPECIAL-CASE OPTIONS</h2>
<dl>
<dt><code>-w &lt;width&gt;</code></p>
<dd> specifies the desired page width in pixels per line. Default is 1728 PELs, and this is mandatory if you want to send the fax to a standard fax machine. If one of the input files doesn&#8217;t match this line width (for example because it was created by a broken G3 creator), a warning is printed, and the line width is transparently fixed.</p>
<dt><code>-a </code></p>
<dd> byte-align the end-of-line codes (EOL) in the file. Every EOL will end at a byte boundary, that is, with a &nbsp;<wbr>01 byte.</p>
<dt><code>-p &lt;pad&gt;</code></p>
<dd> specifies a minimum number of bytes that each output line must be padded to. Padding is done with 0-bits before the EOL code.</p>
<dt><code>-R</code></p>
<dd> suppress output of end-of-page code (RTC). </p>
</dl>
<h2>Example</h2>
<p> The following example will put a header line on a given g3 page, &#8216;page1&#8217; and put the result into &#8216;page2&#8217;: </p>
<p> echo &#8216;$header&#8217; | pbmtext | pbm2g3 | g3cat &#8211; page1 &gt;page2 </p>
<h2>FILES</h2>
<p> &#8212; </p>
<h2>BUGS</h2>
<p> Hopefully none :-). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-g32pbm/">g32pbm</a>(1), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8), <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) </p>
<h2>AUTHORS</h2>
<p> <i>g3cat</i> is Copyright (C) 1993 by Gert Doering, &lt;gert [at] greenie.muc.de&gt; </p>
<h2>Index</h2>
