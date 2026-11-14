---
title: "katedec(1)"
name: "katedec"
section: "1"
letter: "k"
url: "/docs/linux/man/1-katedec/"
description: "katedec – decodes Kate streams to a textual description"
---

<h2 class="name">NAME</h2>
<p> katedec &#8211; decodes Kate streams to a textual description</p>
<h2>SYNOPSIS</h2>
<p> <code>katedec</code> <code>[-hVv]</code> <code>[-o </code><i>outfile</i><code>]</code> <code>[-t </code><i>type</i><code>]</code> [ infile ] </p>
<h2>DESCRIPTION</h2>
<p> <code>katedec</code> decodes Kate streams to libkate&#8217;s custom description language. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Show command line help.</p>
<dt><code>-V</code></p>
<dd> Show version information.</p>
<dt><code>-v</code></p>
<dd> Increase verbosity.</p>
<dt><code>-o</code> outfile</p>
<dd> Write the output description file to the given file name (writes to stdout if not specified). It is possible to write to multiple files (eg, if the input contains several Kate streams) by passing printf style formatting tags in the filename. Formatting tags are strings starting with a &#8216;%&#8217; character, followed by the tag itself. Known tags are:<br />
&nbsp;<wbr>&nbsp;<wbr>%&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>replaced by a verbatim&nbsp;<wbr>%&nbsp;<wbr>character<br />
&nbsp;<wbr>&nbsp;<wbr>l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>replaced by the stream language<br />
&nbsp;<wbr>&nbsp;<wbr>c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>replaced by the stream category<br />
&nbsp;<wbr>&nbsp;<wbr>s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>replaced by the stream serial number, in hexadecimal format<br />
&nbsp;<wbr>&nbsp;<wbr>i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>replaced by the index of the stream in the input file, starting from 0 </p>
<dt><code>-t</code> type</p>
<dd> Set the output format type:<br />
&nbsp;<wbr>kate: Kate description format<br />
&nbsp;<wbr>srt: SubRip format&nbsp;<wbr>(non text information will be lost) </p>
</dl>
<h2>EXAMPLES</h2>
<p> Decodes a Kate stream to a textual description: </p>
<p>&nbsp;<wbr>katedec -o output.kate input.ogg </p>
<p> Decodes several multiplexed Kate streams to SubRip files: </p>
<p>&nbsp;<wbr>katedec -t srt -o output.%l.kate input.ogg </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kateenc/">kateenc</a></code>(1), <code><a href="/docs/linux/man/1-katalyzer/">katalyzer</a></code>(1) </p>
<h2>Index</h2>
