---
title: "tv_cat(1)"
name: "tv_cat"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_cat/"
description: "tv_cat – Concatenate XMLTV listings files."
---

<h2 class="name">NAME</h2>
<p> tv_cat &#8211; Concatenate XMLTV listings files. </p>
<h2>SYNOPSIS</h2>
<p> tv_cat [&#8211;help] [&#8211;utf8] [&#8211;output <font SIZE="-1">FILE</font>] [<font SIZE="-1">FILE&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Read one or more <font SIZE="-1">XMLTV</font> files and write a file to standard ouput whose programmes are the concatenation of the programmes in the input files, and whose channels are the union of the channels in the input files. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output </p>
<p> The treatment of programmes and channels is slightly different because for programmes, the ordering is important (typically programmes are processed or displayed in the same order as they appear in the input) whereas channels are just a set indexed by channel id. There is a warning if channel details clash for the same id. </p>
<p> One more wrinkle is the credits (source, generator and so on), they are taken from one of the files and then there&#8217;s a warning if the other files differ. If two input files have different character encodings, then it is not meaningful to combine their data (without recoding or other processing) and tv_cat die with an error message. </p>
<p> But if you do want to combine multiple input files with different character encodings then you can use the &#8211;utf8 command-line parameter which will create a combined output file in <font SIZE="-1">UTF-8</font> format. (Note: it is not safe to combine mixed encodings to anything other than <font SIZE="-1">UTF-8</font> so no other output encoding is provided for.) (Note 2: any input file which does not have an encoding specified in the xml tag is not only naughty but is assumed to already be <font SIZE="-1">UTF-8,</font> which may not be true!) </p>
<p> This tool is rather useless, but it makes a good testbed for the <font SIZE="-1">XMLTV</font> module.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Ed Avis, ed [at] membled.com </p>
<h2>Index</h2>
