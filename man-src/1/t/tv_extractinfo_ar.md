---
title: "tv_extractinfo_ar(1)"
name: "tv_extractinfo_ar"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_extractinfo_ar/"
description: "tv_extractinfo_ar – read Spanish (Argentinean) language listings and extract info from programme descriptions."
---

<h2 class="name">NAME</h2>
<p> tv_extractinfo_ar &#8211; read Spanish (Argentinean) language listings and extract info from programme descriptions. </p>
<h2>SYNOPSIS</h2>
<p> tv_extractinfo_ar [&#8211;help] [&#8211;output <font SIZE="-1">FILE</font>] [<font SIZE="-1">FILE&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Read <font SIZE="-1">XMLTV</font> data and attempt to extract information from Spanish-language programme descriptions, putting it into machine-readable form. For example the human-readable text &#8216;(Repeticion)&#8217; in a programme description might be replaced by the <font SIZE="-1">XML</font> element &lt;previously-shown&gt;. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output </p>
<p> This tool also attempts to split multipart programmes into their constituents, by looking for a description that seems to contain lots of times and titles. But this depends on the description following one particular style and is useful only for some listings sources (Ananova). </p>
<p> If some text is marked with the &#8216;lang&#8217; attribute as being some language other than Spanish (&#8216;es&#8217;), it is ignored.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Mariano Cosentino, Mok [at] marianok.com.ar</p>
<h2>BUGS</h2>
<p> Trying to parse human-readable text is always error-prone, more so with the simple regexp-based approach used here. But because <font SIZE="-1">TV</font> listing descriptions usually conform to one of a few set styles, tv_extractinfo_en does reasonably well. It is fairly conservative, trying to avoid false positives (extracting &#8216;information&#8217; which isn&#8217;t really there) even though this means some false negatives (failing to extract information and leaving it in the human-readable text). </p>
<p> However, the leftover bits of text after extracting information may not form a meaningful Spanish sentence, or the punctuation may be wrong. </p>
<p> On the two listings sources currently supported by the <font SIZE="-1">XMLTV</font> package, this program does a reasonably good job. But it has not been tested with every source of anglophone <font SIZE="-1">TV</font> listings. </p>
<p> This Spanish Version is heavily customized for the <font SIZE="-1">XML</font> results from tv_grab_ar (developed by Christian A. Rodriguez and postriorily updated by Mariano S. Cosentino). </p>
<p> This file should probably be called tv_extractinfo_es, but I have not tested it with any other spanish grabbers, so I don&#8217;t want to be presumptious. </p>
<h2>Index</h2>
