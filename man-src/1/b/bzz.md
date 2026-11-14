---
title: "bzz(1)"
name: "bzz"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bzz/"
description: "bzz – DjVu general purpose compression utility."
---

<h2 class="name">NAME</h2>
<p> bzz &#8211; DjVu general purpose compression utility.</p>
<h2>SYNOPSIS</h2>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Encoding:</h2>
<p> <code>bzz -e</code><i>[blocksize]</i><i>inputfile</i><i>outputfile</i></p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Decoding:</h2>
<p> <code>bzz -d </code><i>inputfile</i><i>outputfile</i> </p>
<h2>DESCRIPTION</h2>
<p> The first form of the command line (option <code>-e</code>) compresses the data from file <i>inputfile </i> and writes the compressed data into <i>outputfile</i>. The second form of the command line (option <code>-d</code>) decompressed file <i>inputfile</i> and writes the output to <i>outputfile</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Decoding mode.</p>
<dt><code>-e</code><i>[blocksize]</i></p>
<dd> Encoding mode. The optional argument <i>blocksize</i> specifies the size of the input file blocks processed by the Burrows-Wheeler transform expressed in kilobytes. The default block sizes is 2048 <font SIZE="-1">KB.</font> The maximal block size is 4096 <font SIZE="-1">KB.</font> Specifying a larger block size usually produces higher compression ratios and increases the memory requirements of both the encoder and decoder. It is useless to specify a block size that is larger than the input file. </p>
</dl>
<h2>ALGORITHMS</h2>
<p> The Burrows-Wheeler transform is performed using a combination of the Karp-Miller-Rosenberg and the Bentley-Sedgewick algorithms. This is comparable to (Sadakane, DCC 98) with a slightly more flexible ranking scheme. Symbols are then ordered according to a running estimate of their occurrence frequencies. The symbol ranks are then coded using a simple fixed tree and the ZP binary adaptive coder (Bottou, DCC 98). </p>
<p> The Burrows-Wheeler transform is also used in the well known compressor <code>bzip2</code>. The originality of <code>bzz</code> is the use of the ZP adaptive coder. The adaptation noise can cost up to 5 percent in file size, but this penalty is usually offset by the benefits of adaptation. </p>
<h2>PERFORMANCE</h2>
<p> The following table shows comparative results (in bits per character) on the Canterbury Corpus ( <code><a rel="nofollow" href="http://corpus.canterbury.ac.nz">http://corpus.canterbury.ac.nz</a></code> ). The very good <code>bzz</code> performance on the spreadsheet file <i>excl</i> puts the weighted average ahead of much more sophisticated compressors such as <code>fsmx</code>. <font SIZE="-2"> </p>
<p> </font><center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=14>Compression performance
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center>text</td>
<td ALIGN=center>fax</td>
<td ALIGN=center>csrc</td>
<td ALIGN=center>excl</td>
<td ALIGN=center>sprc</td>
<td ALIGN=center>tech</td>
<td ALIGN=center>poem</td>
<td ALIGN=center>html</td>
<td ALIGN=center>lisp</td>
<td ALIGN=center>man</td>
<td ALIGN=center>play</td>
<td ALIGN=center>Weighted</td>
<td ALIGN=center>Average
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=14>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>compress&nbsp;<wbr></td>
<td ALIGN=right>3.27&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>0.97&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.56&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.41&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>4.21&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.06&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.38&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.68&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.90&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>4.43&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.51&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.55&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>gzip -9&nbsp;<wbr></td>
<td ALIGN=right>2.85&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>0.82&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.24&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>1.63&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.67&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.71&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.23&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.59&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.65&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.08&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.53&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>bzip2 -9&nbsp;<wbr></td>
<td ALIGN=right>2.27&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>0.78&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.18&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>1.01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.70&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.42&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.48&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.79&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.33&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.53&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>1.54&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.23&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>ppmd&nbsp;<wbr></td>
<td ALIGN=right>2.31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>0.99&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>1.08&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.68&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.19&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.48&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.38&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.43&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.53&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>1.65&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.20&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>fsmx&nbsp;<wbr></td>
<td ALIGN=right><code>2.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right>0.79&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right><code>1.89&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right>1.48&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right><code>2.52&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right><code>1.84&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right><code>2.21&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right><code>2.24&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right><code>2.29&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right><code>2.91&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right><code>2.35&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right>1.63&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right><code>2.06&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>bzz&nbsp;<wbr></code></td>
<td ALIGN=right>2.25&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right><code>0.76&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right>2.13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right><code>0.78&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right>2.67&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.40&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.52&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.60&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>3.19&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>2.52&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right><code>1.44&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></td>
<td ALIGN=right>2.16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
</table>
</table>
<p></center> <font SIZE="-2"> </p>
<p> Note that DjVu contributors have several entries in this table. Program <code>compress</code> was written some time ago by Joe Orost. Program <code>ppmd</code> is an improvement of the </font><font SIZE="-3">PPM-C</font> method invented by Paul Howard. </p>
<h2>CREDITS</h2>
<p> Program <code>bzz </code> was written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was then improved by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt;, Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) </p>
<h2>Index</h2>
