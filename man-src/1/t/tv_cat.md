---

title: "tv_cat(1)"
name: "tv_cat"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_cat/"
description: "tv_cat – Concatenate XMLTV listings files."
---

<p> tv_cat &#8211; Concatenate XMLTV listings files. </p>
<h2>SYNOPSIS</h2>
<p> tv_cat [&#8211;help] [&#8211;utf8] [&#8211;output FILE] [FILE&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Read one or more XMLTV files and write a file to standard ouput whose programmes are the concatenation of the programmes in the input files, and whose channels are the union of the channels in the input files. </p>
<p> <code>&#8211;output </code><code>FILE</code> write to FILE rather than standard output </p>
<p> The treatment of programmes and channels is slightly different because for programmes, the ordering is important (typically programmes are processed or displayed in the same order as they appear in the input) whereas channels are just a set indexed by channel id. There is a warning if channel details clash for the same id. </p>
<p> One more wrinkle is the credits (source, generator and so on), they are taken from one of the files and then there&#8217;s a warning if the other files differ. If two input files have different character encodings, then it is not meaningful to combine their data (without recoding or other processing) and tv_cat die with an error message. </p>
<p> But if you do want to combine multiple input files with different character encodings then you can use the &#8211;utf8 command-line parameter which will create a combined output file in UTF-8 format. (Note: it is not safe to combine mixed encodings to anything other than UTF-8 so no other output encoding is provided for.) (Note 2: any input file which does not have an encoding specified in the xml tag is not only naughty but is assumed to already be UTF-8, which may not be true!) </p>
<p> This tool is rather useless, but it makes a good testbed for the XMLTV module.</p>
<h2>SEE ALSO</h2>
<p> <i>xmltv</i>(5).</p>
<h2>AUTHOR</h2>
<p> Ed Avis, ed [at] membled.com </p>
