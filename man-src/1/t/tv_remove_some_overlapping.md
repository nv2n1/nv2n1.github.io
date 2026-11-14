---
title: "tv_remove_some_overlapping(1)"
name: "tv_remove_some_overlapping"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_remove_some_overlapping/"
description: "tv_remove_some_overlapping – Remove some overlapping programmes from XMLTV data."
---

<h2 class="name">NAME</h2>
<p> tv_remove_some_overlapping &#8211; Remove some overlapping programmes from XMLTV data. </p>
<h2>SYNOPSIS</h2>
<p> tv_remove_some_overlapping [&#8211;help] [&#8211;output <font SIZE="-1">FILE</font>] [<font SIZE="-1">FILE&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Read one or more <font SIZE="-1">XMLTV</font> files and write a file to standard ouput containing the same data, except that some &#8216;magazine&#8217; programmes which seem to contain two or more other programmes are removed. </p>
<p> For example, if &#8216;Schools <font SIZE="-1">TV</font>&#8216; runs from 10:00 to 12:00, and there are two programmes &#8216;History&#8217; from 10:00 to 11:00 and &#8216;Geography&#8217; from 11:00 to 12:00 on the same channel, then &#8216;Schools <font SIZE="-1">TV</font>&#8216; could be removed. A programme is removed only if there are two or more other programmes which partition its timeslot, which implies that it and these other programmes must have stop times specified. </p>
<p> To avoid throwing away any real programmes, no programme will be discarded if it has content data other than title and <font SIZE="-1">URL.</font> </p>
<p> Filtering this tool won&#8217;t remove all overlapping programmes but it will deal with the &#8216;big magazine programme containing smaller programmes&#8217; data commonly seen from listings sources. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Ed Avis, ed [at] membled.com </p>
<h2>Index</h2>
